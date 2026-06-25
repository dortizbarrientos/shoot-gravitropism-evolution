# Working Preview Network Views

These folders contain terminal-generated working previews derived from the v0.1 truth CSV tables:

- `../../candidate_nodes.csv`
- `../../candidate_edges.csv`

These previews are not source data.

They are not publication-quality figures.

They are for checking graph logic, edge direction, signs, modules, and relation types.

## Views

### 01_causal_spine_view

Generated with:

```text
include_in_first_sbgn = yes
```

This view shows the simplified causal chain from gravistimulation to shoot bending over time.

### 02_genotype_modulation_view

Generated with:

```text
include_in_first_sbgn = yes or maybe
```

This view shows the causal spine plus genotype modulation edges.

### 03_full_network_supplementary_view

Generated with:

```text
include_in_first_sbgn = yes, maybe, or no
```

This view shows all current v0.1 candidate edges, including causal, modulation, context, and classification relationships.

It is a working full-network preview and should be treated as supplementary-style material only.

## Visual Grammar

- Solid black arrows: positive causal edges.
- Red blunt-ended edges: negative causal edges, if present.
- Dashed blue arrows: modulation edges.
- Dotted grey arrows: context edges.
- Dashed grey arrows: classification edges.

## Scientific Status

All current v0.1 network views are hypothesis-level.

No edge is curated unless a specific reference is added to support it.

A visually polished network should not be treated as stronger evidence than the underlying references.
