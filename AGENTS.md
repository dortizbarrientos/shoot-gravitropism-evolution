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
