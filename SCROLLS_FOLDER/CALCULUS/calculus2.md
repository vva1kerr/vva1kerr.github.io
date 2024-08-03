<!-- C:\Users\razer\Desktop\walkerrh.github.io\SCROLLS_FOLDER\CALCULUS\calculus2.md -->




[Home](/index.html)

# College Calculus 2 Notes

## Techniques of Integration
### Description
Various methods for finding integrals, extending the basic techniques learned in Calculus 1.
### Formula
- Integration by Parts:
  $$ \int u \, dv = uv - \int v \, du $$
- Trigonometric Integrals:
  $$ \int \sin^m(x) \cos^n(x) \, dx $$
- Trigonometric Substitution:
  $$ \int \sqrt{a^2 - x^2} \, dx $$
- Partial Fraction Decomposition:
  $$ \frac{P(x)}{Q(x)} = \frac{A}{x - r_1} + \frac{B}{x - r_2} + \ldots $$

## Improper Integrals
### Description
Integrals with infinite limits or integrands that approach infinity within the limits of integration.
### Formula
$$ \int_{a}^{\infty} f(x) \, dx $$
$$ \int_{-\infty}^{\infty} f(x) \, dx $$
$$ \int_{a}^{b} \frac{1}{(x - c)^p} \, dx $$

## Sequences
### Description
A sequence is an ordered list of numbers, often defined recursively or by a formula.
### Formula
General form:
$$ a_n = a_1 + (n-1)d \text{ (arithmetic)} $$
$$ a_n = a_1 r^{n-1} \text{ (geometric)} $$

## Series
### Description
A series is the sum of the terms of a sequence.
### Formula
Arithmetic series:
$$ S_n = \frac{n}{2}(a_1 + a_n) $$
Geometric series:
$$ S_n = a_1 \frac{1 - r^n}{1 - r} $$
Infinite geometric series:
$$ S = \frac{a}{1 - r} \text{ for } |r| < 1 $$

## Convergence Tests
### Description
Methods to determine if a series converges or diverges.
### Formula
- Integral Test:
  $$ \int_{1}^{\infty} f(x) \, dx $$
- Comparison Test:
  $$ 0 \leq a_n \leq b_n $$
- Ratio Test:
  $$ \lim_{{n \to \infty}} \left| \frac{a_{n+1}}{a_n} \right| = L $$
- Root Test:
  $$ \lim_{{n \to \infty}} \sqrt[n]{|a_n|} = L $$

## Power Series
### Description
A power series is a series of the form \( \sum_{n=0}^{\infty} c_n (x - a)^n \).
### Formula
$$ \sum_{n=0}^{\infty} c_n (x - a)^n $$

## Taylor and Maclaurin Series
### Description
Taylor series represent functions as infinite sums of terms calculated from the values of their derivatives at a single point.
### Formula
Taylor series:
$$ f(x) = \sum_{n=0}^{\infty} \frac{f^{(n)}(a)}{n!} (x - a)^n $$
Maclaurin series:
$$ f(x) = \sum_{n=0}^{\infty} \frac{f^{(n)}(0)}{n!} x^n $$

## Parametric Equations
### Description
Parametric equations represent curves by defining both \( x \) and \( y \) as functions of a third variable, usually \( t \).
### Formula
$$ x = f(t), \quad y = g(t) $$

## Polar Coordinates
### Description
Polar coordinates represent points in the plane using a distance from the origin and an angle from the positive x-axis.
### Formula
$$ x = r \cos(\theta) $$
$$ y = r \sin(\theta) $$

## Area in Polar Coordinates
### Description
The area enclosed by a curve defined by polar coordinates.
### Formula
$$ A = \frac{1}{2} \int_{\alpha}^{\beta} r^2 \, d\theta $$

## Arc Length in Parametric and Polar Coordinates
### Description
Formulas to find the length of a curve defined by parametric or polar coordinates.
### Formula
Parametric:
$$ L = \int_{a}^{b} \sqrt{\left( \frac{dx}{dt} \right)^2 + \left( \frac{dy}{dt} \right)^2} \, dt $$
Polar:
$$ L = \int_{\alpha}^{\beta} \sqrt{r^2 + \left( \frac{dr}{d\theta} \right)^2} \, d\theta $$

## Surface Area in Parametric and Polar Coordinates
### Description
Formulas to find the surface area of a solid of revolution defined by parametric or polar coordinates.
### Formula
Parametric (about x-axis):
$$ S = 2\pi \int_{a}^{b} y \sqrt{\left( \frac{dx}{dt} \right)^2 + \left( \frac{dy}{dt} \right)^2} \, dt $$
Polar:
$$ S = 2\pi \int_{\alpha}^{\beta} r \sin(\theta) \sqrt{r^2 + \left( \frac{dr}{d\theta} \right)^2} \, d\theta $$

## Differential Equations
### Description
Equations involving derivatives that describe various physical phenomena.
### Formula
General form:
$$ \frac{dy}{dx} = f(x, y) $$
Separable:
$$ \frac{dy}{dx} = g(x)h(y) $$
Solution:
$$ \int \frac{1}{h(y)} \, dy = \int g(x) \, dx $$

## Center of Mass
### Description
The center of mass of an object is the point at which the mass of the object is considered to be concentrated.
### Formula
For a system of particles:
$$ \bar{x} = \frac{\sum m_i x_i}{\sum m_i} $$
$$ \bar{y} = \frac{\sum m_i y_i}{\sum m_i} $$

