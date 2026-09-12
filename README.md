<p align="center">
  <img src="assets/pretraining-lab-cover.png" width="100%" alt="Pretraining Lab — cinematic 3D visualization of one GPU powering two auditable language-model pretraining runs">
</p>

<p align="center">
  <a href="models/135m.md">135M model</a> ·
  <a href="models/1b.md">1.1B model</a> ·
  <a href="catalog.json">machine-readable catalog</a>
</p>

# Pretraining Lab

An evidence-first collection of language models trained from random
initialization on a single NVIDIA L20. Each project keeps its own history,
experiments, and release boundary; this repository provides one clean place to
discover and compare them without merging incompatible metrics.

## Model collection

| Model | Parameters | Training tokens | Hardware | Public artifacts | Status |
|---|---:|---:|---|---|---|
| [L20-Edu-135M](models/135m.md) | 134.5M | ~13B total | 1× NVIDIA L20 | [Code](https://github.com/yinli-systems/l20-edu-135m-pretrain) · [Weights](https://huggingface.co/AliceYin/l20-edu-135m) | Released |
| [L20-1B-20B-Base](models/1b.md) | 1.100B | 19.9997B prediction tokens | 1× NVIDIA L20 | [Code](https://github.com/yinli-systems/l20-1b-pretraining) · [Weights](https://huggingface.co/AliceYin/L20-1B-20B-Base) | Base released; research active |

The headline scores are intentionally not placed in one ranking column. The
135M release uses a six-task suite and includes an SFT interpolation, while the
1.1B release is a base model evaluated on a seven-task suite. Their model pages
state the exact protocol and claim boundary.

## What makes a run part of this collection

Every model must make the following separations explicit:

- random initialization versus inherited weights;
- training tokens versus downloaded or prepared tokens;
- point telemetry versus run-wide measurements;
- development selection versus final evaluation;
- code tests versus live GPU execution;
- measured results versus forecasts or literature comparisons;
- successful runs versus preserved negative results.

Large checkpoints, raw corpora, mutable logs, secrets, and machine-local caches
do not belong in Git history. Public weights use Hugging Face; compact manifests,
hashes, metrics, protocols, and reproducible plotting code stay with each model.

## Evidence map

| Evidence class | 135M | 1.1B |
|---|---|---|
| From-zero initialization | Documented in public repository | Documented in public code and evidence repository |
| Data controls | MinHash/LSH, overlap filtering, source caps | Global exact deduplication, language/content filtering, benchmark screening |
| Evaluation | Six-task same-harness comparison | Seven-task frozen same-protocol comparison with sample-level intervals |
| Efficiency | Single-L20 run records | 12,845 tok/s and 71.17% point MFU snapshot |
| Negative evidence | Full-SFT and GSM8K RLVR limitations retained | Continuation A not promoted; continuation B remains gated |
| Public weights | [AliceYin/l20-edu-135m](https://huggingface.co/AliceYin/l20-edu-135m) | [AliceYin/L20-1B-20B-Base](https://huggingface.co/AliceYin/L20-1B-20B-Base) |

## Research trajectory

```text
135M systems study                         1.1B scaling study
random init                               random init + new tokenizer
    │                                         │
10B FineWeb-Edu                           20B mixed English corpus
    │                                         │
3B curated continuation                  frozen base evaluation
    │                                         │
SFT interpolation + RLVR negative        evidence-gated post-training
    │                                         │
public checkpoint                         public base checkpoint
```

This is a research collection, not a claim that every model is state of the
art. Comparisons are valid only for the named checkpoint, task set, metric,
revision, and evaluation protocol.

## Repository structure

```text
assets/       Collection identity and diagrams
models/       One evidence-bounded page per model
catalog.json  Machine-readable model and artifact index
```

Validate the catalog and all repository-local links with:

```bash
python validate_catalog.py
```

## Maintainer

[Yin Li](https://github.com/yinli-systems) · model releases on
[Hugging Face](https://huggingface.co/AliceYin)
