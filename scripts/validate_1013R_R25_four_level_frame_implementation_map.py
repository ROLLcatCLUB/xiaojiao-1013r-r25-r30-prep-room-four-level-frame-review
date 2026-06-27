from __future__ import annotations

import json
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

STAGE_ID = "1013R_R25_FOUR_LEVEL_FRAME_IMPLEMENTATION_MAP"
OUT_DIR = ROOT / "outputs" / "PREP_ROOM_RENDER_CANVAS_DEEPEN_V1" / "1013R_R25_four_level_frame_implementation_map"
DOC_PATH = ROOT / "docs" / "1013R_R25_four_level_frame_implementation_map.md"


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
    from backend.xiaobei_ai import prep_room_four_level_frame_implementation_map_1013R_R25 as module

    errors: list[str] = []
    bundle = module.build_implementation_sample_bundle()
    frame_map = bundle.get("implementation_map", {})
    levels = frame_map.get("levels", [])
    boundary = frame_map.get("boundary", {})
    decisions = frame_map.get("asset_decisions", [])
    doc = DOC_PATH.read_text(encoding="utf-8", errors="ignore") if DOC_PATH.exists() else ""

    if bundle.get("stage") != STAGE_ID:
        fail(errors, "stage_id_mismatch")
    if frame_map.get("map_id") != "SHIWEI_FOUR_LEVEL_FRAME_IMPLEMENTATION_MAP_R0":
        fail(errors, "map_id_mismatch")
    if frame_map.get("framework_reference") != "docs/1013R_product_frame_four_level.md":
        fail(errors, "framework_reference_missing")
    if len(levels) != 4:
        fail(errors, "four_levels_not_defined")
    if [item.get("level_key") for item in levels] != [
        "platform_shell",
        "room_workspace",
        "tool_frame",
        "content_rendering",
    ]:
        fail(errors, "level_order_mismatch")

    consumes = frame_map.get("consumes", {})
    expected_consumes = {
        "l0_shell_registry_stage": "1013L_R0_MAIN_RENDER_SHELL_BASELINE_AND_BACKEND_REUSE_REGISTRY",
        "l5_shell_adapter_stage": "1013L_R5_MAIN_SHELL_BACKEND_VIEWMODEL_READONLY_FETCH_ADAPTER",
        "r17_render_blocks_stage": "1013R_R17_RENDER_BLOCKS_PROTOCOL_R0",
        "r21_page_binding_stage": "1013R_R21_PAGE_COPY_BINDS_UNIFIED_PACKAGE",
        "r24_component_boundary_stage": "1013R_R24_RENDER_BLOCK_COMPONENT_BOUNDARY_MAP",
    }
    for key, value in expected_consumes.items():
        if consumes.get(key) != value:
            fail(errors, f"consume_stage_mismatch:{key}")

    decision_ids = {item.get("asset_id") for item in decisions}
    for asset_id in [
        "1013L_shell_registry_and_fetch_adapter",
        "1013R_unified_package_render_blocks_component_boundary",
        "1013R_R21_current_page_copy",
        "1013K_big_unit_and_courseware_assets",
        "platform_core_render_blocks_0954C",
        "system_semantic_interaction_runtime",
        "frontend_workbench_legacy_assets",
        "openclaw_history_and_scans",
    ]:
        if asset_id not in decision_ids:
            fail(errors, f"asset_decision_missing:{asset_id}")

    history = frame_map.get("history_viewer_intake", {})
    if history.get("used_for") != "asset_index_and_scan_clues_only":
        fail(errors, "history_viewer_not_limited_to_index")
    if "product_truth" not in history.get("not_used_for", []):
        fail(errors, "history_viewer_product_truth_guard_missing")

    routing = frame_map.get("routing_principles", {})
    for key in [
        "route_intent_by_framework_level",
        "diagnose_issues_by_framework_level",
        "assign_features_by_framework_level",
        "implement_recursively_by_framework_level",
    ]:
        if routing.get(key) is not True:
            fail(errors, f"routing_principle_missing:{key}")

    blocked_true_flags = [
        "openclaw_runtime_imported",
        "openclaw_memory_imported",
        "page_dom_modified",
        "prototype_copy_created",
        "new_disconnected_page_created",
        "route_registered",
        "endpoint_registered",
        "component_implementation_created",
        "R36_modified",
        "main_shell_modified",
        "existing_page_modified",
        "runtime_connected",
        "provider_called",
        "model_called",
        "database_written",
        "memory_written",
        "vector_index_written",
        "feishu_written",
        "formal_apply_performed",
    ]
    for flag in blocked_true_flags:
        if boundary.get(flag):
            fail(errors, f"readonly_boundary_broken:{flag}")
    if boundary.get("four_level_frame_implementation_map_defined") is not True:
        fail(errors, "implementation_map_boundary_not_marked")

    for token in [
        "history_viewer_used_as_index_only=true",
        "OpenClaw_runtime_imported=false",
        "new_disconnected_page_created=false",
        "R26：在当前 R21 页面副本内加四级框架标记",
        "R28 各室注册表必须从 1013L 的已有状态派生",
        "OpenClaw history/scans -> 只作归档索引",
    ]:
        if token not in doc:
            fail(errors, f"doc_token_missing:{token}")

    evidence = {
        "module": "backend.xiaobei_ai.prep_room_four_level_frame_implementation_map_1013R_R25",
        "map_id": frame_map.get("map_id"),
        "level_count": len(levels),
        "asset_decision_count": len(decisions),
        "implementation_sequence": frame_map.get("implementation_sequence"),
        "boundary": boundary,
    }
    result = {
        "stage_id": STAGE_ID,
        "status": "PASS" if not errors else "FAIL",
        "validator_pass": not errors,
        "created_at": now(),
        "checks": {
            "implementation_map_defined": frame_map.get("map_id") == "SHIWEI_FOUR_LEVEL_FRAME_IMPLEMENTATION_MAP_R0",
            "four_levels_defined": len(levels) == 4,
            "existing_bottom_assets_reused": not any(code.startswith("asset_decision_missing") for code in errors),
            "history_viewer_index_only": history.get("used_for") == "asset_index_and_scan_clues_only",
            "no_disconnected_page_created": boundary.get("new_disconnected_page_created") is False,
            "no_openclaw_runtime_import": boundary.get("openclaw_runtime_imported") is False,
            "no_runtime_or_provider": boundary.get("runtime_connected") is False and boundary.get("provider_called") is False,
            "formal_apply_performed": False,
        },
        "failed_checks": errors,
    }
    return result, evidence, errors


