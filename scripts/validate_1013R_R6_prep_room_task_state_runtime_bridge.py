from __future__ import annotations

import json
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

STAGE_ID = "1013R_R6_PREP_ROOM_OLD_MATERIAL_RUNTIME_BRIDGE"
STAGE_DIR = ROOT / "outputs" / "PREP_ROOM_RENDER_CANVAS_DEEPEN_V1" / "1013R_R6_prep_room_old_material_runtime_bridge"


def now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def write_json(path: Path, payload: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def fail(errors: list[str], message: str) -> None:
    errors.append(message)


def run_flask_smoke() -> dict[str, Any]:
    from flask import Flask  # noqa: PLC0415
    from backend.xiaobei_ai.routes import create_blueprint  # noqa: PLC0415
    from backend.xiaobei_ai import prep_room_task_state_bridge_1013R_R6 as bridge  # noqa: PLC0415

    app = Flask("prep_room_task_state_runtime_bridge_smoke")
    app.register_blueprint(create_blueprint())
    rules = sorted(str(rule.rule) for rule in app.url_map.iter_rules())
    with app.test_client() as client:
        get_response = client.get(bridge.TASK_ROUTE)
        get_payload = get_response.get_json(silent=True) or {}
        post_response = client.post(bridge.ACTION_ROUTE, json={"action_id": "confirm_real_textbook_anchor"})
        post_payload = post_response.get_json(silent=True) or {}
    return {
        "flask_test_client_used": True,
        "http_server_started": False,
        "task_route": bridge.TASK_ROUTE,
        "action_route": bridge.ACTION_ROUTE,
        "task_route_registered": bridge.TASK_ROUTE in rules,
        "action_route_registered": bridge.ACTION_ROUTE in rules,
        "url_rule_count": len(rules),
        "get_status_code": get_response.status_code,
        "get_ok": get_payload.get("ok") is True,
        "get_stage": get_payload.get("stage"),
        "get_title": (get_payload.get("task_object") or {}).get("title"),
        "post_status_code": post_response.status_code,
        "post_ok": post_payload.get("ok") is True,
        "post_stage": post_payload.get("stage"),
        "post_write_allowed": ((post_payload.get("state_patch_preview") or {}).get("write_allowed")),
    }


def validate() -> tuple[dict[str, Any], dict[str, Any], list[str]]:
    from backend.xiaobei_ai import prep_room_task_state_bridge_1013R_R6 as bridge  # noqa: PLC0415

    errors: list[str] = []
    task_state, task_status = bridge.handle_task_state_request()
    action_response, action_status = bridge.handle_action_request({"action_id": "confirm_real_textbook_anchor"})
    flask_smoke = run_flask_smoke()

    task_object = task_state.get("task_object") or {}
    base_context = task_state.get("base_context") or {}
    boundary = task_state.get("boundary") or {}
    current_task_text = json.dumps(
        {
            "task_object": task_state.get("task_object"),
            "known_materials": (task_state.get("xiaojiao_task_state") or {}).get("known_materials"),
            "lesson_chain": (base_context.get("lesson_chain") or []),
            "route": task_state.get("route"),
        },
        ensure_ascii=False,
    )
    state_text = json.dumps(task_state, ensure_ascii=False)

    if task_status != 200:
        fail(errors, "task_state_status_not_200")
    if task_state.get("stage") != STAGE_ID:
        fail(errors, "stage_id_mismatch")
    if task_state.get("runtime_mode") != "local_readonly_task_state_bridge":
        fail(errors, "runtime_mode_mismatch")
    if task_object.get("title") != "三年级《色彩的渐变》":
        fail(errors, "task_object_title_mismatch")
    if task_object.get("grade") != "三年级":
        fail(errors, "task_object_grade_mismatch")
    if task_object.get("unit_title") != "第二单元《多彩的世界》":
        fail(errors, "task_object_unit_title_mismatch")
    if task_object.get("textbook_page") != 6:
        fail(errors, "task_object_textbook_page_mismatch")
    if "g3_u2_color_gradient" not in (task_state.get("route") or {}).get("task_state", ""):
        fail(errors, "task_route_not_color_gradient")

    if "色彩的感觉" in current_task_text:
        fail(errors, "deprecated_color_feeling_leaked_into_current_task")
    if "穿穿编编" in current_task_text:
        fail(errors, "chuanchuanbianbian_leaked_into_current_task")

    textbook_catalog = (base_context.get("textbook_catalog") or {}).get("catalog") or []
    if len(textbook_catalog) < 10:
        fail(errors, "textbook_catalog_not_rearranged")
    if not any(item.get("unit_title") == "多彩的世界" for item in textbook_catalog):
        fail(errors, "catalog_missing_unit_multicolor_world")
    if not any(
        lesson.get("lesson_title") == "色彩的渐变"
        for unit in textbook_catalog
        for lesson in unit.get("lessons", [])
    ):
        fail(errors, "catalog_missing_color_gradient")
    if (base_context.get("knowledge_base_policy") or {}).get("textbook_images_in_kb_have_ocr") is not False:
        fail(errors, "kb_ocr_status_must_be_false")
    if (base_context.get("deprecation_notice") or {}).get("must_not_use_as_textbook_anchor") is not True:
        fail(errors, "deprecated_lesson_notice_missing")

    expected_true = [
        "old_material_runtime_bridge",
        "runtime_connected",
        "reuse_previous_material_first",
        "preview_only",
        "teacher_review_required",
        "textbook_catalog_rearranged",
        "ai_generated_source_reference_only",
    ]
    expected_false = [
        "new_system_created",
        "runtime_write_allowed",
        "textbook_ocr_available",
        "source_material_standard_alignment_allowed",
        "field_schema_standard_alignment_allowed",
        "provider_called",
        "model_called",
        "database_written",
        "memory_written",
        "vector_index_written",
        "feishu_written",
        "formal_apply_performed",
        "R36_modified",
        "main_shell_modified",
        "main_project_pushed",
    ]
    for key in expected_true:
        if boundary.get(key) is not True:
            fail(errors, f"{key}_must_be_true")
    for key in expected_false:
        if boundary.get(key) is not False:
            fail(errors, f"{key}_must_be_false")

    sources = task_state.get("source_matrix") or []
    source_ids = {item.get("source_id") for item in sources}
    for required_source in [
        "user_provided_g3_textbook_catalog_photo",
        "kb_g3_textbook_image_index_no_ocr",
        "work_plan_render_packet_0993B_real_catalog_hint",
        "kb_g3_u1_old_ai_gradient_unit_doc",
        "kb_g3_u1_old_ai_lesson2_pigment_gradient_reference",
        "legacy_color_feeling_static_to_deprecate",
    ]:
        if required_source not in source_ids:
            fail(errors, f"missing_source:{required_source}")
    if not any(item.get("authority_status") == "ai_generated_reference_only" for item in sources):
        fail(errors, "missing_ai_generated_reference_only_source")
    if not any(item.get("source_status") == "indexed_partial_no_ocr" for item in sources):
        fail(errors, "missing_no_ocr_textbook_index_source")

    if action_status != 200 or action_response.get("ok") is not True:
        fail(errors, "action_response_not_ok")
    if (action_response.get("state_patch_preview") or {}).get("write_allowed") is not False:
        fail(errors, "action_patch_write_allowed_not_false")
    if action_response.get("boundary", {}).get("formal_apply_performed") is not False:
        fail(errors, "action_formal_apply_not_false")

    for smoke_key in ["task_route_registered", "action_route_registered", "get_ok", "post_ok"]:
        if flask_smoke.get(smoke_key) is not True:
            fail(errors, f"flask_smoke_{smoke_key}_failed")
    if flask_smoke.get("get_title") != "三年级《色彩的渐变》":
        fail(errors, "flask_smoke_get_title_mismatch")
    if flask_smoke.get("post_write_allowed") is not False:
        fail(errors, "flask_smoke_post_write_allowed_not_false")

    result = {
        "stage_id": STAGE_ID,
        "status": "PASS" if not errors else "FAIL",
        "validator_pass": not errors,
        "created_at": now(),
        "task_object_title": task_object.get("title"),
        "route": {
            "task_state": bridge.TASK_ROUTE,
            "action": bridge.ACTION_ROUTE,
        },
        "checks": {
            "old_material_reused": True,
            "real_textbook_catalog_rearranged": boundary.get("textbook_catalog_rearranged") is True,
            "color_gradient_targeted": task_object.get("title") == "三年级《色彩的渐变》",
            "deprecated_color_feeling_blocked": "色彩的感觉" not in current_task_text,
            "new_system_created": False,
            "runtime_connected": boundary.get("runtime_connected") is True,
            "runtime_write_allowed": boundary.get("runtime_write_allowed") is True,
            "source_matrix_count": len(sources),
            "flask_route_smoke_pass": not any(
                not flask_smoke.get(key) for key in ["task_route_registered", "action_route_registered", "get_ok", "post_ok"]
            ),
        },
        "boundary_flags": boundary,
        "failed_checks": errors,
    }
    evidence = {
        "task_state": task_state,
        "action_response": action_response,
        "flask_smoke": flask_smoke,
        "catalog": textbook_catalog,
    }
    return result, evidence, errors


def write_catalog_markdown(catalog: list[dict[str, Any]]) -> str:
    lines = ["# 三年级教材目录重排 1013R_R6", "", "来源：用户本轮提供的三年级教材目录照片。知识库页图索引当前无 OCR。", ""]
    for unit in catalog:
        label = unit["unit_title"]
        unit_no = unit["unit_no"]
        heading = f"第{unit_no}单元 {label}" if isinstance(unit_no, int) else label
        lines.append(f"## {heading}")
        for lesson in unit.get("lessons", []):
            lesson_no = lesson["lesson_no"]
            if isinstance(lesson_no, int):
                lines.append(f"- 第{lesson_no}课 {lesson['lesson_title']} / {lesson['page']}")
            else:
                lines.append(f"- {lesson['lesson_title']} / {lesson['page']}")
        if unit.get("page_span"):
            lines.append(f"- 页段：{unit['page_span']}")
        lines.append("")
    return "\n".join(lines)


def write_outputs(result: dict[str, Any], evidence: dict[str, Any]) -> None:
    write_json(STAGE_DIR / "1013R_R6_result.json", result)
    write_json(STAGE_DIR / "runtime_task_state_1013R_R6.json", evidence["task_state"])
    write_json(STAGE_DIR / "runtime_action_preview_1013R_R6.json", evidence["action_response"])
    write_json(STAGE_DIR / "runtime_route_smoke_1013R_R6.json", evidence["flask_smoke"])
    write_json(STAGE_DIR / "g3_textbook_catalog_rearranged_1013R_R6.json", evidence["catalog"])
    write_text(STAGE_DIR / "g3_textbook_catalog_rearranged_1013R_R6.md", write_catalog_markdown(evidence["catalog"]))
    report = f"""# 1013R_R6 旧资料接 runtime 只读桥

## 定位

本轮纠正前一版伪课题：`色彩的感觉` 不在教师提供的三年级教材目录中。
当前 runtime 任务对象改为真实教材锚点：三年级第二单元《多彩的世界》第1课《色彩的渐变》。

```text
stage_id={STAGE_ID}
task_object=三年级《色彩的渐变》
route=/api/prep-room/task-state/g3_u2_color_gradient
old_material_reused=true
textbook_catalog_rearranged=true
textbook_ocr_available=false
new_system_created=false
runtime_connected={str(result['boundary_flags'].get('runtime_connected')).lower()}
runtime_write_allowed={str(result['boundary_flags'].get('runtime_write_allowed')).lower()}
provider_called=false
model_called=false
formal_apply_performed=false
```

## 资料口径

1. 教材目录以教师本轮提供的目录照片为准。
2. 本地知识库 `kb_art_g3_textbook_images_20260427.txt` 只有图片索引，明确未完成 OCR。
3. 旧 AI 教案、旧字段设计、旧《色彩的感觉》原型只能作为错误追踪或技法参考，不能作为标准。

## 验证

```text
validator_pass={str(result['validator_pass']).lower()}
failed_checks={result['failed_checks']}
```
"""
    write_text(STAGE_DIR / "1013R_R6_report.md", report)


def main() -> None:
    result, evidence, errors = validate()
    write_outputs(result, evidence)
    if errors:
        raise SystemExit("FAIL: " + ", ".join(errors))
    print("PASS: 1013R_R6 prep room real textbook color gradient runtime bridge")


if __name__ == "__main__":
    main()
