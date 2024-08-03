<!-- C:\Users\razer\Desktop\walkerrh.github.io\SCROLLS_FOLDER\CALCULUS\calculus1.md -->




[Home](/index.html)

# College Calculus 1 Notes

| Function | Derivative | 
| --- | --- | 
| $$ f(x) = x^n $$ | $$ f'(x) = nx^{n-1} $$ | 
| $$ f(x) = \sin(x) $$ | $$ f'(x) = \cos(x) $$ | 
| $$ f(x) = \cos(x) $$ | $$ f'(x) = -\sin(x) $$ | 
| $$ f(x) = \tan(x) $$ | $$ f'(x) = \sec^2(x) $$ | 
| $$ f(x) = \cot(x) $$ | $$ f'(x) = -\csc^2(x) $$ | 
| $$ f(x) = \csc(x) $$ | $$ f'(x) = -\csc(x) \cot(x) $$ | 
| $$ f(x) = \sec(x) $$ | $$ f'(x) = \sec(x) \tan(x) $$ | 
| $$ f(x) = e^x $$ | $$ f'(x) = e^x $$ | 
| $$ f(x) = \ln(x) $$ | $$ f'(x) = \frac{1}{x} $$ | 
| $$ f(x) = \arcsin(x) $$ | $$ f'(x) = \frac{1}{\sqrt{1-x^2}} $$ | 
| $$ f(x) = \arccos(x) $$ | $$ f'(x) = \frac{-1}{\sqrt{1-x^2}} $$ | 
| $$ f(x) = \arctan(x) $$ | $$ f'(x) = \frac{1}{1+x^2} $$ | 
| $$ f(x) = a^x $$ | $$ f'(x) = a^x \ln(a) $$ | 
| $$ f(x) = \log_a(x) $$ | $$ f'(x) = \frac{1}{x \ln(a)} $$ | 


| Function | Integral | 
| --- | --- | 
| $$ f(x) = x^n $$ | $$ \int x^n \, dx = \frac{x^{n+1}}{n+1} + C $$ | 
| $$ f(x) = \sin(x) $$ | $$ \int \sin(x) \, dx = -\cos(x) + C $$ | 
| $$ f(x) = \cos(x) $$ | $$ \int \cos(x) \, dx = \sin(x) + C $$ | 
| $$ f(x) = \tan(x) $$ | $$ \int \tan(x) \, dx = -\ln\cos(x)| + C $$ | 
| $$ f(x) = \cot(x) $$ | $$ \int \cot(x) \, dx = \ln\sin(x)| + C $$ | 
| $$ f(x) = \csc(x) $$ | $$ \int \csc(x) \, dx = -\ln\csc(x) + \cot(x)| + C $$ | 
| $$ f(x) = \sec(x) $$ | $$ \int \sec(x) \, dx = \ln\sec(x) + \tan(x)| + C $$ | 
| $$ f(x) = \csc^2(x) $$ | $$ \int \csc^2(x) \, dx = -\cot(x) + C $$ | 
| $$ f(x) = \sec^2(x) $$ | $$ \int \sec^2(x) \, dx = \tan(x) + C $$ | 
| $$ f(x) = e^x $$ | $$ \int e^x \, dx = e^x + C $$ | 
| $$ f(x) = \ln(x) $$ | $$ \int \ln(x) \, dx = x \ln(x) - x + C $$ | 
| $$ f(x) = \arcsin(x) $$ | $$ \int \arcsin(x) \, dx = x \arcsin(x) + \sqrt{1-x^2} + C $$ | 
| $$ f(x) = \arccos(x) $$ | $$ \int \arccos(x) \, dx = x \arccos(x) - \sqrt{1-x^2} + C $$ | 
| $$ f(x) = \arctan(x) $$ | $$ \int \arctan(x) \, dx = x \arctan(x) - \frac{1}{2} \ln(1 + x^2) + C $$ | 
| $$ f(x) = a^x $$ | $$ \int a^x \, dx = \frac{a^x}{\ln(a)} + C $$ | 
| $$ f(x) = \log_a(x) $$ | $$ \int \log_a(x) \, dx = \frac{x \ln(x) - x}{\ln(a)} + C $$ | 



## Limits
### Description
The limit of a function describes the behavior of the function as the input approaches a certain value.
### Formula
$$ \lim_{{x \to a}} f(x) = L $$

## Continuity
### Description
A function is continuous at a point if the limit at that point equals the function's value.
### Formula
$$ \lim_{{x \to a}} f(x) = f(a) $$

## Derivatives
### Description
The derivative of a function represents the rate of change of the function with respect to a variable.
### Formula
$$ f'(x) = \lim_{{h \to 0}} \frac{f(x+h) - f(x)}{h} $$

## Differentiation Rules
### Description
Various rules for finding the derivative of functions.
### Formula
- Constant Rule: $$ \frac{d}{dx} [c] = 0 $$
- Power Rule: $$ \frac{d}{dx} [x^n] = nx^{n-1} $$
- Sum Rule: $$ \frac{d}{dx} [f(x) + g(x)] = f'(x) + g'(x) $$
- Product Rule: $$ \frac{d}{dx} [f(x)g(x)] = f'(x)g(x) + f(x)g'(x) $$
- Quotient Rule: $$ \frac{d}{dx} \left[ \frac{f(x)}{g(x)} \right] = \frac{f'(x)g(x) - f(x)g'(x)}{g(x)^2} $$
- Chain Rule: $$ \frac{d}{dx} [f(g(x))] = f'(g(x))g'(x) $$

