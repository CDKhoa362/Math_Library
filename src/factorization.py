from sympy import symbols

x, y = symbols('x y')
expr = x**2 + y**2

# Thay thế x và y với các giá trị khác nhau
result = expr.subs({x: 1, y: 2})
print(result)