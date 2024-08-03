<!-- C:\Users\razer\Desktop\walkerrh.github.io\SCROLLS_FOLDER\WALKERRH\research.md -->
<!-- C:\Users\razer\Desktop\walkerrh.github.io\SCROLLS_FOLDER\ME\research.md -->




[Home](/index.html)

# My Passion for Investing

With over five years of experience in the investment sector, my passion for the financial markets has only grown stronger. 
My journey began with an intense fascination for the complexities of trading stocks and stock options, leading me to dedicate 
more than 12 hours a day to honing my skills. However, I soon realized that to truly excel, I needed to blend my financial 
acumen with technological prowess. This led me to learn coding, enabling me to design, test, and implement my own trading 
strategies, thereby allowing me to work on projects one could only dream of. Such projects have caught the eye of fellow 
comrades and classmates which have joined the initiative.

# Track Record

| Year | Type | Starting Balance | Ending Balance |
| --- |
| 2023 | R&D | - | - |
| 2022 | R&D | - | - |
| 2021 | Cash | $5,000 | $115,000 |
| 2020 | Paper | $100,000 | $120,000 |

# Investment Thesis Lore

The financial market, often perceived as a chaotic and unpredictable entity, is in fact a complex system that, while intricate, 
adheres to discernible patterns. These patterns can be unveiled through the precise application of mathematical tools, much like 
the laws of physics that govern our world. The market's behavior is not random, but rather a reflection of the collective actions 
of emotionally-driven humans actively pricing-in the value of a security. This price, while seemingly fluid, can be predicted and 
is essentially pre-determined, only revealing itself in a two dimensional manner. It's a fascinating interplay of human psychology, 
mathematical precision, and the immutable laws of physics, all converging to shape the financial landscape. This perspective allows 
us to approach investing not as a game of chance, but as a science, where careful analysis and strategic foresight can yield 
predictable outcomes.        


### F_GM_Cointegrated_Jan_2012_to_Jun_2015

![](/assets/walkerrh/research/F_GM_Cointegrated_Jan_2012_to_Jun_2015.png)

### F_p6_nadjp_p_p_h_trendline

![F_p6_nadjp_p_p_h_trendline_](/assets/walkerrh/research/F_p6_nadjp_p_p_h_trendline.png)

### GSPC_p4

![GSPC_p4 (1)](/assets/walkerrh/research/GSPC_p4.png)

### p5_t15_KO

![p5_t15_KO](/assets/walkerrh/research/p5_t15_KO.png)

### p5_t30_KO

![p5_t30_KO](/assets/walkerrh/research/p5_t30_KO.png)

### p5_t60_KO

![p5_t60_KO](/assets/walkerrh/research/p5_t60_KO.png)

### S&P500 divided by M2 Money Supply

![SP500 divided M2SL](/assets/walkerrh/research/S&P500_divided_by_M2_Money_Supply.png)

### FED_Total_Assets_SPY_and_Recessions
![](/assets/walkerrh/research/FED_Total_Assets_SPY_and_Recessions.png)

### Stock price moving through a cube

![](/assets/walkerrh/research/stock_crosses_cube_whiteboard.png)

# ---

60 second in 1 minute

60 minutes in 1 hour

