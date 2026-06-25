# Codex Session Notes

This file summarizes a read-only Codex inspection focused only on
`Flash-P_Plant`. No source code was edited and the FLASH-P pipeline was not run.

## Scope Inspected

The clearest Codex entry point for the plant pipeline is:

- `Flash-P_Plant/Codex/AGENTS.md`

That orchestrator points to stage-specific instruction files under:

- `Flash-P_Plant/Codex/Agent/`

The Claude and OpenCode/Aider/Goose folders mirror the same broad pipeline
shape, but these notes use the Codex variant as the reference.

## Pipeline Overview

FLASH-P Plant is a file-driven, multi-stage pipeline. Each stage writes
structured handoff files that the next stage reads.

The broad flow is:

1. Literature Review
2. Literature Review Judge
3. Builder
4. Biological Judge
5. Perturbation Reconciliation
6. Validation
7. Refinement
8. Export

The Light version uses compact JSON or TOON-style handoff files. In the compact
format, DOIs are the main provenance field.

## Stage 1: Literature Review

Input:

- A phenotype/species request, such as `Shoot Branching in Arabidopsis`.
- No prior network files are required.

Output:

- `data/curated_edges.json`
- `data/perturbation_dataset.json`

Purpose:

- Build the raw literature repository.
- Capture DOI-backed causal edges.
- Capture DOI-backed perturbation tests.

Instruction files:

- `Flash-P_Plant/Codex/AGENTS.md`
- `Flash-P_Plant/Codex/Agent/LITERATURE_REVIEW_AGENT.md`
- `Flash-P_Plant/Codex/Agent/shared/LEXICON.md`

Relevant Python scripts:

- `Agent/shared/validate_schema.py` checks output schema.
- `Agent/shared/toon_codec.py` supports compact tabular storage.
- `Agent/shared/compact.py` can compact files, but is optional.

## Stage 1.5: Literature Review Judge

Input:

- `data/curated_edges.json`
- `data/perturbation_dataset.json`

Output:

- Updated `data/curated_edges.json`
- Updated `data/perturbation_dataset.json`
- `data/literature_judge_report.json`

Purpose:

- Audit Step 1 for missing canonical biology.
- Add missing pathways, hubs, receptors, mutants, treatments, or crosstalk.
- Preserve Step 1 output and append new findings.

Instruction files:

- `Flash-P_Plant/Codex/AGENTS.md`
- `Flash-P_Plant/Codex/Agent/LITERATURE_REVIEW_JUDGE_AGENT.md`

Relevant Python scripts:

- `Agent/shared/validate_schema.py` checks updated files.

## Stage 2: Builder

Input:

- `data/curated_edges.json`
- `data/literature_judge_report.json`
- Optionally, a previous judge review if applying feedback.

Output:

- `network/network.json`
- `network/algebraic_equations.json`
- `network/ode_equations.json`
- `network/node_annotations.json`

Purpose:

- Convert the literature edge pool into a causal model.
- Select only edges that belong in the mechanistic network.
- Generate algebraic and ODE equations.

Instruction files:

- `Flash-P_Plant/Codex/AGENTS.md`
- `Flash-P_Plant/Codex/Agent/BUILDER_AGENT.md`

Relevant Python scripts:

- `Agent/shared/check_network_structure.py` checks network structure.
- `Agent/shared/validate_schema.py` checks schema compliance.

Important checks:

- No floating nodes.
- Every node should reach the phenotype through a directed path.
- Every edge needs a DOI.
- There should be exactly one phenotype node.
- Source-node flags should match edge structure.

## Stage 2.5: Biological Judge

Input:

- `network/network.json`
- `network/algebraic_equations.json`
- `network/ode_equations.json`
- `network/node_annotations.json`
- `data/curated_edges.json`
- `data/literature_judge_report.json`

Forbidden input:

- `data/perturbation_dataset.json`
- `data/reconciled_perturbation_dataset.json`
- Anything under `validation/`
- Anything under `refinement/`

Output:

- `network/judge_review_iteration_1.json`

Purpose:

- Review biological completeness before validation.
- Suggest additions or changes using curated evidence.
- Avoid optimizing against test results.

Instruction files:

- `Flash-P_Plant/Codex/AGENTS.md`
- `Flash-P_Plant/Codex/Agent/JUDGE_AGENT.md`

Relevant Python scripts:

- No main Python script owns this stage.
- `validate_schema.py` may still be used for JSON shape checks.

## Stage 3: Perturbation Reconciliation

Input:

- `data/perturbation_dataset.json`
- `network/network.json`

Output:

- `data/reconciled_perturbation_dataset.json`

Purpose:

- Map raw perturbation tests onto network nodes.
- Keep testable in-network perturbations.
- Encode knockout, knockdown, overexpression, treatment, rescue, modifiers, and
  comparison baselines.

