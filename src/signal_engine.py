def generate_signal(
    probability,
    expected_return
):
    """
    Generate trading signal.
    """

    if (
        probability >= 0.60
        and expected_return >= 0.02
    ):
        return "BUY"

    elif (
        probability >= 0.50
        and expected_return >= 0.01
    ):
        return "WATCH"

    else:
        return "HOLD"