# Codex Session Note: Flash-P Plant Pipeline

This note summarizes a read-only inspection of the `Flash-P_Plant` pipeline.
The pipeline was not run, and no source code was edited.

## Scope

The inspection focused on the Codex version of the plant pipeline:

- `Flash-P_Plant/Codex/AGENTS.md`
- `Flash-P_Plant/Codex/Agent/*_AGENT.md`
- `Flash-P_Plant/Codex/Agent/shared/*.py`

The Claude and OpenCode/Aider/Goose folders appear to mirror the same general
pipeline structure, but this note treats the Codex folder as the reference.

## What This Pipeline Does

FLASH-P Plant turns literature about a plant trait and species into a causal
network that can be tested against perturbation experiments.

The pipeline is file-driven. Each stage writes structured files, usually JSON
or CSV, and the next stage reads those files. The agent instruction files define
what each stage is allowed to read, write, and reason about.

## Stage-by-Stage Summary

### 1. Literature Review

Input:

- A plant trait/species request.

Output:

- `data/curated_edges.json`
- `data/perturbation_dataset.json`

Instruction files:

- `Flash-P_Plant/Codex/AGENTS.md`
- `Flash-P_Plant/Codex/Agent/LITERATURE_REVIEW_AGENT.md`
- `Flash-P_Plant/Codex/Agent/shared/LEXICON.md`

Python scripts:

- `Agent/shared/validate_schema.py`
- Optional compact-format helpers: `toon_codec.py`, `compact.py`

Plain English:

This stage gathers DOI-backed causal edges and perturbation tests from the
literature. In the Light workflow, it drafts from known biology, verifies with
WebSearch, and stores DOI-backed findings.

### 2. Literature Review Judge

Input:

- `data/curated_edges.json`
- `data/perturbation_dataset.json`

Output:

- Updated `data/curated_edges.json`
- Updated `data/perturbation_dataset.json`
- `data/literature_judge_report.json`

Instruction files:

- `Flash-P_Plant/Codex/Agent/LITERATURE_REVIEW_JUDGE_AGENT.md`

Python scripts:

- `Agent/shared/validate_schema.py`

Plain English:

This stage audits the literature collection for missing canonical biology, such
as missing pathways, hubs, receptors, treatments, or mutants. It appends
findings rather than deleting Step 1 output.

### 3. Builder

Input:

- `data/curated_edges.json`
- `data/literature_judge_report.json`

Output:

- `network/network.json`
- `network/algebraic_equations.json`
- `network/ode_equations.json`
- `network/node_annotations.json`

Instruction files:

- `Flash-P_Plant/Codex/Agent/BUILDER_AGENT.md`

Python scripts:

- `Agent/shared/check_network_structure.py`
- `Agent/shared/validate_schema.py`

Plain English:

This stage selects a biologically defensible subset of curated edges and turns
it into a connected causal network with algebraic and ODE equations.

Important rule:

- The Builder must not read perturbation results or validation outputs.

### 4. Biological Judge

Input:

- `network/*.json`
- `data/curated_edges.json`
- `data/literature_judge_report.json`

Output:

- `network/judge_review_iteration_1.json`

Instruction files:

- `Flash-P_Plant/Codex/Agent/JUDGE_AGENT.md`

Python scripts:

- No main stage-specific script. `validate_schema.py` may still be used for JSON
  shape checks.

Plain English:

This stage reviews the biological quality of the network before validation. It
suggests changes backed by curated evidence, but it does not directly edit the
network.

Forbidden inputs:

- Raw perturbation data.
- Reconciled perturbation data.
- Validation results.
- Refinement outputs.

### 5. Perturbation Reconciliation

Input:

- `data/perturbation_dataset.json`
- `network/network.json`

Output:

- `data/reconciled_perturbation_dataset.json`

Instruction files:

- `Flash-P_Plant/Codex/Agent/PERTURBATION_AGENT.md`

Python scripts:

- `Agent/shared/validate_schema.py`

Plain English:

This stage maps raw literature perturbation tests onto actual network nodes, so
the validators know which node to perturb and what result to expect.

### 6. Validator

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
- Supporting CSV files and steady-state dumps.

Instruction files:

- `Flash-P_Plant/Codex/Agent/VALIDATOR_AGENT.md`

Python scripts:

- `Agent/shared/validate_pipeline_inputs.py`
- `Agent/shared/flashp_validator.py`
- `Agent/shared/ode_validator.py`
- `Agent/shared/rwr_validator.py`
- `Agent/shared/validate_schema.py`

Plain English:

This stage runs three prediction methods against the reconciled perturbation
tests: algebraic, ODE, and signed Random-Walk-with-Restart.

### 7. Refinement

Input:

- `validation/`
- `network/`
- Failure analysis from the Validator.

Output:

- `refinement/iteration_N/` snapshots.
- Potential final refined model files under `refinement/`.

Instruction files:

- `Flash-P_Plant/Codex/Agent/REFINEMENT_AGENT.md`

Python scripts:

- `Agent/shared/flashp_validator.py`
- `Agent/shared/ode_validator.py`
- `Agent/shared/rwr_validator.py`
- `Agent/shared/check_network_structure.py`
- `Agent/shared/validate_schema.py`

Plain English:

This is the first stage allowed to look at validation results. It diagnoses
failures and applies conservative, evidence-backed fixes, then re-runs
validators.

### 8. Export

Input:

- Best available model from `refinement/` or fallback `network/`.
- Literature data from `data/`.
- Validation results from `validation/`.

Output:

- `supplementary/Table_S*.csv`
- `supplementary/master_test_level.csv`
- `supplementary/Fig_Data/`
- `network/cytoscape/`
- `provenance/`

Instruction files:

- `Flash-P_Plant/Codex/Agent/EXPORT_AGENT.md`

Python scripts:

- `Agent/shared/export_supplementary.py`
- `Agent/shared/network_to_cytoscape.py`
- `Agent/shared/export_all_csvs.py`
- `Agent/shared/export_master_csv.py`
- `Agent/shared/record_provenance.py`

Plain English:

This stage turns the final model and validation results into tables, figure
data, Cytoscape files, and provenance records.

## Data Flow Diagram

Plain-English flow:

`trait/species request`

-> Literature Review creates `curated_edges.json` and `perturbation_dataset.json`

-> Literature Review Judge appends missing biology and writes
`literature_judge_report.json`

-> Builder creates `network.json`, `algebraic_equations.json`, and
`ode_equations.json`

-> Biological Judge writes `judge_review_iteration_1.json`

-> Perturbation stage maps tests into `reconciled_perturbation_dataset.json`

-> Validator writes prediction results, metrics, and failure analysis

-> Refinement writes iteration snapshots and possibly a refined best model

-> Export writes supplementary tables, figure data, Cytoscape exports, and
provenance.

## Safety Notes

- Start from `Flash-P_Plant/Codex/` when using the Codex version, because the
  instructions and script paths are relative.
- Do not run the pipeline casually; a full run writes many files across `data/`,
  `network/`, `validation/`, `refinement/`, `supplementary/`, and `provenance/`.
- The validation and export scripts expect a populated network run directory.
  Inspect their expected inputs before running them.
