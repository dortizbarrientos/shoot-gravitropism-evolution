# Evidence Gaps For Seed Network v0

This file lists evidence needed before the seed network can become curated
biology.

Current status: hypothesis-level seed network, not curated biology.

## Global Gaps

- Define the first focal species or clade.
- Define the developmental stage being modelled.
- Define the phenotype readout: angle, curvature, bending rate, recovery time,
  or another measurable trait.
- Decide whether the first model represents one time point or a trajectory.
- Separate direct molecular mechanisms from broader causal summaries.

## Edge-Level Evidence Needed

Every edge in `candidate_edges.csv` currently needs a specific reference.

For each edge, collect:

- DOI or other stable citation.
- Species and developmental stage.
- Experimental system.
- Whether evidence is direct, indirect, genetic, physiological, imaging-based,
  or comparative.
- Whether the sign is supported clearly or only inferred.

## Priority Evidence Questions

1. Which shoot tissues are the best-supported gravity-sensing tissues for the
   first focal species?
2. What evidence links amyloplast sedimentation to LAZY/LZY signalling in
   shoots?
3. What evidence links LAZY/LZY activity to PIN polarity or auxin
   redistribution?
4. How does auxin asymmetry affect cell expansion in shoots, and does this
   differ by tissue or developmental stage?
5. Which genes or families are associated with natural variation in shoot
   gravitropic bending?
6. Are there documented agravitropic or weakly gravitropic families, genotypes,
   or lineages relevant to the planned evolutionary comparison?

## Curation Rule

Do not move an edge from `hypothesis` to `curated` until it has a specific
reference and a short note explaining what that reference actually supports.
