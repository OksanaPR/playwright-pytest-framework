

def discount(price: float, percent: int) -> float:
    if percent < 0 or percent > 100:
        raise ValueError("Discount must be between 0 and 100")

    return price - (price * (percent/100))
