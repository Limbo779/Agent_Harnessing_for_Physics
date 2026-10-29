### Core Mission: Quantum Derivation of a Classical Projectile

**Objective:** Derive the exact normalized wave function $\psi(x, y)$ for a particle of mass $m$ launched in air from the ground ($y = 0$) with initial velocity magnitude $u$ at launch angle $\theta$ under uniform gravity ($g = 10\text{ m/s}^2$). The particle obeys the 2D Time-Independent Schrödinger Equation under the potential:

$$V(x, y) = \begin{cases} mgy, & \text{for } y \ge 0 \\ \infty, & \text{for } y < 0 \end{cases}$$

---

### Parallel Agent Delegations

#### **Agent 4: Ground Boundary Conditions & Eigenvalue Constraints**

* **Primary Task:** Analyze ground boundary constraints and zero-point energy matching.
* **Instructions:**
1. Apply the infinite hard-wall condition at ground level: $Y(y=0) = 0$.
2. Evaluate $z(0) = -\left(\frac{2m^2 g}{\hbar^2}\right)^{1/3} \frac{E_y}{mg} = -\left(\frac{2 m E_y^3}{\hbar^2 g^2}\right)^{1/3}$.
3. Express $z(0)$ in terms of the negative zeros $a_n$ of the Airy function $\text{Ai}(a_n) = 0$.
4. Establish the exact quantum relation between vertical energy states $E_{y, n}$, gravitational acceleration $g$, mass $m$, and Planck's reduced constant $\hbar$.



---