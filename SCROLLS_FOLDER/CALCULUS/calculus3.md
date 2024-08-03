<!-- C:\Users\razer\Desktop\walkerrh.github.io\SCROLLS_FOLDER\CALCULUS\calculus3.md -->




[Home](/index.html)

# College Calculus 3 Notes

## Vectors in Three-Dimensional Space
### Description
Vectors are quantities with both magnitude and direction, and they can be represented in three-dimensional space.
### Formula
Vector representation:
$$ \mathbf{v} = \langle v_1, v_2, v_3 \rangle $$
Magnitude of a vector:
$$ |\mathbf{v}| = \sqrt{v_1^2 + v_2^2 + v_3^2} $$

## Dot Product
### Description
The dot product is a way to multiply two vectors to get a scalar, indicating the product of their magnitudes and the cosine of the angle between them.
### Formula
$$ \mathbf{a} \cdot \mathbf{b} = a_1 b_1 + a_2 b_2 + a_3 b_3 $$
$$ \mathbf{a} \cdot \mathbf{b} = |\mathbf{a}| |\mathbf{b}| \cos(\theta) $$

## Cross Product
### Description
The cross product of two vectors results in a third vector that is perpendicular to the plane containing the original vectors.
### Formula
$$ \mathbf{a} \times \mathbf{b} = \left| \begin{matrix} \mathbf{i} & \mathbf{j} & \mathbf{k} \\ a_1 & a_2 & a_3 \\ b_1 & b_2 & b_3 \end{matrix} \right| $$
$$ \mathbf{a} \times \mathbf{b} = |\mathbf{a}| |\mathbf{b}| \sin(\theta) \mathbf{n} $$

## Equations of Lines and Planes
### Description
Equations to represent lines and planes in three-dimensional space.
### Formula
Line through point \( \mathbf{r}_0 \) with direction vector \( \mathbf{v} \):
$$ \mathbf{r}(t) = \mathbf{r}_0 + t \mathbf{v} $$

Plane through point \( \mathbf{r}_0 \) with normal vector \( \mathbf{n} \):
$$ \mathbf{n} \cdot (\mathbf{r} - \mathbf{r}_0) = 0 $$

## Cylindrical and Spherical Coordinates
### Description
Alternative coordinate systems for representing points in three-dimensional space.
### Formula
Cylindrical coordinates:
$$ x = r \cos(\theta) $$
$$ y = r \sin(\theta) $$
$$ z = z $$

Spherical coordinates:
$$ x = \rho \sin(\phi) \cos(\theta) $$
$$ y = \rho \sin(\phi) \sin(\theta) $$
$$ z = \rho \cos(\phi) $$

## Vector-Valued Functions
### Description
Functions that take a real variable as input and output a vector.
### Formula
$$ \mathbf{r}(t) = \langle x(t), y(t), z(t) \rangle $$

## Arc Length and Curvature
### Description
Formulas to calculate the arc length of a curve and the curvature, which measures how quickly a curve changes direction.
### Formula
Arc length:
$$ L = \int_a^b \sqrt{\left( \frac{dx}{dt} \right)^2 + \left( \frac{dy}{dt} \right)^2 + \left( \frac{dz}{dt} \right)^2} \, dt $$

Curvature:
$$ \kappa = \frac{|\mathbf{r}'(t) \times \mathbf{r}''(t)|}{|\mathbf{r}'(t)|^3} $$

## Multivariable Functions
### Description
Functions of more than one variable.
### Formula
$$ f(x, y, z) $$

## Partial Derivatives
### Description
Partial derivatives represent the rate of change of a function with respect to one of its variables, keeping the others constant.
### Formula
$$ f_x = \frac{\partial f}{\partial x}, \quad f_y = \frac{\partial f}{\partial y}, \quad f_z = \frac{\partial f}{\partial z} $$

## Gradient
### Description
The gradient is a vector that points in the direction of the greatest rate of increase of a function.
### Formula
$$ \nabla f = \left\langle \frac{\partial f}{\partial x}, \frac{\partial f}{\partial y}, \frac{\partial f}{\partial z} \right\rangle $$

