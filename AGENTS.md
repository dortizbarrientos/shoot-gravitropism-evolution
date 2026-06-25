# Project Instructions

## Project Purpose

This repository is for studying the evolution and development of shoot
gravitropism. The long-term aim is to organize literature, hypotheses,
graphical models, mathematical ideas, developmental models, and evolutionary
comparisons into a clear scientific project.

## Working Style

- Inspect files before editing them.
- Explain commands before running them when they could change files, require
  network access, install dependencies, or affect Git history.
- Prefer small, reviewable changes.
- Keep notes close to the modelling step they describe.
- Use existing project folders before creating new ones.

## Subagent Use

- Use one main Codex agent by default.
- Do not spawn subagents unless I explicitly ask for them.
- Use subagents only for bounded, independent tasks such as literature
  searches, codebase inspection, tool comparison, or checking separate evidence
  streams.
- Do not use multiple agents to edit the same files in parallel.
- When subagents are used, assign each one a clear scope and ask for a concise
  written summary.
- The main agent must integrate subagent findings and decide what, if anything,
  should be edited.
- For this project, prefer single-agent work when editing network CSVs,
  AGENTS.md, README files, or model source files.

## Scientific Caution

- Keep toy examples separate from curated biological claims.
- Clearly label teaching examples, placeholders, guesses, and unverified ideas.
- Do not present a claim as curated biology unless it is backed by a specific
  reference or an explicit user-provided source.
- Treat signed edges as curated causal summaries, not as proof of a direct
  molecular mechanism.
- Preserve uncertainty. If a mechanism, direction, species scope, or timescale
  is unclear, say so plainly.

## Network Representation Rules

- Treat candidate_nodes.csv and candidate_edges.csv as the editable source
  tables for hypothesis networks.
- Treat SBGN files as derived graphical/model representations, not as the
  primary source of truth.
- Do not create or update SBGN files until the corresponding node and edge
  tables have been reviewed.
- For SBGN Activity Flow exports, include only edges explicitly marked for
  inclusion, such as include_in_first_sbgn = yes.
- Keep modulation, context, and classification edges separate from simple
  signed causal edges.
- Do not run PSoup or other model-conversion tools unless explicitly asked.
- Always label whether a network is hypothesis-level, review-supported,
  primary-paper-supported, or curated.
- Do not treat a diagram standard such as SBGN as evidence that the biology is
  correct.

## Visualisation Workflow

- candidate_nodes.csv and candidate_edges.csv remain the source of truth for
  network structure.
- Graphviz and Mermaid outputs are derived previews for inspection, teaching,
  and documentation.
- SBGN files are derived standards-oriented representations, not the editable
  source of truth.
- Newt may be used occasionally for SBGN visual validation, but it is not
  required for daily work.
- Prefer terminal-first visualisation from CSV tables before using GUI tools.
- Do not install visualisation dependencies unless explicitly asked.
- Do not run PSoup, SBGNview, Cytoscape, or other model-conversion tools unless
  explicitly asked.
- Place generated visual outputs in an exports/ folder near the relevant model
  version.
- Clearly label generated previews as derived artifacts.
- When exporting SVG figures for review in ChatGPT or other preview tools, also
  create a PNG copy for visual inspection.
- For future network previews, always export both .svg and .png. 
  Treat SVG as the editable/vector source and PNG as the quick-review file.

## Publication Figure Rules

- Distinguish three figure stages:
  1. working previews;
  2. draft figure elements;
  3. publication-quality figures.
- Terminal-generated Graphviz, Mermaid, or SVG outputs are working previews
  unless explicitly labelled otherwise.
- Working previews are for checking graph logic, signs, edge direction,
  modules, and evidence status.
- Draft figure elements may be used as starting material for a manuscript
  figure, but they are not automatically publication quality.
- Publication-quality network figures require an explicit figure-design step.
- Network figures must be readable on A4 or letter-sized pages.
- Do not force a large network into one panel if labels, arrows, or signs
  become hard to read.
- Prefer modular views over crowded whole-network views.
- Before producing a publication-quality network figure, ask or infer:
  - target journal or format;
  - page size and column width;
  - whether the figure is single-column, double-column, or full-page;
  - final output format required, such as PDF, SVG, EPS, TIFF, or PNG;
  - required resolution if raster output is needed;
  - colour constraints, including colour-blind-safe palettes and greyscale
    legibility;
  - whether labels must remain inside nodes or move to a legend/table.
