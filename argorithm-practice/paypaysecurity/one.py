def solution(csv):
    brands = {}

    for line in csv:
        brand, price = line.split(",")
        value = float(price)

        if brand not in brands:
            brands[brand] = {
                "high": (value, price),
                "open": (value, price),
                "close": (value, price),
                "low": (value, price)
            }
        else:
            data = brands[brand]

            if value > data["high"][0]:
                data["high"] = (value, price)

            if value < data["low"][0]:
                data["low"] = (value, price)

            data["close"] = (value, price)

    result = []

    for brand in sorted(brands):
        data = brands[brand]

        result.append(",".join([
            brand,
            data["high"][1],
            data["open"][1],
            data["close"][1],
            data["low"][1]
        ]))

    return result