## Directional Derivatives
### Description
The directional derivative measures the rate of change of a function in the direction of a given vector.
### Formula
$$ D_{\mathbf{u}} f = \nabla f \cdot \mathbf{u} $$

## Tangent Planes and Normal Lines
### Description
Formulas to find the tangent plane to a surface at a given point and the normal line to the surface at that point.
### Formula
Tangent plane to \( z = f(x, y) \) at \( (x_0, y_0, z_0) \):
$$ z - z_0 = f_x(x_0, y_0)(x - x_0) + f_y(x_0, y_0)(y - y_0) $$

Normal line:
$$ \mathbf{r}(t) = \mathbf{r}_0 + t \nabla f $$

## Double and Triple Integrals
### Description
Integrals to compute volumes under surfaces in two and three dimensions.
### Formula
Double integral:
$$ \iint_D f(x, y) \, dA $$

Triple integral:
$$ \iiint_V f(x, y, z) \, dV $$

## Change of Variables in Multiple Integrals
### Description
Techniques to simplify the evaluation of multiple integrals by changing variables.
### Formula
For double integrals:
$$ \iint_D f(x, y) \, dx \, dy = \iint_{D'} f(g(u, v), h(u, v)) \left| \frac{\partial(x, y)}{\partial(u, v)} \right| \, du \, dv $$

For triple integrals:
$$ \iiint_V f(x, y, z) \, dx \, dy \, dz = \iiint_{V'} f(g(u, v, w), h(u, v, w), k(u, v, w)) \left| \frac{\partial(x, y, z)}{\partial(u, v, w)} \right| \, du \, dv \, dw $$

## Divergence and Curl
### Description
Vector calculus operations that measure the magnitude of a source or sink at a given point and the rotation of a vector field.
### Formula
Divergence:
$$ \nabla \cdot \mathbf{F} = \frac{\partial F_1}{\partial x} + \frac{\partial F_2}{\partial y} + \frac{\partial F_3}{\partial z} $$

Curl:
$$ \nabla \times \mathbf{F} = \left( \frac{\partial F_3}{\partial y} - \frac{\partial F_2}{\partial z}, \frac{\partial F_1}{\partial z} - \frac{\partial F_3}{\partial x}, \frac{\partial F_2}{\partial x} - \frac{\partial F_1}{\partial y} \right) $$

## Line Integrals
### Description
Integrals where the function to be integrated is evaluated along a curve.
### Formula
$$ \int_C f(x, y, z) \, ds $$

For vector fields:
$$ \int_C \mathbf{F} \cdot d\mathbf{r} $$

## Surface Integrals
### Description
Integrals that extend the concept of multiple integrals to integration over surfaces.
### Formula
$$ \iint_S f(x, y, z) \, dS $$

For vector fields:
$$ \iint_S \mathbf{F} \cdot d\mathbf{S} $$

## Green's Theorem
### Description
Relates a line integral around a simple closed curve \( C \) to a double integral over the plane region \( D \) bounded by \( C \).
### Formula
$$ \int_C (P \, dx + Q \, dy) = \iint_D \left( \frac{\partial Q}{\partial x} - \frac{\partial P}{\partial y} \right) \, dA $$

## Stokes' Theorem
### Description
Relates a surface integral of the curl of a vector field over a surface \( S \) to a line integral of the vector field over its boundary \( \partial S \).
### Formula
$$ \iint_S (\nabla \times \mathbf{F}) \cdot d\mathbf{S} = \int_{\partial S} \mathbf{F} \cdot d\mathbf{r} $$

## Divergence Theorem
### Description
Relates the flux of a vector field through a closed surface to the triple integral of the divergence of the field over the region enclosed by the surface.
### Formula
$$ \iint_S \mathbf{F} \cdot d\mathbf{S} = \iiint_V (\nabla \cdot \mathbf{F}) \, dV $$

## Triple Integrals in Cylindrical Coordinates
### Description
Triple integrals can be evaluated using cylindrical coordinates to simplify the integration process.
### Formula
$$ \iiint_V f(r, \theta, z) \, r \, dr \, d\theta \, dz $$

## Triple Integrals in Spherical Coordinates
### Description
Triple integrals can be evaluated using spherical coordinates to simplify the integration process.
### Formula
$$ \iiint_V f(\rho, \phi, \theta) \, \rho^2 \sin(\phi) \, d\rho \, d\phi \, d\theta $$

## Mass and Density
### Description
Calculating the mass of an object with variable density using triple integrals.
### Formula
Mass:
$$ m = \iiint_V \rho(x, y, z) \, dV $$

## Center of Mass and Moments of Inertia
### Description
Finding the center of mass and moments of inertia for three-dimensional objects.
### Formula
Center of mass:
$$ \bar{x} = \frac{1}{M} \iiint_V x \rho(x, y, z) \, dV $$
$$ \bar{y} = \frac{1}{M} \iiint_V y \rho(x, y, z) \, dV $$
$$ \bar{z} = \frac{1}{M} \iiint_V z \rho(x, y, z) \, dV $$

Moments of inertia:
$$ I_x = \iiint_V (y^2 + z^2) \rho(x, y, z) \, dV $$
$$ I_y = \iiint_V (x^2 + z^2) \rho(x, y, z) \, dV $$
$$ I_z = \iiint_V (x^2 + y^2) \rho(x, y, z) \, dV $$

## Scalar and Vector Fields
### Description
Scalar fields assign a scalar value to each point in space, while vector fields assign a vector to each point.
### Formula
Scalar field:
$$ f(x, y, z) $$

Vector field:
$$ \mathbf{F}(x, y, z) = \langle F_1(x, y, z), F_2(x, y, z), F_3(x, y, z) \rangle $$

## Gradient, Divergence, and Curl in Cylindrical and Spherical Coordinates
### Description
Calculating the gradient, divergence, and curl in cylindrical and spherical coordinate systems.
### Formula
Gradient in cylindrical coordinates:
$$ \nabla f = \frac{\partial f}{\partial r} \mathbf{e}_r + \frac{1}{r} \frac{\partial f}{\partial \theta} \mathbf{e}_\theta + \frac{\partial f}{\partial z} \mathbf{e}_z $$

Divergence in cylindrical coordinates:
$$ \nabla \cdot \mathbf{F} = \frac{1}{r} \frac{\partial (rF_r)}{\partial r} + \frac{1}{r} \frac{\partial F_\theta}{\partial \theta} + \frac{\partial F_z}{\partial z} $$

Curl in cylindrical coordinates:
$$ \nabla \times \mathbf{F} = \left( \frac{1}{r} \frac{\partial F_z}{\partial \theta} - \frac{\partial F_\theta}{\partial z} \right) \mathbf{e}_r + \left( \frac{\partial F_r}{\partial z} - \frac{\partial F_z}{\partial r} \right) \mathbf{e}_\theta + \frac{1}{r} \left( \frac{\partial (rF_\theta)}{\partial r} - \frac{\partial F_r}{\partial \theta} \right) \mathbf{e}_z $$

Gradient in spherical coordinates:
$$ \nabla f = \frac{\partial f}{\partial \rho} \mathbf{e}_\rho + \frac{1}{\rho} \frac{\partial f}{\partial \phi} \mathbf{e}_\phi + \frac{1}{\rho \sin \phi} \frac{\partial f}{\partial \theta} \mathbf{e}_\theta $$

Divergence in spherical coordinates:
$$ \nabla \cdot \mathbf{F} = \frac{1}{\rho^2} \frac{\partial (\rho^2 F_\rho)}{\partial \rho} + \frac{1}{\rho \sin \phi} \frac{\partial (F_\phi \sin \phi)}{\partial \phi} + \frac{1}{\rho \sin \phi} \frac{\partial F_\theta}{\partial \theta} $$

Curl in spherical coordinates:
$$ \nabla \times \mathbf{F} = \frac{1}{\rho \sin \phi} \left( \frac{\partial (F_\phi \sin \phi)}{\partial \theta} - \frac{\partial F_\theta}{\partial \phi} \right) \mathbf{e}_\rho + \frac{1}{\rho} \left( \frac{1}{\sin \phi} \frac{\partial F_\rho}{\partial \theta} - \frac{\partial (\rho F_\theta)}{\partial \rho} \right) \mathbf{e}_\phi + \frac{1}{\rho} \left( \frac{\partial (\rho F_\phi)}{\partial \rho} - \frac{\partial F_\rho}{\partial \phi} \right) \mathbf{e}_\theta $$

## Applications to Physics and Engineering
### Description
Using calculus to solve problems in physics and engineering, such as fluid dynamics, electromagnetism, and thermodynamics.
### Formula
Electromagnetic field equations:
$$ \nabla \cdot \mathbf{E} = \frac{\rho}{\epsilon_0} $$
$$ \nabla \cdot \mathbf{B} = 0 $$
$$ \nabla \times \mathbf{E} = -\frac{\partial \mathbf{B}}{\partial t} $$
$$ \nabla \times \mathbf{B} = \mu_0 \mathbf{J} + \mu_0 \epsilon_0 \frac{\partial \mathbf{E}}{\partial t} $$

Fluid flow:
$$ \nabla \cdot \mathbf{v} = 0 $$
$$ \nabla \times \mathbf{v} = \mathbf{0} $$

Thermodynamics:
$$ \frac{\partial Q}{\partial t} = k \nabla^2 T $$

## Surface Integrals and Flux
### Description
Calculating the flux of a vector field across a surface.
### Formula
$$ \iint_S \mathbf{F} \cdot d\mathbf{S} $$

## Divergence Theorem in Cylindrical and Spherical Coordinates
### Description
Applying the Divergence Theorem to problems in cylindrical and spherical coordinates.
### Formula
Cylindrical coordinates:
$$ \iiint_V (\nabla \cdot \mathbf{F}) \, r \, dr \, d\theta \, dz $$

Spherical coordinates:
$$ \iiint_V (\nabla \cdot \mathbf{F}) \, \rho^2 \sin(\phi) \, d\rho \, d\phi \, d\theta $$

## Line Integrals of Vector Fields
### Description
Calculating the work done by a vector field along a curve.
### Formula
$$ \int_C \mathbf{F} \cdot d\mathbf{r} $$

## Potential Functions and Conservative Fields
### Description
A vector field is conservative if it is the gradient of some scalar potential function.
### Formula
$$ \mathbf{F} = \nabla \phi $$

## Parametric Surfaces and Surface Integrals
### Description
Evaluating surface integrals over parametric surfaces.
### Formula
Surface area:
$$ S = \iint_D \left| \frac{\partial \mathbf{r}}{\partial u} \times \frac{\partial \mathbf{r}}{\partial v} \right| \, du \, dv $$

## Green's Theorem in the Plane
### Description
Relating a line integral around a simple closed curve to a double integral over the plane region it encloses.
### Formula
$$ \int_C (P \, dx + Q \, dy) = \iint_D \left( \frac{\partial Q}{\partial x} - \frac{\partial P}{\partial y} \right) \, dA $$

## Stokes' Theorem in Three Dimensions
### Description
Relating a surface integral of the curl of a vector field to a line integral around its boundary.
### Formula
$$ \iint_S (\nabla \times \mathbf{F}) \cdot d\mathbf{S} = \int_{\partial S} \mathbf{F} \cdot d\mathbf{r} $$

## Divergence Theorem in Three Dimensions
### Description
Relating the flux of a vector field through a closed surface to the triple integral of the divergence over the region it encloses.
### Formula
$$ \iint_S \mathbf{F} \cdot d\mathbf{S} = \iiint_V (\nabla \cdot \mathbf{F}) \, dV $$

## Applications to Physical Sciences
### Description
Using multivariable calculus to solve problems in physics, chemistry, and engineering.
### Formula
Electromagnetic fields:
$$ \mathbf{E} = -\nabla \phi - \frac{\partial \mathbf{A}}{\partial t} $$
$$ \mathbf{B} = \nabla \times \mathbf{A} $$

Fluid dynamics:
$$ \nabla \cdot \mathbf{v} = 0 $$
$$ \nabla \times \mathbf{v} = \mathbf{0} $$

Heat equation:
$$ \frac{\partial T}{\partial t} = k \nabla^2 T $$


