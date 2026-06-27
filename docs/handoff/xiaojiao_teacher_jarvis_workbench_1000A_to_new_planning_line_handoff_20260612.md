# Xiaojiao Teacher Jarvis Workbench 1000A To New Planning Line Handoff

Date: 2026-06-12

Workspace:

```text
D:\Documents\SmartEdu\xiaobei-core
```

Purpose:

```text
This document lets a new Codex session continue the planning line without reconstructing the whole conversation.
It records the completed 1000A package, the file index, the next planning route, and the GitHub review upload habit for GPT review.
```

## Current Status

Latest completed stage:

```text
1000A_XIAOJIAO_TEACHER_JARVIS_WORKBENCH_CONCEPT_CONTRACT
```

Final status:

```text
XIAOJIAO_TEACHER_JARVIS_WORKBENCH_CONCEPT_CONTRACT_PASS
```

Validator marker:

```text
ALL_1000A_XIAOJIAO_TEACHER_JARVIS_WORKBENCH_CONCEPT_CONTRACT_CHECKS_OK
```

Validation evidence:

```powershell
python scripts/validate_xiaojiao_teacher_jarvis_workbench_concept_contract_1000A.py
python scripts/validate_xiaojiao_teacher_jarvis_workbench_concept_contract_1000A.py --root .
```

Both commands passed on 2026-06-12.

ZIP:

```text
docs/audit_packages/xiaojiao_teacher_jarvis_workbench_concept_contract_1000A.zip
```

ZIP SHA256:

```text
559763E316C611BF44134ACA846CCF4CF464112B0C5A53439F538A8AEE745B14
```

ZIP entry count:

```text
9
```

Manifest alignment:

```text
manifest_minus_zip=[]
zip_minus_manifest=[]
```

## What 1000A Means

1000A is a concept-contract package. It does not implement UI and does not connect runtime.

It locks the product-shape boundary for:

- `Unified Xiaojiao Agent / 统一小教智能体`
- `Agent-led Progressive Workspace / 小教主导的渐进式工作台`
- `Dynamic Work Panel / 动态工作面板`
- `Work Object / 工作对象`
- `Work Action / 工作动作`
- `Work State / 工作状态`
- `Work View Composer / 工作视图组合器`
- `Assistant Surface / 小教交互表层`

Important boundary:

```text
Jarvis is internal metaphor only.
Teacher-facing copy must use Xiaojiao / 小教 language, not Jarvis.
```

Important product relation:

```text
周工作图谱 does not replace 学期周历表.
学期周历表 = semester progress supporting table.
周工作图谱 = higher-level weekly work panel.
```

Important legacy boundary:

```text
小备 / Xiaobei / xiaobei remain legacy internal namespace.
Do not perform blind full-repository rename.
```

## File Index

### Planning And Handoff

| Purpose | Path |
| --- | --- |
| 1000 planning notes | `docs/handoff/teacher_jarvis_workbench_planning_notes_1000_20260612.md` |
| 1000A executable handoff | `docs/handoff/xiaojiao_teacher_jarvis_workbench_1000A_execution_handoff_20260612.md` |
| This new-line handoff | `docs/handoff/xiaojiao_teacher_jarvis_workbench_1000A_to_new_planning_line_handoff_20260612.md` |

### 1000A Contract

| Purpose | Path |
| --- | --- |
| Concept contract markdown | `docs/foundation/xiaojiao_teacher_jarvis_workbench_concept_contract_1000A.md` |
| Concept contract JSON | `docs/foundation/xiaojiao_teacher_jarvis_workbench_concept_contract_1000A.json` |

### 1000A Audit

| Purpose | Path |
| --- | --- |
| Report | `docs/audit/xiaojiao_teacher_jarvis_workbench_concept_contract_1000A_report.md` |
| Result | `docs/audit/xiaojiao_teacher_jarvis_workbench_concept_contract_1000A_result.json` |
| Checklist | `docs/audit/xiaojiao_teacher_jarvis_workbench_concept_contract_1000A_checklist.json` |

### 1000A Package