def write_outputs(result: dict[str, Any], evidence: dict[str, Any]) -> None:
    from backend.xiaobei_ai import prep_room_four_level_frame_implementation_map_1013R_R25 as module

    bundle = module.build_implementation_sample_bundle()
    write_json(OUT_DIR / "1013R_R25_result.json", result)
    write_json(OUT_DIR / "four_level_frame_implementation_map_1013R_R25.json", bundle["implementation_map"])
    write_json(OUT_DIR / "asset_decisions_1013R_R25.json", bundle["asset_decisions"])
    write_json(OUT_DIR / "implementation_sequence_1013R_R25.json", bundle["implementation_sequence"])
    write_json(OUT_DIR / "implementation_evidence_1013R_R25.json", evidence)
    report = f"""# 1013R_R25 four level frame implementation map

```text
stage_id={STAGE_ID}
map_id=SHIWEI_FOUR_LEVEL_FRAME_IMPLEMENTATION_MAP_R0
history_viewer_used_as_index_only=true
openclaw_runtime_imported=false
openclaw_memory_imported=false
new_disconnected_page_created=false
R36_modified=false
route_registered=false
endpoint_registered=false
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
1013R_R26_PAGE_COPY_FOUR_LEVEL_FRAME_MARKERS
```
"""
    write_text(OUT_DIR / "1013R_R25_report.md", report)


def main() -> None:
    result, evidence, errors = validate()
    write_outputs(result, evidence)
    if errors:
        raise SystemExit("FAIL: " + ", ".join(errors))
    print("PASS: 1013R_R25 four level frame implementation map")


if __name__ == "__main__":
    main()
