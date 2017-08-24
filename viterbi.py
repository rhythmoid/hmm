import numpy as np
import random

A = np.array([[0.1,0.2,0.7],[0.3,0.4,0.3],[0.5,0.4,0.1]])
B = np.array([[0.1,0.1,0.1,0.3,0.4],[0.5,0.5,0.0,0.0,0.0],[0.2,0.2,0.2,0.2,0.2]])
pi = np.array([1.0,0.0,0.0])

N = 3
M = 5

T = 30

o = [random.randint(0,M-1) for i in range(T)]

print(o)

#---- Viterbiアルゴリズム
# 1
delta = [pi[i] * B[i,o[0]] for i in range(N)]
psi = np.zeros((T,N))

# 2
for t in range(T-1):
    delta_new = [0 for i in range(N)]
    for j in range(N):
        da = [delta[i] * A[i,j] for i in range(N)]
        delta_new[j] = max(da) * B[j,o[t+1]]
        psi[t+1,j] = np.argmax(da)
    delta = delta_new

# 3
P = max(delta)
q = [0 for _ in range(T)]
q[T-1] = np.argmax(delta)

# 4
for t in range(T-2,-1,-1):
    q[t] = int(psi[t+1,q[t+1]])


print(P,q)
