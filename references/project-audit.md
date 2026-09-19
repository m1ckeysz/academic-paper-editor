# Project Audit Workflow

Use this workflow during the initial project review. Adapt it to the files that actually exist and do not pretend to have inspected unavailable material.

## Contents

1. Build a Project Map
2. Understand the Manuscript
3. Cross-Check Quantitative Evidence
4. Inspect Research Code Without Running It
5. Inspect Figures and Tables
6. Inspect the Rendered PDF
7. Check LaTeX Compilation
8. Build Context for Later Polishing

## Scope and Coverage

Review the main manuscript, supplied supplement, important figures and tables, and the code and existing results relevant to its claims. A file inventory is not proof that every file was read. Do not claim complete review of files that were only listed, sampled, skipped, or unavailable.

Keep a short working record of the material actually inspected and any important gaps. This can remain in the current conversation context; do not require a database, generated report file, or new project configuration. If a requested check cannot be completed, state that specific gap briefly using `references/output-format.md` before implying readiness. Do not block unrelated paragraph polishing solely because an optional artifact is absent.

## 1. Build a Project Map

Identify the files and directories relevant to the paper, including when present:

- main `.tex` entry file;
- included section or chapter `.tex` files;
- `.bib` bibliography files;
- document-class and style files;
- compiled paper PDF and supplementary PDF;
- figure directories and source figure files;
- table source files;
- source code and experiment scripts;
- configuration files;
- existing result files such as `.csv`, `.tsv`, `.json`, `.jsonl`, `.txt`, `.log`, `.npy`, `.npz`, or generated summaries;
- README files and experiment documentation;
- LaTeX build logs and auxiliary files when they are useful for diagnosis.

Use `scripts/project_inventory.py` when a filesystem-backed directory is available.

Ignore obvious caches, version-control internals, dependency directories, large model weights, large checkpoints, and unrelated generated artifacts unless they are specifically needed for the paper audit. Do not read credentials or follow symbolic links outside the supplied project. If the inventory output is truncated, inspect additional relevant paths before claiming coverage of them.

## 2. Understand the Manuscript

Determine:

- the research question;
- the motivation and claimed gap;
- the central method or idea;
- the contributions claimed by the paper;
- the experimental setup;
- the primary evaluation criteria;
- the main empirical findings;
- the intended narrative from abstract through conclusion.

Track important terminology, abbreviations, symbols, method names, dataset names, and metric conventions so that later polishing does not introduce inconsistencies.

## 3. Cross-Check Quantitative Evidence

For important quantitative claims, compare the manuscript against available evidence.

Check for mismatches among:

- abstract numbers;
- introduction claims;
- method-specific constants or settings;
- experiment prose;
- tables;
- figure annotations;
- captions;
- existing result files;
- logs;
- generated summaries.

Distinguish carefully among:

- absolute improvement;
- relative improvement;
- percentage points;
- percentages;
- means;
- standard deviations;
- confidence intervals;
- error bars;
- best-case versus average-case values;
- validation versus test results.

For claims likely to be used in subsequent editing, retain the source location when available, such as a file and section, table row, PDF page, or result key. Distinguish manuscript assertions, values recorded in existing outputs, and independently reproduced results. Reading code does not establish that it was executed for a particular reported result. Do not infer a deliberate trade-off from weaker performance unless the project evidence supports that design objective.

For citations, distinguish an existing citation key from verified bibliographic information and from a source that actually supports the claim. Do not invent missing references or describe an unread source as verified.

Do not run research evaluation or analysis code merely to resolve a mismatch. Record the conflict and wait for explicit authorization when execution would be necessary.

## 4. Inspect Research Code Without Running It

Read relevant code to understand, when possible:

- dataset construction and split definitions;
- preprocessing assumptions;
- model or method configuration;
- training settings relevant to manuscript claims;
- metric computation;
- baseline definitions;
- evaluation protocol;
- aggregation logic;
- random-seed handling;
- figure and table generation logic;
- terminology and naming conventions used by the implementation.

Do not execute training, evaluation, plotting, analysis, ablation, benchmarking, metric recomputation, or result-generating preprocessing without explicit user authorization.

## 5. Inspect Figures and Tables

Check:

- numbering and cross-references;
- labels;
- legends;
- units;
- axis names;
- metric direction;
- readability;
- font size;
- caption accuracy;
- consistency between displayed values and prose;
- consistency across multiple tables or figures;
- whether the figure or table actually supports the nearby claim;
- whether formatting accidentally overemphasizes or obscures a comparison.

Do not infer unsupported numeric values from low-resolution images when the source data is available elsewhere.

## 6. Inspect the Rendered PDF

When a compiled PDF is available, inspect what a reviewer actually sees rather than relying only on extracted text. Render or open page images for figures, tables, and layout; text extraction alone does not establish visual inspection. If page rendering is unavailable, disclose that the visual check was not performed.

Check for:

- missing or clipped figures;
- overlapping text;
- unreadable labels;
- poor line or page breaks;
- broken references;
- misplaced floats;
- inconsistent table rendering;
- unexpected blank pages;
- obvious citation or bibliography issues;
- visibly inconsistent notation;
- captions separated awkwardly from their figures or tables.

Treat the rendered PDF as the representation of that compiled presentation while using LaTeX source to understand structure and intent. Check for signs that the PDF belongs to an older source version. Do not silently choose either source as the factual authority when versions or numerical results conflict.

## 7. Check LaTeX Compilation

If an existing build log is available, inspect it first.

A non-destructive compilation check may be performed when tooling is available and the project can be built without modifying the manuscript source.

Look for:

- compilation errors;
- undefined references;
- undefined citations;
- missing files;
- duplicate labels;
- severe overfull boxes;
- bibliography failures;
- figure inclusion failures;
- package or class errors that affect output.

Follow the LaTeX compilation boundary in `SKILL.md`: use isolated outputs, disable shell escape, do not automatically execute project build hooks, and do not install dependencies or use the network without authorization. Skip compilation and inspect existing artifacts when these safeguards or required tools are unavailable.

Do not edit source files during the audit solely to make the build pass unless the user explicitly requests fixes.

After compilation, inspect the rendered PDF when possible. A successful compiler exit alone is not sufficient to verify presentation quality.

## 8. Build Context for Later Polishing

Before switching to Polishing Mode, retain a working understanding of:

- the paper's central contribution;
- the strongest supported evidence;
- key terminology and notation;
- section-level rhetorical roles;
- important design trade-offs;
- metric definitions;
- comparison conventions;
- unresolved inconsistencies that could affect wording.

Reuse this context for later passages in the same project. If files change, recheck affected sections and evidence rather than repeating the entire review. Do not carry one paper's facts into another paper. When earlier context is unavailable, reread relevant sources or request the minimum missing material instead of claiming permanent project memory.

Do not dump the audit by default. Follow the completion behavior and brief exceptions defined in `references/output-format.md`. When an audit report is explicitly requested, prioritize issues that affect meaning or evidence and include concrete source locations. Distinguish confirmed conflicts from questions that need author input.
