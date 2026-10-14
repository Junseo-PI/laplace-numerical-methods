import numpy as np
import matplotlib.pylab as plt


def LaplaceNeumann(len_x, len_y, u_top, u_right):
    x = np.linspace(0, len_x, len_x+1)
    y = np.linspace(0, len_y, len_y+1)

    X, Y = np.meshgrid(x, y)
    grid_X, grid_Y = np.meshgrid(np.linspace(0, 10, len_x), np.linspace(0, 5, len_y))

    u_new = np.zeros_like(X)

    u_new[-1, :] = u_top
    u_new[:, -1] = u_right  # set neumann bc

    for iteration in range(1, 10000):
        for i in reversed(range(len_y)):
            for j in reversed(range(len_x)):
                if i == 0 and j == 0:
                    break
                elif i == 0:
                    u_new[i][j] = u_new[i + 2][j]
                elif j == 0:
                    u_new[i][j] = u_new[i][j + 2]
                else:
                    if (i == 1 and j == 0) or (i == 0 and j == 4):
                        break
                    else:
                        u_new[i][j] = 0.25 * (u_new[i + 1][j] + u_new[i - 1][j] + u_new[i][j + 1] + u_new[i][j - 1])

    u_new = np.delete(u_new, 0, 0)
    u_new = np.delete(u_new, 0, 1)

    print(u_new)

    plt.figure(figsize=(10, 5))
    plt.contourf(grid_X, grid_Y, u_new, 1000, cmap='jet')
    plt.colorbar(ticks=[0, 20, 40, 60, 80, 100, 120])
    plt.show()


if __name__ == '__main__':
    u_top = 120
    u_right = 20

    len_x = 100
    len_y = 50

    LaplaceNeumann(len_x, len_y, u_top, u_right)
