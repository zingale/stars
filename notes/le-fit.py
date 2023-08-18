"""
integrate the Lane-Emden equation:       

  (1/xi**2) (xi**2 phi')' = -phi**n

here, we define two variables,

  y = phi 
  z = phi' (= d(y)/dxi)

We'll use 4th order RK and do fitting 

At the center, the BCs are:

  y(0) = 1
  z(0) = 0 

at the edge of the star, xi_s, the BCs are:

  y(xi_s) = 0
  z(xi_s) = alpha  

initially, we don't know alpha or xi_s  

We will integrate outward from the center (giving yout,zout) and
inward from the surface (giving yin,zin) and make the solution match 
at some fitting point, xi_fit.  

We use a secant method to force the solution to match by adjusting
alpha and xi_s for shorthand, we'll call the system H = (y, z)
"""

import math
import numpy
import pylab
import scipy
from scipy.integrate import ode

def rhs(xi, H, n):
    
    y = H[0]
    z = H[1]

    f0 = z

    if (xi == 0.0):
        f1 = (2./3.) - y**n
    else:
        f1 = -2.0*z/xi - y**n

    return numpy.array([f0, f1])


def le_integrate(xi_start, xi_end, H0, n):

    # use the explicit (adams) integrator from the VODE package
    r = ode(rhs).set_integrator("vode", method="adams",
                                atol=1.e-13, rtol=1.e-13,
                                nsteps=15000, order=12)
    r.set_initial_value(H0, xi_start)

    # pass n into the rhs() routine
    r.set_f_params(n)

    xi_out = [xi_start]
    y_out = [H0[0]]
    z_out = [H0[1]]

    # we want to know what the solution looks like on some regular grid
    xi = numpy.linspace(xi_start, xi_end, 100)

    iend = 1
    if (xi_end > xi_start):
        while r.successful() and r.t < xi_end:
            r.integrate(xi[iend])

            xi_out.append(r.t)
            y_out.append(r.y[0])
            z_out.append(r.y[1])
            
            iend += 1

    else:
        while r.successful() and r.t > xi_end:
            r.integrate(xi[iend])

            xi_out.append(r.t)
            y_out.append(r.y[0])
            z_out.append(r.y[1])
            
            iend += 1


    return numpy.array(xi_out), numpy.array(y_out), numpy.array(z_out)



#-----------------------------------------------------------------------------

# polytropic index
n = 4.5

# initial guesses for the unknowns -- if we aren't careful with the
# guess at the outer boundary, we can get 2 roots.  Here we know that
# n = 1 has xi_s = pi
if (n > 2.0):
    xi_s = 8.0
else:
    xi_s = math.pi

alpha = -0.01

# for numerical differentiation
eps = 1.e-7


# main iteration loop
converged = 0
iter = 1
while not converged:

    # fitting point
    xi_fit = xi_s/2.0


    # baseline integration

    # outward from the center
    H0 = numpy.array([1.0,0.0])
    xi_out, y_out, z_out = le_integrate(0.0, xi_fit, H0, n)

    # inward from xi_s
    H0 = numpy.array([0.0,alpha])
    xi_in, y_in, z_in = le_integrate(xi_s, xi_fit, H0, n)

    # the two functions we want to zero
    nin = len(y_in)
    nout = len(y_out)

    Ybase = y_in[nin-1] - y_out[nout-1]
    Zbase = z_in[nin-1] - z_out[nout-1]

    # now do alpha + eps*alpha, xi_s
    # inward from xi_s
    H0 = numpy.array([0.0,alpha*(1.0+eps)])
    xi_in, y_in, z_in = le_integrate(xi_s, xi_fit, H0, n)

    Ya = y_in[nin-1] - y_out[nout-1]
    Za = z_in[nin-1] - z_out[nout-1]

    # our derivatives
    dYdalpha = (Ya-Ybase)/(alpha*eps)
    dZdalpha = (Za-Zbase)/(alpha*eps)

    # now do alpha, xi_s + eps*xi_s
    # inward from xi_s
    H0 = numpy.array([0.0,alpha])
    xi_in, y_in, z_in = le_integrate(xi_s*(1.0+eps), xi_fit, H0, n)

    Yxi = y_in[nin-1] - y_out[nout-1]
    Zxi = z_in[nin-1] - z_out[nout-1]

    # our derivatives
    dYdxi_s = (Yxi-Ybase)/(xi_s*eps)
    dZdxi_s = (Zxi-Zbase)/(xi_s*eps)

    # compute the correction for our two parameters
    if (dZdxi_s - dZdalpha*dYdxi_s/dYdalpha == 0.0):
        dxi_s = 2.0*dxi_s
    else:
        dxi_s = - (Zbase - dZdalpha*Ybase/dYdalpha)/ \
                (dZdxi_s - dZdalpha*dYdxi_s/dYdalpha)

    dalpha = -(Ybase + dYdxi_s*dxi_s)/dYdalpha


    # limit the changes per iteration
    if (abs(dalpha) > 0.1*abs(alpha)):
        dalpha = 0.1*abs(alpha)*math.copysign(1.0,dalpha)

    if (abs(dxi_s) > 0.1*abs(xi_s)):
        dxi_s = 0.1*abs(xi_s)*math.copysign(1.0,dxi_s)

    print "corrections: ", dalpha, dxi_s


    alpha += dalpha
    xi_s += dxi_s

    pylab.clf()
    pylab.plot(xi_in, y_in, color="r", label=r"$\theta$")
    pylab.plot(xi_out, y_out, color="r", ls="--")

    pylab.plot(xi_in, z_in, color="b", label=r"$\theta'$")
    pylab.plot(xi_out, z_out, color="b", ls="--")

    pylab.xlabel(r"$\xi$", fontsize=14)
    pylab.ylabel(r"$\theta,\, \theta'$", fontsize=14)

    t = pylab.title(r"solution of $\frac{1}{\xi^2} \frac{d}{d\xi}\left ( \xi^2 \frac{d\theta}{d\xi} \right ) = -\theta^n$ via fitting")
    t.set_y(1.05)

    ax = pylab.gca()
    pylab.text(0.5, 0.9, "n = %3.2f polytrope, iteration # %d" % (n, iter),
               transform=ax.transAxes, fontsize=14, horizontalalignment="center")

    pylab.legend(frameon=False, loc="best")

    pylab.tight_layout()

    f = pylab.gcf()
    f.set_size_inches(12.8,7.2)

    pylab.savefig("le-n%3.2f-iter%02d.png" % (n, iter))

    iter += 1

    if (abs(dalpha) < eps*abs(alpha) and abs(dxi_s) < eps*abs(xi_s)):
        converged = 1

    
