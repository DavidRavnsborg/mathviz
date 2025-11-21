import numpy as np


def f(v, gamma, tau, N):
    """
    One-step max-growth mapping for a single party with share v,
    assuming the other N-1 parties split (1-v) evenly.
    """
    other = (1 - v) / (N - 1)
    # baseline b
    b = v**gamma / (v**gamma + (N - 1) * other**gamma)
    # add noise
    return (1 - tau) * b + tau * (1 - v)


def find_threshold(N, gamma, tau, tol=1e-6):
    """
    Find the unstable fixed point v* solving v = f(v) in (0,1).
    Returns v* if found, else None.
    """
    # sample grid for sign changes of g(v)=f(v)-v
    vs = np.linspace(0, 1, 2001)
    gs = f(vs, gamma, tau, N) - vs
    roots = []
    for i in range(len(vs) - 1):
        if gs[i] == 0:
            roots.append(vs[i])
        elif gs[i] * gs[i + 1] < 0:
            a, b = vs[i], vs[i + 1]
            ga, gb = gs[i], gs[i + 1]
            # bisection
            for _ in range(50):
                m = 0.5 * (a + b)
                gm = f(m, gamma, tau, N) - m
                if ga * gm <= 0:
                    b, gb = m, gm
                else:
                    a, ga = m, gm
            roots.append(0.5 * (a + b))
    # filter interior roots
    roots = sorted(set(roots))
    interior = [r for r in roots if tol < r < 1 - tol]
    if not interior:
        return None
    # # if multiple interior, unstable is the middle root
    # return interior[len(interior) // 2]
    # # instead of the unstable middle root, pick the lowest to match your calculator algorithm
    # return interior[0]
    # or, instead return all roots
    return interior


def threshold_lock_in(X0, gamma, tau):
    """
    Analytic lock-in check using recursive threshold:
    - Compute threshold v* (unstable fixed point).
    - Return (will_lock_in, threshold).
    """
    X0 = np.array(X0, dtype=float)
    N = len(X0)
    leader_share = X0.max()
    thresholds = find_threshold(N, gamma, tau)
    # Grab the lowest threshold
    threshold = thresholds[0]
    if threshold is None:
        return False, None
    return leader_share > threshold, thresholds


# Example usage
if __name__ == "__main__":
    # X0 = [0.8, 0.05, 0.05, 0.05, 0.05]
    X0 = [0.2, 0.2, 0.2, 0.2, 0.2]
    gamma = 1.5
    tau = 0.04
    lock, thresholds = threshold_lock_in(X0, gamma, tau)
    if thresholds:
        formatted = ", ".join(f"{v:.6f}" for v in thresholds)
    else:
        formatted = "none"
    print(f"Thresholds v* = {formatted}, lock-in = {lock}")
