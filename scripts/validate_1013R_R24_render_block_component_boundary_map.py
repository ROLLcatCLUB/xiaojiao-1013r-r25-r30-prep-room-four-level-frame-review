from __future__ import annotations

import json
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

STAGE_ID = "1013R_R24_RENDER_BLOCK_COMPONENT_BOUNDARY_MAP"
STAGE_DIR = ROOT / "outputs" / "PREP_ROOM_RENDER_CANVAS_DEEPEN_V1" / "1013R_R24_render_block_component_boundary_map"
DOC_PATH = ROOT / "docs" / "1013R_R24_render_block_component_boundary_map.md"


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
    from backend.xiaobei_ai import prep_room_render_block_component_boundary_1013R_R24 as module

    errors: list[str] = []
    bundle = module.build_boundary_sample_bundle()
    boundary_map = bundle.get("component_boundary_map", {})
    entries = bundle.get("component_boundary_entries", [])
    boundary = bundle.get("boundary", {})
    doc = DOC_PATH.read_text(encoding="utf-8", errors="ignore") if DOC_PATH.exists() else ""

    if bundle.get("stage") != STAGE_ID:
        fail(errors, "stage_id_mismatch")
    if boundary_map.get("boundary_id") != "SHIWEI_RENDER_BLOCK_COMPONENT_BOUNDARY_MAP_R0":
        fail(errors, "boundary_id_mismatch")
    if boundary_map.get("consumes", {}).get("r17_stage") != "1013R_R17_RENDER_BLOCKS_PROTOCOL_R0":
        fail(errors, "r17_not_consumed")
    if boundary_map.get("consumes", {}).get("r20_stage") != "1013R_R20_PREP_ROOM_UNIFIED_PACKAGE_READONLY_EXPORT_R0":
        fail(errors, "r20_not_consumed")
    if boundary_map.get("consumes", {}).get("r23_stage") != "1013R_R23_PREP_ROOM_TEACHER_WALKTHROUGH_SCRIPT":
        fail(errors, "r23_not_consumed")
    if len(entries) < 14:
        fail(errors, "component_boundary_entries_too_few")
    components = {item.get("future_component") for item in entries}
    for component in [
        "PrepRoomObjectHeader",
        "XiaojiaoTaskStatePanel",
        "TeachingProcessTimeline",
        "CoursewareScriptPreview",
        "ClassroomDisplayPreview",
        "WorksheetPreviewSlot",
        "AssessmentBlockedPanel",
        "SourceEvidencePanel",
        "TeacherActionGatePanel",
    ]:
        if component not in components:
            fail(errors, f"component_missing:{component}")
    for entry in entries:
        interaction = entry.get("allowed_interaction_boundary", {})
        if interaction.get("may_save_or_export"):
            fail(errors, f"component_may_save_or_export:{entry.get('slot_id')}")
        if interaction.get("may_call_provider"):
            fail(errors, f"component_may_call_provider:{entry.get('slot_id')}")
        source = entry.get("source_policy_boundary", {})
        if source.get("must_not_promote_ai_draft_to_standard") is not True:
            fail(errors, f"source_policy_boundary_missing:{entry.get('slot_id')}")

    blocked_true_flags = [
        "component_implementation_created",
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
    if not boundary.get("render_block_component_boundary_defined"):
        fail(errors, "render_block_component_boundary_not_marked")
    for token in ["component_implementation_created=false", "route_registered=false", "formal_apply_performed=false"]:
        if token not in doc:
            fail(errors, f"r24_doc_token_missing:{token}")

    evidence = {
        "module": "backend.xiaobei_ai.prep_room_render_block_component_boundary_1013R_R24",
        "boundary_id": boundary_map.get("boundary_id"),
        "entry_count": len(entries),
        "component_groups": boundary_map.get("component_groups"),
        "boundary": boundary,
    }
    result = {
        "stage_id": STAGE_ID,
        "status": "PASS" if not errors else "FAIL",
        "validator_pass": not errors,
        "created_at": now(),
        "checks": {
            "component_boundary_map_defined": boundary_map.get("boundary_id") == "SHIWEI_RENDER_BLOCK_COMPONENT_BOUNDARY_MAP_R0",
            "major_components_present": not any(code.startswith("component_missing") for code in errors),
            "no_component_implementation": boundary.get("component_implementation_created") is False,
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
    from backend.xiaobei_ai import prep_room_render_block_component_boundary_1013R_R24 as module

    bundle = module.build_boundary_sample_bundle()
    write_json(STAGE_DIR / "1013R_R24_result.json", result)
    write_json(STAGE_DIR / "render_block_component_boundary_map_1013R_R24.json", bundle["component_boundary_map"])
    write_json(STAGE_DIR / "component_boundary_entries_1013R_R24.json", bundle["component_boundary_entries"])
    write_json(STAGE_DIR / "component_boundary_evidence_1013R_R24.json", evidence)
    report = f"""# 1013R_R24 render block component boundary map

```text
stage_id={STAGE_ID}
boundary_id=SHIWEI_RENDER_BLOCK_COMPONENT_BOUNDARY_MAP_R0
component_implementation_created=false
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
1013R_R25_READONLY_ROUTE_REGISTRATION_GATE
```
"""
    write_text(STAGE_DIR / "1013R_R24_report.md", report)


def main() -> None:
    result, evidence, errors = validate()
    write_outputs(result, evidence)
    if errors:
        raise SystemExit("FAIL: " + ", ".join(errors))
    print("PASS: 1013R_R24 render block component boundary map")


if __name__ == "__main__":
    main()
