import numpy as np

"""
Resources:
https://chatgpt.com/g/g-p-679832501f4081918c5361b9ebda12c2-beetlewizards/c/681bc4bd-4790-8007-a831-7630950905a4
https://chatgpt.com/g/g-p-679832501f4081918c5361b9ebda12c2-beetlewizards/c/681b8805-709c-8007-802f-fbdbb7702b32
"""


def iterate_state(X0, gamma, tau, n, record=False):
    """
    Simulate the Markov chain with state vector X0, parameters gamma and tau, for n steps.
    If record is True, returns an array of shape (n+1, K) of all state vectors from X0 through X_n.
    If record is False (default), returns only the state vector at step n.
    """
    X = np.array(X0, dtype=float)
    rng = np.random.default_rng()

    # Prepare trajectory recording if needed
    if record:
        trajectory = [X.copy()]

    for _ in range(n):
        # baseline softmax b_j
        b = X**gamma
        b = b / b.sum()

        # build transition matrix P
        K = len(X)
        P = np.zeros((K, K))

        for i in range(K):
            # sample Dirichlet noise for row i
            w = rng.dirichlet(np.ones(K))
            P[i, :] = (1 - tau) * b + tau * w

        # update state: X <- X @ P
        X = X @ P

        if record:
            trajectory.append(X.copy())

    return np.array(trajectory) if record else X


def lock_in_condition(X, gamma, tau):
    """
    Determine if parameters gamma and tau guarantee absorption (lock-in) to a single party from X.
    Returns True if guaranteed, False otherwise.
    """
    X = np.array(X, dtype=float)
    if gamma <= 1:
        # No positive extinction threshold if gamma <= 1
        return False

    # baseline softmax
    b = X**gamma
    b = b / b.sum()

    # extinction threshold
    threshold = (1 - tau) ** (1 / (gamma - 1))

    # Check if all non-winning parties start below or equal to threshold (1st),
    # and if any non-winning parties start below or equal to threshold (2nd).
    losers = np.delete(b, np.argmax(X))
    return np.all(losers <= threshold), np.any(losers <= threshold)


def improved_lock_in_condition(X0, gamma, tau):
    """
    Analytic test for guaranteed absorption (lock-in) from X0.
    Uses the worst-case noise boost: any party j can at most jump from (1-tau)*b_j up to (1-tau)*b_j + tau.
    We guarantee j will decline if (1-tau)*b_j + tau < X0[j].
    If every non-winning party satisfies that, lock-in is guaranteed.
    """
    X0 = np.array(X0, dtype=float)
    if gamma <= 1:
        return False

    # baseline softmax b_j
    b = X0**gamma
    b /= b.sum()

    # identify losers (exclude the current leading party)
    i_star = np.argmax(X0)
    losers_idx = [j for j in range(len(X0)) if j != i_star]

    # worst-case next share for each loser
    # max_boost = tau, min_shrink = 0
    # so X1_j <= (1-tau)*b_j + tau
    X0_losers = X0[losers_idx]
    b_losers = b[losers_idx]
    X1_max = (1 - tau) * b_losers + tau
    print(X1_max)
    print(X0_losers)

    # require X1_max < X0_losers for each loser -> guaranteed decline
    return np.all(X1_max < X0_losers)


# Example usage to record trajectory:
if __name__ == "__main__":
    # X0 = [0.8, 0.05, 0.05, 0.05, 0.05]
    # X0 = [0.824, 0.044, 0.044, 0.044, 0.044]
    X0 = [0.24, 0.19, 0.19, 0.19, 0.19]
    gamma = 2.0
    tau = 0.04
    n_steps = 1

    results = {}
    party_A_results = []
    count = 0
    while True:
        count += 1
        result = iterate_state(X0, gamma, tau, n_steps, record=True)
        if (
            result[-1][1] > 0.19
            or result[-1][2] > 0.19
            or result[-1][3] > 0.19
            or result[-1][4] > 0.19
        ):
            print(count)
            print(result)
            break
        elif count % 100 == 0:
            print(count)
    # for i in range(1000):
    #     result = iterate_state(X0, gamma, tau, n_steps, record=True)
    #     party_A_results.append(result[-1][0])
    #     if result[-1][0] < 0.7:
    #         results[i] = result
    # hist, bins = np.histogram(party_A_results, bins=np.arange(0, 1.1, 0.1))
    # print(hist)
    # print(bins)
    # print(results)
    # guaranteed_absorption, guaranteed_extinction = lock_in_condition(X0, gamma, tau)
    # # print(f"Starting conditions guarantee absorption: {guaranteed_absorption}")
    # # print(f"Starting conditions guarantee extinction: {guaranteed_extinction}")

    # # Get only final state
    # print(f"Initial state: {X0}")
    # trajectory = iterate_state(X0, gamma, tau, n_steps, record=True)
    # print(f"Final state: {trajectory[-1]}")
    # # print(f"Trajectory shape: {trajectory.shape}")
    # # # print("Trajectory:", trajectory)

    # # for i, X in enumerate(trajectory):
    # #     guaranteed_absorption, guaranteed_extinction = lock_in_condition(X0, gamma, tau)
    # #     if guaranteed_absorption:
    # #         print(f"Guaranteed absorption @ {i}: {X}")
    # #     elif guaranteed_extinction:
    # #         print(f"Guaranteed extinction @ {i}: {X}")
    # print(
    #     f"Mean support for Party A: {np.array([traj[0] for traj in trajectory]).mean()}"
    # )
    # print(
    #     f"Mean support for Party B: {np.array([traj[1] for traj in trajectory]).mean()}"
    # )
    # print(
    #     f"Mean support for Party C: {np.array([traj[2] for traj in trajectory]).mean()}"
    # )
    # print(
    #     f"Mean support for Party D: {np.array([traj[3] for traj in trajectory]).mean()}"
    # )
    # print(
    #     f"Mean support for Party E: {np.array([traj[4] for traj in trajectory]).mean()}"
    # )
