# PSoup Representation Notes

This folder contains a PSoup-oriented representation of the shoot gravitropism seed network:

- `shoot_gravitropism_seed_network_v0_psoup_af.sbgn`

This is a hypothesis-level seed network, not curated biology.

## What PSoup Seems To Need

From inspecting the PSoup repository, PSoup is designed to convert SBGN Activity Flow diagrams into mathematical model descriptions.

In practical terms, PSoup expects a network representation with:

- an SBGN map whose language is `activity flow`;
- compartments, such as stimulus, sensing, signalling, response, phenotype, or evolutionary layer;
- biological activity nodes inside those compartments;
- directed arcs between nodes;
- signed arc types such as `positive influence` or `negative influence`.

## What Was Created Here

The file `shoot_gravitropism_seed_network_v0_psoup_af.sbgn` translates the existing CSV scaffold into a simple SBGN Activity Flow style XML file.

Each row in `candidate_nodes.csv` became a `biological activity` glyph.

Each row in `candidate_edges.csv` became a directed arc.

At present, all candidate edges in the seed network have `sign = 1`, so all arcs were written as `positive influence`.

If later versions include `sign = -1`, those edges should be represented as `negative influence`.

## Important Cautions

This file has not been validated by PSoup.

PSoup was cloned locally for inspection, but the package was not installed and no R code was run.

This representation should therefore be treated as a starting point for discussion and testing, not as a confirmed PSoup-ready model.

No edge in this network should be treated as curated unless a specific reference is added.

Signed edges are causal summaries for modelling. They are not proof of a direct molecular mechanism.

## Suggested Next Checks

Before using this representation scientifically, the next checks should be:

1. Open the SBGN file in a compatible SBGN editor, such as Newt, if available.
2. Confirm that the diagram is recognized as an Activity Flow map.
3. Run PSoup conversion only after creating a local test environment and installing its R dependencies with explicit approval.
4. Compare every edge against primary literature before marking it as curated.
