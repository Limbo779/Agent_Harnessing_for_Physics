### Goal :
to build a learning system where it's problem solving and self discovery learning first
we are building two independant systems 
let's name it GRAPHY, BOOKY 
(let's focus purely on GRAPHY and that's why there is no BOOKY details here, forget BOOKY for now)

## **GRAPHY**:
- it's a system I throw in a textbook It splits into chunks and find embedding similarly for each chunk among all the other chunk and put that as a weighted edge between each nodes which is the chunks I will use a small LLM to see whether I need chunk A for chunk B
- If A is prerequisites of B then edge go from A to B
- Each chunk or node is given a score which is sum of outgoing node weight minus sum of incoming node weight The chunk with highest score is the fundamental topic which needs to be studied first Then I take a problem set for the book either from the book itself of external source Then I run similarity check with each chunk and get a score for each chunk for that problem Then I multiply that score for each chunk for that problem with the foundation score of each chunks
- The final number that we get for each problem is the problems foundationess
- So it's good to start with problems of highest foundation score
- Then I choose set of four problem from the top of the list and it's each chunk details Get the chunks data pass it to LLM and ask it to give me the bare minimum topics and concepts needed and rest of the things should be self discovered by me
*(the following below is specific for Competitive Programming, but when i say problem it can be textbook problems, assignments etc. because it's CP question we have the option to stress test our solution. never the less normal problems from textbooks will be difficult because I'm trying to solve with bare minimum and trying to self discover)*
- Then I will go on to solve the problems Then I run automated test case runner that runs thousands of test cases until it hacks my code. Once my problem cannot be hacked then I can move on
- All the submission to the problems would be analysed and then determine whether I self discovered the topics If not then LLM would tell me those topics along with the bare bone concepts for next set of problems If I failed solving the problems or I could resolve the hacking Then LLM not only give the un discovered topics but also the topics that will help me to not struggle.

### Constraints for Making GRAPHY
- strictly use containerization through podman and get the container details like files and images to make it after the completion of this project
- I have installed podman in my **Arch Linux** machine through pacman but if you want any dependancy fix or any fix related to installation, feel free to do so
- use git to track our project and name that repo as 'GRAPHY'
- ignore extremely big files in git so i can push it to my Github but do make sure it can be remade, eg requirements.txt instead of entire venv directry 
- YOU ARE NOT ALLOWED TO PUSH TO MY GITHUB
- JUST TRACK EVERYTHING IN GIT, I WILL PUSH IT MYSELF
- we are mostly gonna deal with Math, Physics, Computer Science textbook so make sure the chunking and embedding for these complex books are perfect, if you feel existing tools are problem then fix it yourself and rememer to focus on general scope instead of specific book. remember i should not have any problem with chunking and embedding for any book
- and make sure embedding is accurate, you may use Local AI models for this embedding task but just make sure it can understand code, figures and technical, scientific and academic terms
- you may use special data types for graph like GraphAr or any better one, because we are dealing with big directed and weighted graph
- to store score for each node/chunk you may use JSON
- use JSON to store both Chunk's score for each problem 
- also store overal net foundationess score of a problem in JSON
- use Local AI to determine the pre request of each chunk
- and also use Local AI for determining the bare minimum concepts needed, analyzing solutions, giving the rest of self discovery topic and topic for next set of problems
- this is my Machine's specs:
=== CPU ===
CPU(s):                                  12
Model name:                              13th Gen Intel(R) Core(TM) i5-1335U

=== RAM ===
Mem:            15Gi       6.5Gi       838Mi       1.1Gi       8.6Gi       8.8Gi

=== GPU ===
00:02.0 VGA compatible controller: Intel Corporation Raptor Lake-P [Iris Xe Graphics] (rev 04)

- sure it may be weak but you can optimize my system specs to it's core and unapologitically squeeze out every bit of performance from my machine
- and you can use Vector database, RAG and Agent Harnessing to split the task into small task and let the agents focus on small problems
- i guess this should make Local AI more powerful
- you are allowed to use suitable AI model for it and any framework but keep our performance demand in mind

