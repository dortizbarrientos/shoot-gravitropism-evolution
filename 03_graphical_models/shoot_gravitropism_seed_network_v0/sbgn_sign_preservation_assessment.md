# SBGN Sign Preservation Assessment

This note assesses whether the v0 SBGN Activity Flow representation preserves the edge signs from the v0 candidate edge table.

This is a hypothesis-level seed network, not curated biology.

## Files Assessed

- `candidate_edges.csv`
- `shoot_gravitropism_seed_network_v0_psoup_af.sbgn`
- `psoup_representation_notes.md`

PSoup was not run.

No R packages were installed.

## Assessment

### 1. Does the SBGN file preserve all edge signs from `candidate_edges.csv`?

Yes, for the current v0 files.

Every edge in `candidate_edges.csv` has `sign = 1`.

Every arc in `shoot_gravitropism_seed_network_v0_psoup_af.sbgn` is encoded as:

```xml
class="positive influence"
```

So the current SBGN file preserves the signs in the current v0 candidate edge table.

### 2. Are any edges encoded as positive influence when `sign = -1` or `sign = NA`?

No.

There are no edges with `sign = -1` or `sign = NA` in the current v0 `candidate_edges.csv`.

Therefore, there is no current sign conflict between the CSV and the SBGN file.

### 3. Does SBGN Activity Flow support negative influence and modulation arcs in the format PSoup expects?

Negative influence appears to be supported.

From inspecting PSoup's local parser code, PSoup maps SBGN Activity Flow:

- `positive influence` to stimulation
- `negative influence` to inhibition
- `necessary stimulation` to necessary stimulation
- `unknown influence` to unknown

Generic `modulation` should be treated cautiously for Activity Flow in PSoup.

In the inspected PSoup mapping, generic `modulation` appears under Entity Relationship rather than Activity Flow. For PSoup-compatible SBGN Activity Flow files, it is safer to use explicit Activity Flow arc classes such as `positive influence`, `negative influence`, or `unknown influence`.

### 4. Does this SBGN file encode the old v0 network rather than the revised v0.1 logic?

Yes.

The current SBGN file encodes the v0 scaffold. It is an all-positive hypothesis-level network derived from the current `candidate_edges.csv`.

It does not encode any revised v0.1 logic, such as newly added inhibitory edges, uncertain signs, changed causal direction, or revised treatment of genotype and evolutionary effects.

### 5. Should this file be kept or recreated?

Keep this file as a learning artifact.

Do not treat it as the working scientific model once v0.1 exists.

Recommended interpretation:

```text
shoot_gravitropism_seed_network_v0_psoup_af.sbgn
= learning / v0 / unvalidated / all-positive scaffold
```

After the v0.1 node and edge tables are built, create a new SBGN Activity Flow file from those revised tables.

## Plain-English Conclusion

The current v0 SBGN file accurately represents the current v0 edge signs because all edges are positive.

It is useful as a teaching example showing how a candidate edge table can be translated into SBGN Activity Flow format.

It should not be used as the authoritative model for later shoot gravitropism hypotheses unless the underlying candidate node and edge tables are revised and the SBGN file is regenerated.
