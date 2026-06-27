from __future__ import annotations

import json
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

STAGE_ID = "1013R_R23_PREP_ROOM_TEACHER_WALKTHROUGH_SCRIPT"
STAGE_DIR = ROOT / "outputs" / "PREP_ROOM_RENDER_CANVAS_DEEPEN_V1" / "1013R_R23_prep_room_teacher_walkthrough_script"
DOC_PATH = ROOT / "docs" / "1013R_R23_prep_room_teacher_walkthrough_script.md"


def now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def write_json(path: Path, payload: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def fail(errors: list[str], code: str) -> None:
    errors.append(code)


def validate() -> tuple[dict[str, Any], dict[str, Any], list[str]]:
    from backend.xiaobei_ai import prep_room_teacher_walkthrough_script_1013R_R23 as module

    errors: list[str] = []
    bundle = module.build_walkthrough_sample_bundle()
    script = bundle.get("teacher_walkthrough_script", {})
    steps = bundle.get("walkthrough_steps", [])
    boundary = bundle.get("boundary", {})
    doc = DOC_PATH.read_text(encoding="utf-8", errors="ignore") if DOC_PATH.exists() else ""

    if bundle.get("stage") != STAGE_ID:
        fail(errors, "stage_id_mismatch")
    if script.get("script_id") != "SHIWEI_PREP_ROOM_TEACHER_WALKTHROUGH_SCRIPT_R0":
        fail(errors, "script_id_mismatch")
    if script.get("current_object", {}).get("title") != "2-1《色彩的渐变》":
        fail(errors, "current_object_not_preserved")
    if script.get("consumes", {}).get("r20_stage") != "1013R_R20_PREP_ROOM_UNIFIED_PACKAGE_READONLY_EXPORT_R0":
        fail(errors, "r20_not_consumed")
    if script.get("consumes", {}).get("r22_stage") != "1013R_R22_TEACHER_READABILITY_AND_2K_LINKAGE_SMOKE":
        fail(errors, "r22_not_consumed")
    if len(steps) < 6:
        fail(errors, "walkthrough_steps_too_few")
    required_step_ids = {"open_prep_room", "read_known_and_missing", "preview_display", "preview_courseware", "try_assessment", "teacher_confirm_next"}
    present = {item.get("step_id") for item in steps}
    for step_id in required_step_ids:
        if step_id not in present:
            fail(errors, f"walkthrough_step_missing:{step_id}")
    text = json.dumps(script, ensure_ascii=False)
    for token in ["大屏", "课件", "学习单", "评价表", "阻断", "告诉小教你要推进哪一步"]:
        if token not in text:
            fail(errors, f"walkthrough_token_missing:{token}")

    blocked_true_flags = [
        "route_registered",
        "endpoint_registered",
        "provider_called",
        "model_called",
        "database_written",
        "memory_written",
        "formal_apply_performed",
        "R36_modified",
        "main_shell_modified",
        "existing_page_modified",
    ]
    for flag in blocked_true_flags:
        if boundary.get(flag):
            fail(errors, f"readonly_boundary_broken:{flag}")
    if not boundary.get("teacher_walkthrough_script_defined"):
        fail(errors, "teacher_walkthrough_script_not_marked")
    for token in ["R36_modified=false", "route_registered=false", "formal_apply_performed=false"]:
        if token not in doc:
            fail(errors, f"r23_doc_token_missing:{token}")

    evidence = {
        "module": "backend.xiaobei_ai.prep_room_teacher_walkthrough_script_1013R_R23",
        "script_id": script.get("script_id"),
        "step_count": len(steps),
        "acceptance": script.get("acceptance"),
        "boundary": boundary,
    }
    result = {
        "stage_id": STAGE_ID,
        "status": "PASS" if not errors else "FAIL",
        "validator_pass": not errors,
        "created_at": now(),
        "checks": {
            "walkthrough_script_defined": script.get("script_id") == "SHIWEI_PREP_ROOM_TEACHER_WALKTHROUGH_SCRIPT_R0",
            "major_teacher_flow_present": required_step_ids.issubset(present),
            "readonly_boundaries_intact": not any(code.startswith("readonly_boundary_broken") for code in errors),
            "R36_modified": False,
            "provider_called": False,
            "model_called": False,
            "formal_apply_performed": False,
        },
        "failed_checks": errors,
    }
    return result, evidence, errors


def write_outputs(result: dict[str, Any], evidence: dict[str, Any]) -> None:
    from backend.xiaobei_ai import prep_room_teacher_walkthrough_script_1013R_R23 as module

    bundle = module.build_walkthrough_sample_bundle()
    write_json(STAGE_DIR / "1013R_R23_result.json", result)
    write_json(STAGE_DIR / "teacher_walkthrough_script_1013R_R23.json", bundle["teacher_walkthrough_script"])
    write_json(STAGE_DIR / "walkthrough_steps_1013R_R23.json", bundle["walkthrough_steps"])
    write_json(STAGE_DIR / "teacher_walkthrough_evidence_1013R_R23.json", evidence)
    report = f"""# 1013R_R23 prep room teacher walkthrough script

```text
stage_id={STAGE_ID}
script_id=SHIWEI_PREP_ROOM_TEACHER_WALKTHROUGH_SCRIPT_R0
current_object=三年级第二单元第1课《色彩的渐变》
R36_modified=false
route_registered=false
endpoint_registered=false
provider_called=false
model_called=false
database_written=false
memory_written=false
formal_apply_performed=false
```

## 验证

```text
validator_pass={str(result["validator_pass"]).lower()}
failed_checks={result["failed_checks"]}
```

## 下一步

```text
1013R_R24_RENDER_BLOCK_COMPONENT_BOUNDARY_MAP
```
"""
    write_text(STAGE_DIR / "1013R_R23_report.md", report)


def main() -> None:
    result, evidence, errors = validate()
    write_outputs(result, evidence)
    if errors:
        raise SystemExit("FAIL: " + ", ".join(errors))
    print("PASS: 1013R_R23 prep room teacher walkthrough script")


if __name__ == "__main__":
    main()
