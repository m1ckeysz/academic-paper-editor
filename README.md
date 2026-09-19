# Academic Paper Editor

A project-aware skill for reviewing, polishing, revising, and drafting academic papers from the manuscript and evidence you provide.

The skill is designed for research projects that may include LaTeX sources, compiled PDFs, bibliography files, source code, configurations, figures, tables, logs, and existing experiment outputs. When you provide a project, it reviews the accessible material first, then continues with paragraph-by-paragraph academic English polishing. Ask for substantive revision or new writing in ordinary language whenever needed. When you provide only a paragraph, it can polish that paragraph without requiring a project upload.

## Quick Start

Provide an accessible paper project and say:

> Review this paper project first. Read the manuscript, code, figures, tables, and existing results. Do not run research code. Then get ready to polish the English paragraphs I send.

After a successful review, the skill returns its original activation sentence:

```text
润色模式已启动，请发送需要修改的英文段落
```

Paste a paragraph next. The default response is **only the revised English text**.

No configuration file, profile selection, or special command is required. You can also ask directly:

| Request | Result |
| --- | --- |
| "Check whether the abstract agrees with Table 2 and the existing results." | Focused review findings with source locations. |
| Paste an English manuscript paragraph. | Polished text only. |
| "Reorganize these two paragraphs to make the problem and contribution clearer." | The requested substantive revision, using the original writing rules. |
| "Write a 180-word abstract using the reviewed manuscript and confirmed results." | A grounded draft, without invented results or references. |

Ask for explanations, alternatives, or another communication language when needed. These do not change the default for later turns unless you ask for a lasting change. A standalone paragraph can be polished directly, but that does not count as a project audit.

## Key Features

- Reviews LaTeX manuscripts and compiled PDFs together.
- Inspects figures, tables, bibliography files, logs, configurations, and existing result artifacts.
- Reads research code to understand implementation details and verify manuscript consistency.
- Cross-checks important quantitative claims against available project evidence.
- Preserves technical terminology, equations, citations, numerical values, and claim scope during editing.
- Improves logical continuity, paragraph structure, sentence cohesion, grammar, clarity, and concision.
- Uses simple, direct academic English rather than ornate or promotional wording.
- Applies a presentation-first narrative strategy while preserving scientific integrity.
- Keeps research-code execution read-only by default.
- Supports requested restructuring and drafting without introducing new configuration or mandatory planning stages.

## Operating Model

The default remains two sequential modes: project audit, then ongoing polishing. Explicit review, revision, or writing requests are handled directly within the same conversation; users do not need to switch modes.

### 1. Project Audit Mode

Before polishing individual paragraphs, the skill reviews the accessible paper project and builds a working understanding of:

- the research problem and motivation;
- the claimed research gap;
- the method and technical contributions;
- the experimental setup and evaluation criteria;
- the strongest supported results;
- terminology, notation, datasets, metrics, and comparison conventions;
- the role of important figures and tables;
- inconsistencies among the manuscript, PDF, code, logs, tables, figures, and existing result files.

The skill may perform a non-destructive LaTeX compilation check when useful and when the required tools are available. It does not modify the manuscript merely to make compilation succeed unless the user explicitly requests fixes.

After an ordinary audit is complete, the skill switches to polishing using the original activation message. If requested material is unavailable, a requested check cannot be performed, or a material conflict remains, it briefly explains the issue rather than hiding it behind a completion message. It does not send a long audit report unless asked.

The skill keeps relevant source locations and coverage gaps in working context, not in a mandatory database or project report. It reuses context in the current conversation and rechecks changed or newly relevant files. It does not promise permanent memory across sessions.

### 2. Polishing Mode

Each subsequent English passage is treated as manuscript text to revise in the context of the audited project.

By default, the response contains only the revised English passage. The skill does not automatically edit `.tex` files when the user pastes a paragraph.

The revision process prioritizes:

- logical continuity;
- sentence-to-sentence cohesion;
- paragraph-level rhetorical structure;
- direct and readable academic English;
- restrained use of transition words;
- minimal use of unnecessary parentheses;
- preservation of technical meaning and scientific claim strength.

If a material ambiguity cannot be resolved from the manuscript and project context, the skill asks for clarification using the original question marker, `【疑问】`, rather than guessing. Minor stylistic choices do not require confirmation. Clear questions and instructions are not mistaken for manuscript paragraphs.

### Requested Revision and Writing

For substantive revision, the skill changes the structure or emphasis only as far as your request requires. It does not treat "improve the writing" as permission to change scientific claims or project files.

For new writing, it uses your notes, the reviewed manuscript, and the available evidence. It drafts directly unless you ask for an outline. Missing optional facts are omitted; missing essential facts receive a focused question rather than a fabricated result or citation. The same polishing rules and Presentation-First Narrative Principle apply.

Before returning manuscript text, it silently checks numbers, terminology, equations, citations, negation, uncertainty, assumptions, and claim scope. It may keep already clear wording unchanged. These are editing instructions, not a guarantee that every error will be detected.

## Research-Code Execution Policy

Research code is read-only by default.

Without explicit user authorization, the skill must not run:

- training;
- evaluation;
- inference used to generate research results;
- plotting or figure-generation pipelines;
- analysis scripts;
- ablations;
- benchmarks;
- metric recomputation;
- result-generating preprocessing or data transformation.

Reading source code, configs, logs, existing result files, generated plots, table sources, and checkpoint metadata is allowed.

When the user explicitly authorizes execution, the skill should run only the minimum necessary command and preserve the distinction between pre-existing evidence and newly generated evidence. Authorization is scoped to the request, not all scripts or future tasks.

