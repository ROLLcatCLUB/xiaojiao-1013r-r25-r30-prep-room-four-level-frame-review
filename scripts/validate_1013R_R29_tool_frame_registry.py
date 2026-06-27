from __future__ import annotations

import json
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

STAGE_ID = "1013R_R29_TOOL_FRAME_REGISTRY"
OUT_DIR = ROOT / "outputs" / "PREP_ROOM_RENDER_CANVAS_DEEPEN_V1" / "1013R_R29_tool_frame_registry"
DOC_PATH = ROOT / "docs" / "1013R_R29_tool_frame_registry.md"


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
    from backend.xiaobei_ai import prep_room_tool_frame_registry_1013R_R29 as module

    errors: list[str] = []
    bundle = module.build_tool_registry_sample_bundle()
    registry = bundle.get("tool_frame_registry", {})
    tools = bundle.get("tool_frames", [])
    render_groups = bundle.get("render_group_bindings", [])
    component_groups = bundle.get("component_group_bindings", [])
    boundary = bundle.get("boundary", {})
    doc = DOC_PATH.read_text(encoding="utf-8", errors="ignore") if DOC_PATH.exists() else ""

    if bundle.get("stage") != STAGE_ID:
        fail(errors, "stage_id_mismatch")
    if registry.get("registry_id") != "SHIWEI_TOOL_FRAME_REGISTRY_R0":
        fail(errors, "registry_id_mismatch")
    consumes = registry.get("consumes", {})
    if consumes.get("r28_stage") != "1013R_R28_ROOM_WORKSPACE_REGISTRY":
        fail(errors, "r28_not_consumed")
    if consumes.get("l5_stage") != "1013L_R5_MAIN_SHELL_BACKEND_VIEWMODEL_READONLY_FETCH_ADAPTER":
        fail(errors, "l5_not_consumed")
    if consumes.get("r17_stage") != "1013R_R17_RENDER_BLOCKS_PROTOCOL_R0":
        fail(errors, "r17_not_consumed")
    if consumes.get("r24_stage") != "1013R_R24_RENDER_BLOCK_COMPONENT_BOUNDARY_MAP":
        fail(errors, "r24_not_consumed")

    tool_ids = {tool.get("tool_id") for tool in tools}
    for tool_id in [
        "prep_notebook",
        "prep_room_home",
        "big_unit_design",
        "single_lesson_prep",
        "courseware_workspace",
        "classroom_display_preview",
        "material_intake",
        "schedule_context",
        "teacher_action_gate",
        "source_evidence",
        "xiaojiao_bottom_composer",
    ]:
        if tool_id not in tool_ids:
            fail(errors, f"tool_missing:{tool_id}")

    for tool in tools:
        if tool.get("level") != 3:
            fail(errors, f"tool_level_not_three:{tool.get('tool_id')}")
        if tool.get("formal_apply_allowed") is not False:
            fail(errors, f"tool_formal_apply_allowed:{tool.get('tool_id')}")
        if tool.get("may_call_provider") is not False:
            fail(errors, f"tool_provider_allowed:{tool.get('tool_id')}")

    group_ids = {group.get("group_id") for group in render_groups}
    for group_id in ["lesson_core", "derivatives", "governance"]:
        if group_id not in group_ids:
            fail(errors, f"render_group_missing:{group_id}")
    component_group_ids = {group.get("group_id") for group in component_groups}
    for group_id in ["prep_room_core", "derivative_objects", "governance_and_actions"]:
        if group_id not in component_group_ids:
            fail(errors, f"component_group_missing:{group_id}")

    rule = registry.get("registry_rule", {})
    for key in [
        "derive_from_l5_active_capabilities",
        "derive_content_modes_from_r17_block_groups",
        "derive_component_boundaries_from_r24",
        "tool_frame_controls_level_4_content",
        "tool_actions_must_respect_teacher_confirmation_gate",
        "do_not_make_tool_frame_a_new_page",
    ]:
        if rule.get(key) is not True:
            fail(errors, f"registry_rule_missing:{key}")
    if rule.get("formal_apply_allowed") is not False:
        fail(errors, "registry_rule_formal_apply_allowed")

    blocked_true_flags = [
        "tool_behavior_implemented",
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
    if boundary.get("derived_from_l5_and_r17_r24") is not True:
        fail(errors, "derived_from_l5_and_r17_r24_not_marked")
    if boundary.get("static_registry_only") is not True:
        fail(errors, "static_registry_only_not_marked")

    for token in [
        "derive_from_l5_active_capabilities=true",
        "derive_content_modes_from_r17_block_groups=true",
        "tool_actions_must_respect_teacher_confirmation_gate=true",
        "tool_behavior_implemented=false",
        "1013R_R30_RENDER_SURFACE_CONNECTOR_PLAN_OR_VISUAL_TOOL_POLISH",
    ]:
        if token not in doc:
            fail(errors, f"doc_token_missing:{token}")

    evidence = {
        "module": "backend.xiaobei_ai.prep_room_tool_frame_registry_1013R_R29",
        "registry_id": registry.get("registry_id"),
        "tool_count": len(tools),
        "render_group_count": len(render_groups),
        "component_group_count": len(component_groups),
        "boundary": boundary,
    }
    result = {
        "stage_id": STAGE_ID,
        "status": "PASS" if not errors else "FAIL",
        "validator_pass": not errors,
        "created_at": now(),
        "checks": {
            "tool_registry_defined": registry.get("registry_id") == "SHIWEI_TOOL_FRAME_REGISTRY_R0",
            "all_expected_tools_present": not any(code.startswith("tool_missing") for code in errors),
            "render_groups_from_r17": not any(code.startswith("render_group_missing") for code in errors),
            "component_groups_from_r24": not any(code.startswith("component_group_missing") for code in errors),
            "tool_behavior_not_implemented": boundary.get("tool_behavior_implemented") is False,
            "formal_apply_performed": False,
        },
        "failed_checks": errors,
    }
    return result, evidence, errors


def write_outputs(result: dict[str, Any], evidence: dict[str, Any]) -> None:
    from backend.xiaobei_ai import prep_room_tool_frame_registry_1013R_R29 as module

    bundle = module.build_tool_registry_sample_bundle()
    write_json(OUT_DIR / "1013R_R29_result.json", result)
    write_json(OUT_DIR / "tool_frame_registry_1013R_R29.json", bundle["tool_frame_registry"])
    write_json(OUT_DIR / "tool_frame_registry_tools_1013R_R29.json", bundle["tool_frames"])
    write_json(OUT_DIR / "tool_frame_registry_render_groups_1013R_R29.json", bundle["render_group_bindings"])
    write_json(OUT_DIR / "tool_frame_registry_component_groups_1013R_R29.json", bundle["component_group_bindings"])
    write_json(OUT_DIR / "tool_frame_registry_evidence_1013R_R29.json", evidence)
    report = f"""# 1013R_R29 tool frame registry

```text
stage_id={STAGE_ID}
registry_id=SHIWEI_TOOL_FRAME_REGISTRY_R0
derived_from_l5_and_r17_r24=true
static_registry_only=true
tool_behavior_implemented=false
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
1013R_R30_RENDER_SURFACE_CONNECTOR_PLAN_OR_VISUAL_TOOL_POLISH
```
"""
    write_text(OUT_DIR / "1013R_R29_report.md", report)


def main() -> None:
    result, evidence, errors = validate()
    write_outputs(result, evidence)
    if errors:
        raise SystemExit("FAIL: " + ", ".join(errors))
    print("PASS: 1013R_R29 tool frame registry")


if __name__ == "__main__":
    main()
