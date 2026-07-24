from pathlib import Path
import pandas as pd


def convert_volume(volume):
    """Convert volume strings like 7.04M or 850K to numbers."""

    if pd.isna(volume):
        return 0

    volume = str(volume).strip().upper()

    if volume in ("", "-", "N/A"):
        return 0

    try:
        if volume.endswith("M"):
            return float(volume[:-1]) * 1_000_000

        if volume.endswith("K"):
            return float(volume[:-1]) * 1_000

        return float(volume)

    except ValueError:
        return 0


def load_single_csv(file_path: Path):
    """Load one Investing.com CSV."""

    with open(file_path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    records = []

    # Skip first 3 lines
    for line in lines[3:]:

        line = line.strip()

        if not line:
            continue

        parts = line.split("\t")

        if len(parts) != 7:
            continue

        if any(p.strip() == "" for p in parts):
            continue

        records.append(parts)

    df = pd.DataFrame(
        records,
        columns=[
            "Date",
            "Close",
            "Open",
            "High",
            "Low",
            "Volume",
            "Change %",
        ],
    )

    # Convert types
    df["Date"] = pd.to_datetime(df["Date"])

    for col in ["Close", "Open", "High", "Low"]:

        df[col] = (
            df[col]
            .astype(str)
            .str.replace(",", "", regex=False)
            .str.strip()
       )

        df[col] = pd.to_numeric(df[col], errors="coerce")

    df["Volume"] = df["Volume"].apply(convert_volume)

    # Drop unused column
    df.drop(columns=["Change %"], inplace=True)

    # Sort oldest → newest
    df = df.sort_values("Date").reset_index(drop=True)

    return df


def load_all_data(raw_data_path: Path):
    """Load every CSV under data/raw."""

    all_data = []

    for sector_folder in raw_data_path.iterdir():

        if not sector_folder.is_dir():
            continue

        sector = sector_folder.name

        for csv_file in sector_folder.glob("*.csv"):

            ticker = csv_file.stem.upper()

            print(f"Loading {ticker}...")

            df = load_single_csv(csv_file)

            df["Ticker"] = ticker
            df["Sector"] = sector

            all_data.append(df)

    merged_df = pd.concat(all_data, ignore_index=True)
    
    # Create processed folder if it doesn't exist
    processed_folder = raw_data_path.parent / "processed"
    processed_folder.mkdir(exist_ok=True)

    output_file = processed_folder / "ngx_tier1_master.csv"

    merged_df.to_csv(output_file, index=False)

    print(f"\nDataset saved to:\n{output_file}")
    return merged_df