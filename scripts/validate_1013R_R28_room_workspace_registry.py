from __future__ import annotations

import json
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

STAGE_ID = "1013R_R28_ROOM_WORKSPACE_REGISTRY"
OUT_DIR = ROOT / "outputs" / "PREP_ROOM_RENDER_CANVAS_DEEPEN_V1" / "1013R_R28_room_workspace_registry"
DOC_PATH = ROOT / "docs" / "1013R_R28_room_workspace_registry.md"


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
    from backend.xiaobei_ai import prep_room_room_workspace_registry_1013R_R28 as module

    errors: list[str] = []
    bundle = module.build_room_registry_sample_bundle()
    registry = bundle.get("room_workspace_registry", {})
    rooms = bundle.get("rooms", [])
    boundary = bundle.get("boundary", {})
    doc = DOC_PATH.read_text(encoding="utf-8", errors="ignore") if DOC_PATH.exists() else ""

    if bundle.get("stage") != STAGE_ID:
        fail(errors, "stage_id_mismatch")
    if registry.get("registry_id") != "SHIWEI_ROOM_WORKSPACE_REGISTRY_R0":
        fail(errors, "registry_id_mismatch")
    if registry.get("consumes", {}).get("r27_stage") != "1013R_R27_XIAOJIAO_INTENT_FRAME_ROUTER_FIXTURE":
        fail(errors, "r27_not_consumed")
    if registry.get("consumes", {}).get("l0_stage") != "1013L_R0_MAIN_RENDER_SHELL_BASELINE_AND_BACKEND_REUSE_REGISTRY":
        fail(errors, "l0_not_consumed")
    if registry.get("consumes", {}).get("l5_stage") != "1013L_R5_MAIN_SHELL_BACKEND_VIEWMODEL_READONLY_FETCH_ADAPTER":
        fail(errors, "l5_not_consumed")

    room_ids = {room.get("room_id") for room in rooms}
    for room_id in ["prep_room", "classroom", "research_room", "material_room", "review_room", "archive_room"]:
        if room_id not in room_ids:
            fail(errors, f"room_missing:{room_id}")
    prep_room = next((room for room in rooms if room.get("room_id") == "prep_room"), {})
    if prep_room.get("status") != "active_from_1013L_registry":
        fail(errors, "prep_room_not_active_from_1013L")
    prep_state_ids = {state.get("state_id") for state in prep_room.get("states", [])}
    for state_id in [
        "prep_notebook",
        "big_unit_design",
        "single_lesson_design",
        "courseware_workspace",
        "classroom_display_preview",
        "material_intake",
        "week_calendar",
    ]:
        if state_id not in prep_state_ids:
            fail(errors, f"prep_state_missing:{state_id}")
    if len(prep_state_ids) < 7:
        fail(errors, "prep_room_state_count_too_low")
    for room in rooms:
        if room.get("room_id") != "prep_room" and room.get("status") != "future_placeholder":
            fail(errors, f"future_room_not_placeholder:{room.get('room_id')}")

    agent = registry.get("agent_profile", {})
    if agent.get("display_name") != "小教":
        fail(errors, "agent_display_name_not_xiaojiao")
    if agent.get("same_agent_across_rooms") is not True:
        fail(errors, "same_agent_across_rooms_missing")
    rule = registry.get("registry_rule", {})
    for key in [
        "derive_from_1013L_states_before_adding_new_rooms",
        "do_not_make_each_room_a_chat_page",
        "level_2_changes_work_context",
        "level_1_shell_stays_persistent",
    ]:
        if rule.get(key) is not True:
            fail(errors, f"registry_rule_missing:{key}")

    blocked_true_flags = [
        "new_room_runtime_created",
        "new_disconnected_page_created",
        "route_registered",
        "endpoint_registered",
        "runtime_connected",
        "provider_called",
        "model_called",
        "database_written",
        "memory_written",
        "vector_index_written",
        "feishu_written",
        "formal_apply_performed",
        "R36_modified",
        "main_shell_modified",
    ]
    for flag in blocked_true_flags:
        if boundary.get(flag):
            fail(errors, f"readonly_boundary_broken:{flag}")
    if boundary.get("derived_from_1013L_states") is not True:
        fail(errors, "derived_from_1013L_states_not_marked")
    if boundary.get("static_registry_only") is not True:
        fail(errors, "static_registry_only_not_marked")

    for token in [
        "derive_from_1013L_states_before_adding_new_rooms=true",
        "do_not_make_each_room_a_chat_page=true",
        "same_agent_across_rooms=true",
        "new_room_runtime_created=false",
        "1013R_R29_TOOL_FRAME_REGISTRY",
    ]:
        if token not in doc:
            fail(errors, f"doc_token_missing:{token}")

    evidence = {
        "module": "backend.xiaobei_ai.prep_room_room_workspace_registry_1013R_R28",
        "registry_id": registry.get("registry_id"),
        "room_count": len(rooms),
        "prep_room_state_count": len(prep_state_ids),
        "boundary": boundary,
    }
    result = {
        "stage_id": STAGE_ID,
        "status": "PASS" if not errors else "FAIL",
        "validator_pass": not errors,
        "created_at": now(),
        "checks": {
            "room_registry_defined": registry.get("registry_id") == "SHIWEI_ROOM_WORKSPACE_REGISTRY_R0",
            "prep_room_derived_from_1013L": not any(code.startswith("prep_state_missing") for code in errors),
            "future_rooms_are_placeholders": not any(code.startswith("future_room_not_placeholder") for code in errors),
            "same_xiaojiao_across_rooms": agent.get("same_agent_across_rooms") is True,
            "static_registry_only": boundary.get("static_registry_only") is True,
            "formal_apply_performed": False,
        },
        "failed_checks": errors,
    }
    return result, evidence, errors


def write_outputs(result: dict[str, Any], evidence: dict[str, Any]) -> None:
    from backend.xiaobei_ai import prep_room_room_workspace_registry_1013R_R28 as module

    bundle = module.build_room_registry_sample_bundle()
    write_json(OUT_DIR / "1013R_R28_result.json", result)
    write_json(OUT_DIR / "room_workspace_registry_1013R_R28.json", bundle["room_workspace_registry"])
    write_json(OUT_DIR / "room_workspace_registry_rooms_1013R_R28.json", bundle["rooms"])
    write_json(OUT_DIR / "room_workspace_registry_evidence_1013R_R28.json", evidence)
    report = f"""# 1013R_R28 room workspace registry

```text
stage_id={STAGE_ID}
registry_id=SHIWEI_ROOM_WORKSPACE_REGISTRY_R0
derived_from_1013L_states=true
static_registry_only=true
new_room_runtime_created=false
new_disconnected_page_created=false
route_registered=false
endpoint_registered=false
runtime_connected=false
provider_called=false
model_called=false
formal_apply_performed=false
```

## 验证

```text
validator_pass={str(result["validator_pass"]).lower()}
failed_checks={result["failed_checks"]}
```

## 下一步

```text
1013R_R29_TOOL_FRAME_REGISTRY
```
"""
    write_text(OUT_DIR / "1013R_R28_report.md", report)


def main() -> None:
    result, evidence, errors = validate()
    write_outputs(result, evidence)
    if errors:
        raise SystemExit("FAIL: " + ", ".join(errors))
    print("PASS: 1013R_R28 room workspace registry")


if __name__ == "__main__":
    main()
