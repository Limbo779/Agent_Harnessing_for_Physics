# Adaptive Learning & Competitive Programming Multi-Agent Architecture

## 1. System Overview

This system is an adaptive learning framework designed for competitive programming and self-guided discovery. It uses specialized AI agents to curate problem sets, split domain knowledge into minimal theory versus discoverable concepts, run adversarial hacking rounds, enforce strict optimization constraints, and recursively re-evaluate student weaknesses.

```
+-----------------------------------------------------------------------------------+
|                                   SYSTEM FLOW                                     |
|                                                                                   |
|  [PC Agent] ---> [Teacher Agent] ---> [User/Judge] ---> [Hacker Agent]           |
|       ^               |                                       |                   |
|       |               v                                       v                   |
|       +--- (Branch A: Remediation) <--- [Strict Limit] <---+                      |
|                                              |                                    |
|                                              +---> (Branch B: Mastery Completion) |
+-----------------------------------------------------------------------------------+
```

---

## 2. Agent Definitions & Roles

### 2.1 Problem Controller (PC) Agent
* **Role:** Curriculum & Problem Selection Engine.
* **Objective:** Selects structured problem sets matched to the learner's current progression state.
* **Core Responsibilities:**
  * **Initial Selection (`PC1`):** Selects the first set of 4 benchmark problems.
  * **Adaptive Re-Selection (`PC2`):** Decides the logical and optimal next set of 4 problems based on feedback from the Teacher Agent.
* **Inputs:** Historical performance logs, current skill matrix, and feedback payloads from the Teacher Agent.
* **Outputs:** 4-problem candidate sets for pedagogical structuring.
* **Interactions:**
  * Passes selected problem sets to the **Teacher Agent**.
  * Receives updated weakness profiles and remediation instructions from the **Teacher Agent** during Branch A.

---

### 2.2 Teacher Agent (`Teach`)
* **Role:** Pedagogical Structuring, Concept Splitter, & Performance Analyst.
* **Objective:** Maximizes self-discovery while ensuring the learner has minimal foundational theory.
* **Core Responsibilities:**
  1. **Problem Ordering (`T1`):** Arranges problems in strictly increasing order of difficulty tailored for self-discovery.
  2. **Concept Splitting (`T2`):** Divides total topic knowledge into two distinct subsets:
     * **Bare-Bones Theory (`BB1`):** Minimum necessary theory required to approach problems; serves as the base for self-discovery.
     * **Self-Discovery Theory (`SD1`):** Advanced insights, tricks, or theoretical leaps that the user is meant to discover independently while solving problems.
  3. **Content Delivery (`BB2`):** Delivers Bare-Bones theory to the user before problem-solving begins.
  4. **Performance Hardening (`T_LIMIT`):** Analyzes contest submissions and tightens time/memory limits to force code optimization.
  5. **Remediation Analysis (`TA1` - Branch A):** Evaluates failed or abandoned attempts, identifies specific struggle points, combines them with uncollected self-discovery topics, and restructures the curriculum to prevent repeated failure.
  6. **Final Mastery Evaluation (`TA2` & `TELL` - Branch B):** Analyzes all historical submissions upon completion, determines which self-discovery concepts were successfully discovered, and directly teaches remaining missed gaps.
* **Inputs:** Raw problem sets from PC Agent; user execution logs from Local Judge; hack results from Hacker Agent.
* **Outputs:** Bare-Bones learning modules, updated time/memory constraints, remediation context for PC Agent, final gap analysis.
* **Interactions:**
  * Receives problems from **PC Agent**.
  * Delivers theory to the **User**.
  * Adjusts contest rules on the **Local Judge System**.
  * Coordinates loop-backs via **PC Agent** on failure, or completes user training on success.

---

### 2.3 Hacker Agent (`Hacker`)
* **Role:** Adversarial Tester & Edge-Case Validator.
* **Objective:** Expose flaws, unhandled edge cases, time-complexity vulnerabilities, and incorrect logic in user submissions.
* **Core Responsibilities:**
  * Acts as a rival participant in the contest environment.
  * Attempts to break ("hack") user solutions using automated input generation and constraint checking.
  * Can leverage SMT/Constraint solvers (e.g., **Z3**) to mathematically construct counter-examples and breaking test cases.
  * Constrained to a maximum of **3 hack attempts per solution**, provided further hacks remain available.
* **Inputs:** User submission source code, problem constraints, execution logs.
* **Outputs:** Hack Pass/Fail status, breaking input test cases.
* **Interactions:**
  * Intercepts passed solutions from the **Virtual Contest / Local Judge System**.
  * Routes outcomes:
    * **Failed Hack Round (`H_FAIL`):** Triggers Branch A (Remediation).
    * **Cleared Hack Round (`H_PASS`):** Escalates submission to the Teacher Agent for limit tightening.

