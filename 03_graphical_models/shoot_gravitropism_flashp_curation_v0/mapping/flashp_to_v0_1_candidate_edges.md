# FlashP To v0.1 Candidate Edge Mapping

This file maps the first FlashP-style curation pass back to the v0.1 hypothesis network.

Do not automatically rewrite:

```text
../shoot_gravitropism_seed_network_v0_1/candidate_edges.csv
```

Review the evidence table first.

## Mapping Summary

### Edges with Arabidopsis primary-paper prior support

- H001: `Gravistimulation -> Amyloplast_Displacement`
- H002: `Endodermal_Statocyte_Gravity_Sensing -> Amyloplast_Displacement`
- H003: `Amyloplast_Displacement -> LAZY_LZY_Module`
- H004: `LAZY_LZY_Module -> PIN_Auxin_Redistribution`
- H005: `PIN_Auxin_Redistribution -> Auxin_Asymmetry`
- H006: `Auxin_Asymmetry -> Differential_Cell_Expansion`
- H007: `Differential_Cell_Expansion -> Curvature`

These are not Senecio-supported yet.

They are Arabidopsis mechanistic-prior support.

### Edges still hypothesis-only

- H008: `Curvature -> Shoot_Gravitropic_Bending_Over_Time`
- H009: `Family_Genotype_Effects -> LAZY_LZY_Module`
- H010: `Family_Genotype_Effects -> PIN_Auxin_Redistribution`
- H011: `Family_Genotype_Effects -> Differential_Cell_Expansion`
- H012: `Family_Genotype_Effects -> Shoot_Gravitropic_Bending_Over_Time`
- H013: `Shoot_Gravitropic_Bending_Over_Time -> Gravitropic_vs_Agravitropic_Families`

These need direct phenotype, genotype, or family-comparison evidence.

For H012 and H013, the preferred evidence would be direct `Senecio lautus` dark-rotation / 8-hour bending data.

## Important Caveat

The FlashP Light `curated_edges.json` format only stores signed causal edges with `x = 1` or `x = -1`.

It does not naturally store:

- context edges;
- modulation edges;
- classification edges;
- `sign = NA` relations.

Therefore, some v0.1 rows appear in the evidence table but not in `curated_edges.json`.

## Next Review Step

Before changing v0.1:

1. Review `evidence/edge_evidence_table.csv`.
2. Confirm the seed references against paper records.
3. Search for direct `Senecio lautus` evidence.
4. Decide whether any v0.1 rows should move from `hypothesis` to `primary-paper-supported`.
5. If changing v0.1, edit `candidate_edges.csv` only after review.
