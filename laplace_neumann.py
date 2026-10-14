import numpy as np
import scipy
import scipy.linalg
import scipy.sparse
import scipy.sparse.linalg
import matplotlib.pylab as plt


def setup_LaplaceNeumann_xy(Ttop, Tright, nx, ny):
    n = (nx) * (ny)
    d = np.ones(n)  # make a size=n array filled with 1
    b = np.zeros(n)  # make a size=n array filled with 0

    d0 = d.copy() * -4
    d1_lower = d.copy()[0:-1]
    d1_upper = d1_lower.copy()

    dnx_lower = d.copy()[0:-nx]
    dnx_upper = dnx_lower.copy()

    d1_lower[nx - 1::nx] = 0
    d1_upper[nx - 1::nx] = 0
    d1_upper[::nx] = 2

    dnx_upper[0:nx] = 2

    b[-nx:] = -Ttop
    b[nx - 1::nx] += -Tright

    A = scipy.sparse.diags([d0, d1_upper, d1_lower, dnx_upper, dnx_lower], [0, 1, -1, nx, -nx], format='csc')

    return A, b


def plot_SurfaceNeumann_xy(Temp, Ttop, Tright, xmax, ymax, Nx, Ny):
    x = np.linspace(0, xmax, Nx + 1)
    y = np.linspace(0, ymax, Ny + 1)

    X, Y = np.meshgrid(x, y)

    T = np.zeros_like(X)

    T[-1, :] = Ttop
    T[:, -1] = Tright
    k = 1
    for j in range(Ny):
        T[j, :-1] = Temp[Nx * (k - 1):Nx * k]
        k += 1

    plt.figure(figsize=(10, 5))

    plt.contourf(X, Y, T, 1000, cmap='jet')

    plt.colorbar(ticks=[20, 40, 60, 80, 100, 120])
    plt.title("Laplace's Equation with Neumann Boundary Conditions")
    plt.show()


if __name__ == '__main__':
    Ttop = 120
    Tright = 20

    len_x = 10
    len_y = 5

    Nx = 20
    Ny = 10

    A, b = setup_LaplaceNeumann_xy(Ttop, Tright, Nx, Ny)

    Temp = scipy.sparse.linalg.spsolve(A, b)

    # print(A)
    # print(b)
    # print(Temp)

    plot_SurfaceNeumann_xy(Temp, Ttop, Tright, len_x, len_y, Nx, Ny)