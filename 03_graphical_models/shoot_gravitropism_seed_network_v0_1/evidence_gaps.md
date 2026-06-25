# Evidence Gaps For v0.1

This is a hypothesis-level seed network, not curated biology.

## Main Evidence Gaps

1. Clarify the species scope.

The model currently uses general plant shoot gravitropism language. It does not yet distinguish evidence from Arabidopsis, crop systems, woody plants, or other lineages.

2. Support the combined sensing node.

`Endodermal_Statocyte_Gravity_Sensing` is a modelling simplification. Literature is needed to justify when endodermal statocytes are the appropriate sensing context for the shoots and taxa being studied.

3. Define amyloplast displacement carefully.

The model treats `Amyloplast_Displacement` as a sensing process downstream of gravistimulation. Literature is needed to define whether displacement, sedimentation, position change, or another term best matches the intended biological mechanism.

4. Check LAZY/LZY placement.

The edge from `Amyloplast_Displacement` to `LAZY_LZY_Module` is a hypothesis. It needs specific references before being treated as curated.

5. Check the auxin transport and growth response chain.

The path from LAZY/LZY signalling to PIN-mediated auxin redistribution, auxin asymmetry, differential expansion, curvature, and bending trajectory needs specific references and may differ by tissue, taxon, age, and timescale.

6. Separate genotype modulation from direct mechanism.

`Family_Genotype_Effects` is currently represented as a modulator. It should not be interpreted as a single causal molecule or direct biological mechanism.

7. Treat gravitropic versus agravitropic families as an observation.

`Gravitropic_vs_Agravitropic_Families` is downstream of bending behaviour in v0.1. It is an observed classification, not an upstream cause.

## Before Curation

Before any edge is marked curated:

- add at least one specific reference;
- record the species or taxonomic scope;
- record the tissue and developmental stage;
- record the measured phenotype and timescale;
- decide whether the relation is causal, modulatory, contextual, or classificatory.
