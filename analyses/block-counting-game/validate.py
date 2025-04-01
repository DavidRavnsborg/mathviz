import math


def count_game_state(c, n, k, h):
    """
    Compute the total number of game state permutations.

    Parameters:
      c (int): number of colors.
      n (int): number of blocks per color.
      k (int): number of towers.
      h (int): maximum height of each tower.

    Returns:
      int: total number of game state permutations.

    The function first counts the number of ways to distribute
    the c*n blocks among k towers (each tower holding at most h blocks)
    using inclusion-exclusion. Then it multiplies by the number of ways
    to assign colors (with n copies per color) to the block positions.
    """

    total_blocks = c * n
    # Maximum j in the inclusion-exclusion sum:
    max_j = total_blocks // (h + 1)
    distributions = 0
    for j in range(max_j + 1):
        term = (
            ((-1) ** j)
            * math.comb(k, j)
            * math.comb(total_blocks - j * (h + 1) + k - 1, k - 1)
        )
        distributions += term

    color_assignments = math.factorial(total_blocks) // (math.factorial(n) ** c)
    return distributions * color_assignments


# Example usage:
if __name__ == "__main__":
    # For example, the case c=3, n=1, k=4, h=2:
    # Total blocks = 3. The distributions count (via inclusion–exclusion) is computed as follows:
    #   For j = 0:
    #      term = comb(4,0) * comb(3 - 0*3 + 4 - 1, 3) = 1 * comb(6,3) = 20.
    #   For j = 1:
    #      term = - comb(4,1) * comb(3 - 1*3 + 4 - 1, 3) = -4 * comb(3,3) = -4.
    #   Sum of distributions = 20 - 4 = 16.
    #
    # The color assignments are 3! = 6 (since we have 3 distinct blocks).
    # Thus the total should be 16 * 6 = 96.

    result = count_game_state(c=1, n=10, k=2, h=10)
    print("For c=1, n=10, k=2, h=10, the number of permutations is:", result)
    result = count_game_state(c=2, n=2, k=3, h=2)
    print("For c=2, n=2, k=3, h=2, the number of permutations is:", result)
    result = count_game_state(c=3, n=1, k=4, h=2)
    print("For c=3, n=1, k=4, h=2, the number of permutations is:", result)
    result = count_game_state(c=3, n=2, k=4, h=2)
    print("For c=3, n=2, k=4, h=2, the number of permutations is:", result)
    result = count_game_state(c=3, n=2, k=4, h=3)
    print("For c=3, n=2, k=4, h=3, the number of permutations is:", result)
    result = count_game_state(c=3, n=1, k=5, h=2)
    print("For c=3, n=1, k=5, h=2, the number of permutations is:", result)
    result = count_game_state(c=3, n=2, k=5, h=2)
    print("For c=3, n=2, k=5, h=2, the number of permutations is:", result)
    result = count_game_state(c=3, n=2, k=5, h=3)
    print("For c=3, n=2, k=5, h=3, the number of permutations is:", result)
    result = count_game_state(c=4, n=1, k=5, h=2)
    print("For c=4, n=1, k=5, h=2, the number of permutations is:", result)
    result = count_game_state(c=4, n=2, k=5, h=2)
    print("For c=4, n=2, k=5, h=2, the number of permutations is:", result)
