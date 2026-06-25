# Codex Continuation Handoff

Date: 2026-06-25

Use this file to start a new Codex session for this repository.

## Copy-Paste Prompt For A New Session

```text
Read AGENTS.md first.

We are working in:
/Users/uqdortiz/repos/shoot-gravitropism-evolution

This is a scientific project on the evolution and development of shoot gravitropism.

Follow these rules:
- Inspect before editing.
- Prefer small, reviewable changes.
- Do not run full FlashP pipelines unless explicitly asked.
- Do not install packages unless explicitly asked.
- Do not commit or push unless explicitly asked.
- Keep toy examples, hypothesis-level networks, reviewed evidence, and curated biology separate.
- Do not present any edge as curated unless it has a specific DOI or user-provided source.
- Treat candidate_nodes.csv and candidate_edges.csv as source-of-truth tables for hypothesis networks.
- Treat SBGN, Graphviz, Mermaid, SVG, and PNG outputs as derived artifacts.

Current project status:
- v0.1 hypothesis network exists at:
  03_graphical_models/shoot_gravitropism_seed_network_v0_1/
- Its source tables are:
  03_graphical_models/shoot_gravitropism_seed_network_v0_1/candidate_nodes.csv
  03_graphical_models/shoot_gravitropism_seed_network_v0_1/candidate_edges.csv
- Its SBGN causal-spine draft is:
  03_graphical_models/shoot_gravitropism_seed_network_v0_1/sbgn/shoot_gravitropism_seed_network_v0_1_causal_spine_af.sbgn
- Its retained working previews are in:
  03_graphical_models/shoot_gravitropism_seed_network_v0_1/exports/working_previews/
- The terminal preview renderer is:
  tools/render_network.py
- A cautious FlashP literature-curation start plan is:
  03_graphical_models/shoot_gravitropism_flashp_curation_v0/flashp_literature_curation_start_plan.md
- A first FlashP-style curation workspace now exists at:
  03_graphical_models/shoot_gravitropism_flashp_curation_v0/

Before doing new work:
1. Run git status --short.
2. Inspect the relevant README files near the work area.
3. Explain what you plan to change before editing.
4. Stop before commit or push unless I explicitly ask.
```

## Current Repo Purpose

This repository is for studying shoot gravitropism across developmental and evolutionary scales.

The immediate modelling focus is a cautious progression from:

1. hypothesis-level causal scaffolds;
2. derived visual previews;
3. FlashP-style literature curation;
4. later, reviewed or curated network models.

## Important Existing Files

- `AGENTS.md`: durable project instructions for Codex.
- `README.md`: top-level project overview.
- `03_graphical_models/shoot_gravitropism_seed_network_v0_1/`: current hypothesis-level seed network.
- `03_graphical_models/shoot_gravitropism_flashp_curation_v0/`: FlashP-style literature curation workspace.
- `tools/render_network.py`: standard-library renderer for working previews.

## Current Network State

The v0.1 network is hypothesis-level, not curated biology.

The source-of-truth files are:

```text
03_graphical_models/shoot_gravitropism_seed_network_v0_1/candidate_nodes.csv
03_graphical_models/shoot_gravitropism_seed_network_v0_1/candidate_edges.csv
```

Key v0.1 modelling choices:

- `Endodermal_Statocyte_Gravity_Sensing` replaced separate `Statocytes` and `Endodermis` causal nodes.
- `Amyloplast_Displacement` is downstream of gravistimulation.
- `Family_Genotype_Effects` modulates intermediate mechanisms and bending trajectory.
- `Gravitropic_vs_Agravitropic_Families` is an observed classification downstream of bending, not a cause.
- `relation_type` separates causal, modulation, context, and classification relations.
- `include_in_first_sbgn` controls first SBGN/preview inclusion; it is not a biological truth label.

## Visual Outputs

Retained working previews are:

```text
03_graphical_models/shoot_gravitropism_seed_network_v0_1/exports/working_previews/
  01_causal_spine_view/
  02_genotype_modulation_view/
  03_full_network_supplementary_view/
```

Each retained view should keep:

- `README.md`
- `network_preview.svg`
- `network_preview.png`

Intermediate `.dot` and `.mmd` files are reproducible and should not be kept unless explicitly selected.

## FlashP Status

We have not run FlashP.

We inspected the local FlashP Plant Codex instructions at:

```text
/Users/uqdortiz/repos/FlashP/Flash-P_Plant/Codex/
```

The first cautious FlashP step should be literature curation only.

The curation workspace is:

```text
03_graphical_models/shoot_gravitropism_flashp_curation_v0/
```

It currently separates direct Senecio evidence from Arabidopsis mechanistic-prior
evidence:

```text
03_graphical_models/shoot_gravitropism_flashp_curation_v0/data/senecio_specific/
03_graphical_models/shoot_gravitropism_flashp_curation_v0/data/arabidopsis_mechanistic_prior/
```

The start plan is:

```text
03_graphical_models/shoot_gravitropism_flashp_curation_v0/flashp_literature_curation_start_plan.md
```

The Senecio-specific JSON files are intentionally empty until direct evidence is
found. Arabidopsis JSON files should be treated as transfer-prior evidence, not
direct Senecio evidence.

Do not run Builder, Perturbation reconciliation, Validator, Refinement, Export, or a full pipeline unless explicitly asked.

## Latest Curation Audit

A read-only audit checked the first curation workspace:

- Senecio-specific JSON files were valid JSON and intentionally empty.
- Arabidopsis mechanistic-prior JSON files were valid JSON and structurally
  Light-style.
- DOI values in `evidence/edge_evidence_table.csv` were present in
  `evidence/reference_index.csv`.
- Edge IDs in the evidence table matched v0.1 `candidate_edges.csv`.
- Primary-paper-supported rows had support notes.
- Arabidopsis rows had transfer caveats.
- H008-H013 were not overclaimed.
- No obvious generated preview, cache, or duplicate files were found inside the
  curation workspace.

## Suggested Next Session Options

Good next tasks:

1. Review the curation workspace files before staging them.
2. Inspect `evidence/edge_evidence_table.csv` and decide whether the support
   notes are clear enough for PhD-student reading.
3. Inspect `mapping/flashp_to_v0_1_candidate_edges.csv` before deciding whether
   any v0.1 source CSV should be updated later.
4. Add README notes to evidence subfolders only if they would make the evidence
   separation clearer.
5. Start a WebSearch-based literature review only if explicitly asked.

Tasks to avoid unless explicitly requested:

- Running the full FlashP pipeline.
- Merging Arabidopsis evidence into Senecio claims.
- Rewriting v0.1 candidate CSVs from unreviewed FlashP output.
- Creating publication-quality figures without a figure-design step.
- Deleting generated files without a cleanup plan.

## Git State At Handoff

At the time this file was updated, known uncommitted changes included:

- modified root `README.md`, intentionally changed by the user to add a section
  about the HO framework;
- the new FlashP curation workspace under
  `03_graphical_models/shoot_gravitropism_flashp_curation_v0/`;
- this handoff file.

Run this at the start of the next session:

```bash
git status --short
```
