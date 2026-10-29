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

omegas = [1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9] # relaxation parameters to try (1.0 = original Gauss-Seidel)
tol = 1e-6 # stop when the largest change in one sweep is below this

results = [] # (omega, iterations) for each run
print(f"{'omega':>6} {'iterations':>11} {'vs omega=1':>11}") # table header

for omega in omegas: # repeat the original solve for each omega
    u_sol = np.empty((len_x, len_y))
    u_sol.fill(u_grid)


    u_sol[:, -1] = u_top
    u_sol[:, 0] = u_bottom
    u_sol[0, :] = u_right
    u_sol[-1, :] = u_left

    for iteration in range(1, 10000): # stops early below
        max_change = 0 
        for i in range(1, len_x-1):
            for j in range(1, len_y-1):
                u_gs = 0.25 * (u_sol[i+1][j] + u_sol[i-1][j] + u_sol[i][j+1] + u_sol[i][j-1])
                u_new = (1 - omega) * u_sol[i, j] + omega * u_gs # SOR update
                max_change = max(max_change, abs(u_new - u_sol[i, j]))
                u_sol[i, j] = u_new
        if max_change < tol:
            break

    results.append((omega, iteration))
    print(f"{omega:6.2f} {iteration:11d} {iteration / results[0][1]:11.2f}") # one row per omega

best_omega, best_iter = min(results, key=lambda r: r[1])
print(f"\nbest omega = {best_omega}: {best_iter} iterations "
      f"({results[0][1] / best_iter:.1f}x fewer than Gauss-Seidel)")

plt.figure(figsize=(10, 5))
plt.contourf(X, Y, u_sol, 1000, cmap='jet')
plt.colorbar(ticks=[0, 20, 40, 60, 80, 100, 120])
plt.show()