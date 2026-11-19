# Problem 4: Maximum Rectangle Intersection
# Original CodeSignal-style practice problem based on the recruiter's coordinate-intersection topic. Not an actual PayPay exam question.
# Problem Description
# You are given a two-dimensional integer array rectangles, where each element represents an axis-aligned rectangle on a Cartesian coordinate plane.
#
# Each rectangle is represented by four integers:
#
# [x1, y1, x2, y2]
#
# Here, (x1, y1) represents the bottom-left corner, and (x2, y2) represents the top-right corner.
#
# Your task is to find the maximum intersection area between any two distinct rectangles.
#
# Two rectangles intersect if they share a region with positive area. If they only touch at an edge or a corner, their intersection area is zero.
#
# Return the maximum intersection area among all possible pairs of rectangles.
#
# If no two rectangles overlap, return 0
from typing import List

# rectangles = [
#     [0, 0, 4, 4],
#     [2, 2, 6, 6],
#     [5, 5, 8, 8]
# ]  # = 4


# rectangles = [
#     [0, 0, 2, 2],
#     [2, 0, 4, 2]
# ]  # = 0


rectangles = [
    [0, 0, 10, 10],
    [2, 2, 8, 8],
    [4, 4, 12, 12]
]  # = 36


def intersect(R: List[List[int]]) -> int:
    n = len(R)
    # (1). 1 <= i < j <= N
    M = 0
    for i in range(n):
        for j in range(i + 1, n):
            x1, y1, x2, y2 = R[i]
            a1, b1, a2, b2 = R[j]
            w = max(0, min(x2, a2) - max(x1, a1))
            h = max(0, min(y2, b2) - max(y1, b1))

            M = max(M, w * h)

    return M


print(intersect(rectangles))
