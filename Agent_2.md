### Core Mission: Quantum Derivation of a Classical Projectile

**Objective:** Derive the exact normalized wave function $\psi(x, y)$ for a particle of mass $m$ launched in air from the ground ($y = 0$) with initial velocity magnitude $u$ at launch angle $\theta$ under uniform gravity ($g = 10\text{ m/s}^2$). The particle obeys the 2D Time-Independent Schrödinger Equation under the potential:

$$V(x, y) = \begin{cases} mgy, & \text{for } y \ge 0 \\ \infty, & \text{for } y < 0 \end{cases}$$

---

### Parallel Agent Delegations

#### **Agent 2: Horizontal Motion ODE Solver ($x$-axis)**

* **Primary Task:** Solve the horizontal free-particle motion equation.
* **Instructions:**
1. Take the decoupled horizontal ODE:

$$-\frac{\hbar^2}{2m}\frac{d^2 X(x)}{dx^2} = E_x X(x)$$


2. Solve for the spatial wave solution $X(x)$ in complex exponential/plane-wave form.
3. Derive the explicit expression for the horizontal wavevector $k_x = \frac{\sqrt{2mE_x}}{\hbar}$ directly in terms of launch parameters $(m, u, \theta, \hbar)$.
4. Set up the 1D spatial probability density normalization integral for $X(x)$.



---