- For large networks, create several figure types:
  1. causal spine view;
  2. layer/module view;
  3. evidence-status view;
  4. genotype/modulation view;
  5. full network as supplementary material only.
- For publication-quality figures, produce or propose:
  - a simplified main-panel network;
  - optional supplementary full-network view;
  - concise node labels;
  - a clear visual legend;
  - consistent line weights and font sizes;
  - evidence-status encoding only if it does not clutter the causal message.
- Keep node labels short in figures; put long definitions in tables or
  captions.
- Use consistent visual grammar:
  - solid black arrows for positive causal edges;
  - red blunt-ended or clearly marked edges for negative causal edges;
  - dashed blue arrows for modulation;
  - dotted grey edges for context;
  - dashed grey edges for classification or analysis labels.
- Keep related nodes aligned by layer when possible: stimulus, sensing,
  signalling, response, phenotype, evolutionary layer.
- Prefer left-to-right layouts for causal chains and top-to-bottom layouts for
  layered summaries.
- Avoid crossing edges where possible.
- Use exports/ for generated figure files and include a README explaining how
  each figure was generated.
- Always state whether a figure is hypothesis-level, review-supported,
  primary-paper-supported, or curated.
- If terminal tools cannot make a publication-quality figure, say so plainly
  and propose the correct finishing path, such as manual refinement in
  Illustrator, Inkscape, Affinity Designer, Cytoscape, or a scripted
  matplotlib/SVG workflow.
- Never imply that a generated preview is manuscript-ready unless it has passed
  a publication-figure review.
- Do not treat a visually polished network as stronger evidence than the
  underlying references.

## Reproducible Figure Code

- Prefer Python-generated figures for reproducible manuscript figure elements.
- Keep figure code in Git beside the model version it renders.
- Keep the input CSV tables, optional layout CSV files, plotting scripts, and
  generated outputs together or clearly linked.
- Use candidate_nodes.csv and candidate_edges.csv as the source of truth for
  network content.
- Use NetworkX for graph checks, path checks, filtering, and structural
  diagnostics.
- Do not rely on NetworkX default drawing for final manuscript figures.
- Use Graphviz for quick automatic layout previews when useful.
- For publication-quality network figures, prefer scripted matplotlib/SVG/PDF
  output with fixed node coordinates and explicit styling.
- Export both vector output, such as SVG or PDF, and a PNG preview for quick
  inspection.
- Treat generated figures as derived artifacts; if the CSV changes, regenerate
  the figure.
- Do not install Python plotting dependencies unless explicitly asked.

## Generated File Hygiene

- Do not keep every exploratory render.
- Keep source files, scripts, reviewed outputs, and README notes.
- Treat raw preview outputs as disposable unless they are explicitly selected
  for retention.
- Prefer a small number of named outputs over many auto-numbered variants.
- Use exports/working_previews/ for temporary visual checks.
- Use exports/publication_drafts/ for selected figure elements worth refining.
- Do not delete files without showing a cleanup plan first.
- Before cleanup, list files proposed for deletion and explain why each is safe
  to remove.
- Never delete source CSVs, scripts, README files, evidence notes, SBGN files,
  or committed results unless explicitly asked.
- If a generated file can be reproduced from source tables and scripts, it may
  be removed after the retained output is chosen.
- Keep .gitignore updated so caches, logs, and bulky temporary exports do not
  accumulate.

## Reproducibility

- Document commands that were run and what they were intended to check.
- Record assumptions behind modelling choices.
- Note input files, output files, and any manual changes.
- Prefer plain text notes and small structured files that can be reviewed in
  Git.

## Safety

Do not do any of the following unless explicitly asked:

- Run full pipelines.
- Install packages.
- Delete files.
- Rewrite Git history.
- Commit changes.
- Push to GitHub.
- Treat toy files as real scientific evidence.

Before destructive or broad actions, stop and ask.

## Writing

- Use clear plain English.
- Minimize jargon.
- Define technical terms when they first appear.
- Prefer short explanations that a new PhD student can follow.
- Separate observations, interpretations, and next steps.
