import numpy as np
import random

A = np.array([[0.1,0.2,0.7],[0.3,0.4,0.3],[0.5,0.4,0.1]])
B = np.array([[0.1,0.1,0.1,0.3,0.4],[0.5,0.5,0.0,0.0,0.0],[0.2,0.2,0.2,0.2,0.2]])
pi = np.array([1.0,0.0,0.0])

N = 3
M = 5

T = 30

alpha = [0 for i in range(N)]
o = [random.randint(0,M-1) for i in range(T)]

print(o)

#---- 前向きアルゴリズム
# 1
for i in range(N):
    alpha[i] = pi[i] * B[i,o[0]]

# 2
for t in range(T-1):
    alpha_new = [0 for i in range(N)]
    for j in range(N):
        alpha_new[j] = np.array(alpha).dot(A)[j] * B[j,o[t+1]]
    alpha = alpha_new

# 3
P_forward = sum(alpha)


#---- 後向きアルゴリズム
# 1
beta = [1 for i in range(N)]

# 2
for t in range(T-2,-1,-1):
    beta_new = [0 for i in range(N)]
    for i in range(N):
        for j in range(N):
            beta_new[i] += A[i,j] * B[j,o[t+1]] * beta[j]
    beta = beta_new

# 3
P_backward = sum(pi[i] * B[i,o[0]] * beta[i] for i in range(N))


print(P_forward, P_backward)