Instruction files:

- `Flash-P_Plant/Codex/AGENTS.md`
- `Flash-P_Plant/Codex/Agent/PERTURBATION_AGENT.md`

Relevant Python scripts:

- `Agent/shared/validate_schema.py` checks raw and reconciled perturbation files.

## Stage 4: Validator

Input:

- `network/network.json`
- `network/algebraic_equations.json`
- `data/reconciled_perturbation_dataset.json`

Output:

- `validation/script_validation_results.json`
- `validation/ode_validation_results.json`
- `validation/rwr_validation_results.json`
- `validation/accuracy_metrics.json`
- `validation/failure_analysis.json`
- `validation/method_comparison.json`
- Per-method CSV result files.
- Per-method steady-state dumps.

Purpose:

- Run perturbation tests against the network.
- Compare algebraic, ODE, and signed Random-Walk-with-Restart methods.
- Produce accuracy metrics and failure analysis.

Instruction files:

- `Flash-P_Plant/Codex/AGENTS.md`
- `Flash-P_Plant/Codex/Agent/VALIDATOR_AGENT.md`

Relevant Python scripts:

- `Agent/shared/validate_pipeline_inputs.py`
- `Agent/shared/flashp_validator.py`
- `Agent/shared/ode_validator.py`
- `Agent/shared/rwr_validator.py`
- `Agent/shared/validate_schema.py`

## Stage 5: Refinement

Input:

- Files under `validation/`
- Files under `network/`
- Failure details such as `validation/failure_analysis.json`

Output:

- `refinement/iteration_N/` snapshots.
- Potential final refined files such as:
  - `refinement/refined_network.json`
  - `refinement/refined_equations.json`
  - `refinement/refinement_report.json`

Purpose:

- Use validation failures to make bounded, evidence-backed fixes.
- Prefer diagnosis before changes.
- Re-run validators after changes.
- Stop after a small bounded number of iterations.

Instruction files:

- `Flash-P_Plant/Codex/AGENTS.md`
- `Flash-P_Plant/Codex/Agent/REFINEMENT_AGENT.md`

Relevant Python scripts:

- `Agent/shared/flashp_validator.py`
- `Agent/shared/ode_validator.py`
- `Agent/shared/rwr_validator.py`
- `Agent/shared/check_network_structure.py`
- `Agent/shared/validate_schema.py`

## Stage 6: Export

Input:

- Best network and equation files, either from `refinement/` or fallback
  `network/`.
- `data/curated_edges.json`
- `data/perturbation_dataset.json`
- `data/reconciled_perturbation_dataset.json`
- Validation result files under `validation/`.

Output:

- Supplementary tables under `supplementary/`.
- Figure data CSVs under `supplementary/Fig_Data/`.
- Cytoscape files under `network/cytoscape/`.
- Provenance output under `provenance/`.

Purpose:

- Produce final artifacts for readers, figures, Cytoscape, and downstream
  analysis.

Instruction files:

- `Flash-P_Plant/Codex/AGENTS.md`
- `Flash-P_Plant/Codex/Agent/EXPORT_AGENT.md`

Note:

- The Plant Codex export file appears to contain some copied cattle wording, but
  it is still the export instruction file present under `Flash-P_Plant/Codex`.

Relevant Python scripts:

- `Agent/shared/export_supplementary.py`
- `Agent/shared/network_to_cytoscape.py`
- `Agent/shared/export_all_csvs.py`
- `Agent/shared/export_master_csv.py`
- `Agent/shared/record_provenance.py`
- `Agent/shared/validate_schema.py`

## Plain-English Data Flow

User asks for a plant trait and species.

The Literature Review builds a DOI-backed pool of edges and perturbation tests.

The Literature Review Judge fills obvious biology gaps in that pool.

The Builder selects a connected, causal subset and writes equations.

The Biological Judge reviews the model before anyone looks at test results.

The Perturbation stage maps raw experiments onto network nodes.

The Validator runs algebraic, ODE, and RWR predictions against those tests.

The Refinement stage uses failures to make conservative, evidence-backed fixes.

The Export stage writes supplementary tables, figure data, Cytoscape files, and
provenance.

In short:

`trait/species request`
-> `curated edges + raw tests`
-> `gap-audited edge/test pool`
-> `network + equations`
-> `judge review`
-> `reconciled tests`
-> `validation results`
-> `refined best model`
-> `tables + figures + Cytoscape + provenance`

## Safety Notes

- Start from the correct agent folder, such as `Flash-P_Plant/Codex/`, because
  the pipeline uses relative paths.
- Do not run the full pipeline casually; it writes many JSON, CSV, validation,
  refinement, export, and provenance files.
- Validation and export scripts are helpers for existing run directories. They
  are not a substitute for understanding the stage inputs first.
