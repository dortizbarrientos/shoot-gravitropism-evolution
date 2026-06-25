# Shoot Gravitropism FlashP Curation v0

This workspace is for a cautious FlashP-style literature curation pass for shoot gravitropism.

It is separate from the v0.1 hypothesis network.

The goal is to move candidate edges toward review-supported or primary-paper-supported status without overwriting the hypothesis tables.

## Trait And Context

- trait: shoot gravitropic bending over time
- phenotype node: `Shoot_Gravitropic_Bending_Over_Time`
- experimental context: dark rotation / gravitropic response over 8 hours
- comparison context: gravitropic versus agravitropic families

## Evidence Streams

Two evidence streams are kept separate:

- `data/senecio_specific/`: direct `Senecio lautus` evidence only.
- `data/arabidopsis_mechanistic_prior/`: Arabidopsis mechanistic-prior evidence only.

At this stage, no direct `Senecio lautus` literature evidence has been entered.

The Arabidopsis files contain a small seed set based on user-provided seed references. These entries are transfer-prior evidence, not direct Senecio evidence.

## FlashP Scope

This workspace uses only the FlashP Light literature-curation shape:

- `curated_edges.json`
- `perturbation_dataset.json`

Do not run:

- Builder
- Judge
- Perturbation reconciliation
- Validator
- Refinement
- Export
- the full FlashP pipeline

## Source Of Truth

The v0.1 hypothesis source tables remain:

```text
../shoot_gravitropism_seed_network_v0_1/candidate_nodes.csv
../shoot_gravitropism_seed_network_v0_1/candidate_edges.csv
```

Do not rewrite those tables from this workspace automatically.

First review the evidence and mapping tables.
