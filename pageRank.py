import numpy as np

# Step 1: Create adjacency matrix
M = np.array([[0,1,1,0],
              [1,0,0,0],
              [0,1,0,1],
              [0,0,1,0]])

# Step 2: PageRank Algorithm
def page_rank(M, d=0.85, tol=1e-6, max_iter=100):
    n = len(M)
    outlinks = np.sum(M, axis=0)
    outlinks[outlinks == 0] = 1
    M_hat = M / outlinks
    PR = np.ones(n) / n
    for _ in range(max_iter):
        new_PR = (1-d)/n + d * M_hat.dot(PR)
        if np.linalg.norm(new_PR - PR, 1) < tol:
            break
        PR = new_PR
    return PR

PR = page_rank(M)
print("PageRank Scores:", PR)

# Step 3: HITS Algorithm
def hits(M, max_iter=100, tol=1e-6):
    n = len(M)
    auth = np.ones(n)
    hub = np.ones(n)
    for _ in range(max_iter):
        new_auth = M.T.dot(hub)
        new_hub = M.dot(new_auth)
        new_auth /= np.linalg.norm(new_auth, 2)
        new_hub /= np.linalg.norm(new_hub, 2)
        if np.linalg.norm(new_auth - auth) < tol:
            break
        auth, hub = new_auth, new_hub
    return auth, hub

auth, hub = hits(M)
print("Authority Scores:", auth)
print("Hub Scores:", hub)
