To get an AI model to write a fully functional, production-ready system without hitting edge-case loops or broken dependencies, you must remove all ambiguity regarding **architecture, data formats, and logic boundaries** before writing any code.

---

## Phase 1: Constructing the System Specification

Write your specification document using these five essential structural blocks:

### 1. Hard System Boundaries & Technology Stack

* **Target Runtime:** State the exact language, version, and operating system requirements.
* **Allowed Libraries:** Explicitly list mandatory dependencies and ban problematic/bloated alternatives (e.g., *"Use standard library `dataclasses` and `pathlib`. Do not use heavy ML or native C drivers unless specified"*).
* **Execution Constraint:** Define resource limits (CPU-only, memory ceiling, local vs. cloud API constraints).

### 2. Strict Input/Output Data Contracts

Models fail when data shapes are implicit. Define schemas explicitly:

* **Input Schema:** Specify file formats, JSON keys, string encodings, or CLI arguments expected by the system.
* **Internal Data Models:** Provide exact types for intermediate data structures (e.g., using Python `TypedDict`, `dataclasses`, or Pydantic models).
* **Output Schema:** Define the precise output format (e.g., Markdown structure, database schema, or CLI stdout format).

### 3. Logic Separation (Deterministic vs. Probabilistic)

Divide your algorithm into two distinct categories so the model doesn't use an LLM for operations easily handled by code:

* **Deterministic Logic:** Provide exact mathematical equations, graph formulas, sorting rules, and filter operations.
* **Probabilistic Logic:** Specify the exact prompt, temperature, input variables, and expected JSON output schema for any LLM call embedded in the system.

### 4. Modular Decomposition

Break the system into isolated, single-responsibility components:

* Module A: Data Ingestion & Normalization
* Module B: Core Business/Algorithmic Engine
* Module C: External API / Execution Runner
* Module D: Storage / Interface Layer

### 5. Failure Modes & Edge Case Rules

List explicitly how the software must handle failure:

* What happens when an input file is missing or malformed?
* How are API timeouts or rate limits retried?
* What is the fallback if a sub-process fails or exits with a non-zero code?

---

## Phase 2: The Step-by-Step AI Execution Strategy

Do not ask the model to output the entire codebase in a single prompt. Split the execution across four distinct prompts:

```
[Prompt 1: Architecture & Interfaces] ──> [Prompt 2: Core Data Models & Utilities]
                                                         │
[Prompt 4: Integration & Execution Script] <── [Prompt 3: Feature Modules (Iterative)]

```

### Step 1: Request the Architecture & Interface Skeleton

* **Action:** Pass your spec and instruct the model to generate *only* the directory structure, class interfaces, abstract methods, and typed data schemas.
* **Goal:** Verify that the model understands the data flow and system boundary before implementation begins.

### Step 2: Implement Utilities & Low-Level Helpers

* **Action:** Ask for the foundational modules (file parsing, deterministic math helpers, data transformers).
* **Goal:** Ensure all low-level building blocks work independently without external LLM dependencies.

### Step 3: Implement Core Business Modules (One by One)

* **Action:** Request code for one module at a time. Instruct the model to include inline unit tests or verification functions for each module.
* **Goal:** Prevent context-window truncation and enforce modular isolation.

### Step 4: Assemble the Main Execution Script & CLI

* **Action:** Instruct the model to wire the tested modules together into a single entry-point script (`main.py` or CLI runner) with logging and error handling.

---

## Phase 3: The Meta-Prompt Specification Template

Copy and fill out this blueprint structure when preparing your system prompt:

```markdown
# SYSTEM SPECIFICATION: [Project Name]

## 1. OBJECTIVE
[Single-sentence summary of what the software does and its primary output]

## 2. ENVIRONMENT & STACK CONSTRAINTS
- Language/Runtime: [e.g., Python 3.11+]
- Allowed Libraries: [List exact libraries]
- Explicitly Banned: [List forbidden tools/frameworks]

## 3. DATA CONTRACTS
### Input:
- Format: [e.g., CSV, JSON, raw text]
- Structure: [Define schema]

### Output:
- Format: [e.g., Hybrid Markdown, JSON database]
- Structure: [Define schema]

## 4. SYSTEM ARCHITECTURE & MODULES
- Module 1 (`parser`): Reads input and normalizes into Data Schema X.
- Module 2 (`engine`): Applies Formula Y: `Score = (A - B) * C`.
- Module 3 (`runner`): Executes sub-process Z and parses stdout.

## 5. DETERMINISTIC RULES & FORMULAS
- Rule 1: [Explicit math or logic constraint]
- Rule 2: [Sorting/Filtering criterion]

## 6. INSTRUCTIONS FOR CODE GENERATION
1. Write fully runnable, type-hinted code.
2. Include docstrings for all functions.
3. Handle missing files and API failures gracefully using explicit try/except blocks.
4. Do not leave placeholder comments like `pass` or `# TODO: implement this`.