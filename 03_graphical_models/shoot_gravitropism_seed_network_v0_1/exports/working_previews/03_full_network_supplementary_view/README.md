# Derived Network Previews

This folder contains terminal-generated previews derived from candidate network CSV tables.

These files are not source data.

The editable source tables remain `candidate_nodes.csv` and `candidate_edges.csv` in the model folder.

## Generated Files

- `network_preview.dot`: Graphviz DOT representation.
- `network_preview.mmd`: Mermaid flowchart representation.
- `network_preview.svg`: Graphviz-rendered SVG preview.
- `network_preview.png`: Graphviz-rendered PNG quick-review preview.

## Interpretation

These previews are for inspection, teaching, and discussion.

They do not make the biology curated.

They do not replace SBGN visual validation in Newt.

They should be regenerated whenever the source node or edge tables change.