For a continuous object:
$$ \bar{x} = \frac{\int_a^b x \rho(x) \, dx}{\int_a^b \rho(x) \, dx} $$
$$ \bar{y} = \frac{\int_a^b y \rho(y) \, dy}{\int_a^b \rho(y) \, dy} $$

## Moments and Centers of Mass
### Description
Moments are the measures of the tendency of a force to rotate an object about an axis. The center of mass is the point where the object can be balanced.
### Formula
Moment about the x-axis:
$$ M_x = \int_a^b y \rho(x) \, dx $$

Moment about the y-axis:
$$ M_y = \int_a^b x \rho(x) \, dx $$

Center of mass:
$$ \bar{x} = \frac{M_y}{m}, \quad \bar{y} = \frac{M_x}{m} $$
where \( m \) is the total mass.

## Work
### Description
Work is the measure of energy transfer when a force moves an object over a distance.
### Formula
For a constant force:
$$ W = Fd $$

For a variable force:
$$ W = \int_a^b F(x) \, dx $$

## Fluid Pressure and Force
### Description
Fluid pressure is the force per unit area exerted by a fluid on a surface. Fluid force is the total force exerted by a fluid.
### Formula
Fluid pressure:
$$ P = \rho gh $$

Fluid force:
$$ F = \int_a^b P(x) \, dA $$

## Parametric Surfaces and Their Areas
### Description
Parametric surfaces are surfaces defined by parametric equations. The area of such surfaces can be computed using surface integrals.
### Formula
Surface area:
$$ S = \int \int_D \left| \frac{\partial \mathbf{r}}{\partial u} \times \frac{\partial \mathbf{r}}{\partial v} \right| \, du \, dv $$

## Line Integrals
### Description
Line integrals are integrals where the function to be integrated is evaluated along a curve.
### Formula
$$ \int_C f(x, y) \, ds $$

For vector fields:
$$ \int_C \mathbf{F} \cdot d\mathbf{r} $$

## Green's Theorem
### Description
Green's Theorem relates a line integral around a simple closed curve \( C \) to a double integral over the plane region \( D \) bounded by \( C \).
### Formula
$$ \int_C (P \, dx + Q \, dy) = \iint_D \left( \frac{\partial Q}{\partial x} - \frac{\partial P}{\partial y} \right) \, dA $$

## Divergence and Curl
### Description
Divergence measures the magnitude of a field's source or sink at a given point, while curl measures the rotation of the field.
### Formula
Divergence:
$$ \nabla \cdot \mathbf{F} = \frac{\partial F_1}{\partial x} + \frac{\partial F_2}{\partial y} + \frac{\partial F_3}{\partial z} $$

Curl:
$$ \nabla \times \mathbf{F} = \left( \frac{\partial F_3}{\partial y} - \frac{\partial F_2}{\partial z}, \frac{\partial F_1}{\partial z} - \frac{\partial F_3}{\partial x}, \frac{\partial F_2}{\partial x} - \frac{\partial F_1}{\partial y} \right) $$

## Surface Integrals
### Description
Surface integrals are the extension of multiple integrals to integration over surfaces.
### Formula
$$ \iint_S f(x, y, z) \, dS $$

For vector fields:
$$ \iint_S \mathbf{F} \cdot d\mathbf{S} $$

## Stokes' Theorem
### Description
Stokes' Theorem relates a surface integral of the curl of a vector field over a surface \( S \) to a line integral of the vector field over its boundary \( \partial S \).
### Formula
$$ \iint_S (\nabla \times \mathbf{F}) \cdot d\mathbf{S} = \int_{\partial S} \mathbf{F} \cdot d\mathbf{r} $$

## Divergence Theorem
### Description
The Divergence Theorem relates the flux of a vector field through a closed surface to the triple integral of the divergence of the field over the region enclosed by the surface.
### Formula
$$ \iint_S \mathbf{F} \cdot d\mathbf{S} = \iiint_V (\nabla \cdot \mathbf{F}) \, dV $$

## Triple Integrals
### Description
Triple integrals extend the concept of double integrals to functions of three variables.
### Formula
$$ \iiint_V f(x, y, z) \, dV $$

## Cylindrical and Spherical Coordinates
### Description
Cylindrical and spherical coordinates are alternative coordinate systems for three-dimensional space.
### Formula
Cylindrical coordinates:
$$ x = r \cos(\theta) $$
$$ y = r \sin(\theta) $$
$$ z = z $$

Spherical coordinates:
$$ x = \rho \sin(\phi) \cos(\theta) $$
$$ y = \rho \sin(\phi) \sin(\theta) $$
$$ z = \rho \cos(\phi) $$

## Volume Integrals
### Description
Volume integrals are used to compute the volume of a solid region in three-dimensional space.
### Formula
Cylindrical coordinates:
$$ \iiint_V f(r, \theta, z) \, r \, dr \, d\theta \, dz $$

Spherical coordinates:
$$ \iiint_V f(\rho, \phi, \theta) \, \rho^2 \sin(\phi) \, d\rho \, d\phi \, d\theta $$

## Applications to Physics
### Description
Calculus is widely used in physics to model and analyze physical phenomena.
### Formula
Work done by a variable force:
$$ W = \int_a^b F(x) \, dx $$

Center of mass:
$$ \bar{x} = \frac{1}{M} \int_V x \rho(x, y, z) \, dV $$

Moment of inertia:
$$ I = \int_V r^2 \rho(x, y, z) \, dV $$


