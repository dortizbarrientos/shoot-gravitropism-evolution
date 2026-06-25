# Edge Evidence Notes

This table is a cautious first pass.

It does not mark any edge as curated.

## Evidence Streams

- `senecio_specific`: direct evidence from `Senecio lautus`.
- `arabidopsis_mechanistic_prior`: Arabidopsis evidence used only as a mechanistic prior.
- `none`: no supporting reference entered yet.

## Current Interpretation

No direct `Senecio lautus` evidence has been entered in this pass.

The strongest support is for the Arabidopsis mechanistic causal spine:

```text
Gravistimulation
  -> Amyloplast_Displacement
  -> LAZY_LZY_Module
  -> PIN_Auxin_Redistribution
  -> Auxin_Asymmetry
  -> Differential_Cell_Expansion
  -> Curvature
```

These are treated as Arabidopsis transfer-prior edges, not direct Senecio evidence.

The family/genotype and gravitropic-versus-agravitropic classification edges remain hypothesis-only.

## Review Needed

Before upgrading any edge further:

1. Confirm each DOI against the paper record.
2. Decide whether the paper directly supports the v0.1 edge or only a mechanistic refinement.
3. Search specifically for `Senecio lautus` dark rotation / 8-hour shoot bending evidence.
4. Keep Arabidopsis evidence separate from Senecio evidence.