an arc minute is one-sixtieth of a degree and is divided into 60 arc seconds
arc-minute: 1/60 of a degree, symbol (')
arc-second: 1/3600 of a degree, symbol ('')


# ---

| Cycle                     | Duration (Years) | Description                                                                                                                                                       |
| ------------------------- | ---------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 25920-Year Cycle          | 25920            | Years for the Earth's rotational axis to return to the same point. Gradual change in Earth's rotational axis orientation, influencing equinox and solstice timings over millennia, known as precession of the equinoxes.             |
| 21600-Year Cycle          | 21600            | Variations in Earth's axial tilt, affecting the distribution of solar radiation and seasonal contrasts over long periods, known as obliquity or axial tilt cycle. |

5:6 = pentagram:hexagram






## Precession of the Equinoxes (25920-Year Cycle)

### Calculation:
The precession of the equinoxes is primarily caused by the gravitational forces exerted by the Sun and the Moon on Earth's equatorial bulge. This force creates a torque that slowly changes the orientation of Earth's rotational axis.

- **Torque Calculation:**
  $$
  \tau = I \cdot \alpha
  $$
  Where $$ \tau $$ is the torque, $$ I $$ is Earth's moment of inertia, and $$ \alpha $$ is the angular acceleration.

- **Period Calculation:**
  $$
  T_p = \frac{2\pi}{\alpha}
  $$
  The period $$ T_p $$ is approximately 25920 years.

- **Angular Acceleration:**
  $$
  \alpha \approx \frac{2 \cdot 3.1416}{25920} \text{ radians/year} \approx 7.66 \times 10^{-7} \text{ radians/year}
  $$

- **Period:** Approximately 25920 years.

### Scientific Explanation:
- The precession period is derived from complex calculations involving:
  - Earth's moment of inertia.
  - Gravitational forces from the Sun and Moon.
  - Distribution of mass within Earth and its orbit around the Sun.

## Obliquity or Axial Tilt (21600-Year Cycle)

### Calculation:
- The variation in Earth's axial tilt (obliquity) is influenced by gravitational interactions, primarily from Jupiter and Saturn, over long periods.

- **Rate of Change of Obliquity:**
  $$
  \dot{\theta} \approx \frac{24.5^\circ - 22.1^\circ}{21600 \text{ years}} \approx 0.0111^\circ/\text{year}
  $$

- **Rate f Change of Obliquity:**
  $$
  \dot{\theta} \approx \frac{24.5^\circ - 22.1^\circ}{21600 \text{ years}} \approx 1.11 \times 10^{-3} \text{ degrees/year}
  $$

- **Range:** 
    - Varies between approximately 22.1° and 24.5° over a cycle of about 21600 years.
    - Obliquity varies between approximately 22.1° and 24.5° over a cycle of about 21600 years.

### Scientific Explanation:
- Obliquity changes are calculated based on:
  - Gravitational forces from Jupiter and Saturn.
  - Torque exerted on Earth's rotational axis.
  - Celestial mechanics governing the stability of Earth's axial tilt.























# Draw a cube in Python with matplotlib

![](/assets/walkerrh/research/python_matplotlib_cube.png)

![](/assets/walkerrh/research/python_matplotlib_cube_drawing.png)

```python
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

# Define the vertices of a cube
vertices = [
    [0, 0, 0],
    [1, 0, 0],
    [1, 1, 0],
    [0, 1, 0],
    [0, 0, 1],
    [1, 0, 1],
    [1, 1, 1],
    [0, 1, 1]
]

# Define the six faces of the cube
faces = [
    [vertices[0], vertices[1], vertices[2], vertices[3]],
    [vertices[4], vertices[5], vertices[6], vertices[7]],
    [vertices[0], vertices[1], vertices[5], vertices[4]],
    [vertices[2], vertices[3], vertices[7], vertices[6]],
    [vertices[1], vertices[2], vertices[6], vertices[5]],
    [vertices[4], vertices[7], vertices[3], vertices[0]]
]

# Create a new figure
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Create a 3D polygon collection and add it to the axes
poly3d = Poly3DCollection(faces, facecolors='cyan', linewidths=1, edgecolors='r', alpha=.25)
ax.add_collection3d(poly3d)

# Set the limits of the axes
ax.set_xlim([0, 1])
ax.set_ylim([0, 1])
ax.set_zlim([0, 1])

# Set labels
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Show the plot
plt.show()
```

# Draw a rotatable cube in Python with turtle

![](/assets/walkerrh/research/turtle_rotated_square.png)

# Mathematical Structure Behind the 3D Cube Drawing in Turtle Graphics

This script uses basic principles of 3D geometry and transformations to draw a 3D cube on a 2D screen using the turtle module. Here's a breakdown of the mathematical concepts involved:

## 1. Coordinate System
The cube is defined in a 3D coordinate system with vertices given as (x, y, z) coordinates. The vertices of the cube are centered around the origin (0, 0, 0).

## 2. Rotation Matrices
To rotate a point around an axis, we use rotation matrices. The rotations are applied to the vertices of the cube.

### Rotation around the X-axis:

The rotation matrix for the X-axis is:

$$
\begin{bmatrix}
1 & 0 & 0 \\
0 & \cos(\theta) & -\sin(\theta) \\
0 & \sin(\theta) & \cos(\theta)
\end{bmatrix}
$$

For a point \((x, y, z)\), the rotated coordinates are:

$$
\begin{align}
x' &= x \\
y' &= y \cos(\theta) - z \sin(\theta) \\
z' &= y \sin(\theta) + z \cos(\theta)
\end{align}
$$

### Rotation around the Y-axis:

The rotation matrix for the Y-axis is:

$$
\begin{bmatrix}
\cos(\theta) & 0 & \sin(\theta) \\
0 & 1 & 0 \\
-\sin(\theta) & 0 & \cos(\theta)
\end{bmatrix}
$$

For a point \((x, y, z)\), the rotated coordinates are:

$$
\begin{align}
x' &= x \cos(\theta) + z \sin(\theta) \\
y' &= y \\
z' &= -x \sin(\theta) + z \cos(\theta)
\end{align}
$$

### Rotation around the Z-axis:

The rotation matrix for the Z-axis is:

$$
\begin{bmatrix}
\cos(\theta) & -\sin(\theta) & 0 \\
\sin(\theta) & \cos(\theta) & 0 \\
0 & 0 & 1
\end{bmatrix}
$$

For a point \((x, y, z)\), the rotated coordinates are:

$$
\begin{align}
x' &= x \cos(\theta) - y \sin(\theta) \\
y' &= x \sin(\theta) + y \cos(\theta) \\
z' &= z
\end{align}
$$

## 3. Perspective Projection
To convert 3D coordinates to 2D coordinates for drawing, we use a simple perspective projection. The idea is to scale the coordinates based on their distance from the viewer, creating a sense of depth.

The perspective projection formula used is:

$$
\begin{align}
\text{factor} &= \frac{200}{z + 300} \\
x_{\text{proj}} &= x \times \text{factor} \\
y_{\text{proj}} &= y \times \text{factor}
\end{align}
$$

This projects the 3D coordinates \((x, y, z)\) onto the 2D plane.

## 4. Drawing with Turtle
The turtle module is used to draw lines between the projected 2D points to form the edges of the cube.

## Code Explanation

### Initialization:
- Initialize the turtle and screen.

### Drawing Function:
- `draw_line(p1, p2)`: Draws a line between two 2D points.
- `project(x, y, z)`: Projects 3D coordinates to 2D using perspective projection.

### Rotation Functions:
- `rotate_x(point, angle)`: Rotates a point around the X-axis.
- `rotate_y(point, angle)`: Rotates a point around the Y-axis.
- `rotate_z(point, angle)`: Rotates a point around the Z-axis.

### Drawing the Cube:
- `draw_cube(size, angle_x, angle_y, angle_z)`: Defines the vertices and edges of the cube, applies the rotations, projects the vertices, and draws the edges.

### Main Execution:
- Define the size of the cube and rotation angles.
- Call the `draw_cube()` function to draw the cube with the specified parameters.
- Hide the turtle and display the window.

```python
import turtle
import math

# Initialize turtle
t = turtle.Turtle()
screen = turtle.Screen()
screen.bgcolor("white")
t.speed(0)

# Function to draw a line between two 3D points
def draw_line(p1, p2):
    t.penup()
    t.goto(p1[0], p1[1])
    t.pendown()
    t.goto(p2[0], p2[1])

# Function to project 3D coordinates to 2D
def project(x, y, z):
    factor = 200 / (z + 300)
    x_proj = x * factor
    y_proj = y * factor
    return (x_proj, y_proj)

# Function to rotate a point around the x-axis
def rotate_x(point, angle):
    x, y, z = point
    y_rot = y * math.cos(angle) - z * math.sin(angle)
    z_rot = y * math.sin(angle) + z * math.cos(angle)
    return (x, y_rot, z_rot)

# Function to rotate a point around the y-axis
def rotate_y(point, angle):
    x, y, z = point
    x_rot = x * math.cos(angle) + z * math.sin(angle)
    z_rot = -x * math.sin(angle) + z * math.cos(angle)
    return (x_rot, y, z_rot)

# Function to rotate a point around the z-axis
def rotate_z(point, angle):
    x, y, z = point
    x_rot = x * math.cos(angle) - y * math.sin(angle)
    y_rot = x * math.sin(angle) + y * math.cos(angle)
    return (x_rot, y_rot, z)

# Function to draw the cube
def draw_cube(size, angle_x, angle_y, angle_z):
    # Define the vertices of the cube
    vertices = [
        [-size / 2, -size / 2, -size / 2],
        [size / 2, -size / 2, -size / 2],
        [size / 2, size / 2, -size / 2],
        [-size / 2, size / 2, -size / 2],
        [-size / 2, -size / 2, size / 2],
        [size / 2, -size / 2, size / 2],
        [size / 2, size / 2, size / 2],
        [-size / 2, size / 2, size / 2]
    ]

    # Define the edges of the cube
    edges = [
        (0, 1), (1, 2), (2, 3), (3, 0),  # front square
        (4, 5), (5, 6), (6, 7), (7, 4),  # back square
        (0, 4), (1, 5), (2, 6), (3, 7)   # connecting lines
    ]

    # Apply rotation and project the vertices
    rotated_vertices = [rotate_x(v, angle_x) for v in vertices]
    rotated_vertices = [rotate_y(v, angle_y) for v in rotated_vertices]
    rotated_vertices = [rotate_z(v, angle_z) for v in rotated_vertices]
    projected = [project(x, y, z) for x, y, z in rotated_vertices]

    # Draw the edges
    for edge in edges:
        draw_line(projected[edge[0]], projected[edge[1]])

# Set the size of the cube
cube_size = 100

# Set the rotation angles in radians
angle_x = math.radians(40)
angle_y = math.radians(40)
angle_z = math.radians(40)

# Draw the cube
draw_cube(cube_size, angle_x, angle_y, angle_z)

# Hide the turtle and display the window
t.hideturtle()
turtle.done()
```




# The Forty-One-Month Cycle

### source: 
  - Title: CYCLES - The Mysterious Forces That Trigger Events
  - Written by: Edward R. Dewey with Og Mandino
  - Published by: Hawthorn Books, INC.
  - Published in: New York

![](/assets/walkerrh/research/41_month_cycle_a-1.png)

![](/assets/walkerrh/research/41_month_cycle_b-1.png)

  - In 1912, a New York group of investors discovered that the Rothschilds had analyzed British consols and identified repeating price fluctuations used for forecasting. The group hired a mathematician who, using the Dow Jones Railroad Averages, identified a forty-one-month cycle and three other cycles, aiding their successful investments around World War I.
  - Around ten years later, Professor W. L. Crum of Harvard identified a similar cycle in New York commercial-paper rates. Concurrently, Professor Joseph Kitchin of Harvard found a forty-month cycle in economic indicators in Great Britain and the United States from 1890 to 1922.
  - In 1935, twenty-three years after the original discovery, Chapin Hoskins independently identified this cycle in various economic data, including common-stock prices. His extensive study in 1938 refined the cycle to 40.68 months, showing consistent patterns from 1868 through 1945, despite wars and economic changes.
  - Despite numerous theories, including random behavior, interference from other cycles, and public awareness, the exact cause of this disruption remains unexplained.
