# Numerical Methods for Laplace's Equation on a Rectangular Region

![Python](https://img.shields.io/badge/Python-3-blue)
![NumPy](https://img.shields.io/badge/NumPy-SciPy-orange)

Undergraduate research project — **MATH 496, University of Illinois Chicago (Fall 2022)**
Advised by Prof. Shokouh Pourarian, with McLean Milavickas.

We solved the steady-state heat equation (Laplace's Equation) on a 10 x 5 rectangle with a hot top edge (120°) and compared several numerical approaches.

📄 [Final presentation (PDF)](final-presentation.pdf)

## Approaches

| File | Boundary condition | Method |
|---|---|---|
| `laplace_solution.py` | Dirichlet (fixed temperature on all four edges) | Iterative 5-point averaging (Gauss–Seidel) |
| `laplace_neumann_central.py` | Neumann (insulated left and bottom edges) | Iterative, using ghost points |
| `laplace_neumann.py` | Neumann | Sparse linear system `A T = b`, solved directly with SciPy |


## How to run

```bash
pip install numpy scipy matplotlib
python3 laplace_neumann.py
```

> [!NOTE]
> Each script opens a matplotlib window showing the temperature distribution.

## Acknowledgment

The sparse-matrix setup in 'laplace_newmann.py' is adapted from
Leif Rune Hellevik, [*Numerical Methods for Engineers*](https://leifh.folk.ntnu.no/teaching/tkt4140/._main056.html)
Section 6.3.1 "Newmann boundary conditions".