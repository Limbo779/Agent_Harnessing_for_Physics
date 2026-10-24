### Core Mission: Quantum Derivation of a Classical Projectile

**Objective:** Derive the exact normalized wave function $\psi(x, y)$ for a particle of mass $m$ launched in air from the ground ($y = 0$) with initial velocity magnitude $u$ at launch angle $\theta$ under uniform gravity ($g = 10\text{ m/s}^2$). The particle obeys the 2D Time-Independent Schrödinger Equation under the potential:

$$V(x, y) = \begin{cases} mgy, & \text{for } y \ge 0 \\ \infty, & \text{for } y < 0 \end{cases}$$

---

### Parallel Agent Delegations

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