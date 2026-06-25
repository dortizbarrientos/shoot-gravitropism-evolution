#!/usr/bin/env python3
"""Render hypothesis-network CSV tables into terminal-friendly previews."""

from __future__ import annotations

import argparse
import csv
import html
import os
import re
import shutil
import subprocess
from collections import defaultdict
from pathlib import Path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Render candidate_nodes.csv and candidate_edges.csv previews."
    )
    parser.add_argument("--nodes", required=True, help="Path to candidate_nodes.csv")
    parser.add_argument("--edges", required=True, help="Path to candidate_edges.csv")
    parser.add_argument("--outdir", required=True, help="Directory for preview files")
    parser.add_argument(
        "--include-column",
        default="include_in_first_sbgn",
        help="Edge column used to decide which rows to render",
    )
    parser.add_argument(
        "--include-values",
        nargs="+",
        default=["yes"],
        help="Accepted values in --include-column, for example: yes maybe",
    )
    return parser.parse_args()


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def normalize(value: str | None) -> str:
    return (value or "").strip()


def slug(value: str) -> str:
    cleaned = re.sub(r"[^A-Za-z0-9_]", "_", value.strip())
    if not cleaned:
        return "unnamed"
    if cleaned[0].isdigit():
        return f"n_{cleaned}"
    return cleaned


def dot_quote(value: str) -> str:
    return '"' + value.replace("\\", "\\\\").replace('"', '\\"') + '"'


def node_label(node: dict[str, str]) -> str:
    return normalize(node.get("label")) or normalize(node.get("node_id"))


def edge_style(edge: dict[str, str]) -> dict[str, str]:
    relation_type = normalize(edge.get("relation_type")).lower()
    sign = normalize(edge.get("sign")).upper()

    if relation_type == "causal" and sign == "1":
        return {
            "color": "black",
            "fontcolor": "black",
            "style": "solid",
            "arrowhead": "normal",
            "label_suffix": "+",
            "mermaid_arrow": "-->",
            "mermaid_color": "#111111",
            "mermaid_style": "stroke-width:2px",
        }
    if relation_type == "causal" and sign == "-1":
        return {
            "color": "red",
            "fontcolor": "red",
            "style": "solid",
            "arrowhead": "tee",
            "label_suffix": "-",
            "mermaid_arrow": "--x",
            "mermaid_color": "#b3261e",
            "mermaid_style": "stroke-width:2px",
        }
    if relation_type == "modulation" and sign == "NA":
        return {
            "color": "#1f77b4",
            "fontcolor": "#1f77b4",
            "style": "dashed",
            "arrowhead": "normal",
            "label_suffix": "modulation",
            "mermaid_arrow": "-.->",
            "mermaid_color": "#1f77b4",
            "mermaid_style": "stroke-width:2px,stroke-dasharray:5 5",
        }
    if relation_type == "context" and sign == "NA":
        return {
            "color": "gray50",
            "fontcolor": "gray40",
            "style": "dotted",
            "arrowhead": "normal",
            "label_suffix": "context",
            "mermaid_arrow": "-.->",
            "mermaid_color": "#777777",
            "mermaid_style": "stroke-width:1.5px,stroke-dasharray:2 4",
        }
    if relation_type == "classification" and sign == "NA":
        return {
            "color": "gray45",
            "fontcolor": "gray35",
            "style": "dashed",
            "arrowhead": "normal",
            "label_suffix": "classification",
            "mermaid_arrow": "-.->",
            "mermaid_color": "#666666",
            "mermaid_style": "stroke-width:1.5px,stroke-dasharray:6 4",
        }

    return {
        "color": "gray30",
        "fontcolor": "gray30",
        "style": "solid",
        "arrowhead": "normal",
        "label_suffix": relation_type or sign or "edge",
        "mermaid_arrow": "-->",
        "mermaid_color": "#444444",
        "mermaid_style": "stroke-width:1.5px",
    }


def filter_edges(
    edges: list[dict[str, str]], include_column: str, include_values: set[str]
) -> list[dict[str, str]]:
    if include_column not in edges[0]:
        raise SystemExit(f"Missing include column in edge table: {include_column}")
    return [
        edge
        for edge in edges
        if normalize(edge.get(include_column)).lower() in include_values
    ]


def render_dot(nodes: dict[str, dict[str, str]], edges: list[dict[str, str]]) -> str:
    included_node_ids = {
        normalize(edge.get("source")) for edge in edges
    } | {normalize(edge.get("target")) for edge in edges}
    included_node_ids.discard("")

    layers: dict[str, list[str]] = defaultdict(list)
    for node_id in sorted(included_node_ids):
        layer = normalize(nodes.get(node_id, {}).get("layer")) or "unlayered"
        layers[layer].append(node_id)

    lines = [
        "digraph network_preview {",
        "  graph [rankdir=LR, bgcolor=\"white\", compound=true, fontname=\"Helvetica\", label=\"Hypothesis-level network preview derived from candidate CSV tables\", labelloc=t];",
        "  node [shape=box, style=\"rounded,filled\", fillcolor=\"white\", color=\"#455a64\", fontname=\"Helvetica\", fontsize=11];",
        "  edge [fontname=\"Helvetica\", fontsize=9];",
        "",
    ]

    for index, (layer, layer_node_ids) in enumerate(sorted(layers.items())):
        lines.extend(
            [
                f"  subgraph cluster_{index} {{",
                f"    label={dot_quote(layer)};",
                "    color=\"#d0d7de\";",
                "    style=\"rounded\";",
            ]
        )
        for node_id in layer_node_ids:
            node = nodes.get(node_id, {"node_id": node_id, "label": node_id})
            lines.append(
                f"    {dot_quote(node_id)} [label={dot_quote(node_label(node))}];"
            )
        lines.extend(["  }", ""])

    for edge in edges:
        style = edge_style(edge)
        edge_id = normalize(edge.get("edge_id"))
        label = f"{edge_id} {style['label_suffix']}".strip()
        attrs = {
            "label": label,
            "color": style["color"],
            "fontcolor": style["fontcolor"],
            "style": style["style"],
            "arrowhead": style["arrowhead"],
        }
        attr_text = ", ".join(
            f"{key}={dot_quote(value)}" for key, value in attrs.items()
        )
        lines.append(
            f"  {dot_quote(normalize(edge.get('source')))} -> "
            f"{dot_quote(normalize(edge.get('target')))} [{attr_text}];"
        )

    lines.append("}")
    return "\n".join(lines) + "\n"


