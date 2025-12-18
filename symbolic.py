import sympy as sp

n = sp.symbols('n', integer=True, positive=True)
k = sp.symbols('k', integer=True, nonnegative=True)

# Piecewise Fourier coefficients
b1 = (3*k**3 - 6*n*k**2 - 3*k + 4*n**3 + 2*n) / (6*n**2)  # 0 <= k <= n-1
b2 = (-k**3 + 6*n*k**2 - 12*n**2*k + k + 8*n**3 - 2*n) / (6*n**2)  # n <= k <= 2n-2

S1 = sp.summation(k * b1, (k, 1, n-1)) + sp.summation(k * b2, (k, n, 2*n-2))
E1 = sp.simplify((2/n**2) * S1)

S2 = sp.summation(k**2 * b1, (k, 1, n-1)) + sp.summation(k**2 * b2, (k, n, 2*n-2))
E2 = sp.simplify((2/n**2) * S2)

Var = sp.simplify(E2 - E1**2)

print("E[K] =", E1)
print("E[K^2] =", E2)
print("Var[K] =", Var)