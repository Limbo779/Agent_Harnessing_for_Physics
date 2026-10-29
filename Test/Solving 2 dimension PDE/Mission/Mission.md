### Core Mission: Quantum Derivation of a Classical Projectile

**Objective:** Derive the exact normalized wave function $\psi(x, y)$ for a particle of mass $m$ launched in air from the ground ($y = 0$) with initial velocity magnitude $u$ at launch angle $\theta$ under uniform gravity ($g = 10\text{ m/s}^2$). The particle obeys the 2D Time-Independent Schrödinger Equation under the potential:

$$V(x, y) = \begin{cases} mgy, & \text{for } y \ge 0 \\ \infty, & \text{for } y < 0 \end{cases}$$

---

### Parallel Agent Delegations

#### **Agent 1: Potential Mapping & Separation of Variables**

* **Primary Task:** Establish the differential equation foundation and separate variables.
* **Instructions:**
1. Define the spatial domain $(x \in (-\infty, \infty), y \in [0, \infty))$ and boundary conditions.
2. Express the classical kinetic energy components in terms of launch parameters:

$$E_x = \frac{1}{2}m(u\cos\theta)^2, \quad E_y = \frac{1}{2}m(u\sin\theta)^2$$


3. Write down the full 2D Hamiltonian operator $\hat{H} = -\frac{\hbar^2}{2m} \nabla^2 + V(x, y)$.
4. Apply the separable ansatz $\psi(x, y) = X(x)Y(y)$ to decouple the time-independent Schrödinger equation into two independent 1D Ordinary Differential Equations (ODEs) for $X(x)$ and $Y(y)$.



---

#### **Agent 2: Horizontal Motion ODE Solver ($x$-axis)**

* **Primary Task:** Solve the horizontal free-particle motion equation.
* **Instructions:**
1. Take the decoupled horizontal ODE:

$$-\frac{\hbar^2}{2m}\frac{d^2 X(x)}{dx^2} = E_x X(x)$$


2. Solve for the spatial wave solution $X(x)$ in complex exponential/plane-wave form.
3. Derive the explicit expression for the horizontal wavevector $k_x = \frac{\sqrt{2mE_x}}{\hbar}$ directly in terms of launch parameters $(m, u, \theta, \hbar)$.
4. Set up the 1D spatial probability density normalization integral for $X(x)$.



---

#### **Agent 3: Vertical Motion ODE Solver ($y$-axis & Airy Transformation)**

* **Primary Task:** Transform and solve the vertical linear potential differential equation.
* **Instructions:**
1. Take the decoupled vertical ODE:

$$-\frac{\hbar^2}{2m}\frac{d^2 Y(y)}{dy^2} + mgy Y(y) = E_y Y(y)$$


2. Perform the dimensionless variable transformation:

$$z(y) = \left(\frac{2m^2 g}{\hbar^2}\right)^{1/3} \left(y - \frac{E_y}{mg}\right)$$


3. Show how this converts the differential equation into Airy's canonical equation:

$$\frac{d^2 Y(z)}{dz^2} - z Y(z) = 0$$


4. Apply physical boundary conditions as $y \to \infty$ to eliminate the exponentially growing Airy branch $\text{Bi}(z)$, leaving $Y(y) = C_y \text{Ai}(z(y))$.



---

#### **Agent 4: Ground Boundary Conditions & Eigenvalue Constraints**

* **Primary Task:** Analyze ground boundary constraints and zero-point energy matching.
* **Instructions:**
1. Apply the infinite hard-wall condition at ground level: $Y(y=0) = 0$.
2. Evaluate $z(0) = -\left(\frac{2m^2 g}{\hbar^2}\right)^{1/3} \frac{E_y}{mg} = -\left(\frac{2 m E_y^3}{\hbar^2 g^2}\right)^{1/3}$.
3. Express $z(0)$ in terms of the negative zeros $a_n$ of the Airy function $\text{Ai}(a_n) = 0$.
4. Establish the exact quantum relation between vertical energy states $E_{y, n}$, gravitational acceleration $g$, mass $m$, and Planck's reduced constant $\hbar$.



---

#### **Agent 5: Normalization Integral & Full Wavefunction Assembly**

* **Primary Task:** Compute integration constants and synthesize the final 2D wavefunction.
* **Instructions:**
1. Evaluate the vertical normalization integral using Airy function properties:

$$\int_{0}^{\infty} \vert{}Y(y)\vert{}^2 dy = 1 \implies C_y^2 \int_{z(0)}^{\infty} \text{Ai}^2(z) \, dz = 1$$


2. Solve explicitly for the normalization constant $C_y$ using $\int \text{Ai}^2(z) dz = z \text{Ai}^2(z) - \text{Ai}'^2(z)$.
3. Combine $X(x)$ and $Y(y)$ into the complete 2D wave function $\psi(x, y) = X(x) Y(y)$.
4. Write out the unified final equation with all constants fully substituted in terms of $(m, u, \theta, g, \hbar)$.