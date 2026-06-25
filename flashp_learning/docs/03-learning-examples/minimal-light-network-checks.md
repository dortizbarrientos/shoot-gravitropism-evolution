# Minimal Light Network: Learning Checks

This note documents the learning-only `minimal_light_network` example and the
safe checks selected for it. The full FLASH-P pipeline was not run.

## Example Location

`shoot_gravitropism/flashp_learning/learning_examples/minimal_light_network/`

Files created for teaching:

- `curated_edges.json`
- `network.json`
- `perturbation_dataset.json`
- `reconciled_perturbation_dataset.json`
- `README.md`

The example is intentionally tiny:

```text
MAX2 --(+)-> BRC1 --(-)-> Shoot_Branching
```

It is biologically plausible as a teaching motif, but it is not a real curated
network. The placeholder DOI marks records as instructional examples rather
than scientific provenance.

## Why Schema Checks Are Appropriate

The repository provides `Flash-P_Plant/Codex/Agent/shared/validate_schema.py`.
That script can validate individual JSON files by filename. This is suitable
for the toy example because each file uses a schema-recognized name.

The repository also provides `check_network_structure.py`, but that script
expects a pipeline-style directory layout containing `network/network.json`.
The teaching example is intentionally flat, so the structure checker is not the
right first check without changing the example layout.

## What The Safe Checks Mean

Checking `curated_edges.json` confirms that the toy edge pool follows the
Light-format `CuratedEdgesFile` schema.

Checking `network.json` confirms that the toy network follows the Light-format
`NetworkFile` schema.

Checking `perturbation_dataset.json` confirms that the raw toy perturbation
test follows the Light-format `PerturbationDatasetFile` schema.

Checking `reconciled_perturbation_dataset.json` confirms that the mapped
perturbation test follows the Light-format `ReconciledPerturbationFile` schema.

Schema success means the JSON shape is compatible with the relevant Pydantic
model. It does not mean the biology is real, complete, or scientifically
curated.

Schema failure means the teaching file does not match the expected field names,
types, or enum values and should be corrected before students use it as a
format example.

## Check Attempted In This Session

Command attempted:

```bash
python Flash-P_Plant/Codex/Agent/shared/validate_schema.py shoot_gravitropism/flashp_learning/learning_examples/minimal_light_network/curated_edges.json
```

What it was meant to check:

- Only `shoot_gravitropism/flashp_learning/learning_examples/minimal_light_network/curated_edges.json`.
- Specifically, whether that file matches the `CuratedEdgesFile` Pydantic
  schema.

Why it was safe:

- It was a single-file schema check.
- It does not run the FLASH-P pipeline.
- It does not write output files.

Result:

- The check could not start because the local Python environment does not have
  `pydantic` installed.
- The error was `ModuleNotFoundError: No module named 'pydantic'`.

Interpretation:

- This is an environment/dependency issue, not a schema verdict on the toy
  example.
- No conclusion should be drawn about whether `curated_edges.json` passes or
  fails until `pydantic` is available and the validator can actually run.

Why no further repository validators were run:

- `check_network_structure.py` expects a full pipeline-style layout with
  `network/network.json`, while this learning example is intentionally flat.
- Running more validation commands without the required dependency would add
  noise rather than useful learning signal.

## Documentation Organization

The `flashp_learning/docs/` folder is organized as a learning path:

- `00-overview/`: first-pass repository orientation.
- `01-pipeline/`: stage-by-stage pipeline notes.
- `02-data-structures/`: schemas and object shapes.
- `03-learning-examples/`: toy examples and safe-check notes.
