import numpy as np
import pandas as pd

# Parameters
gamma = 1.5
theta = 0.01


def update_share(X, gamma=gamma, theta=theta):
    """
    Compute the next expected vote-share vector for given X.
    """
    w = (X + theta) ** gamma
    return w / w.sum()


def compute_X10(X0, steps=10):
    X = X0.copy()
    for _ in range(steps):
        X = update_share(X)
    return X


# Initial states
X0_1 = np.array([0.3, 0.3, 0.2, 0.1, 0.1])
X0_2 = np.array([0.2, 0.3, 0.2, 0.15, 0.15])

# Compute X10 for both
X10_1 = compute_X10(X0_1)
X10_2 = compute_X10(X0_2)

# Count how many parties >= 0.10
count_1 = np.sum(X10_1 >= 0.10)
count_2 = np.sum(X10_2 >= 0.10)

# Prepare DataFrame for display
results = pd.DataFrame(
    {
        "Party": ["A", "B", "C", "D", "E"],
        "X10_from_0.3,0.3,0.2,0.1,0.1": X10_1,
        "X10_from_0.2,0.3,0.2,0.15,0.15": X10_2,
    }
)
results[">=10% in scenario 1?"] = results["X10_from_0.3,0.3,0.2,0.1,0.1"] >= 0.10
results[">=10% in scenario 2?"] = results["X10_from_0.2,0.3,0.2,0.15,0.15"] >= 0.10

# Also print counts
print(f"Number of parties with ≥10% in first scenario: {int(count_1)}")
print(f"Number of parties with ≥10% in second scenario: {int(count_2)}")
