import numpy as np
from scipy.optimize import minimize


def distance_squared(params):
    # The equations
    x1, theta = params
    y1 = -0.033506787 * x1**2 + 56.6
    x2 = 25 * np.cos(theta)
    y2 = 25 * np.sin(theta) + 25
    # Squared distance calculation
    return (x1 - x2)**2 + (y1 - y2)**2


initial_guess = [0, 0]


bounds = [(None, None), (0, 2 * np.pi)]

result = minimize(distance_squared, initial_guess, bounds=bounds)

x1_opt, theta_opt = result.x
min_distance = np.sqrt(result.fun)

y1_opt = -0.033506787 * x1_opt**2 + 56.6

x2_opt = 25 * np.cos(theta_opt)
y2_opt = 25 * np.sin(theta_opt) + 25

print("Optimal Point on Parabola: (", x1_opt, ",", y1_opt, ")")
print("Optimal Point on Circle: (", x2_opt, ",", y2_opt, ")")
print("Minimum Distance:", min_distance)