def mermaid_id(node_id: str) -> str:
    return slug(node_id)


def mermaid_label(value: str) -> str:
    return html.escape(value.replace('"', "'"))


def render_mermaid(nodes: dict[str, dict[str, str]], edges: list[dict[str, str]]) -> str:
    included_node_ids = {
        normalize(edge.get("source")) for edge in edges
    } | {normalize(edge.get("target")) for edge in edges}
    included_node_ids.discard("")

    layers: dict[str, list[str]] = defaultdict(list)
    for node_id in sorted(included_node_ids):
        layer = normalize(nodes.get(node_id, {}).get("layer")) or "unlayered"
        layers[layer].append(node_id)

    lines = [
        "flowchart LR",
        "  %% Hypothesis-level preview derived from candidate CSV tables.",
    ]

    for layer, layer_node_ids in sorted(layers.items()):
        lines.append(f"  subgraph {slug(layer)}[{mermaid_label(layer)}]")
        for node_id in layer_node_ids:
            node = nodes.get(node_id, {"node_id": node_id, "label": node_id})
            lines.append(
                f"    {mermaid_id(node_id)}[\"{mermaid_label(node_label(node))}\"]"
            )
        lines.append("  end")

    link_styles = []
    for index, edge in enumerate(edges):
        style = edge_style(edge)
        source = mermaid_id(normalize(edge.get("source")))
        target = mermaid_id(normalize(edge.get("target")))
        label = f"{normalize(edge.get('edge_id'))} {style['label_suffix']}".strip()
        arrow = style["mermaid_arrow"]
        lines.append(f"  {source} {arrow}|{mermaid_label(label)}| {target}")
        link_styles.append(
            f"  linkStyle {index} stroke:{style['mermaid_color']},{style['mermaid_style']}"
        )

    lines.extend(link_styles)
    return "\n".join(lines) + "\n"


def write_readme(outdir: Path, dot_available: bool) -> None:
    graphviz_notes = (
        "- `network_preview.svg`: Graphviz-rendered SVG preview.\n"
        "- `network_preview.png`: Graphviz-rendered PNG quick-review preview.\n"
        if dot_available
        else (
            "- `network_preview.svg`: not written because Graphviz `dot` was not found.\n"
            "- `network_preview.png`: not written because Graphviz `dot` was not found.\n"
        )
    )
    readme = f"""# Derived Network Previews

This folder contains terminal-generated previews derived from candidate network CSV tables.

These files are not source data.

The editable source tables remain `candidate_nodes.csv` and `candidate_edges.csv` in the model folder.

## Generated Files

- `network_preview.dot`: Graphviz DOT representation.
- `network_preview.mmd`: Mermaid flowchart representation.
{graphviz_notes}
## Interpretation

These previews are for inspection, teaching, and discussion.

They do not make the biology curated.

They do not replace SBGN visual validation in Newt.

They should be regenerated whenever the source node or edge tables change.
"""
    (outdir / "README.md").write_text(readme, encoding="utf-8")


def main() -> None:
    args = parse_args()
    nodes_path = Path(args.nodes)
    edges_path = Path(args.edges)
    outdir = Path(args.outdir)
    outdir.mkdir(parents=True, exist_ok=True)

    node_rows = read_csv(nodes_path)
    edge_rows = read_csv(edges_path)
    if not edge_rows:
        raise SystemExit("Edge table is empty.")

    include_values = {value.lower() for value in args.include_values}
    included_edges = filter_edges(edge_rows, args.include_column, include_values)
    nodes = {normalize(row.get("node_id")): row for row in node_rows}

    dot_path = outdir / "network_preview.dot"
    mmd_path = outdir / "network_preview.mmd"
    svg_path = outdir / "network_preview.svg"
    png_path = outdir / "network_preview.png"

    dot_path.write_text(render_dot(nodes, included_edges), encoding="utf-8")
    mmd_path.write_text(render_mermaid(nodes, included_edges), encoding="utf-8")

    dot_executable = shutil.which("dot")
    if dot_executable:
        subprocess.run(
            [dot_executable, "-Tsvg", str(dot_path), "-o", str(svg_path)],
            check=True,
        )
        subprocess.run(
            [dot_executable, "-Tpng", str(dot_path), "-o", str(png_path)],
            check=True,
        )

    write_readme(outdir, dot_available=bool(dot_executable))

    print(f"Wrote {dot_path}")
    print(f"Wrote {mmd_path}")
    if dot_executable:
        print(f"Wrote {svg_path}")
        print(f"Wrote {png_path}")
    else:
        print("Skipped network_preview.svg and network_preview.png because Graphviz dot was not found.")


if __name__ == "__main__":
    main()