### How the final thing should be
- i don't care if it's a podman container that i can spin up and use
- or a neat GUI app or a local web instance
- I'm technical enough to read the output from terminal also
- the main point is do not change our system or tradeoff anything in it for neat frontend
- but do MAKE SURE IT'S USABLE ATLEASE
- finally document the entire thing along with instruction to use
- it should be reliable and work everytime 
- don't let the bugs creep in and give bad result
- REMEMBER PEOPLE ARE GONNA USE THIS TO LEARN SO BE RESPONSIBLE 

- you may ask for any clarifications if you want along the way



## **BOOKY**:
- once GRAPHY gave us the topics to study we will learn that from BOOKY
- after all GRAPHY gives up topic or chunk from the book
- so BOOKY's Job is to explain that so i actually learn
- it's gonna be modified version of this amazing [Github Project](https://github.com/amosblomqvist/learnharness) by [ Eero Alvar](https://github.com/amosblomqvist)
- below is the theoritical framework behind his learning system

---

# Mastering Hard Topics with AI: The Complete Learning Framework

*A detailed synthesis of Eero Alvar's 3-part series on mental compression, 1-on-1 AI pedagogy, and learning agent harnesses.*

---

## Executive Overview & System Architecture

This system re-engineers technical learning around a single goal: **maximizing real, usable understanding built per unit of mental effort spent**.

Rather than treating learning as passive content consumption, this framework treats knowledge as a graph built inside the human brain. It shifts AI from an answer generator into a strict **Socratic Learning Harness** that detects your exact knowledge edge, guides single-step reasoning, and continuously tests recall across changing contexts.

```
┌─────────────────────────────────────────────────────────────────────────┐
│                          PHILOSOPHICAL FOUNDATION                       │
│     Video 1: Mental Models, Cold-Start & Conceptual Compression         │
└────────────────────────────────────┬────────────────────────────────────┘
                                     │
                                     ▼
┌─────────────────────────────────────────────────────────────────────────┐
│                            PEDAGOGICAL LOOP                             │
│       Video 2: Probe ──► Plan ──► Teach ──► Close (The 1-on-1 Loop)     │
└────────────────────────────────────┬────────────────────────────────────┘
                                     │
                                     ▼
┌─────────────────────────────────────────────────────────────────────────┐
│                           SYSTEM ARCHITECTURE                           │
│     Video 3: Agent Harness (Thinking Fields, Sub-Agents & Persistent DB) │
└─────────────────────────────────────────────────────────────────────────┘

```

---

## Part 1: How to Learn Difficult Things (Conceptual Foundation)

### 1. The Nature of Hard Topics

* **Abstraction Density:** Difficult technical subjects (mathematics, theoretical computer science, complex codebase architecture) are dense with layers of abstractions.
* **The Illusion of Understanding:** Following along with a textbook or lecture creates a false sense of mastery. Real understanding only exists when concepts can be derived and applied independently.
* **The Cold Start Problem:** Beginning a new complex topic causes severe friction because your mind lacks the basic mental models required to anchor new concepts.

### 2. "Click" as Conceptual Compression

* **What is Compression?** Learning is not memorizing facts; it is compressing redundant information into elegant mental models.
* **Collapse of Abstractions:** When a concept finally "clicks," rigid textbook definitions collapse into intuitive preferences. You move from memorizing someone else’s arbitrary framing to expressing core ideas in your own personal language.
* **Overcoming Friction:** To reach compression, you must embrace the temporary frustration of non-linear progress. Frustration is the active processing step required for compression.

### 3. Core Tactics for Difficult Material

* **Solve Cold Start First:** Build high-level intuitive metaphors and simple low-rigor models before diving into formal proofs or syntax.
* **Recursive Skill Acquisition:** Break complex skills down into minimal isolated components, master each micro-skill, and systematically recombine them.
* **Active Derivation:** Never accept a statement as true until you can predict or derive the next step yourself.

---

## Part 2: How to Use AI to Learn Things (The Pedagogical Engine)

### 1. Shift in Learning Paradigms

