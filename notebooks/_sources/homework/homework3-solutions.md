# Homework 3 solutions


## 1. Degeneracy



## 2. Non-zero temperature degeneracy

We want to consider finite-temperature, but non-relativistic degeneracy.
We can do this analytically.

Finite temperature means that the degeneracy parameter,

$$\Psi = \frac{\mu - mc^2}{kT}$$

is not infinite.

### a.

We start by writing our number density as the integral of the Fermi-Dirac distribution
over all momentum:

$$n_e = \frac{8\pi}{h^3} \int_0^\infty p^2 \frac{dp}{e^{\mathcal{E}/kT - \Psi} + 1}$$

We then change variable in terms of $\mathcal{E}$:

$$p = \sqrt{2 m \mathcal{E}} \rightarrow dp = \sqrt{\frac{m}{2\mathcal{E}}} d\mathcal{E}$$

giving

$$n_e = \frac{4\pi}{h^3} (2m)^{3/2} \int_0^\infty \frac{\mathcal{E}^{1/2} d\mathcal{E}}{e^{\mathcal{E}/kt - \Psi} + 1}$$

Finally, defining $\xi \equiv \mathcal{E}/(kT)$, we have:

$$n_e = \frac{4\pi}{h^3} (2 m k T)^{3/2} \int_0^\infty \frac{\xi^{1/2} d\xi}{e^{\xi - \Psi} + 1} = \frac{4\pi}{h^3} (2mkT)^{3/2} F_{1/2} (\Psi)$$

where we used the definition of the Fermi-Dirac integral given in the problem:

$$F_n(\Psi) = \int_0^\infty \frac{\xi_n}{e^{\xi - \Psi} + 1} d\xi$$

The pressure is done similarly:

$$P_e = \frac{8\pi}{3 h^3} \int_0^\infty p \frac{p}{m} \frac{p^2 dp}{e^{\mathcal{E}/kT - \Psi} + 1}$$

where we used the non-relativistic velocity, $v = p/m$.  Doing the same substitutions, we have:

$$P_e = \frac{8\pi}{3h^2} (2m)^{3/2} \int_0^\infty \frac{\mathcal{E}^{3/2} d\mathcal{E}}{e^{\mathcal{E}/kT - \Psi} + 1} = \frac{8\pi}{3h^3} (2mkT)^{3/2} k T F_{3/2}(\Psi)$$

we see from these relations that:

$$\frac{P_e}{n_e} = \frac{2}{3} k T \frac{F_{3/2}(\Psi)}{F_{1/2}(\Psi)}$$

### b.

We now want to use the expansion for $\Psi \rightarrow \infty$:

$$F_n(\Psi) = \frac{\Psi^{n+1}}{n+1} \left [ 1 + \frac{\pi^2}{6} (n+1) n \Psi^{-2} + \mathcal{O}(\Psi^{-4}) \right ]$$

Keeping only the first term for number density, we have:

$$F_{1/2}(\Psi) \sim \frac{2}{3} \Psi^{3/2}$$

```{note}
The next term would be $\propto \Psi^{-1/2}$ which tends to $0$ for $\Psi \rightarrow \infty$, which
is why we can ignore it.
```

This gives us

$$n_e \sim \frac{8\pi}{2h^3} (2m kT)^{3/2} \Psi^{3/2}$$

or

$$\Psi \sim \left ( \frac{3h^3}{8\pi} \right )^{2/3} \frac{n_e^{2/3}}{2 m k T}$$

### c.

For the pressure integral, we use

$$F_{3/2}(\Psi) \sim \frac{2}{5} \Psi^{5/2} + \frac{\pi^2}{4} \Psi^{1/2}$$

(again, the next terms tend to zero for $\Psi \rightarrow \infty$).

This allows us to write our pressure as:

$$P_e = n_e k T \frac{2}{3} \frac{\frac{2}{5} \Psi^{5/2} + \frac{\pi^2}{4} \Psi^{1/2}}{\frac{2}{3}\Psi^{3/2}}$$

or, substituting in our expression $\Psi(n_e)$,

\begin{align*}
P_e &= n_e k T \frac{2}{3} \left [ \frac{3}{5} \left ( \frac{3h^3}{8\pi} \right )^{2/3} \frac{n_e^{2/3}}{2mkT} +
                                   \frac{3}{8} \pi^2 \left (\frac{3h^3}{8\pi} \right )^{-2/3} \frac{2mkT}{n_e^{2/3}} \right ] \\
    &= \frac{h^2}{20m} \left ( \frac{3}{\pi} \right )^{2/3} n_e^{5/3} \left [ 1 + \frac{40\pi^2}{(3/\pi)^{4/3}} \frac{m^2}{h^4} \frac{(kT)^2}{n_e^{4/3}} \right ]
\end{align*}

We see that the first term is the zero-temperature expression we derived in class for non-relativistic electron degeneracy.  The second term is the finite-temperature
correction.

## 3. Intensity vs. flux

