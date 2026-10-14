import numpy as np
import matplotlib.pyplot as plt

len_x = 10
len_y = 5

X, Y = np.meshgrid(np.arange(0, len_x), np.arange(0, len_y), indexing='ij')

u_top = 120
u_bottom = 0
u_left = 20
u_right = 20

u_grid = 30

u_sol = np.empty((len_x, len_y))
u_sol.fill(u_grid)


u_sol[:, -1] = u_top
u_sol[:, 0] = u_bottom
u_sol[0, :] = u_right
u_sol[-1, :] = u_left

for iteration in range(1, 100):
    for i in range(1, len_x-1):
        for j in range(1, len_y-1):
            u_sol[i, j] = 0.25 * (u_sol[i+1][j] + u_sol[i-1][j] + u_sol[i][j+1] + u_sol[i][j-1])


plt.figure(figsize=(10, 5))
plt.contourf(X, Y, u_sol, 1000, cmap='jet')
plt.colorbar(ticks=[0, 20, 40, 60, 80, 100, 120])
plt.show()