| Purpose | Path |
| --- | --- |
| Manifest | `docs/audit_packages/xiaojiao_teacher_jarvis_workbench_concept_contract_1000A_manifest.json` |
| ZIP | `docs/audit_packages/xiaojiao_teacher_jarvis_workbench_concept_contract_1000A.zip` |
| Validator | `scripts/validate_xiaojiao_teacher_jarvis_workbench_concept_contract_1000A.py` |

### GitHub Review Upload Guide

| Purpose | Path |
| --- | --- |
| Existing upload template | `docs/guides/github_review_upload_prompt_template_for_gpt.md` |

## ZIP Entries

The 1000A ZIP contains:

```text
docs/handoff/xiaojiao_teacher_jarvis_workbench_1000A_execution_handoff_20260612.md
docs/handoff/teacher_jarvis_workbench_planning_notes_1000_20260612.md
docs/foundation/xiaojiao_teacher_jarvis_workbench_concept_contract_1000A.md
docs/foundation/xiaojiao_teacher_jarvis_workbench_concept_contract_1000A.json
docs/audit/xiaojiao_teacher_jarvis_workbench_concept_contract_1000A_report.md
docs/audit/xiaojiao_teacher_jarvis_workbench_concept_contract_1000A_result.json
docs/audit/xiaojiao_teacher_jarvis_workbench_concept_contract_1000A_checklist.json
docs/audit_packages/xiaojiao_teacher_jarvis_workbench_concept_contract_1000A_manifest.json
scripts/validate_xiaojiao_teacher_jarvis_workbench_concept_contract_1000A.py
```

The ZIP does not include itself. When building a GitHub review repo, copy the ZIP file as a separate top-level review artifact under the same relative path.

## Recommended Next Planning Line

Do not enter 1000B until 1000A is reviewed or explicitly accepted.

Next recommended stage:

```text
1000B_EDUCATION_PRE_CLASS_WORK_SAMPLE_ROOM_BUSINESS_STRUCTURE
```

1000B should define the education pre-class sample room using primary art teacher as the first sample role, without hardcoding art-teacher logic as a system-wide rule.

1000B should not implement the full UI yet unless explicitly instructed. It should first define business structure:

- teacher role profile
- work scopes
- pre-class artifact map
- teaching work plan main document
- supporting artifact graph
- weekly work graph
- today work items
- classroom preparation package chain

## New Session Start Instruction

Use this if starting a fresh Codex session:

```text
Read:
docs/handoff/xiaojiao_teacher_jarvis_workbench_1000A_to_new_planning_line_handoff_20260612.md
docs/audit/xiaojiao_teacher_jarvis_workbench_concept_contract_1000A_result.json
docs/audit/xiaojiao_teacher_jarvis_workbench_concept_contract_1000A_report.md
docs/audit_packages/xiaojiao_teacher_jarvis_workbench_concept_contract_1000A_manifest.json

First verify 1000A if needed:
python scripts/validate_xiaojiao_teacher_jarvis_workbench_concept_contract_1000A.py
python scripts/validate_xiaojiao_teacher_jarvis_workbench_concept_contract_1000A.py --root .

Then either:
1. upload 1000A to a GitHub review repo for GPT review, or
2. if the user accepts 1000A locally, plan 1000B_EDUCATION_PRE_CLASS_WORK_SAMPLE_ROOM_BUSINESS_STRUCTURE.

Do not execute 1000B before the user asks.
```

## GitHub Review Habit

The preferred review habit is:

```text
stage outputs
-> ZIP + manifest
-> local validator no-arg and --root pass
-> dedicated public GitHub review repo
-> raw links for GPT review
-> optional fresh-clone validator pass
-> only then decide next stage
```

Do not push the whole `xiaobei-core` project. Use a small dedicated review repo containing only review artifacts and source anchors needed by the reviewer.

Suggested repo:

```text
ROLLcatCLUB/xiaojiao-1000a-teacher-jarvis-workbench-review
```

Suggested local review root:

```text
D:\Documents\SmartEdu\xiaobei-github-review\xiaojiao-1000a-teacher-jarvis-workbench-review
```

### Review Repo Copy List

Copy these files, preserving relative paths:

