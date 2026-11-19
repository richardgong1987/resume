def solution(numbers, pivot):
    IsPositive = pivot > 0
    IsNegative = pivot < 0

    result = []
    for i in range(len(numbers)):
        if IsPositive and numbers[i] > 0:
            result.append(1)
            pass
        elif IsNegative and numbers[i] < 0:
            result.append(1)

        elif [i] == pivot:
            result.append(0)

        elif numbers[i] == 0:
            result.append(0)
        else:
            result.append(-1)
    return result


print(solution([42, 42, 42, 0], 42))
