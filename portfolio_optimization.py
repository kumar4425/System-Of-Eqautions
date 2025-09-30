# portfolio_optimization.py

import numpy as np


A = np.array([
    [1, 1],        
    [0.08, 0.12]    # 0.08x + 0.12y = 960
])

# Constants (RHS)
B = np.array([10000, 960])

# Solve system
solution = np.linalg.solve(A, B)

x = solution[0]  # Investment in Stock A
y = solution[1]  # Investment in Stock B

print("Optimal Investment:")
print(f"Stock A (8% return): ${x:,.2f}")
print(f"Stock B (12% return): ${y:,.2f}")
print(f"Expected Return: ${0.08*x + 0.12*y:,.2f}")