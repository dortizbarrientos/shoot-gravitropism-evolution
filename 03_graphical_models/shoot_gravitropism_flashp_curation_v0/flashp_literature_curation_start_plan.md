# FlashP Literature Curation Start Plan

This document explains how to start a cautious FlashP-style literature curation run for shoot gravitropism.

No FlashP pipeline has been run.

No packages have been installed.

No v0.1 hypothesis network files have been overwritten.

## Goal

Create a separate FlashP-style curation workspace for:

- trait: shoot gravitropic bending over time;
- species/context: `Senecio lautus` if evidence exists;
- fallback mechanistic prior: `Arabidopsis thaliana`, with clear transfer caveats;
- experimental context: dark rotation / gravitropic response over 8 hours;
- comparison context: gravitropic versus agravitropic families.

The planned workspace is:

```text
03_graphical_models/shoot_gravitropism_flashp_curation_v0/
```

This workspace should stay separate from:

```text
03_graphical_models/shoot_gravitropism_seed_network_v0_1/
```

## Relevant FlashP Instruction Files

Use the local FlashP clone at:

```text
/Users/uqdortiz/repos/FlashP
```

The most relevant Plant Codex files are:

```text
/Users/uqdortiz/repos/FlashP/Flash-P_Plant/Codex/AGENTS.md
/Users/uqdortiz/repos/FlashP/Flash-P_Plant/Codex/Agent/LITERATURE_REVIEW_AGENT.md
/Users/uqdortiz/repos/FlashP/Flash-P_Plant/Codex/Agent/LITERATURE_REVIEW_JUDGE_AGENT.md
/Users/uqdortiz/repos/FlashP/Flash-P_Plant/Codex/Agent/shared/LEXICON.md
/Users/uqdortiz/repos/FlashP/Flash-P_Plant/Codex/Agent/shared/schemas/literature.py
```

Useful later, but not for the first cautious curation step:

```text
/Users/uqdortiz/repos/FlashP/Flash-P_Plant/Codex/Agent/BUILDER_AGENT.md
/Users/uqdortiz/repos/FlashP/Flash-P_Plant/Codex/Agent/PERTURBATION_AGENT.md
/Users/uqdortiz/repos/FlashP/Flash-P_Plant/Codex/Agent/VALIDATOR_AGENT.md
```

## Recommended Folder Structure

When the curation workspace is implemented, use:

```text
03_graphical_models/shoot_gravitropism_flashp_curation_v0/
  README.md
  prompts/
    literature_review_prompt.md
  data/
    senecio_specific/
      curated_edges.json
      perturbation_dataset.json
    arabidopsis_mechanistic_prior/
      curated_edges.json
      perturbation_dataset.json
  mapping/
    flashp_to_v0_1_candidate_edges.md
    flashp_to_v0_1_candidate_edges.csv
  notes/
    evidence_scope_notes.md
    transfer_caveats.md
```

This structure keeps direct `Senecio lautus` evidence separate from Arabidopsis mechanistic prior evidence.

## Prompt For The Literature Review Stage

Use the Plant Codex Literature Review Agent in FlashP Light mode.

Suggested prompt:

```text
Read:
/Users/uqdortiz/repos/FlashP/Flash-P_Plant/Codex/AGENTS.md
/Users/uqdortiz/repos/FlashP/Flash-P_Plant/Codex/Agent/LITERATURE_REVIEW_AGENT.md
/Users/uqdortiz/repos/FlashP/Flash-P_Plant/Codex/Agent/shared/LEXICON.md

Run only Step 1 Literature Review in FLASH-P Light style.

Do not run Builder, Judge, Perturbation reconciliation, Validator, Refinement, or Export.
Do not build network.json.
Do not infer curated biology without a DOI.
Do not merge species evidence streams.

Trait:
shoot gravitropic bending over time

Phenotype node:
Shoot_Gravitropic_Bending_Over_Time

Experimental context:
dark rotation / gravitropic response over 8 hours;
compare gravitropic and agravitropic families.

Species priority:
1. Search first for Senecio lautus evidence.
2. If Senecio lautus evidence is absent or sparse, search Arabidopsis thaliana as mechanistic prior.
3. Keep Senecio-specific evidence and Arabidopsis-prior evidence in separate outputs.
4. Clearly flag Arabidopsis evidence as transfer-prior evidence, not direct Senecio evidence.

Extract:
- regulatory or causal edges relevant to shoot gravitropic bending;
- perturbation tests relevant to gravity sensing, amyloplast displacement, LAZY/LZY signalling, PIN-mediated auxin redistribution, auxin asymmetry, differential growth, curvature, and bending over time;
- family/genotype or gravitropic-versus-agravitropic comparisons only when directly supported.

Use FLASH-P Light JSON:
curated_edges.json:
{metadata, nodes:{NAME:TYPE}, edges:[{eid,s,t,x,d}]}

perturbation_dataset.json:
{metadata, perturbations:[{id,g,pt,ed,sp,d}]}

Use DOI-only provenance in field d.
Do not include titles, authors, evidence sentences, or candidate_papers.json.
Use WebSearch verification only unless explicitly told otherwise.
```

