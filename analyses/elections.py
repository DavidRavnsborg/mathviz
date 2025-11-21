# A new democracy has 5 political parties: $A$, $B$, $C$, $D$ and $E$. Each party's support prior to the election is represented by the state vector:
# \[
# X_0 = \begin{pmatrix} 0.2 \\ 0.2 \\ 0.2 \\ 0.2 \\ 0.2 \end{pmatrix}
# \]

# Each element represents the proportion of the voting population that supports that party (party $A$ is row 1, party $B$ is row 2, and so on). Thus, given a starting state $X_0$ (and three additional parameters $\gamma$, $\theta$, and $\epsilon$), the outcome of this country's elections can be modeled using a discrete-time Markov Chain, where $X_1$ represents the outcome of the first election, $X_2$ represents the outcome of the second election, and $X_t$ represents the outcome of the $t$-th election where:
# \[
# X_t = \begin{pmatrix} X_t^A \\ \vdots \\ X_t^E \end{pmatrix}
# \]

# The transition between states can be modeled by the transition matrix/kernel, which satisfies:
# \[
# Pr(X_{t+1} | X_t, X_{t-1}, \cdots) = Pr(X_{t+1} | X_t) = P_{X_t, X_{t+1}}(X_t, \gamma, \theta, \epsilon) = shock(Q_t)
# \]

# and the elements of $Q_{X_t, X_{t+1}}$ are computed first by:
# \[
# p_ij(X_t) = \frac{(X_t^j + \theta)^\gamma}{\sum_{k=1}^5(X_t^k + \theta)^\gamma}
# \] then a probability $\epsilon$ determines if there is a shock, in which case one party transitions an extra 0.1 from itself to another party, where the gaining and losing elements are selected according to a uniform distribution for each. Example: with $\epsilon =0.5$ and 5 parties,

# Given $\gamma = 1.5$, $\theta = 0.01$, and $\epsilon = 0.1$ how many parties are expected to receive at least 10% of the vote as $\lim_{t\to\infty}$?


# A new democracy has five parties $A$, $B$, $C$, $D$, and $E$.
# Each party's support among the voting age population is represented by the following state vector after election $t$
# \[
# X_t = \begin{pmatrix} X_t^A \\ X_t^B \\ X_t^C \\ X_t^D \\ X_t^E \end{pmatrix}
# \]
# such that $\sum_i X_t^i = 1$ and $X_t^i \ge 0$.

# Prior to the first election, the starting state is:
# \[
# X_0 = \begin{pmatrix} 0.2 \\ 0.2 \\ 0.2 \\ 0.2 \\ 0.2 \end{pmatrix}
# \]

# X_t is time-inhomogenous...


# <Some ChatGPT output>


# No, I want an analytical approach. I don't want it to have to know the previous initial conditions. I want it to be able to check the current conditions and determine whether lock-in is inevitable. That value should be tau + a little bit, as far as I can see. This makes sense logically too. You can get a surprise rebound up to the value of tau from the other states if the Dirichlet distribution gives a value of 1 for a particular party for every other party. This is in addition to the base amount from b. I have noticed too that the contribution from b is maximized when the other party support is most evenly distributed, so the maximum contribution possible comes from assuming the other support is (1 - starting_support) / len(X).

# I have a proposal. I constructed a recursive function for the maximum possible next value, given an arbitrary number of values, and I believe the true threshold can be found as the function always seems to converge. However, it is very sensitive to the starting value of gamma. For instance, given tau=0.04, changing gamma from 1.5 to 1.55 causes the value it converges to to change massively (>0.9 vs. <0.1). Also, the function seems to converge to 2 different values when gamma is higher (from a bit under 1.55 and up) and to only 1 higher value when gamma is lower (from a bit over 1.5 and down).

# Function:
# state_value can be anything from 0 to 1. It can represent a low or high value, and it will converge over time.
# (1 - tau) * state_value^gamma /