| Learning Paradigm | Structure | Key Drawback / Friction |
| --- | --- | --- |
| **One Teaches Many** | Traditional lectures, online courses | Rigid pace; ignores your personal edge; wastes time on known concepts or bails on missing foundations. |
| **One Learns from Many** | Tab switching across docs, videos & LLMs | High cognitive load; context switching, mismatched notation, and interface overhead. |
| **One-to-One (AI Teacher)** | Socratic 1-on-1 AI learning loop | Keeps struggle centered purely on material; dynamically adapts to your personal knowledge boundary. |

---

### 2. The 4-Step Socratic AI Loop

```
       ┌────────────────────────┐
       │        1. PROBE        │ ◄── Locate exact knowledge edge
       └───────────┬────────────┘
                   │
                   ▼
       ┌────────────────────────┐
       │        2. PLAN         │ ◄── Generate Mermaid DAG map
       └───────────┬────────────┘
                   │
                   ▼
       ┌────────────────────────┐
       │        3. TEACH        │ ◄── 1-step teaching + predict + quiz
       └───────────┬────────────┘
                   │
                   ▼
       ┌────────────────────────┐
       │        4. CLOSE        │ ◄── Lock in intuition ("obviously true")
       └────────────────────────┘

```

#### Step 1: Probe (Finding the Real Edge)

* **Never Guess your Starting Point:** Standard AI chats start either too basic or too advanced. Probing binary-searches your background knowledge to pinpoint where your understanding breaks down.
* **Interactive Diagnostic:** The AI uses quiz tools or explicit questions rather than plain text summaries.
* **Stream-of-Consciousness Input:** You explain what you know in raw, unfiltered thinking. "I don't know" or a wrong guess reveals your precise edge.

#### Step 2: Plan (Graph-Based Learning)

* **Mermaid DAG (Directed Acyclic Graph):** The AI generates a structured dependency tree of concepts specifically tailored to your mind.
* **Eliminate Survey Dumping:** Prevents the AI from rambling through textbook chapter structures.
* **Persistence:** The session graph is saved locally (e.g., in `.alvar/sessions/`) so progress can be resumed across multiple agents.

#### Step 3: Teach (One Stone, Then a Quiz)

* **Micro-Stepping:** The AI teaches **exactly one reasoning step** at a time. It is forbidden from dumping whole slides or multi-paragraph textbook explanations.
* **Predict Before Explanation:** Before the AI explains a step, you are asked to **predict the next move**. This forces active cognitive engagement and uncovers misaligned intuition.
* **Verification Gate:** After teaching a single node, the AI quizzes you. You only advance when that single step is completely locked in.

#### Step 4: Close (Intuition Check)

* **Goal State:** A concept is only considered learned when it feels **obviously true**.
* **Closing Gaps:** If a step fails, the AI pauses, inserts a missing prerequisite node into the graph, and resolves the foundational block.

---

## Part 3: Agent Harness for Learning Things (The Full Technical System)

An **Agent Harness** is the software infrastructure built around an LLM allowing it to act inside a specific domain:

* *Coding Harness* $\rightarrow$ Environment is the Computer.
* *Research Harness* $\rightarrow$ Environment is the Internet.
* *Learning Harness* $\rightarrow$ **Environment is the Human Brain**. You are the system being acted upon.

```
┌──────────────────────────────────────────────────────────────────────────┐
│                         LEARNING AGENT HARNESS                           │
├──────────────────────────────────────────────────────────────────────────┤
│  ┌───────────────────────┐                    ┌───────────────────────┐  │
│  │   THINKING FIELDS     │                    │  KNOWLEDGE GRAPH DB   │  │
│  │  Stream of conscious  │                    │ Persistent Memory &   │  │
│  │   diagnostic logs     │                    │    Knowledge Decay    │  │
│  └───────────┬───────────┘                    └───────────▲───────────┘  │
│              │                                            │              │
│              ▼                                            │              │
│  ┌────────────────────────────────────────────────────────┴───────────┐  │
│  │                      SPECIALIZED SUB-AGENTS                        │  │
│  │  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐  ┌─────────┐  │  │
│  │  │ Researcher   │  │ PDF Reader   │  │ SVG Maker    │  │ Demo Bldr│  │  │
│  │  └──────────────┘  └──────────────┘  └──────────────┘  └─────────┘  │  │
│  └───────────────────────────────────┬────────────────────────────────┘  │
│                                      │                                   │
│                                      ▼                                   │
│  ┌────────────────────────────────────────────────────────────────────┐  │
│  │                    ADAPTIVE PRACTICE ENGINE                        │  │
│  │          Cue-Broadening & Demand-Based Recall Optimization         │  │
│  └────────────────────────────────────────────────────────────────────┘  │
└──────────────────────────────────────────────────────────────────────────┘

```