## Expected Outputs

For each evidence stream, expect:

```text
curated_edges.json
perturbation_dataset.json
```

FlashP Light `curated_edges.json` shape:

```json
{
  "metadata": {
    "flash_p_version": "light-1.0",
    "phenotype": "shoot gravitropic bending over time",
    "species": "Senecio lautus",
    "created": "YYYY-MM-DD",
    "total_edges": 0
  },
  "nodes": {},
  "edges": [
    {
      "eid": "E001",
      "s": "Amyloplast_Displacement",
      "t": "LAZY_LZY_Module",
      "x": 1,
      "d": "10.xxxx/xxxxx"
    }
  ]
}
```

FlashP Light `perturbation_dataset.json` shape:

```json
{
  "metadata": {
    "flash_p_version": "light-1.0",
    "phenotype": "shoot gravitropic bending over time",
    "species": "Arabidopsis thaliana",
    "created": "YYYY-MM-DD",
    "total_perturbations": 0
  },
  "perturbations": [
    {
      "id": "T001",
      "g": "LZY1",
      "pt": "ko",
      "ed": "dn",
      "sp": "Arabidopsis thaliana",
      "d": "10.xxxx/xxxxx"
    }
  ]
}
```

## Evidence Stream Separation

Do not mix `Senecio lautus` evidence with Arabidopsis mechanistic-prior evidence at first.

Use:

```text
data/senecio_specific/
data/arabidopsis_mechanistic_prior/
```

Interpretation:

- `senecio_specific`: direct evidence for `Senecio lautus`, gravitropic or agravitropic families, dark rotation, or 8-hour bending if found.
- `arabidopsis_mechanistic_prior`: mechanistic prior only. This can suggest candidate mechanisms but is not direct evidence for `Senecio`.

If a combined model is built later, it should include an explicit merge note saying which edges are `Senecio`-supported and which are transferred Arabidopsis priors.

## Mapping FlashP Outputs Back To v0.1

The v0.1 source table is:

```text
03_graphical_models/shoot_gravitropism_seed_network_v0_1/candidate_edges.csv
```

Map FlashP edges by:

```text
source + target + sign
```

Suggested mapping categories:

```text
exact_match
same_concept_different_name
mechanistic_refinement
new_candidate_edge
species_prior_only
conflict_or_unclear
```

Example:

```text
v0.1 edge:
Amyloplast_Displacement -> LAZY_LZY_Module

Possible FlashP edge:
Amyloplast_Sedimentation -> LZY1

mapping:
mechanistic_refinement

scope:
Arabidopsis prior unless a Senecio DOI exists
```

Do not automatically rewrite `candidate_edges.csv`.

First produce a mapping table and review it.

## What Not To Do Yet

Do not:

- run the full FlashP pipeline;
- run Builder;
- create `network.json`;
- reconcile perturbations;
- run validation;
- run refinement;
- merge `Senecio` and Arabidopsis evidence;
- overwrite `shoot_gravitropism_seed_network_v0_1`;
- treat Arabidopsis edges as `Senecio` biology;
- treat DOI-backed Arabidopsis evidence as proof of the same mechanism in `Senecio`;
- create SBGN or publication figures from this curation until the evidence tables are reviewed.

## Plain-English Summary

The first cautious FlashP step is not model building.

It is a separated literature curation step that produces DOI-backed edge and perturbation repositories.

Direct `Senecio lautus` evidence should be searched first and kept separate.

Arabidopsis evidence can be used as a mechanistic prior only, with explicit transfer caveats.
