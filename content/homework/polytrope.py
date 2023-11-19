import matplotlib.pyplot as plt
import numpy as np

class Polytrope:
    """a polytrope of index n"""
    def __init__(self, n, h0=1.e-2, tol=1.e-12):
        self.n = n
        self.xi = []
        self.theta = []
        self.dtheta_dxi = []
        
        self._integrate(h0, tol)

    def _integrate(self, h0, tol):
        """integrate the Lane-Emden system"""

        # our solution vector q = (y, z)
        q = np.zeros(2, dtype=np.float64)
        xi = 0.0

        h = h0

        # initial conditions
        q[0] = 1.0
        q[1] = 0.0

        while h > tol:
            # 4th order RK integration -- first find the slopes
            k1 = self._rhs(xi, q)
            k2 = self._rhs(xi+0.5*h, q+0.5*h*k1)
            k3 = self._rhs(xi+0.5*h, q+0.5*h*k2)
            k4 = self._rhs(xi+h, q+h*k3)

            # now update the solution to the new xi
            q += (h/6.0)*(k1 + 2*k2 + 2*k3 + k4)
            xi += h

            # set the new stepsize--our systems is always convex
            # (theta'' < 0), so the intersection of theta' with the
            # x-axis will always be a conservative estimate of the
            # radius of the star.  Make sure that the stepsize does
            # not take us past that.
            R_est = xi - q[0]/q[1]

            if xi + h > R_est:
                h = -q[0]/q[1]

            # store the solution:
            self.xi.append(xi)
            self.theta.append(q[0])
            self.dtheta_dxi.append(q[1])

        self.xi = np.array(self.xi)
        self.theta = np.array(self.theta)
        self.dtheta_dxi = np.array(self.dtheta_dxi)

    def _rhs(self, xi, q):
        """ the righthand side of the LE system, q' = f"""

        f = np.zeros_like(q)

        # y' = z
        f[0] = q[1]
        
        # for z', we need to use the expansion if we are at xi = 0,
        # to avoid dividing by 0
        if xi == 0.0:
            f[1] = (2.0/3.0) - q[0]**self.n
        else:
            f[1] = -2.0*q[1]/xi - q[0]**self.n

        return f

    def get_params(self):
        """ return the standard polytrope parameters xi_1,
        and [-xi**2 theta']_{xi_1} """
        xi1 = self.xi[-1]
        p2 = -xi1**2 * self.dtheta_dxi[-1]
        return xi1, p2

    def plot(self):
        """ plot the solution """
        fig = plt.figure()
        ax = fig.add_subplot(111)
        ax.plot(self.xi, self.theta, label=r"$\theta$")
        ax.plot(self.xi, self.theta**self.n, label=r"$\rho/\rho_c$")
        ax.set_xlabel(r"$\xi$")
        ax.legend(frameon=False)
        return fig