---

### 1. Key System Components

#### A. Thinking Fields (Raw Diagnostic Stream)

* Every interface interaction contains a mandatory text field where you type your raw, unfiltered stream-of-consciousness thought process.
* **Why?** The agent requires telemetry on *how* you think, not just your final right/wrong answer. This lets it pinpoint mental missteps immediately.

#### B. The Specialized Sub-Agents

To keep teaching accurate and clear, the core harness coordinates four specialized tooling sub-agents:

1. **Researcher Sub-Agent:** Fact-checks formulas, technical documentation, and claims in real-time to eliminate LLM hallucinations.
2. **PDF Reader Sub-Agent:** Parses dense reference papers and textbooks to pull precise context on demand.
3. **SVG Maker Sub-Agent:** Generates precise, visual diagrams on the fly to turn abstract ideas into intuitive visual mental models.
4. **Demo Builder Sub-Agent:** Code-generates interactive mini-applications and dynamic widgets to let you manipulate variables directly.

#### C. Adaptive Practice Engine (Cue Broadening)

* **Understanding vs. Recall:** Real understanding fails in practice if knowledge is tied to a single narrow cue.
* **Broadening Cues:** Practice problems are not random quizzes; they are engineered demands that force you to recall knowledge under novel, unfamiliar contexts.
* **Difficulty Scaling:**
* *Concept Density:* Combining multiple learned nodes into a single complex problem.
* *Cue Familiarity:* Stripping away familiar problem phrasing to test if your model holds under non-standard framing.



#### D. Persistent Knowledge Graph (Memory & Decay)

* Tracks all mastered nodes, weak connections, and date of last review.
* Integrates decay mechanisms (similar to Spaced Repetition / Anki principles) to automatically revisit decaying concepts before embarking on complex downstream topics.

---

## Actionable Implementation Guide

To set up this AI learning workflow in your local development environment:

### 1. Configuration & Repository Setup

Using open-source harness integrations (such as `amosblomqvist/learn` or `Alvarmethod`), instantiate local learner state tracking:

```bash
# Example setup structure for local agent skills (e.g., Claude Code, OpenCode, Codex)
mkdir -p .alvar/sessions
touch .alvar/LEARNER.md

```

### 2. Core System Instructions (Prompt / System Skill Definition)

Add these rules to your AI system instructions or custom skill definitions:

```markdown
# SYSTEM ROLE: Socratic Learning Harness

1. PROBE FIRST: Never explain a subject immediately. Ask targeted diagnostic questions to locate the user's precise knowledge boundary.
2. ONE STEP RULE: Teach exactly ONE step at a time. Never output long multi-paragraph summaries or full textbook chapters.
3. PREDICT BEFORE TEACHING: Before introducing a concept or derivation step, force the user to predict what comes next.
4. VISUAL & DEMO INTEGRATION: Output clean SVG diagrams or dynamic code sandboxes whenever a concept involves spatial or multi-variable relationships.
5. THINKING FIELDS: Require raw stream-of-consciousness input from the user before validating solutions.
6. NO EASY ANSWERS: If the user is stuck, provide the minimal hint required to unblock their own derivation.

```

---

## Summary Checklist for Practical Learning

* [ ] **Identify the Cold Start:** Start with high-level metaphors before tackling mathematical or syntactical rigor.
* [ ] **Build the DAG:** Map out topic dependencies visually before starting a lesson.
* [ ] **Enforce Micro-Stepping:** Learn one node at a time; lock it in with a quiz before advancing.
* [ ] **Expose Thinking Process:** Talk/type through your messy reasoning so the AI agent can spot misconceptions.
* [ ] **Broaden Context Cues:** Practice applying concepts outside the environment in which they were first taught.
* [ ] **Compress into Personal Mental Models:** Express the final concept in your own words until it feels self-evident.