```text
docs/handoff/xiaojiao_teacher_jarvis_workbench_1000A_to_new_planning_line_handoff_20260612.md
docs/handoff/xiaojiao_teacher_jarvis_workbench_1000A_execution_handoff_20260612.md
docs/handoff/teacher_jarvis_workbench_planning_notes_1000_20260612.md
docs/foundation/xiaojiao_teacher_jarvis_workbench_concept_contract_1000A.md
docs/foundation/xiaojiao_teacher_jarvis_workbench_concept_contract_1000A.json
docs/audit/xiaojiao_teacher_jarvis_workbench_concept_contract_1000A_report.md
docs/audit/xiaojiao_teacher_jarvis_workbench_concept_contract_1000A_result.json
docs/audit/xiaojiao_teacher_jarvis_workbench_concept_contract_1000A_checklist.json
docs/audit_packages/xiaojiao_teacher_jarvis_workbench_concept_contract_1000A_manifest.json
docs/audit_packages/xiaojiao_teacher_jarvis_workbench_concept_contract_1000A.zip
scripts/validate_xiaojiao_teacher_jarvis_workbench_concept_contract_1000A.py
docs/guides/github_review_upload_prompt_template_for_gpt.md
```

Add a review `README.md` in the review repo with:

- stage code
- final status
- validator commands and marker
- ZIP SHA256
- raw link index
- GPT review prompt
- warning that this is a review area, not the full source repo

### Forbidden Uploads

Never upload:

```text
.env
token
secret
real student data
real classroom logs
Feishu token
provider raw prompt/response
node_modules
__pycache__
the whole xiaobei-core repo
database files
```

### Important Git Attribute

Before committing the review repo, add a `.gitattributes` file to prevent line-ending normalization from changing validator hashes:

```powershell
[System.IO.File]::WriteAllBytes(
  (Join-Path $target ".gitattributes"),
  [System.Text.Encoding]::ASCII.GetBytes("* -text`n")
)
```

Then run the validator inside the review repo:

```powershell
Set-Location $target
python scripts/validate_xiaojiao_teacher_jarvis_workbench_concept_contract_1000A.py
python scripts/validate_xiaojiao_teacher_jarvis_workbench_concept_contract_1000A.py --root .
```

## GitHub Upload Commands

Preferred path with `gh` and git:

```powershell
cd D:\Documents\SmartEdu\xiaobei-core
gh auth status -h github.com

$reviewRoot = "D:\Documents\SmartEdu\xiaobei-github-review"
$repoName = "xiaojiao-1000a-teacher-jarvis-workbench-review"
$target = Join-Path $reviewRoot $repoName
New-Item -ItemType Directory -Force -Path $target | Out-Null

# Copy files from the copy list, preserving relative paths.
# Add README.md and .gitattributes.

Set-Location $target
git init -b master
git add .
git commit -m "Add Xiaojiao 1000A review package"
gh repo create ROLLcatCLUB/$repoName --public --source . --remote origin --push
```

If the repo already exists:

```powershell
Set-Location $target
git init -b master
git add .
git commit -m "Refresh Xiaojiao 1000A review package"
git remote add origin https://github.com/ROLLcatCLUB/$repoName.git
git push -u origin master --force
```

If normal `git push` fails because the HTTPS helper is broken, use GitHub API upload as a fallback. Keep it scoped to the review directory and upload file bytes, not generated chat text. Use `gh api` or a small PowerShell script that:

```text
1. creates/clears the target review repo
2. reads each allowed file as bytes
3. base64 encodes content
4. PUTs to /repos/ROLLcatCLUB/<repo>/contents/<relative-path>
5. uses branch=master
6. verifies raw links after upload
```

## Raw Link Template

After upload, raw links should look like:

```text
Repo:
https://github.com/ROLLcatCLUB/xiaojiao-1000a-teacher-jarvis-workbench-review

README:
https://raw.githubusercontent.com/ROLLcatCLUB/xiaojiao-1000a-teacher-jarvis-workbench-review/master/README.md

