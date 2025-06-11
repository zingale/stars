# Homework 2 solutions

## 1. Solid or gas?

We want to determine if the Earth is solid.  We start by writing the separation between atoms in the Earth as:

$$d \sim n^{-1/3} = \left ( \frac{\mu m_u}{\rho} \right )^{-1/3}$$

then the Coulomb energy is

$$E_c = \frac{Z^2 e^2}{d} = Z^2 e^2 \left ( \frac{\rho}{\mu m_u} \right )^{1/3}$$

Now the thermal energy is $k T$, and we can take our estimate of $T$ from the Virial
theorem:

$$kT = \frac{1}{5} \mu m_u \frac{GM}{R}$$

the ratio is then

$$\Gamma = \frac{E_c}{kT} = 4 Z^2 e^2 \left ( \frac{\rho}{\mu m_u} \right )^{1/3} \frac{1}{\mu m_u} \frac{R}{GM}$$

and substituting in the average density, $\rho \sim M / R^3$, we have

$$\Gamma \sim 5 Z^2 e^2 \frac{1}{(\mu m_u)^{4/3}} \frac{1}{GM^{2/3}}$$

putting in numbers, taking the core to be iron, $Z = 26$, $\mu = 56$,
and the mass of the Earth as $M_\oplus = 6\times 10^{27}~\mathrm{g}$,
we have

$$\Gamma \sim 800$$

This is very large, so clearly the Earth is solid.


## 2. Dimensional analysis

We want to use the equations of stellar structure + Kramers' opacity
to predict main-sequence stellar properties.

We assume uniform composition and a fully-radiative star.  Our equations of stellar structure are:


* radiation:

  $$L = -(4\pi r^2)^2 \frac{ac}{3\kappa} \frac{dT^4}{dM} \rightarrow L \sim \frac{T^4 R^4}{\kappa M}$$

* energy:

  $$\frac{dL}{dM} = \epsilon \rightarrow L \sim M \epsilon$$

* HSE:

  $$\frac{dP}{dM} = -\frac{GM}{4\pi r^4} \rightarrow P \sim \frac{GM^2}{R^4}$$

* continuity:

  $$\frac{dr}{dM} = \frac{1}{4\pi r^2 \rho} \rightarrow \rho \sim \frac{M}{R^3}$$

we also have our equation of state:

$$P = \frac{\rho k T}{\mu m_u} \sim \frac{\rho T}{\mu}$$

### a.

We want to find the luminosity-mass relationship.  We start by combining HSE + EOS:

$$\frac{\rho T}{\mu} \sim \frac{G M^2}{R^4} \rightarrow T \sim \frac{M\mu}{R}$$

and we use radiation, substituting this temperature expression:

$$L \sim \frac{T^4 R^4}{\kappa M} \sim \frac{R^4}{\kappa M} \left (\frac{M\mu}{R} \right )^4 \sim \frac{M^3\mu^4}{\kappa}$$

Now we assume an opacity of the form $\kappa \sim Z (1 + X) \rho T^{-7/2}$, giving:

$$L \sim \frac{M^3 \mu^4}{Z (1+X)} \frac{1}{\rho} T^{7/2} \sim \frac{M^3 \mu^4}{Z(1+X)} \frac{R^3}{M} \left (\frac{M\mu}{R} \right )^{7/2} \sim \frac{M^{5.5} \mu^{7.5}}{Z (1+X)} R^{-0.5}$$

Now we start with the energy equation and substitute our form of
nuclear energy generation, $\epsilon \sim X^2 \rho T^4$:

$$L \sim M\epsilon \sim M X^2 \rho T^4 \sim M X^2 \left ( \frac{M}{R^3} \right ) \left (\frac{M\mu}{R} \right )^4 \sim \frac{M^6 \mu^4}{R^7} X^2$$

Equating these two expressions for $L$, we find:

$$\frac{M^{5.5} \mu^{7.5}}{Z (1+X)} R^{-0.5} \sim \frac{M^6 \mu^4}{R^7} X^2$$

$$R \sim M^{1/13} \mu^{-7/13} \left [ X^2 (1 + X) Z \right ]^{2/13}$$

Now we can put this back into our expression for L:

$$L \sim \frac{M^{5.5} \mu^{7.5}}{Z (1+X)} M^{-1/26} \mu^{7/26} \left [X^2 (1 + X) Z \right ]^{-1/13}
    \sim M^{71/13} \mu^{101/13} \left [ Z (1 + X) \right ]^{-14/13} X^{-2/13}$$

