from collections import defaultdict


def solution(queries, diff):
    counts = defaultdict(int)
    result = []
    total = 0

    for query in queries:
        action = query[0]
        x = int(query[1:])

        if diff == 0:
            n = counts[x]

            if action == "+":
                total += n * (n - 1) // 2
                counts[x] += 1
            else:
                total -= n * (n - 1) * (n - 2) // 6
                counts[x] = 0

        else:
            combinations = (
                    counts[x - diff] * counts[x - 2 * diff]
                    + counts[x + diff] * counts[x - diff]
                    + counts[x + diff] * counts[x + 2 * diff]
            )

            if action == "+":
                total += combinations
                counts[x] += 1
            else:
                total -= combinations * counts[x]
                counts[x] = 0

        result.append(total)

    return result


print(solution(["+4", "+5", "+6", "+4", "+3", "-4"], 1))
