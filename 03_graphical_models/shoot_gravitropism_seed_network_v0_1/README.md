# Shoot Gravitropism Seed Network v0.1

This is a hypothesis-level seed network, not curated biology.

Version v0.1 supersedes v0 scientifically because it improves the causal logic of the first scaffold.

The v0 model was useful as a learning artifact, but it treated some biological contexts as if they were direct causal nodes. In particular, it separated `Statocytes` and `Endodermis` as causal nodes and placed `Gravitropic_vs_Agravitropic_Families` upstream as if it caused genotype effects and bending.

The v0.1 model changes that structure:

- `Endodermal_Statocyte_Gravity_Sensing` replaces separate statocyte and endodermis causal nodes.
- `Amyloplast_Displacement` is treated as a sensing process downstream of gravistimulation.
- `Family_Genotype_Effects` is treated as a genetic background factor that may modulate intermediate mechanisms and bending trajectory.
- `Gravitropic_vs_Agravitropic_Families` is treated as an observed classification downstream of bending behaviour, not as a causal driver.
- `relation_type` separates direct causal hypotheses from modulation, context, and classification relationships.
- `sign = NA` is used where a relation is not a simple positive or negative causal edge.
- `include_in_first_sbgn` marks which edges should be considered for the first SBGN Activity Flow export.

No v0.1 SBGN file has been created yet.

## Files

- `candidate_nodes.csv`: hypothesis-level nodes for the v0.1 network.
- `candidate_edges.csv`: hypothesis-level relationships among nodes.
- `evidence_gaps.md`: notes on missing evidence and literature checks needed before curation.

## How To Read `candidate_edges.csv`

- `edge_id`: unique edge identifier.
- `source`: upstream node.
- `target`: downstream node.
- `sign`: `1` for promotion or activation, `-1` for inhibition or repression, and `NA` for modulation, context, or classification.
- `relation_type`: plain-English relationship class, such as `causal`, `modulation`, `context`, or `classification`.
- `layer`: broad biological or modelling layer.
- `status`: evidence status. All rows are currently `hypothesis`.
- `rationale`: why the edge is included in this seed model.
- `reference_needed`: whether a specific source is still needed before treating the edge as curated.
- `include_in_first_sbgn`: whether the edge should be included in the first SBGN Activity Flow export. This is a modelling and diagramming choice. It does not define biological truth.

Suggested interpretation of `include_in_first_sbgn`:

- `yes`: include in the first SBGN Activity Flow export.
- `maybe`: discuss before including, because the relation is modulatory or context-dependent.
- `no`: do not include in the first SBGN Activity Flow export.

## Scientific Caution

Every edge in this folder is a hypothesis.

No edge should be described as curated until a specific reference is added.

Signed edges are causal summaries for modelling. They are not proof of a direct molecular mechanism.
