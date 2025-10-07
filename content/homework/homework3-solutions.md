# Homework 3 solutions

## 1. LTE

The equation of HSE is:

$$\frac{dP}{dr} = -\rho |g|$$

we can take $g$ as a constant, using the value at the surface of the Sun:

$$g = \frac{GM_\odot}{R_\odot^2} = \frac{6.67\times 10^{-8}~\mathrm{dyn~cm^2~g^{-2}} \cdot 2\times 10^{33}~\mathrm{g}}{(7\times 10^{10}~\mathrm{cm})^2} = 2.7\times 10^4~\mathrm{cm~s^{-2}}$$

We use the ideal gas law:

$$P = \frac{\rho k T}{\mu m_u}$$

and substituting this into HSE, we have:

$$\frac{1}{\rho} \frac{d\rho}{dr} = \underbrace{\frac{\mu m_u g}{k T}}_{H^{-1}}$$

where $H$ is the scale height. Upon integrating, we get:

$$\rho = \rho_0 e^{-r/H}$$

We can evaluate $H$:

$$H = \frac{kT}{\mu m_u g} = \frac{1.38\times 10^{-16}~\mathrm{erg~K^{-1}} \cdot 6000~\mathrm{K}}{0.6 \cdot 1.66\times 10^{-24}~\mathrm{g} \cdot 2.7\times 10^4~\mathrm{cm~s^{-2}}} = 300~\mathrm{km}$$

Now, we know that the mean free path is:

$$\lambda_\gamma = \frac{1}{\kappa \rho}$$

If we take $\kappa = 0.264~\mathrm{cm^2~g^{-1}}$ and $\rho = 2.5\times 10^{-7}~\mathrm{g~cm^{-3}}$ (both typical of the photosphere), then we find:

$$\lambda_\gamma = \frac{1}{0.264~\mathrm{cm^2~g^{-1}} \cdot 2.5\times 10^{-7}~\mathrm{g~cm^{-3}}} = 150~\mathrm{km}$$

Since $\lambda_\gamma \sim H$, we cannot assume LTE in the photosphere.

## 2. Limb darkening

From class, we know that

$$\langle I \rangle = \frac{1}{2} \int_{-1}^1 I(\mu) d\mu$$

and

$$U = \frac{2\pi}{c} \int_{-1}^1 I(\mu) d\mu$$

together this tells us that

$$U = \frac{4\pi}{c} \langle I \rangle$$

Now, if we:

* Use the closure $P = (1/3) U$

* Assume we are isotropic and in radiative equilibrium, so
 $\langle I \rangle = S$

then we have

$$P(\tau) = \frac{F}{c} \left (\tau + \frac{2}{3} \right ) =
   \frac{4\pi}{3c} S$$

which says that

$$S = \frac{3}{4\pi} F \left (\tau + \frac{2}{3} \right )$$

The outgoing solution to the rad transfer equation is:

$$I(\tau, \mu> 0) = \frac{1}{\mu} \int_\tau^\infty e^{-(t-\tau)/\mu} S(t) dt$$

(we took the reference to be $\tau_0 \rightarrow \infty$).
Substituting in our $S(\tau)$ and evaluating at $\tau = 0$, we have:

$$I_0(\mu> 0) = \frac{1}{\mu} \int_0^\infty e^{-t/\mu} \left [ \frac{3F}{4\pi} \left ( t + \frac{2}{3} \right ) \right ] dt$$

making the substitution $\xi = t / \mu$, we have:

$$I_0(\mu > 0) = \frac{3F}{3\pi} \int_0^\infty e^{-\xi} \left (\mu \xi + \frac{2}{3} \right ) d\xi = \frac{3F}{4\pi} \mu \Gamma(2) - \frac{1}{2} \frac{F}{\pi} \left . e^{-\xi} \right |_0^\infty$$

or

$$I_0(\mu > 0) = \frac{3F}{4\pi} \left (\mu + \frac{2}{3} \right )$$

What does this mean?

* $\theta = 0 \rightarrow \mu = 1$ means the center of the disk, where the intensity is the greatest

* $\theta = \pi/2 \rightarrow \mu = 0$ means the limb.  But notice that the intensity is not zero there!

Normalizing by the intensity at the center of the Sun, we have:

$$\frac{I_0(\mu)}{I_0(\mu = 1)} = \frac{3}{5} \left (\cos\theta + \frac{2}{3} \right)$$

## 3. Atmospheres

Starting with the solution to the radiation transfer equation, with our referenece optical depth $\tau_0$:


we now assume:

* We are looking from above, so we care about the $\mu = 1$ direction
* We are at the top of the slab, so we can take $\tau = 0$:

$$I_0 = e^{-\tau_0} I(\tau_0) - \int_{\tau_0}^0 e^{-t} S(t) dt$$

Finally, taking $S$ as constant, we can do the integral:

$$I_0 = e^{-\tau_0} I(\tau_0) - S \int_{\tau_0}^0 e^{-t} dt =
        e^{-\tau_0} I(\tau_0) + S \left (1 - e^{-\tau_0} \right )$$

Now we can consider different cases:

a. If $\tau_0 \gg 1$, then $e^{-\tau_0} \rightarrow 0$, and $I_0 = S = B--we see blackbody radiation.

b. If $\tau_0 \ll 1$, then $e^{-\tau_0} \sim 1 - \tau_0$, and we have:

   $$I_0 = I(\tau_0) - \tau_0 [I(\tau_0) - S] $$

   * If $I(\tau_0) > S$, then we see absorption
   * If $I(\tau_0) < S$, then we see emission lines

These are known as [Kirchhoff's laws](https://en.wikipedia.org/wiki/Gustav_Kirchhoff#Kirchhoff's_three_laws_of_spectroscopy).