## Implicit Differentiation
### Description
Implicit differentiation is used to find the derivative of functions that are not explicitly solved for one variable in terms of another.
### Formula
$$ \frac{d}{dx} [f(y)] = f'(y) \frac{dy}{dx} $$

## Applications of Derivatives
### Description
Derivatives are used to solve various real-world problems including rates of change, optimization, and motion.
### Formula
- Velocity: $$ v(t) = s'(t) $$
- Acceleration: $$ a(t) = v'(t) = s''(t) $$

## Mean Value Theorem
### Description
The Mean Value Theorem states that for a continuous function on a closed interval, there exists at least one point where the tangent is parallel to the secant line.
### Formula
$$ f'(c) = \frac{f(b) - f(a)}{b - a} $$

## Integrals
### Description
Integrals are the reverse process of differentiation, representing the accumulation of quantities.
### Formula
$$ \int f(x) \, dx $$

## Definite Integrals
### Description
Definite integrals calculate the net area under a curve over a specific interval.
### Formula
$$ \int_{a}^{b} f(x) \, dx = F(b) - F(a) $$

## Fundamental Theorem of Calculus
### Description
The Fundamental Theorem of Calculus links the concept of differentiation with integration.
### Formula
$$ \frac{d}{dx} \left( \int_{a}^{x} f(t) \, dt \right) = f(x) $$

## Techniques of Integration
### Description
Various methods for finding integrals.
### Formula
- Substitution: $$ \int f(g(x))g'(x) \, dx = \int f(u) \, du $$
- Integration by Parts: $$ \int u \, dv = uv - \int v \, du $$

## Applications of Integration
### Description
Integrals are used to solve various real-world problems including area under a curve, volume of solids of revolution, and work done by a force.
### Formula
- Area: $$ A = \int_{a}^{b} f(x) \, dx $$
- Volume (Disk Method): $$ V = \pi \int_{a}^{b} [f(x)]^2 \, dx $$
- Work: $$ W = \int_{a}^{b} F(x) \, dx $$

## The Squeeze Theorem
### Description
The Squeeze Theorem is used to find the limit of a function trapped between two other functions whose limits are known.
### Formula
$$ \text{If } g(x) \leq f(x) \leq h(x) \text{ for all } x \text{ near } a, \text{ and } \lim_{{x \to a}} g(x) = \lim_{{x \to a}} h(x) = L, \text{ then } \lim_{{x \to a}} f(x) = L $$

## Intermediate Value Theorem
### Description
The Intermediate Value Theorem states that if a function is continuous on a closed interval \([a, b]\), then it takes every value between \(f(a)\) and \(f(b)\).
### Formula
If \( f \) is continuous on \([a, b]\) and \( k \) is a number between \( f(a) \) and \( f(b) \), then there exists at least one number \( c \) in \((a, b)\) such that \( f(c) = k \).

## L'Hôpital's Rule
### Description
L'Hôpital's Rule is used to find the limit of indeterminate forms.
### Formula
$$ \lim_{{x \to a}} \frac{f(x)}{g(x)} = \lim_{{x \to a}} \frac{f'(x)}{g'(x)} $$
provided the limit on the right side exists.

## Higher-Order Derivatives
### Description
Higher-order derivatives are the derivatives of derivatives, representing higher levels of rates of change.
### Formula
Second derivative:
$$ f''(x) = \frac{d^2 y}{dx^2} $$
Nth derivative:
$$ f^{(n)}(x) = \frac{d^n y}{dx^n} $$

## Related Rates
### Description
Related rates problems involve finding the rate of change of one quantity in terms of the rate of change of another quantity.
### Formula
$$ \frac{dy}{dt} = \frac{dy}{dx} \cdot \frac{dx}{dt} $$

## Linear Approximations and Differentials
### Description
Linear approximations use the tangent line to approximate the value of a function near a point.
### Formula
$$ f(x) \approx f(a) + f'(a)(x - a) $$

## Optimization Problems
### Description
Optimization involves finding the maximum or minimum values of a function subject to certain constraints.
### Formula
1. Identify the function to be optimized.
2. Find the critical points by setting the derivative equal to zero.
3. Determine the maximum or minimum values by evaluating the function at the critical points and endpoints.

## Newton's Method
### Description
Newton's Method is an iterative method for approximating the roots of a real-valued function.
### Formula
$$ x_{n+1} = x_n - \frac{f(x_n)}{f'(x_n)} $$

## The Trapezoidal Rule
### Description
The Trapezoidal Rule is a numerical method for approximating the definite integral of a function.
### Formula
$$ \int_{a}^{b} f(x) \, dx \approx \frac{b - a}{2n} \left[ f(x_0) + 2 \sum_{i=1}^{n-1} f(x_i) + f(x_n) \right] $$

## Simpson's Rule
### Description
Simpson's Rule is another numerical method for approximating the definite integral of a function.
### Formula
$$ \int_{a}^{b} f(x) \, dx \approx \frac{b - a}{3n} \left[ f(x_0) + 4 \sum_{i=1}^{n/2} f(x_{2i-1}) + 2 \sum_{i=1}^{n/2-1} f(x_{2i}) + f(x_n) \right] $$

## Arc Length
### Description
The arc length of a curve is the distance along the curve from one point to another.
### Formula
$$ L = \int_{a}^{b} \sqrt{1 + \left( \frac{dy}{dx} \right)^2} \, dx $$

## Surface Area
### Description
The surface area of a solid of revolution is found by rotating a curve around an axis.
### Formula
Surface area around the x-axis:
$$ S = 2\pi \int_{a}^{b} f(x) \sqrt{1 + \left( \frac{dy}{dx} \right)^2} \, dx $$