From this point forward, we'll ignore the $\mu$ and $X$ dependence.  So we have:

$$L \sim M^{71/13} Z^{-14/13}$$

$$R \sim M^{1/13} Z^{2/13}$$

```{note}
This is a much steeper mass dependence for luminosity than we found with the constant electron scattering
opacity.
```

### b.

Now we want to find effective temperature.  We start with the blackbody relation:

$$L \sim R^2 T_\mathrm{eff}^4$$

so

$$T_\mathrm{eff} \sim \frac{L^{1/4}}{R^{1/2}} \sim \frac{M^{71/52} Z^{-14/52}}{M^{1/26}Z^{2/26}} \sim M^{69/52} Z^{-18/52}$$

or replacing $M$ with $L$, we have:

$$T_\mathrm{eff} \sim L^{69/284} Z^{-78/923}$$

and finally

$$L \sim T_\mathrm{eff}^{284/69} \left ( Z^{78/923} \right )^{284/69} \sim T_\mathrm{eff}^{284/69} Z^{8/23}$$

### c.

Our $Z$ dependence shows that for a smaller Z (e.g. pop II stars), a
star is less luminous for the same effective temperature.  This means
that the low metalicity main sequence lies beneath the high metalicity
main sequence.


## 3. Schönberg-Chandrasekhar limit

We want to compute the maximum mass of an isothermal core.

### a.

Let's rederive the Virial theorem without going all the way to the surface.  Starting with HSE:

$$dP = - \frac{GM}{4\pi r^4} dM$$

we multiply by volume and integrate, giving:

$$\int_0^{P(r)} V dP = \frac{\Omega}{3}$$

We'll integrate to the edge of the core, which we'll denote as $R_c$
and the pressure there as $P_c = P(R_c)$ (this is not central pressure).  Then, integrating by parts, our integral is:

$$\int_0^{P_c} V dP = \int_0^{P_c} d(VP) - \int_0^{V_c} P dV = V_c P_c - \int_0^{M_c} \frac{P}{\rho} dM$$

where $M_c$ is the mass of the core.  This is basically what we did
originally when we derived the Virial theorem in class, except now we
have the surface term, $V_c P_c$.

### b.

Now we take the core to be isothermal and of uniform composition and well-described by an ideal gas:

$$V_c P_c - \int_0^{M_c} \frac{k T_c}{\mu_c m_u} dM = \frac{\Omega_c}{3}$$

or

$$\frac{kT_c}{\mu_c m_u} M_c = V_c P_c + \frac{q}{3} \frac{G M_c^2}{R_c}$$

where $q$ is the $\mathcal{O}(1)$ constant in the gravitational potential energy.

Replacing the volume of the core, we have:

$$P_c = \frac{3}{4\pi} \frac{k T_c}{\mu_c m_u} \frac{M_c}{R_c}^3 - \frac{q}{4\pi} \frac{GM_c^2}{R_c^4}$$

### c.

To find the radius where the pressure is maximum, we differentiate with respect to $R_c$ and set it to zero:

$$\frac{dP_c}{dR_c} = -\frac{9}{4\pi} \frac{k T_c}{\mu_c m_u} \frac{M_c}{R_c^4} + \frac{q}{\pi} \frac{G M_c^2}{R_c^5} = 0$$

this gives

$$R_{c,\mathrm{max}} = \frac{4q}{9} \frac{\mu_c m_u}{k T_c} G M_c$$

and the corresponding pressure is

$$P_{c,\mathrm{max}} = P_c(R_{c,\mathrm{max}}) = \frac{3}{16\pi} \left (\frac{9}{4} \right )^3 \frac{1}{q^3}
   \left ( \frac{k T_c}{\mu_c m_u} \right )^4 \frac{1}{G^3 M_c^2}$$


### d.

Requiring that

$$P_c > \frac{3}{8\pi} \frac{GM_\star^2}{R_\star^4}$$

and dropping constants, we have:

$$P_{c, \mathrm{max}}(M_c) \propto \left (\frac{kT_c}{\mu_c m_u} \right )^4 \frac{1}{G^3 M_c^2} \ge \frac{3}{8\pi} \frac{GM_\star^2}{R_\star^4}$$

and from the Virial theorem, we have

$$T_c = \frac{1}{2} \frac{GM_\star}{R_\star} \frac{\mu_\mathrm{env} m_u}{k}$$

giving:

$$\frac{M_c}{M_\star} \le \left (\frac{\mu_\mathrm{env}}{\mu_c} \right )^2 \cdot \mathrm{constant}$$
