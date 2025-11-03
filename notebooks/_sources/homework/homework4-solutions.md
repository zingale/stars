# Homework 4 solutions

## 1. Entropy = buoyancy

We want to derive the criterion for convective instability in terms of entropy.  Convective instability means that if we displace a bubble *upward*, then

$$\underbrace{\rho^\star_b}_\mathrm{bubble} - \underbrace{\rho^\star}_\mathrm{surroundings} < 0$$

where the $\star$ superscript indicates the displaced value.

As the buble rises, it expands adiabatically.  We'll write out EOS as $\rho = \rho(s, p)$.  Then the new density inside the bubble is:

$$\rho^\star_b = \rho_b + \frac{d\rho}{dr} \Delta r =
   \rho_b +
      \left . \frac{\partial \rho}{\partial P} \right |_s
      \left . \frac{\partial P} {\partial r} \right |_b \Delta r +
      \left . \frac{\partial \rho}{\partial s} \right |_P
      \underbrace{\left . \frac{\partial s} {\partial r} \right |_b}_{= 0} \Delta r$$

where $\partial s/\partial r = 0$ since the bubble expands at constant entropy.

Now the surrounding density in the atmsophere changes as:

$$\rho^\star_\mathrm{sur} = \underbrace{\rho_\mathrm{sur}}_\mathrm{= \rho_b} +
      \frac{d\rho}{dr} \Delta r =
      \left . \frac{\partial \rho}{\partial P} \right |_s
      \left . \frac{\partial P} {\partial r} \right |_\mathrm{sur} \Delta r +
      \left . \frac{\partial \rho}{\partial s} \right |_P
      \left . \frac{\partial s} {\partial r} \right |_\mathrm{sur} \Delta r$$

So our criteria for instability is:

$$\rho^\star_b - \rho^\star_\mathrm{sur} =
      \left . \frac{\partial \rho}{\partial P} \right |_s
      \left . \frac{\partial P} {\partial r} \right |_b \Delta r -
      \left . \frac{\partial \rho}{\partial P} \right |_s
      \left . \frac{\partial P} {\partial r} \right |_\mathrm{sur} \Delta r -
      \left . \frac{\partial \rho}{\partial s} \right |_P
      \left . \frac{\partial s} {\partial r} \right |_\mathrm{sur} \Delta r < 0$$

But since the bubble expanded while remaining in pressure equilibrium with its surroundings,

$$\left . \frac{\partial P} {\partial r} \right |_b = \left . \frac{\partial P} {\partial r} \right |_\mathrm{sur}$$

leaving us with:

$$-\left . \frac{\partial \rho}{\partial s} \right |_P
      \left . \frac{\partial s} {\partial r} \right |_\mathrm{sur} \Delta r < 0$$

Now our Maxwell relations tell us that

$$\left . \frac{\partial \rho}{\partial s} \right |_P = -\rho^2 \left . \frac{\partial T}{\partial P} \right |_s$$

and our convection criterion becomes:

$$\rho^2 \left . \frac{\partial T}{\partial P} \right |_s
      \left . \frac{\partial s} {\partial r} \right |_\mathrm{sur} \Delta r < 0$$

keep in mind that this is for an upward displacement ($\Delta r > 0$).  This thermodynamic derivative, $\partial T / \partial P |_s$ is positive for any reasonable EOS (and is related to $\Gamma_2$).  Therefore, our convective instability criterion becomes:

$$ds < 0$$

```{note}
This is in the direction of displacement, so this means that high entropy beneath low entropy is unstable to convection.
```


## 2. Composition gradients

We want to consider the convective instability in the presence of a composition gradient.  The idea is that the composition inside the bubble is fixed, but outside, we have a non-zero $d\mu/dr$.

As we did in class, we'll consider the displacement of a bubble upward.  Starting with
$\rho = \rho(P, T, \mu)$, we have

