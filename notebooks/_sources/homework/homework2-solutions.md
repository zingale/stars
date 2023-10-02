# Homework 2 solutions

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


