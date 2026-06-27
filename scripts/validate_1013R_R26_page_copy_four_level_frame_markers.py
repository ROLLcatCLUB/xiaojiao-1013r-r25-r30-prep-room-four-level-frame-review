from __future__ import annotations

import json
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

STAGE_ID = "1013R_R26_PAGE_COPY_FOUR_LEVEL_FRAME_MARKERS"
OUT_DIR = ROOT / "outputs" / "PREP_ROOM_RENDER_CANVAS_DEEPEN_V1" / "1013R_R26_page_copy_four_level_frame_markers"
DOC_PATH = ROOT / "docs" / "1013R_R26_page_copy_four_level_frame_markers.md"


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
    from backend.xiaobei_ai import prep_room_page_copy_four_level_markers_1013R_R26 as module
    from backend.xiaobei_ai import prep_room_page_copy_package_binding_1013R_R21 as r21_module

    errors: list[str] = []
    bundle = module.build_marker_sample_bundle()
    contract = bundle.get("marker_contract", {})
    boundary = bundle.get("boundary", {})
    targets = bundle.get("marker_targets", [])
    html = r21_module.build_binding_sample_bundle().get("html", "")
    doc = DOC_PATH.read_text(encoding="utf-8", errors="ignore") if DOC_PATH.exists() else ""

    if bundle.get("stage") != STAGE_ID:
        fail(errors, "stage_id_mismatch")
    if contract.get("marker_id") != "SHIWEI_PAGE_COPY_FOUR_LEVEL_FRAME_MARKERS_R0":
        fail(errors, "marker_id_mismatch")
    if contract.get("consumes", {}).get("r25_stage") != "1013R_R25_FOUR_LEVEL_FRAME_IMPLEMENTATION_MAP":
        fail(errors, "r25_not_consumed")
    if contract.get("consumes", {}).get("r21_stage") != "1013R_R21_PAGE_COPY_BINDS_UNIFIED_PACKAGE":
        fail(errors, "r21_not_consumed")
    if len(targets) != 4:
        fail(errors, "marker_targets_not_four_levels")
    if [item.get("level_key") for item in targets] != ["platform_shell", "room_workspace", "tool_frame", "content_rendering"]:
        fail(errors, "marker_target_order_mismatch")

    required_html_tokens = [
        "const FRAME_STAGE_ID = \"1013R_R26_PAGE_COPY_FOUR_LEVEL_FRAME_MARKERS\"",
        "function markFrameElement",
        "function markFrameElements",
        "function markFourLevelFrames",
        "data-shiwei-four-level-frame",
        "data-shiwei-four-level-stage",
        "data-shiwei-frame-route-rule",
        "data-shiwei-current-room",
        "data-shiwei-current-room-label",
        "data-shiwei-frame-level",
        "data-shiwei-frame-key",
        "data-shiwei-frame-role",
        "__SHIWEI_FOUR_LEVEL_FRAME_MARKERS__",
        "platform_shell",
        "prep_room_workspace",
        "prep_room_side_tool_frame",
        "content_rendering",
        "markFourLevelFrames();",
        "window.setTimeout(markFourLevelFrames",
    ]
    for token in required_html_tokens:
        if token not in html:
            fail(errors, f"html_marker_token_missing:{token}")

    required_contract_attributes = {
        "data-shiwei-four-level-frame",
        "data-shiwei-four-level-stage",
        "data-shiwei-frame-route-rule",
        "data-shiwei-current-room",
        "data-shiwei-frame-level",
        "data-shiwei-frame-key",
        "data-shiwei-frame-role",
        "data-shiwei-frame-stage",
    }
    if not required_contract_attributes.issubset(set(contract.get("marker_data_attributes", []))):
        fail(errors, "marker_data_attributes_incomplete")

    blocked_true_flags = [
        "visible_layout_modified",
        "new_disconnected_page_created",
        "route_registered",
        "endpoint_registered",
        "component_implementation_created",
        "R36_modified",
        "main_shell_modified",
        "source_prototype_modified",
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
    if boundary.get("runtime_dom_data_markers_added") is not True:
        fail(errors, "runtime_dom_data_markers_not_marked")
    if boundary.get("page_copy_four_level_markers_defined") is not True:
        fail(errors, "page_copy_marker_boundary_not_marked")

    for token in [
        "runtime_dom_data_markers_added=true",
        "visible_layout_modified=false",
        "new_disconnected_page_created=false",
        "R36_modified=false",
        "1013R_R27_XIAOJIAO_INTENT_FRAME_ROUTER_FIXTURE",
    ]:
        if token not in doc:
            fail(errors, f"doc_token_missing:{token}")

    evidence = {
        "module": "backend.xiaobei_ai.prep_room_page_copy_four_level_markers_1013R_R26",
        "marker_id": contract.get("marker_id"),
        "target_count": len(targets),
        "marker_data_attributes": contract.get("marker_data_attributes"),
        "html_checks": contract.get("html_checks"),
        "boundary": boundary,
    }
    result = {
        "stage_id": STAGE_ID,
        "status": "PASS" if not errors else "FAIL",
        "validator_pass": not errors,
        "created_at": now(),
        "checks": {
            "marker_contract_defined": contract.get("marker_id") == "SHIWEI_PAGE_COPY_FOUR_LEVEL_FRAME_MARKERS_R0",
            "r21_html_contains_marker_logic": not any(code.startswith("html_marker_token_missing") for code in errors),
            "four_marker_levels_defined": len(targets) == 4,
            "runtime_dom_data_markers_added": boundary.get("runtime_dom_data_markers_added") is True,
            "no_visible_layout_modified": boundary.get("visible_layout_modified") is False,
            "no_disconnected_page_created": boundary.get("new_disconnected_page_created") is False,
            "formal_apply_performed": False,
        },
        "failed_checks": errors,
    }
    return result, evidence, errors


def write_outputs(result: dict[str, Any], evidence: dict[str, Any]) -> None:
    from backend.xiaobei_ai import prep_room_page_copy_four_level_markers_1013R_R26 as module

    bundle = module.build_marker_sample_bundle()
    write_json(OUT_DIR / "1013R_R26_result.json", result)
    write_json(OUT_DIR / "page_copy_four_level_marker_contract_1013R_R26.json", bundle["marker_contract"])
    write_json(OUT_DIR / "page_copy_four_level_marker_targets_1013R_R26.json", bundle["marker_targets"])
    write_json(OUT_DIR / "page_copy_four_level_marker_evidence_1013R_R26.json", evidence)
    report = f"""# 1013R_R26 page copy four level frame markers

```text
stage_id={STAGE_ID}
marker_id=SHIWEI_PAGE_COPY_FOUR_LEVEL_FRAME_MARKERS_R0
runtime_dom_data_markers_added=true
visible_layout_modified=false
new_disconnected_page_created=false
R36_modified=false
main_shell_modified=false
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
1013R_R27_XIAOJIAO_INTENT_FRAME_ROUTER_FIXTURE
```
"""
    write_text(OUT_DIR / "1013R_R26_report.md", report)


def main() -> None:
    result, evidence, errors = validate()
    write_outputs(result, evidence)
    if errors:
        raise SystemExit("FAIL: " + ", ".join(errors))
    print("PASS: 1013R_R26 page copy four level frame markers")


if __name__ == "__main__":
    main()