$$    \frac{d\rho}{\rho} =
    \underbrace{\left. \left ( \frac{\partial \log \rho}{\partial \log P} \right ) \right |_{T,\mu}}_{\equiv \alpha} \frac{dP}{P} +
    \underbrace{\left. \left ( \frac{\partial \log \rho}{\partial \log T} \right ) \right |_{P,\mu}}_{\equiv -\delta} \frac{dT}{T} +
    \underbrace{\left. \left ( \frac{\partial \log \rho}{\partial \log \mu} \right ) \right |_{P,T}}_{\equiv \phi} \frac{d\mu}{\mu}
$$

### a. general case

Our instability condition is:

$$\Delta \rho = \left [ \left ( \frac{d\rho}{dr} \right )_b - \left ( \frac{d\rho}{dr} \right )_\mathrm{sur} \right ] < 0$$

which is

$$\left [ \left \{ \left ( \frac{\alpha}{P} \frac{dP}{dr} \right )_b  -
                   \left ( \frac{\delta}{T} \frac{dT}{dr} \right )_b\right \} -
           \left \{ \left ( \frac{\alpha}{P} \frac{dP}{dr} \right )_\mathrm{sur} -
                            \left ( \frac{\delta}{T} \frac{dT}{dr} \right )_\mathrm{sur} +
           \left ( \frac{\phi}{\mu} \frac{d\mu}{dr} \right )_\mathrm{sur}
           \right \} \right ] < 0 $$

and again, since we are in pressure equilibrium, $dP/dr$ is the same inside and outside of the bubble, so we have:

$$-\left ( \frac{\delta}{T} \frac{dT}{dr} \right )_b +
   \left ( \frac{\delta}{T} \frac{dT}{dr} \right )_\mathrm{sur} -
   \left ( \frac{\phi}{\mu} \frac{d\mu}{dr} \right )_\mathrm{sur} < 0 $$

Next, we can multiply by the pressure scale height, $-P \frac{dr}{dP} > 0$, and get:

$$\delta \left . \frac{d\log T}{d\log P} \right |_b
  -\delta \left . \frac{d\log T}{d\log P} \right |_\mathrm{sur} +
  \phi \left .\frac{d\log\mu}{d\log P} \right |_\mathrm{sur} < 0 $$

and assuming that $\delta > 0$, we have:

$$\left . \frac{d\log T}{d\log P} \right |_\mathrm{sur} >
  \underbrace{\left . \frac{d\log T}{d\log P} \right |_\mathrm{ad}}_\mathrm{bubble~is~ adiabatic} +
  \frac{\phi}{\delta} \left .\frac{d\log\mu}{d\log P} \right |_\mathrm{sur}$$

This is the same as:

$$\nabla > \nabla_\mathrm{ad} + \frac{\phi}{\delta} \nabla_\mu$$

```{note}
Usually $\nabla \mu > 0$ (heavier composition inwards), so the composition gradient stabilizes the atmosphere against convection.
```

### b. Ideal gas + radiation

Now consider:

$$P = \frac{\rho k T}{\mu m_u} + \frac{1}{3} a T^4$$

Expressing this as $\rho = \rho(P, T, \mu)$, we have:

$$\rho = \left (P - \frac{1}{3} a T^4 \right ) \frac{\mu m_u}{k T}$$

then:

$$\left . \frac{\partial \rho}{\partial \mu} \right |_{P,T} = \frac{\rho}{\mu}$$

$$\left . \frac{\partial \rho}{\partial T} \right |_{P, \mu} = -\frac{\rho}{T} \left [ 1 + 4  \frac{1 - \beta}{\beta} \right ]$$

where $\beta = P_g / P$.

Then we can compute the indices in our expansion:

$$-\delta = \left . \frac{\partial \log \rho}{\partial \log T} \right |_{P,\mu} = 1 + 4 \frac{1-\beta}{\beta}$$

$$\phi = \left . \frac{\partial \log \rho}{\partial \log \mu} \right |_{P,T} = 1$$

and our convective instability criterion becomes:

$$\nabla > \nabla_\mathrm{ad} + \frac{\beta}{4 - 3\beta} \nabla_\mu$$
