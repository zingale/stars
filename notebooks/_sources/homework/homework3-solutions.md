# Homework 3 solutions


## 1. Degeneracy

In class, we derived:

\begin{align*}
P_e &= A f(x) \\
\rho e_e &= A g(x)
\end{align*}

with

$$A = \frac{\pi}{3} \left ( \frac{m_e c}{h} \right )^3 m_e c^2$$

and

\begin{align*}
f(x) &= x (2x^2 - 3) (1 + x^2)^{1/2} + 3 \sinh^{-1}(x) \\
g(x) &= 8x^3 \left [ (1+ x^2)^{1/2} - 1 \right ] - f(x)
\end{align*}

where $x = p/(m_e c)$ is the Fermi momentum.

### a.

We want to expand in the non-relativistic limit ($x \ll 1$).

Let's look at the terms in $f(x)$ for $x \ll 1$:

* $(1 + x^2)^{1/2} \sim 1 + \frac{x^2}{2} - \frac{x^4}{8} + \ldots$$

* $\sinh^{-1}(x) \sim x - \frac{x^3}{6} + \frac{3x^5}{40} + \ldots$$

then

\begin{align*}
f(x) &\sim (2x^3 - 3x) \left (1 + \frac{x^2}{2} - \frac{x^4}{8} \right ) + 3x - \frac{1}{2} x^3 + \frac{9}{40}x^5 + \ldots \\
     &\sim \frac{8}{5}x^5
\end{align*}

```{note}
You need to carry up to $x^5$ in your expansions because of all of the
cancellations that occur.  Otherwise you will miss some factors.
```

Now, $g(x)$ expands as:

\begin{align*}
g(x) &= 8x^3 \left [ (1+x^2)^{1/2} - 1 \right ] - f(x) \\
     &\sim 8x^3 \left [1 + \frac{1}{2}x^2 - 1 \right ] - f(x) \\
     &\sim \frac{12}{5} x^5
\end{align*}

This gives:

\begin{align*}
P_e &\sim A \frac{8}{5} x^5 \\
\rho e_e &\sim A \frac{12}{5} x^5
\end{align*}

Now to put in numbers.  We know that

$$\frac{\rho}{\mu_e} = \frac{8\pi}{3} m_u \left (\frac{m_e c}{h} \right )^3 x^3$$

or

$$x = \left ( \frac{3}{8\pi m_u} \right )^{1/3} \frac{h}{m_e c} \left ( \frac{\rho}{\mu_e} \right )^{1/3}$$

then

$$P_e = \frac{8\pi}{15} \left ( \frac{3}{8\pi} \right )^{5/3} \frac{h^2}{m_e} \left (\frac{\rho}{\mu_e m_u} \right )^{5/3}$$

putting in numbers, we have:

$$P_e \sim 9.6\times 10^{12} \left ( \frac{\rho / 1~\mathrm{g~cm^{-3}}}{\mu_e} \right )^{5/3} \mathrm{erg~cm^{-3}}$$

and

$$\rho e_e = \frac{3}{2} P_e$$

### b.

Now we want the relativistic limit, $x \gg 1$.

We first note that $\sinh^{-1}(x)$ is a very slowing varying function
of $x$ (plot it and you will see).  In particular, the leading term of
an expansion of $\sinh^{-1}(x)$ for $|x| \gg 1$ is $\log(2|x|)$ (you
can find this in a table of series expansions).  This grows much
slower than the polynomial growth of the other terms, so we can ignore
this.

Then we have (for $|x| \gg 1$):

$$f(x) \sim x \cdot  \underbrace{(2 x^2)}_{2x^2 -3} \cdot \underbrace{x}_{(1+x^2)^{1/2}} \sim 2x^4$$

and

$$g(x) \sim 8x^3 \cdot \underbrace{x}_{[(1+x^2)^{1/2} - 1]} - f(x) \sim 6 x^4$$

Putting these into our expressions,

$$P_e \sim A 2x^4 = \frac{\pi}{3} \left (\frac{m_e c}{h} \right )^3 m_e c^2 \cdot 2 x^4
      = \frac{2\pi}{3} \left ( \frac{3}{8\pi} \right )^{4/3} h c \left ( \frac{\rho}{\mu_e m_u} \right )^{4/3}$$

and putting in numbers

$$P_e \sim 1.2\times 10^{15} \left ( \frac{\rho / 1~\mathrm{g~cm^{-3}}}{\mu_e} \right )^{5/3} \mathrm{erg~cm^{-3}}$$

finally,

$$\rho e_e = \frac{g(x)}{f(x)} P_e = 3 P_e$$





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

### a.

We want to compare the intensity leaving a source to that received by a detector.

The energy leaving a source with area $dA$ in direction $\theta$ into a cone $d\Omega$ is:

$$dE^\mathrm{emit} = I \cos \theta dA d\Omega dt$$

this is received by a detector a distance $r$ away, with a detector area $dA^\prime$.
That means the solid angle of the detector as seen by the source is:

$$d\Omega = \frac{dA^\prime \cos\theta^\prime}{r^2}$$

where the $\cos\theta^\prime$ is the projection of the detector's $dA^\prime$ onto the
line of sight.  This means that

$$dE^\mathrm{emit} = I \cos \theta dA \frac{dA^\prime \cos\theta^\prime}{r^2} dt$$

Now the detector receives an energy

$$dE^\mathrm{recv} = I^\prime \cos\theta^\prime dA^\prime d\Omega^\prime dt$$

where $d\Omega^\prime$ is the solid angle subtended by the emitter as seen by the
detector.  This is just

$$d\Omega^\prime = \frac{dA \cos \theta}{r^2}$$

so

$$dE^\mathrm{recv} = I^\prime \cos\theta^\prime dA^\prime \frac{dA \cos\theta}{r^2} dt$$

Finally, since $dE^\mathrm{emit} = dE^\mathrm{recv}$, we see that $I = I^\prime$.

### b.

The flux emitted by our source is:

$$f = \int_\Omega I\cos\theta d\Omega = B \int \cos \theta \sin\theta d\theta d\phi$$

where we used $I = B$ is constant.

We need to figure out our integration limits.  The sphere will subtend an angle $\theta_c$
as seen some distance $d$ away, with

$$\theta_c = \tan^{-1} \frac{R}{d} \sim \sin^{-1} \frac{R}{d}$$

then the integration limits are:

$$f = B \int_{\theta=0}^{\theta=\theta_c} \int_{\phi=0}^{\phi=2\pi} \cos\theta \sin\theta d\theta d\phi$$

changing variables, $\xi = \sin\theta \rightarrow d\xi = cos\theta d\theta$, we have:

$$f = 2\pi B \int_0^{R/d} \xi d\xi = \pi B \left ( \frac{R}{d} \right )^2$$

So we see that the flux falls off as $\sim 1/d^2$.
