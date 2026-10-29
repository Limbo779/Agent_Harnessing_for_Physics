### Agent Peer-Review Protocols

#### Objective

Validate the mathematical rigor, dimensional consistency, boundary conditions, and physical applicability of the assigned output. Eliminate errors before combining into the final derivation.

---

### Core Critique Guidelines

1. **Proof-Backed Error Identification**
* Do not claim a step is wrong based on intuition alone. Every flagged error **must** be accompanied by a rigorous, step-by-step mathematical proof demonstrating why the original step fails, along with the corrected line-by-line derivation.


2. **Explicit Admission of Unproven Doubts**
* If a step seems suspicious or non-standard, but a formal mathematical or physical proof of its invalidity cannot be constructed, explicitly state:
> *"I flagged [specific step], but could not provide a conclusive proof of error. Provisionally treating as correct pending full system integration."*




3. **Dimensional Analysis Mandate**
* Verify that every dimensionless variable (e.g., $z(y)$ in Airy equation transformations) is strictly unitless:

$$\text{Dim}\left[\left(\frac{2m^2 g}{\hbar^2}\right)^{1/3} \left(y - \frac{E_y}{mg}\right)\right] = 1$$


* Ensure wavevector dimensions match $[k_x] = \text{L}^{-1}$ and wave function dimensions match $[\psi(x,y)] = \text{L}^{-1}$.


4. **Boundary Condition & Asymptotics Verification**
* Confirm that all boundary conditions ($Y(y=0) = 0$, $\lim_{y \to \infty} Y(y) = 0$, normalization integrals) are satisfied by the proposed solutions without mathematical divergence.



---

### Standardized Critique Report Template

Each critiquing agent must format their evaluation using the following structure:

```markdown
## Peer Critique Report
**Reviewer:** [Agent X]
**Target Output Reviewed:** [Agent Y's Topic/Output]

### 1. Step-by-Step Mathematical Verification
* [Detailed verification of each major algebraic/calculus step performed by the target agent.]

### 2. Flaws & Proven Counter-Derivations
* **Flagged Step:** [Quote or reference the exact equation/step]
* **Nature of Error:** [Algebraic, Boundary Condition, Dimensional, Physical]
* **Rigorous Mathematical Proof of Error:**
  $$ [Step-by-step proof demonstrating the flaw] $$
* **Corrected Formulation:**
  $$ [Correct equation to be substituted] $$

### 3. Unverified Suspicious Points / Admissions
* [Explicit list of any steps that appear dubious but where no definitive proof of error could be established.]

### 4. Final Verdict & Integration Status
* **Status:** [APPROVED / APPROVED WITH CORRECTIONS / REJECTED]
* **Action Items for Integration:** [Clear, itemized fixes required]

```