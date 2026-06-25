# Derived Network Previews

This folder contains terminal-generated previews derived from candidate network CSV tables.

These files are not source data.

The editable source tables remain `candidate_nodes.csv` and `candidate_edges.csv` in the model folder.

## Retained Files

- `network_preview.svg`: vector working preview.
- `network_preview.png`: quick-review image.
- `README.md`: notes for this view.

The intermediate Graphviz DOT and Mermaid files are reproducible from the source CSV tables and `tools/render_network.py`, but they are not retained here.

## Interpretation

These previews are for inspection, teaching, and discussion.

They do not make the biology curated.

They do not replace SBGN visual validation in Newt.

They should be regenerated whenever the source node or edge tables change.
