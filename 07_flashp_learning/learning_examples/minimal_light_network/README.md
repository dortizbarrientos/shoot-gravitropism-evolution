# Minimal Light Network Teaching Example

This folder is a toy teaching example for understanding FLASH-P Light-format
files. It is not a real curated biological network and should not be treated as
evidence for any scientific claim.

The toy pathway is:

```text
MAX2 --(+)-> BRC1 --(-)-> Shoot_Branching
```

In this example, `MAX2` activates `BRC1`, and `BRC1` inhibits
`Shoot_Branching`. A toy `MAX2` knockout is expected to increase shoot
branching because less `MAX2` means less `BRC1`, and less `BRC1` means less
repression of branching.

The DOI value `10.0000/toy-example-not-real` is deliberately fake-looking and
marks these records as instructional placeholders, not real literature
provenance.

## Files

### `curated_edges.json`

This is the toy literature edge pool.

- `metadata`: describes the example dataset.
- `nodes`: maps each node name to a compact node type.
- `edges`: lists causal edges that could be used by a network.

Edge fields:

- `eid`: edge ID.
- `s`: source node.
- `t`: target node.
- `x`: sign, where `1` means activation and `-1` means inhibition.
- `d`: DOI/provenance string.

Node type fields:

- `G`: gene.
- `P`: phenotype.

### `network.json`

This is the model subset actually used for the toy network.

- `metadata`: describes the network and simple counts.
- `nodes`: lists the three model nodes.
- `edges`: lists the two signed causal edges in the model.

Node fields:

- `id`: node name used by edges and perturbations.
- `ty`: node type.
- `fn`: readable full name.
- `src`: whether the node is a source node with no incoming edges.

Edge fields are the same compact fields used in `curated_edges.json`.

### `perturbation_dataset.json`

This is the raw toy perturbation test.

- `id`: test ID.
- `g`: gene or treatment from the literature record.
- `pt`: perturbation type. Here `ko` means knockout.
- `ed`: expected direction. Here `up` means increased.
- `sp`: species label.
- `d`: DOI/provenance string.

### `reconciled_perturbation_dataset.json`

This maps the raw perturbation test onto the toy network.

- `metadata.phenotype_node`: says which node is the measured phenotype.
- `direction_threshold`: threshold a validator would use for calling direction.
- `perturbations`: testable perturbations that map to network nodes.

Reconciled perturbation fields:

- `id`: test ID, matching the raw perturbation.
- `g`: original gene name.
- `pt`: perturbation type.
- `ed`: expected direction.
- `ng`: network gene or genes affected by the test.
- `m`: gene modifier values. `0.0` means knockout.
- `exo`: exogenous supply values. Empty here because there is no treatment.
- `cb`: comparison baseline. `WT` means compare to wild type.
- `rt`: reconciliation type. `em` means exact match.

## What To Notice

The same causal edge shape appears in both `curated_edges.json` and
`network.json`. The difference is conceptual: `curated_edges.json` is the pool
of possible literature-backed edges, while `network.json` is the selected model.

The raw perturbation says what was tested. The reconciled perturbation says how
that test maps onto the model.
