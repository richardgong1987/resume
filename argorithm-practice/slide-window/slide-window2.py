def length_of_longest_substring(s):
    left = 0
    maximum = 0
    seen = set()

    for right in range(len(s)):
        while s[right] in seen:
            seen.remove(s[left])
            left += 1

        seen.add(s[right])

        maximum = max(
            maximum,
            right - left + 1
        )

    return maximum


print(length_of_longest_substring("abcabcbb"))
# 3