Result:
https://raw.githubusercontent.com/ROLLcatCLUB/xiaojiao-1000a-teacher-jarvis-workbench-review/master/docs/audit/xiaojiao_teacher_jarvis_workbench_concept_contract_1000A_result.json

Report:
https://raw.githubusercontent.com/ROLLcatCLUB/xiaojiao-1000a-teacher-jarvis-workbench-review/master/docs/audit/xiaojiao_teacher_jarvis_workbench_concept_contract_1000A_report.md

Checklist:
https://raw.githubusercontent.com/ROLLcatCLUB/xiaojiao-1000a-teacher-jarvis-workbench-review/master/docs/audit/xiaojiao_teacher_jarvis_workbench_concept_contract_1000A_checklist.json

Manifest:
https://raw.githubusercontent.com/ROLLcatCLUB/xiaojiao-1000a-teacher-jarvis-workbench-review/master/docs/audit_packages/xiaojiao_teacher_jarvis_workbench_concept_contract_1000A_manifest.json

Validator:
https://raw.githubusercontent.com/ROLLcatCLUB/xiaojiao-1000a-teacher-jarvis-workbench-review/master/scripts/validate_xiaojiao_teacher_jarvis_workbench_concept_contract_1000A.py

Execution handoff:
https://raw.githubusercontent.com/ROLLcatCLUB/xiaojiao-1000a-teacher-jarvis-workbench-review/master/docs/handoff/xiaojiao_teacher_jarvis_workbench_1000A_execution_handoff_20260612.md

New-line handoff:
https://raw.githubusercontent.com/ROLLcatCLUB/xiaojiao-1000a-teacher-jarvis-workbench-review/master/docs/handoff/xiaojiao_teacher_jarvis_workbench_1000A_to_new_planning_line_handoff_20260612.md
```

## GPT Review Prompt

Paste this to GPT after upload:

```text
请审核这个 GitHub review area：

https://github.com/ROLLcatCLUB/xiaojiao-1000a-teacher-jarvis-workbench-review

重点读取：
- README.md
- docs/handoff/xiaojiao_teacher_jarvis_workbench_1000A_to_new_planning_line_handoff_20260612.md
- docs/handoff/xiaojiao_teacher_jarvis_workbench_1000A_execution_handoff_20260612.md
- docs/audit/xiaojiao_teacher_jarvis_workbench_concept_contract_1000A_result.json
- docs/audit/xiaojiao_teacher_jarvis_workbench_concept_contract_1000A_report.md
- docs/audit/xiaojiao_teacher_jarvis_workbench_concept_contract_1000A_checklist.json
- docs/audit_packages/xiaojiao_teacher_jarvis_workbench_concept_contract_1000A_manifest.json
- scripts/validate_xiaojiao_teacher_jarvis_workbench_concept_contract_1000A.py
- ZIP entry 对齐情况

请判断：
1. final_status 是否可收
2. validator no-arg / --root 通过证据是否成立
3. manifest_minus_zip / zip_minus_manifest 是否为空
4. ZIP 内部路径是否 clean，是否没有绝对路径
5. 是否夹带 forbidden files
6. 是否违反 1000A concept-contract-only 边界
7. 是否正确处理 小教 / Xiaojiao 命名边界
8. 是否正确把 Jarvis 限定为内部隐喻
9. 是否正确保留 Work View Composer 和 Assistant Surface 作为支撑概念
10. 是否正确说明 周工作图谱 不替代 学期周历表
11. 是否可以进入 1000B_EDUCATION_PRE_CLASS_WORK_SAMPLE_ROOM_BUSINESS_STRUCTURE

注意：
这个仓库是 review area，不是完整源码仓库。
1000A 是 concept contract，不是 UI/runtime apply。
不要把“没有实现 UI / 没有接 provider / 没有写库”误判为失败；这些是本阶段边界。
```

## Stop Rules

New session should stop and ask if:

- validator fails after two repair rounds
- ZIP/manifest cannot be aligned
- GitHub upload includes forbidden files
- review repo raw links cannot be verified
- user asks to skip review and directly implement UI

Otherwise, next safe route is:

```text
Upload 1000A to GitHub review repo
-> get GPT review
-> if accepted, plan 1000B
```

