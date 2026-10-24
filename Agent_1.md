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