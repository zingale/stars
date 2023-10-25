import matplotlib.pyplot as plt
import numpy as np

xi = np.linspace(0, 5, 100)

gamma = 5./3.

P_isothermal = np.exp(-xi)

P_isentropic = (1 - (gamma - 1)/gamma * xi)**(gamma/(gamma-1))

fig, ax = plt.subplots()

ax.plot(xi, P_isothermal, label="isothermal")
ax.plot(xi, P_isentropic, label="adiabatic")

ax.set_xlabel("$r/H$")
ax.set_ylabel("$P/P_0$")

ax.legend()
ax.grid(linestyle=":")

fig.savefig("atm.png")

