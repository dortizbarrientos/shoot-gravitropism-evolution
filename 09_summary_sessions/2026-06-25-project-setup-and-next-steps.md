# Work So Far And Suggested Next Sessions

## Work So Far

We separated the shoot gravitropism work from the upstream FLASH-P repository
and created a dedicated GitHub project:

<https://github.com/dortizbarrientos/shoot-gravitropism-evolution>

The local repository is:

```text
/Users/uqdortiz/repos/shoot-gravitropism-evolution
```

The project now has an initial scaffold for studying the evolution and
development of shoot gravitropism.

Current major folders:

- `01_references/`
- `02_hypotheses/`
- `03_graphical_models/`
- `04_mathematical_theories/`
- `05_developmental_models/`
- `06_evolutionary_models/`
- `07_flashp_learning/`
- `08_notes/`
- `09_summary_sessions/`

The `07_flashp_learning/` folder contains the earlier FLASH-P learning notes
and the toy Light-format example. The toy example is labelled as instructional,
not curated biology.

We also created a root `AGENTS.md` file with durable project instructions for
future sessions.

## Project Principles Established

- Inspect before editing.
- Do not run full pipelines unless explicitly asked.
- Do not install packages unless explicitly asked.
- Keep toy examples separate from curated biological claims.
- Treat signed edges as curated causal summaries, not proof of direct molecular
  mechanism.
- Document commands, assumptions, and modelling decisions.
- Use plain English notes suitable for PhD students.

## Suggested Next Sessions

### 1. Commit `AGENTS.md`

Review `AGENTS.md`, then commit and push it so the repository carries its
working rules.

### 2. Create `01_references/paper_index.md`

Start a curated bibliography for shoot gravitropism.

Useful fields:

- DOI
- title
- species
- tissue or organ
- developmental stage
- main claim
- evidence type
- notes on uncertainty

### 3. Draft a biological scope note

Create a plain-English note defining what "shoot gravitropism" means for this
project.

Questions to answer:

- Which species are in scope first?
- Which developmental stages matter?
- What is the phenotype readout?
- Are we modelling early sensing, bending dynamics, long-term development, or
  all of these separately?

### 4. Build a first hypothesis map

Use `02_hypotheses/` to describe likely modules:

- gravity sensing
- auxin redistribution
- auxin transporters
- asymmetric growth
- cell-wall response
- curvature
- recovery or adaptation

Each hypothesis should be labelled as one of:

- toy or teaching idea
- working hypothesis
- review-supported claim
- primary-paper-supported claim

### 5. Make a first graphical model

Use `03_graphical_models/` for a non-curated causal draft.

Every edge should be labelled by evidence status:

- hypothesis
- review-supported
- primary-paper-supported
- uncertain

### 6. Delay FLASH-P-style curation until references are ready

Only after references are curated should we begin turning evidence into:

- candidate nodes
- signed causal edges
- perturbation tests
- expected phenotype directions

At that stage, curated biological files should remain separate from toy
examples.
