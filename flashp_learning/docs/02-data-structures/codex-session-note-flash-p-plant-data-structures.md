# Codex Session Note: Flash-P Plant Data Structures

This note summarizes a read-only inspection of data structures under
`Flash-P_Plant/Codex`. The pipeline was not run, and no source code was edited.

## Scope

Files inspected:

- `Flash-P_Plant/Codex/Agent/shared/schemas/common.py`
- `Flash-P_Plant/Codex/Agent/shared/schemas/literature.py`
- `Flash-P_Plant/Codex/Agent/shared/schemas/network.py`
- `Flash-P_Plant/Codex/Agent/shared/schemas/perturbation.py`
- `Flash-P_Plant/Codex/Agent/shared/LEXICON.md`
- `Flash-P_Plant/Codex/Agent/shared/light_io.py`
- `Flash-P_Plant/Codex/Agent/shared/rwr_validator.py`
- Relevant embedded examples in `Agent/*_AGENT.md`

No generated example files such as `network.json`, `curated_edges.json`,
`perturbation_dataset.json`, or `reconciled_perturbation_dataset.json` were
present inside `Flash-P_Plant/Codex`. The schemas are therefore the source of
truth. Some Markdown examples exist, but several are legacy verbose examples,
not the current Light format.

## Light Format

The Plant Codex pipeline uses a compact "Light" data format.

Key points:

- Record-level fields use short keys.
- `metadata` and `parameters` blocks keep readable keys.
- Schemas accept both short and readable field names.
- Enum values are short in the Light files, but long names are accepted on
  input.
- Provenance is usually a single DOI string, stored as `d`.

Common short keys:

- `eid`: edge ID
- `s`: source
- `t`: target
- `x`: sign
- `d`: DOI
- `ty`: node type
- `fn`: full name
- `src`: is source node
- `id`: test ID
- `g`: gene
- `pt`: perturbation type
- `ed`: expected direction
- `ng`: network gene
- `m`: gene modifiers
- `exo`: exogenous supply
- `cb`: comparison baseline
- `rt`: reconciliation type

## Causal Edge

Causal edges appear in two related structures:

- `curated_edges.json`: full literature edge repository.
- `network.json`: subset of edges actually used in the model.

Schema-defined fields:

```json
{
  "eid": "E001",
  "s": "MAX2",
  "t": "BRC1",
  "x": 1,
  "d": "10.xxxx/example"
}
```

Meaning:

- `eid`: unique edge identifier.
- `s`: source node.
- `t`: target node.
- `x`: edge sign, where `1` means activation and `-1` means inhibition.
- `d`: DOI supporting the causal claim.

In `curated_edges.json`, node types are stored once in a top-level `nodes` map
rather than repeated on each edge.

## Node

Network nodes are defined in `network.json`.

Schema-defined fields:

```json
{
  "id": "BRC1",
  "ty": "G",
  "fn": "BRANCHED 1",
  "src": false
}
```

Meaning:

- `id`: node identifier used by edges, equations, and perturbation mappings.
- `ty`: node type.
- `fn`: readable full name.
- `src`: whether the node is a source node.

Node type codes:

- `G`: gene
- `H`: hormone
- `M`: metabolite
- `E`: environment
- `PC`: protein complex
- `R`: regulatory RNA
- `P`: phenotype
- `PR`: process

## Perturbation Test

There are two perturbation structures:

- Raw tests in `perturbation_dataset.json`.
- Reconciled, model-testable tests in `reconciled_perturbation_dataset.json`.

Raw perturbation example:

```json
{
  "id": "T001",
  "g": "MAX2",
  "pt": "ko",
  "ed": "up",
  "sp": "Arabidopsis thaliana",
  "d": "10.xxxx/example"
}
```

Reconciled perturbation example:

```json
{
  "id": "T001",
  "g": "MAX2",
  "pt": "ko",
  "ed": "up",
  "ng": ["MAX2"],
  "m": {"MAX2": 0.0},
  "exo": {},
  "cb": "WT",
  "rt": "em"
}
```

Meaning:

- `id`: test ID.
- `g`: original gene or treatment from the literature.
- `pt`: perturbation type.
- `ed`: expected direction.
- `ng`: network node or nodes mapped to the test.
- `m`: node-to-modifier mapping.
- `exo`: exogenous supply mapping.
- `cb`: comparison baseline.
- `rt`: reconciliation type.

Modifier meanings:

- `0.0`: knockout
- `0.5`: knockdown
- `1.0`: wild type or unchanged baseline
- `2.0`: overexpression

Expected direction codes:

- `up`: increased
- `dn`: decreased
- `nc`: unchanged

## network.json Shape

`network.json` has three main top-level parts:

```json
{
  "metadata": {
    "flash_p_version": "light-1.0",
    "phenotype": "shoot_branching",
    "species": "Arabidopsis thaliana",
    "created": "2026-06-25",
    "total_nodes": 2,
    "total_edges": 1
  },
  "nodes": [
    {"id": "MAX2", "ty": "G", "fn": "MORE AXILLARY GROWTH 2", "src": true},
    {"id": "Shoot_Branching", "ty": "P", "fn": "Shoot branching", "src": false}
  ],
  "edges": [
    {"s": "MAX2", "t": "Shoot_Branching", "x": -1, "eid": "E001", "d": "10.xxxx/example"}
  ]
}
```

Plain English:

- `metadata` describes the run and counts.
- `nodes` lists model nodes.
- `edges` lists signed causal connections between nodes.

The Builder instructions stress that `network.json` is not a general knowledge
graph. It should contain only nodes and edges participating in a directed
cascade to the phenotype.

## Signed Random-Walk-with-Restart Input

The RWR validator reads:

- `network/network.json`
- `data/reconciled_perturbation_dataset.json`
- optionally `network/algebraic_equations.json` to keep a consistent node set
  for comparison.

From `network.json`, RWR uses:

- node IDs,
- the phenotype node,
- directed edges,
- edge signs.

From reconciled perturbations, RWR uses:

- `gene_modifiers`,
- `exogenous_supply`,
- `expected_direction`,
- `comparison_baseline`,
- phenotype information.

RWR converts perturbation modifiers into initial signal values:

- knockout `0.0` -> `-1.0`
- knockdown `0.5` -> `-0.5`
- wild type `1.0` -> `0.0`
- overexpression `2.0` -> `+1.0`

Then it propagates signal through signed directed edges. Activation edges keep
the signal sign; inhibition edges invert it. The final phenotype signal is
classified as increased, decreased, or unchanged.

## Important Caveat

The schemas use the compact Light format, while some instruction Markdown still
contains older verbose examples with fields such as `effect`, `mechanism`, and
fat `evidence` arrays. For `Flash-P_Plant/Codex`, the schema files and
`LEXICON.md` are the more reliable source for current field shape.
