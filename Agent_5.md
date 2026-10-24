### Core Mission: Quantum Derivation of a Classical Projectile

**Objective:** Derive the exact normalized wave function $\psi(x, y)$ for a particle of mass $m$ launched in air from the ground ($y = 0$) with initial velocity magnitude $u$ at launch angle $\theta$ under uniform gravity ($g = 10\text{ m/s}^2$). The particle obeys the 2D Time-Independent Schrödinger Equation under the potential:

$$V(x, y) = \begin{cases} mgy, & \text{for } y \ge 0 \\ \infty, & \text{for } y < 0 \end{cases}$$

---

### Parallel Agent Delegations

#### **Agent 5: Normalization Integral & Full Wavefunction Assembly**

* **Primary Task:** Compute integration constants and synthesize the final 2D wavefunction.
* **Instructions:**
1. Evaluate the vertical normalization integral using Airy function properties:

$$\int_{0}^{\infty} \vert{}Y(y)\vert{}^2 dy = 1 \implies C_y^2 \int_{z(0)}^{\infty} \text{Ai}^2(z) \, dz = 1$$


2. Solve explicitly for the normalization constant $C_y$ using $\int \text{Ai}^2(z) dz = z \text{Ai}^2(z) - \text{Ai}'^2(z)$.
3. Combine $X(x)$ and $Y(y)$ into the complete 2D wave function $\psi(x, y) = X(x) Y(y)$.
4. Write out the unified final equation with all constants fully substituted in terms of $(m, u, \theta, g, \hbar)$.