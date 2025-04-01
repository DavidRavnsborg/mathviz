import sympy as sp
import itertools
import time
import math

# Define symbols for x and y (affine coordinates)
x, y = sp.symbols("x y", real=True)

tol = 1e-6  # numerical tolerance


def polygon_vertices(n):
    """Return vertices of a regular n-gon on the unit circle in homogeneous coordinates (x, y, 1)."""
    return [
        (sp.N(sp.cos(2 * sp.pi * k / n)), sp.N(sp.sin(2 * sp.pi * k / n)), 1)
        for k in range(n)
    ]


def homogeneous_to_affine(pt):
    """Convert a homogeneous point (x,y,w) to affine coordinates (float(x/w), float(y/w))."""
    x_val, y_val, w_val = pt
    return (float(x_val / w_val), float(y_val / w_val))


def line_from_two_points(P, Q):
    """
    Given two points P=(x1,y1,w1) and Q=(x2,y2,w2) in homogeneous coordinates,
    return the line in standard form: a*x + b*y + c = 0.
    """
    x1, y1, w1 = P
    x2, y2, w2 = Q
    a = sp.N(y1 * w2 - y2 * w1)
    b = sp.N(w1 * x2 - w2 * x1)
    c = sp.N(x1 * y2 - x2 * y1)
    return (a, b, c)


def on_segment(P, Q, R, tol=1e-6):
    """
    Check whether point R (an (x,y) tuple of floats) lies on the segment between P and Q.
    Returns True if R is between P and Q (within tolerance), False otherwise.
    """
    # Convert to floats
    Px, Py = float(P[0]), float(P[1])
    Qx, Qy = float(Q[0]), float(Q[1])
    Rx, Ry = float(R[0]), float(R[1])
    # Check collinearity via cross product (determinant)
    det = (Qx - Px) * (Ry - Py) - (Qy - Py) * (Rx - Px)
    if abs(det) > tol:
        return False
    # Solve for t in R = P + t*(Q-P)
    if abs(Qx - Px) > tol:
        t = (Rx - Px) / (Qx - Px)
    else:
        t = (Ry - Py) / (Qy - Py)
    return -tol <= t <= 1 + tol


def all_diagonals(n):
    """
    For an n-gon with vertices labeled 0,...,n-1 (in cyclic order),
    return a list of pairs (i,j) with i < j that represent a diagonal
    (i.e. skip pairs that are adjacent modulo n).
    """
    diagonals = []
    for i, j in itertools.combinations(range(n), 2):
        if j == i + 1 or (i == 0 and j == n - 1):
            continue
        diagonals.append((i, j))
    return diagonals


def line_intersection(L1, L2):
    """Given two lines L1=(a1,b1,c1) and L2=(a2,b2,c2), solve for the intersection point (x,y) using sp.linsolve."""
    a1, b1, c1 = L1
    a2, b2, c2 = L2
    sol = sp.linsolve([a1 * x + b1 * y + c1, a2 * x + b2 * y + c2], (x, y))
    if sol:
        sol = next(iter(sol))
        return (float(sol[0]), float(sol[1]))
    return None


def polygon_intersections(n):
    """
    Compute the unique intersection points (affine coordinates as floats) of all diagonal segments
    of a regular n-gon. Only retain intersections that lie on both segments.
    """
    vertices = polygon_vertices(n)
    diag_indices = all_diagonals(n)
    # Precompute affine vertices for segment checks
    aff_vertices = [homogeneous_to_affine(v) for v in vertices]

    # Compute the line (a, b, c) for each diagonal
    lines = {}
    for i, j in diag_indices:
        P = vertices[i]
        Q = vertices[j]
        lines[(i, j)] = line_from_two_points(P, Q)

    intersections = []
    # Loop over every pair of diagonals that do NOT share a vertex
    for (i1, j1), (i2, j2) in itertools.combinations(diag_indices, 2):
        if len({i1, j1} & {i2, j2}) != 0:
            continue
        pt = line_intersection(lines[(i1, j1)], lines[(i2, j2)])
        if pt is not None:
            P1 = aff_vertices[i1]
            Q1 = aff_vertices[j1]
            P2 = aff_vertices[i2]
            Q2 = aff_vertices[j2]
            if on_segment(P1, Q1, pt, tol) and on_segment(P2, Q2, pt, tol):
                intersections.append(pt)
    # Remove duplicates (using numerical tolerance)
    unique = []
    for pt in intersections:
        found = False
        for u in unique:
            if math.isclose(pt[0], u[0], abs_tol=tol) and math.isclose(
                pt[1], u[1], abs_tol=tol
            ):
                found = True
                break
        if not found:
            unique.append(pt)
    return unique, intersections


if __name__ == "__main__":
    for n in [4, 5, 6, 7, 8, 9, 10, 11, 12]:
        start = time.time()
        unique_pts, pts = polygon_intersections(n)
        end = time.time()
        print(
            f"n = {n} unique intersection count: {len(unique_pts)}; total intersection count: {len(pts)} (computed in {end - start:.3f} sec)"
        )
        # for pt in pts:
        #     print(pt)
        # print()
    # for n in list(range(3, 29, 2)):
    # for n in list(range(29, 51, 2)):
    #     start = time.time()
    #     unique_pts, pts = polygon_intersections(n)
    #     end = time.time()
    #     if len(unique_pts) != len(pts):
    #         print("UNIQUE AND TOTAL INTERSECTION COUNT DO NOT MATCH!!!")
    #     print(
    #         f"n = {n} unique intersection count: {len(unique_pts)}; total intersection count: {len(pts)} (computed in {end - start:.3f} sec)"
    #     )
