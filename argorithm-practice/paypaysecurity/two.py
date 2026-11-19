def solution(commands):
    rates = {}
    investments = {}

    for command in commands:
        parts = command.split(",")
        action = parts[0]

        if action == "BRAND":
            _, brand, rate = parts
            rates[brand] = int(rate)

        elif action == "INVEST":
            _, investment_id, brand, amount = parts

            investments[investment_id] = {
                "brand": brand,
                "principal": int(amount),
                "balance": int(amount),
                "failed": 0,
                "failed_balance": 0
            }

        elif action == "NEXT_TIME_SLOT":
            for inv in investments.values():
                rate = rates[inv["brand"]]

                inv["balance"] = (
                        inv["balance"] * (100 + rate) // 100
                )

                inv["failed_balance"] = (
                        inv["failed_balance"] * (100 + rate) // 100
                )

        elif action == "PAYMENT_FAILURE_NOTICE":
            _, investment_id, amount = parts

            inv = investments[investment_id]
            amount = int(amount)

            inv["failed"] += amount

            inv["failed_balance"] = (
                    inv["balance"]
                    - inv["balance"]
                    * (inv["principal"] - inv["failed"])
                    // inv["principal"]
            )

    result = []

    for investment_id in sorted(investments):
        inv = investments[investment_id]

        final_balance = (
                inv["balance"] - inv["failed_balance"]
        )

        result.append(
            f"{investment_id},{inv['brand']},{final_balance}"
        )

    return result


print(solution([
    "BRAND,APPX,3",
    "INVEST,a,APPX,1000",
    "INVEST,b,APPX,1000",
    "NEXT_TIME_SLOT",
    "PAYMENT_FAILURE_NOTICE,a,500"
]))

## expected: a,APPX,515
