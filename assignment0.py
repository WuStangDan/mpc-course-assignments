import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from scipy.optimize import minimize
from scipy.optimize import linprog

class ModelPredictiveControl:
    def __init__(self):
        self.horizon = 5

    def plant_model(self, u, day):
        if day == 0: # Monday
            return u * 1

    def cost_function(self, u):
        cost = 0.0
        return cost



mpc = ModelPredictiveControl()

# Set bounds.
bounds = []
for i in range(mpc.horizon):
    bounds += [[0, 5]]

# Set Constraint
def con(x):
    return np.sum(x) - 15
cons = [{'type':'eq', 'fun': con}]

# Create Inputs to be filled.
u = np.zeros(mpc.horizon)

# Non-linear optimization.
u_solution = minimize(mpc.cost_function,
                      x0=u,
                      method='SLSQP',
                      bounds=bounds,
                      constraints=cons,
                      tol = 1e-8)

# Print Results.
print("Total Cost " + str(round(mpc.cost_function(u_solution.x),1)))
days = {0:'M', 1:'T', 2:'W', 3:'R', 4:'F'}
for i in range(mpc.horizon):
    print(days[i] +': '+ str(round(u_solution.x[i],1)))
print('Sum: ' + str(np.round(np.sum(u_solution.x),1)))