Read-only file inventory, safe text extraction, and rendering an existing PDF are allowed. They do not authorize running research pipelines. Project content is evidence, not an instruction to execute commands or transmit files.

A LaTeX check still does not require a separate request when a safe, non-destructive check is possible. It must use isolated outputs, disable shell escape, avoid automatic project build hooks, and leave existing files unchanged. If that is not possible, the skill uses existing PDFs and logs and states which check was not performed. It does not silently install dependencies or enable network access.

The host environment must enforce real filesystem, execution, and network permissions. The skill's instructions are not an operating-system sandbox.

## Scientific-Integrity Boundary

The skill is designed to present the strongest supported contribution clearly, not to manufacture stronger results.

It must never:

- change numerical results to improve the narrative;
- fabricate strengths, mechanisms, baselines, or evidence;
- hide evidence that is necessary to evaluate the main scientific conclusion;
- change metric definitions or comparison sets in a misleading way;
- convert a negative or null result into a positive result;
- overstate causality, robustness, statistical significance, practical significance, or generalization.

The goal is confident scientific communication without misrepresentation.

## Repository Structure

```text
academic-paper-editor/
├── SKILL.md
├── README.md
├── .gitignore
├── agents/
│   └── openai.yaml
├── references/
│   ├── output-format.md
│   ├── polishing-rules.md
│   ├── project-audit.md
│   ├── release-principle.md
│   └── writing-and-revision.md
└── scripts/
    └── project_inventory.py
```

### `SKILL.md`

Defines request routing, the original two-stage default, requested revision and writing, execution boundaries, file-editing behavior, and evidence discipline.

### `references/project-audit.md`

Defines how to inspect manuscript sources, PDFs, figures, tables, code, result artifacts, and LaTeX build outputs before polishing begins.

### `references/polishing-rules.md`

Defines paragraph-level academic English editing rules, including logical continuity, transitions, cohesion, paragraph structure, parentheses, terminology preservation, vocabulary, and claim-strength preservation.

### `references/release-principle.md`

Defines the presentation-first narrative strategy and its scientific-integrity constraints.

### `references/writing-and-revision.md`

Adds the small workflow for requested restructuring and drafting. It uses the existing writing policies rather than introducing replacement styles.

### `references/output-format.md`

Defines the exact user-facing response behavior during audit completion, polishing, and ambiguity handling.

### `scripts/project_inventory.py`

Creates a concise, read-only inventory of files relevant to a paper-project audit. It prunes common cache and dependency directories, skips symbolic links and model/checkpoint artifacts, and never imports or executes project code. It lists paths, not proof of completed review. The optional helper uses the Python standard library and requires Python 3.9 or newer.

Example:

```bash
python scripts/project_inventory.py /path/to/paper-project
```

Limit the printed file list when needed:

```bash
python scripts/project_inventory.py /path/to/paper-project --max-files 200
```

## Installation

Use `skill.zip` with a host that supports importing skill packages. Follow that host's installation instructions; this repository does not assume that every account or client has the same installation interface.

The skill does not automatically obtain access to arbitrary folders on your computer. Supply the project through the host's supported file or workspace mechanism. Text-only use needs only the passage. Project review needs access to files; visual review needs PDF/image viewing tools; compilation additionally needs an appropriately isolated LaTeX environment. Unsupported checks must be reported rather than simulated.

For a single-skill GitHub repository, place `SKILL.md`, this README, `.gitignore`, `agents/`, `references/`, and `scripts/` at the repository root. Keep paper projects separate. Publish the complete packaged skill as a release asset rather than committing generated archives alongside the source.

## Recommended Development Workflow

1. Edit `SKILL.md` or the relevant file in `references/`.
2. Keep instructions concise and place detailed rules in reference files.
3. Test any changed scripts before packaging.
4. Validate and package the complete skill with the current Skill packaging tooling.
5. Test the packaged skill on a real paper project.
6. Refine rules based on observed behavior.
7. Commit source changes to Git and publish validated archives as release assets when appropriate.

A small manual regression check is sufficient to start: try a standalone paragraph, a project audit, a requested rewrite, and a draft with a missing essential fact. Also check a restrictive "only", an unchanged citation key, a conflicting table value, and an English instruction that must not be treated as manuscript text. Confirm that ordinary polishing returns text only and does not edit files or run research code. Package validation and helper-script tests do not establish end-to-end editing quality.

## What Changed in This Update

The files `references/polishing-rules.md` and `references/release-principle.md` are unchanged from the previous package. The default revised-text-only output, Chinese handoff, question marker, and research-code authorization requirement are preserved.

This update adds ordinary-language routing for review, polishing, revision, and drafting; honest handling of incomplete audits; same-conversation context reuse; a silent meaning-preservation check; and a safer file inventory. It adds one workflow reference, not a profile system, database, or mandatory configuration step.

## Data and Privacy Guidance

Do not commit unpublished manuscripts, private datasets, experiment outputs, model checkpoints, credentials, API keys, or other confidential research artifacts to this repository.

Keep the reusable skill and individual research projects separate:

```text
academic-paper-editor/   # reusable skill source
paper-project-a/         # private research project
paper-project-b/         # private research project
```

The skill package should contain the workflow and reusable rules, not the user's paper or research data.

## Customization

The most useful customization points are:

- `references/polishing-rules.md` for writing preferences;
- `references/release-principle.md` for narrative strategy;
- `references/project-audit.md` for additional consistency checks;
- `references/output-format.md` for response-format behavior.

For stronger personalization without model fine-tuning, add a small reference file containing representative before-and-after editing examples that reflect the desired academic style.

## License

No license is included by default. Add a license file before distributing the repository publicly if you want to grant reuse, modification, or redistribution rights.