---

### 2.4 Virtual Contest / Local Judge System (Execution Environment)
* **Role:** Automated Execution, Grading, & Environment Host.
* **Objective:** Provide a sandboxed environment for testing code correctness, time limits, and memory limits.
* **Core Responsibilities:**
  * Host virtual contests for problem sets.
  * Grade user code against base test cases.
  * Enforce standard and restricted time/memory limits.
* **Interactions:**
  * Receives user code submissions.
  * Exposes submission data to **Hacker Agent** and **Teacher Agent**.

---

## 3. Detailed Workflow Stages

### Stage 1: Initial Setup & Concept Split
1. **PC Agent (`PC1`)** selects the first set of 4 problems.
2. **Teacher Agent (`T1`)** orders the 4 problems by increasing difficulty and self-discovery potential.
3. **Teacher Agent (`T2`)** splits required concepts into:
   * **Bare-Bones Theory (`BB1`)**
   * **Self-Discovery Theory (`SD1`)**
4. **Teacher Agent (`BB2`)** presents Bare-Bones theory to the user. User completes study before opening problems.

### Stage 2: Virtual Contest & Adversarial Hacking
1. **User (`VC`)** solves the problem set within a virtual contest on the local judge system.
2. **Hacker Agent (`HR`)** targets solved submissions:
   * Uses Z3 / constraint solvers if required.
   * Allowed up to 3 hacks per submission.
3. **Outcome Routing:**
   * **H_FAIL (User failed Hacker round):** Escalate immediately to **Branch A** (Remediation).
   * **H_PASS (User cleared Hacker round):** Proceed to **Stage 3**.

### Stage 3: Strict Time & Memory Limit Hardening
1. **Teacher Agent (`T_LIMIT`)** reviews submissions and applies restricted time & memory limits to enforce optimal time/space complexity.
2. **Outcome Routing:**
   * **L_PASS (User survived strict limits):** Escalate to **Branch B** (Mastery Completion).
   * **L_FAIL / Give Up:** Escalate to **Branch A** (Remediation).

---

## 4. Execution Branches

### Branch A: Adaptive Remediation Loop (Retry Cycle)
* **Trigger:** User fails Hacker round (`H_FAIL`) OR fails strict constraints / gives up (`L_FAIL` / `GIVE_UP`).
* **Process:**
  1. **Teacher Analysis (`TA1`):** Analyzes historical submissions to pinpoint exact concepts where the user struggled.
  2. **Curriculum Re-organization:** Merges identified weakness topics with uncollected self-discovery topics.
  3. **New Environment (`NV`):** Generates a new virtual contest tailored so the user will not struggle on the same pattern again.
  4. **PC Re-evaluation (`PC2`):** PC Agent decides the logical and optimal next 4 problems based on this updated profile.
  5. **Loop-Back (`C` -> `T1`):** Returns to Stage 1 to re-arrange and re-split concepts for the new problem set.

### Branch B: Mastery Validation & Completion
* **Trigger:** User successfully passes strict time and memory limits (`L_PASS`).
* **Process:**
  1. **Testing Complete (`NO_MORE`):** Terminates the testing and contest cycle.
  2. **Comprehensive Review (`TA2`):** Teacher Agent evaluates all submissions across all rounds to determine which intended self-discovery concepts were successfully discovered independently.
  3. **Gap Filling (`TELL`):** Teacher Agent explicitly presents all remaining undiscovered topics and provides structured explanations to fill final gaps in understanding.

---

## 5. Summary Interaction Matrix

| Source Agent | Target Agent | Trigger Condition | Information Passed |
| :--- | :--- | :--- | :--- |
| **PC Agent** | Teacher Agent | Initial setup or new round | Selected 4-problem set |
| **Teacher Agent** | User | Post concept-split | Bare-bones minimal theory |
| **User** | Local Judge | Problem attempt submission | Source code |
| **Local Judge** | Hacker Agent | Passed initial judge tests | Solution executable & code |
| **Hacker Agent** | Teacher Agent / Branch A | Solution hacked | Breaking test case / fail signal |
| **Hacker Agent** | Teacher Agent / Stage 3 | Solution unhacked (3 attempts) | Hack clear signal |
| **Teacher Agent** | PC Agent | Contest failed / Abandoned | Struggle concepts & left-out topics |
| **Teacher Agent** | User | Contest successfully cleared | Final gap-filling theory presentation |