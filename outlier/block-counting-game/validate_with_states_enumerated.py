import math
import itertools


def unique_permutations(iterable):
    """
    Yield unique permutations of the iterable.
    (This helper avoids duplicates when elements are repeated.)
    """
    seen = set()
    for perm in itertools.permutations(iterable):
        if perm not in seen:
            seen.add(perm)
            yield perm


def game_states(c, n, k, h, colors=None):
    """
    Computes the number of valid game states (or thecolors
      list of states if requested)
    for a sorting game with:
      c = number of colors
      n = blocks per color (and tower height)
      k = number of towers (each tower has a capacity of n)

    The game has a total of c*n blocks that are to be distributed among k towers,
    subject to each tower holding between 0 and n blocks. The state is represented
    as a string with towers separated by "|" and each tower represented as an n-length
    string. Occupied positions show the block’s color, and unoccupied positions are "0".

    If list_combinations is False (default), the function returns just the count.
    If list_combinations is True, it returns a sorted list of configuration strings.
    """
    # Use default colors if not provided (e.g. "R", "B", "G", …)
    if colors is None:
        default_colors = "RBGYOPC"
        colors = list(default_colors[:c])

    total_blocks = c * n

    # Step 1: Generate all valid distributions of blocks among towers.
    # A distribution is a k-tuple (h1, h2, ..., hk) where each hi is in 0..n
    # and h1 + h2 + ... + hk = total_blocks.
    distributions = []
    for dist in itertools.product(range(h + 1), repeat=k):
        if sum(dist) == total_blocks:
            distributions.append(dist)
    # For example, with c=1, n=10, k=2, there are 11 solutions to h1+h2=10.
    # With c=2, n=2, k=3, direct enumeration shows there are 6 valid distributions.

    # Step 2: Compute the number of assignments for each distribution.
    # Regardless of distribution, the number of ways to assign the colors to the
    # occupied positions is given by the multinomial:
    #   (c*n)! / (n!)^c
    count_assignments = math.factorial(total_blocks)
    for _ in range(c):
        count_assignments //= math.factorial(n)

    # Step 3 (only if listing): Build the list of configuration strings.
    #
    # Prepare the multiset of blocks: each color appears n times.
    blocks = []
    for color in colors:
        blocks.extend([color] * n)
    # Generate all unique permutations (each is a tuple of length total_blocks).
    unique_assignments = list(unique_permutations(blocks))

    # Step 4: For each distribution and each unique block assignment, fill the towers.
    # For a given distribution, each tower i gets its first h_i blocks from the assignment,
    # and then we pad with "0" to length n.
    config_list = []
    for assignment in unique_assignments:
        for dist in distributions:
            config_parts = []
            index = 0
            for height in dist:
                # Get the h blocks for this tower and pad with "0" if needed.
                tower_str = "".join(assignment[index : index + height]) + "0" * (
                    n - height
                )
                config_parts.append(tower_str)
                index += height
            config_list.append("|".join(config_parts))

    config_list.sort()

    total_count = len(distributions) * count_assignments

    return config_list, total_count


# Example usage:
if __name__ == "__main__":
    list_combinations = False

    states, count = game_states(c=1, n=10, k=2, h=10)
    print("c=1, n=10, k=2, h=10; Total number of states:", len(states))
    assert len(states) == count
    assert len(states) == len(set(states))
    if list_combinations:
        print("Configurations:")
        for state in states:
            print(state)

    states, count = game_states(c=2, n=2, k=3, h=2)
    print("c=2, n=2, k=3, h=2; Total number of states:", len(states))
    assert len(states) == count
    assert len(states) == len(set(states))
    if list_combinations:
        print("Configurations:")
        for state in states:
            print(state)

    states, count = game_states(c=3, n=1, k=4, h=2)
    print("c=3, n=1, k=4, h=2; Total number of states:", len(states))
    assert len(states) == count
    assert len(states) == len(set(states))
    if list_combinations:
        print("Configurations:")
        for state in states:
            print(state)

    states, count = game_states(c=3, n=2, k=4, h=2)
    print("c=3, n=2, k=4, h=2; Total number of states:", len(states))
    assert len(states) == count
    assert len(states) == len(set(states))
    if list_combinations:
        print("Configurations:")
        for state in states:
            print(state)

    states, count = game_states(c=3, n=2, k=4, h=3)
    print("c=3, n=2, k=4, h=3; Total number of states:", len(states))
    assert len(states) == count
    assert len(states) == len(set(states))
    if list_combinations:
        print("Configurations:")
        for state in states:
            print(state)
