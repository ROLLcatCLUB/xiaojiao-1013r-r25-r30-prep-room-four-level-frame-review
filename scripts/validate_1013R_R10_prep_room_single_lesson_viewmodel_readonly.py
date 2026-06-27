from __future__ import annotations

import json
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))
STAGE_ID = "1013R_R10_PREP_ROOM_SINGLE_LESSON_VIEWMODEL_READONLY_ENDPOINT"
STAGE_DIR = ROOT / "outputs" / "PREP_ROOM_RENDER_CANVAS_DEEPEN_V1" / "1013R_R10_prep_room_single_lesson_viewmodel_readonly"
ROUTES_PATH = ROOT / "backend" / "xiaobei_ai" / "routes.py"


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
    from backend.xiaobei_ai import prep_room_single_lesson_viewmodel_1013R_R10 as endpoint

    errors: list[str] = []
    payload = endpoint.build_single_lesson_viewmodel()
    routes_text = ROUTES_PATH.read_text(encoding="utf-8", errors="ignore")

    if payload.get("stage") != STAGE_ID:
        fail(errors, "stage_id_mismatch")
    if payload.get("viewmodel_type") != "prep_room_single_lesson_readonly":
        fail(errors, "viewmodel_type_mismatch")
    if payload.get("route", {}).get("viewmodel") != "/api/prep-room/single-lesson-viewmodel/g3_u2_l1_color_gradient":
        fail(errors, "viewmodel_route_mismatch")
    if "prep_room_single_lesson_viewmodel_1013R_R10" not in routes_text:
        fail(errors, "route_module_not_imported")
    if "prep_room_single_lesson_viewmodel_1013R_R10.register_routes(bp, _cors_preflight)" not in routes_text:
        fail(errors, "route_module_not_registered")

    lesson = payload.get("prep_view_patch", {}).get("current_lesson", {})
    if lesson.get("title") != "2-1《色彩的渐变》":
        fail(errors, "lesson_title_not_real_textbook_anchor")
    render_payload = {
        "task_object": payload.get("task_object", {}),
        "prep_view_patch": payload.get("prep_view_patch", {}),
        "courseware_screen_patch": payload.get("courseware_screen_patch", []),
    }
    if "色彩的感觉" in json.dumps(render_payload, ensure_ascii=False):
        fail(errors, "deprecated_lesson_title_leaked_into_render_viewmodel")
    if len(lesson.get("flow", [])) < 6:
        fail(errors, "lesson_flow_missing")
    if len(lesson.get("sections", [])) < 7:
        fail(errors, "lesson_sections_too_few")
    if len(lesson.get("process_steps", [])) < 5:
        fail(errors, "process_steps_too_few")
    if len(payload.get("courseware_screen_patch", [])) < 8:
        fail(errors, "courseware_screen_patch_too_few")
    if len(payload.get("prep_view_patch", {}).get("lesson_tree", [])) < 8:
        fail(errors, "lesson_tree_too_small")

    boundary = payload.get("boundary", {})
    blocked_true_flags = [
        "provider_called",
        "model_called",
        "database_written",
        "memory_written",
        "vector_index_written",
        "feishu_written",
        "formal_apply_performed",
        "R36_modified",
        "main_shell_modified",
        "runtime_write_allowed",
        "formal_frontend_binding_performed",
    ]
    for flag in blocked_true_flags:
        if boundary.get(flag):
            fail(errors, f"readonly_boundary_broken:{flag}")
    if not boundary.get("runtime_connected"):
        fail(errors, "runtime_connected_not_marked")
    if not boundary.get("single_lesson_viewmodel_readonly"):
        fail(errors, "single_lesson_viewmodel_readonly_not_marked")
    if payload.get("render_contract", {}).get("target_stage") != "existing_page_static_preview_hydration_next":
        fail(errors, "render_contract_target_mismatch")

    evidence = {
        "module": "backend.xiaobei_ai.prep_room_single_lesson_viewmodel_1013R_R10",
        "viewmodel_route": payload.get("route", {}).get("viewmodel"),
        "action_route": payload.get("route", {}).get("action"),
        "task_state_source": payload.get("route", {}).get("task_state_source"),
        "lesson_title": lesson.get("title"),
        "section_count": len(lesson.get("sections", [])),
        "process_step_count": len(lesson.get("process_steps", [])),
        "courseware_screen_count": len(payload.get("courseware_screen_patch", [])),
        "lesson_tree_unit_count": len(payload.get("prep_view_patch", {}).get("lesson_tree", [])),
        "registered_in_routes": "prep_room_single_lesson_viewmodel_1013R_R10.register_routes(bp, _cors_preflight)" in routes_text,
        "boundary": boundary,
    }
    result = {
        "stage_id": STAGE_ID,
        "status": "PASS" if not errors else "FAIL",
        "validator_pass": not errors,
        "created_at": now(),
        "checks": {
            "backend_endpoint_added": True,
            "route_registered": evidence["registered_in_routes"],
            "real_textbook_anchor": lesson.get("title") == "2-1《色彩的渐变》",
            "renderer_viewmodel_shape_ready": not any(
                code in errors
                for code in [
                    "lesson_flow_missing",
                    "lesson_sections_too_few",
                    "process_steps_too_few",
                    "courseware_screen_patch_too_few",
                ]
            ),
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
    write_json(STAGE_DIR / "1013R_R10_result.json", result)
    write_json(STAGE_DIR / "single_lesson_viewmodel_evidence_1013R_R10.json", evidence)
    report = f"""# 1013R_R10 prep-room single lesson ViewModel readonly endpoint

## 定位

本轮只把三年级第二单元第1课《色彩的渐变》的备课页数据沉到后端 ViewModel。

```text
stage_id={STAGE_ID}
route=/api/prep-room/single-lesson-viewmodel/g3_u2_l1_color_gradient
action_route=/api/prep-room/single-lesson-viewmodel/g3_u2_l1_color_gradient/action
R36_modified=false
main_shell_modified=false
provider_called=false
model_called=false
database_written=false
memory_written=false
vector_index_written=false
feishu_written=false
formal_apply_performed=false
```

## 渲染关系

- R9 仍是静态渲染页。
- R10 提供渲染页可消费的只读 ViewModel。
- 下一步页面副本应 fetch R10，而不是继续靠可见文字替换。

## 验证

```text
validator_pass={str(result["validator_pass"]).lower()}
failed_checks={result["failed_checks"]}
```
"""
    write_text(STAGE_DIR / "1013R_R10_report.md", report)


def main() -> None:
    result, evidence, errors = validate()
    write_outputs(result, evidence)
    if errors:
        raise SystemExit("FAIL: " + ", ".join(errors))
    print("PASS: 1013R_R10 prep room single lesson viewmodel readonly endpoint")


if __name__ == "__main__":
    main()
