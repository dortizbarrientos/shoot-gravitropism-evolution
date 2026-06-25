# Literature Review Prompt

Use this prompt to run a cautious FlashP Light literature review for shoot gravitropism.

```text
Read:
/Users/uqdortiz/repos/FlashP/Flash-P_Plant/Codex/AGENTS.md
/Users/uqdortiz/repos/FlashP/Flash-P_Plant/Codex/Agent/LITERATURE_REVIEW_AGENT.md
/Users/uqdortiz/repos/FlashP/Flash-P_Plant/Codex/Agent/shared/LEXICON.md
/Users/uqdortiz/repos/FlashP/Flash-P_Plant/Codex/Agent/shared/schemas/literature.py

Run only Step 1 Literature Review in FlashP Light style.

Do not run Builder, Judge, Perturbation reconciliation, Validator, Refinement, or Export.
Do not run the full FlashP pipeline.
Do not build network.json.
Do not overwrite:
03_graphical_models/shoot_gravitropism_seed_network_v0_1/

Trait:
shoot gravitropic bending over time

Phenotype node:
Shoot_Gravitropic_Bending_Over_Time

Experimental context:
dark rotation / gravitropic response over 8 hours;
gravitropic vs agravitropic families.

Species priority:
1. Search first for direct Senecio lautus evidence.
2. If Senecio evidence is sparse or absent, use Arabidopsis thaliana as mechanistic prior.
3. Keep the two evidence streams separate.
4. Arabidopsis evidence must be labelled as transfer-prior evidence, not direct Senecio evidence.

Seed references to verify and use only when appropriate:
- Morita et al. 2002, Plant Cell, DOI 10.1105/tpc.010216
- Nakamura et al. 2011, Plant Cell, DOI 10.1105/tpc.110.079442
- Rakusova et al. 2011, Plant Journal, DOI 10.1111/j.1365-313X.2011.04636.x
- Taniguchi et al. 2017, Plant Cell, DOI 10.1105/tpc.16.00575
- Yoshihara and Spalding 2017, Plant Physiology, DOI 10.1104/pp.17.00942

For FlashP Light JSON:
- Use DOI-only provenance in field d.
- Use schema-compatible Light format.
- If no direct Senecio evidence is found, leave Senecio JSON files with empty edges/perturbations and explain that clearly in notes.
- Do not mix Senecio and Arabidopsis evidence in the same JSON file.

First produce:
- curated_edges.json
- perturbation_dataset.json
- evidence/edge_evidence_table.csv
- mapping/flashp_to_v0_1_candidate_edges.csv

Do not mark anything curated.
Mark an edge primary-paper-supported only if a paper directly supports that edge or a close mechanistic refinement.
For uncertain links, keep proposed_status = hypothesis and explain the gap.
```
