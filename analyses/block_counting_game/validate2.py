import itertools
from math import comb, factorial


def count_permutations_wrapper(c, n, k, h):
    tower_heights = [h] * k
    blocks_per_color = [n] * c
    return count_permutations(
        num_colors=c, blocks_per_color=blocks_per_color, tower_heights=tower_heights
    )


def count_permutations(num_colors, blocks_per_color, tower_heights):
    num_towers = len(tower_heights)
    total_blocks = sum(blocks_per_color)

    # Check if the problem is solvable
    if sum(tower_heights) < total_blocks:
        raise ValueError(
            "The total height of towers is insufficient to hold all blocks."
        )

    # Special case for single-color blocks
    if num_colors == 1:
        count = 0
        for x1 in range(min(total_blocks, tower_heights[0]) + 1):
            x2 = total_blocks - x1
            if x2 <= tower_heights[1]:
                count += 1
        return count

    # Generate all block types
    blocks = []
    color_labels = [chr(65 + i) for i in range(num_colors)]  # ['A', 'B', 'C', ...]
    for i, color in enumerate(color_labels):
        blocks.extend([color] * blocks_per_color[i])

    # Generate all permutations of blocks
    permutations = set(itertools.permutations(blocks))
    valid_states = set()

    for perm in permutations:
        # Try all possible ways to assign blocks to towers with bounded height
        def backtrack(i, towers):
            if i == len(perm):
                state = tuple(tuple(t) for t in towers)
                valid_states.add(state)
                return

            for t_idx in range(num_towers):
                if len(towers[t_idx]) < tower_heights[t_idx]:
                    towers[t_idx].append(perm[i])
                    backtrack(i + 1, towers)
                    towers[t_idx].pop()

        backtrack(0, [[] for _ in range(num_towers)])

    return len(valid_states)


# Test cases
def run_tests():
    result1 = count_permutations_wrapper(c=1, n=10, k=2, h=10)
    print(f"Test case 1 result: {result1}")
    assert (
        result1 == 11
    ), f"Test case 1 failed: (c=1, n=10, k=2, h=10) should return 11, but got {result1}."

    result2 = count_permutations_wrapper(c=2, n=2, k=3, h=2)
    print(f"Test case 2 result: {result2}")
    assert (
        result2 == 36
    ), f"Test case 2 failed: (c=2, n=2, k=3, h=2) should return 36, but got {result2}."

    result3 = count_permutations_wrapper(c=3, n=1, k=4, h=2)
    print(f"Test case 3 result: {result3}")
    assert (
        result3 == 96
    ), f"Test case 3 failed: (c=3, n=1, k=4, h=2) should return 96, but got {result3}."

    print(count_permutations_wrapper(c=3, n=2, k=4, h=2))
    print(count_permutations_wrapper(c=3, n=2, k=4, h=3))

    print("All test cases passed.")


run_tests()
