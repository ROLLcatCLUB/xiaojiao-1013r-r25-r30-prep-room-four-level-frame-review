from __future__ import annotations

import json
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

STAGE_ID = "1013R_R15_PREP_ROOM_UNIFIED_VIEWMODEL_R0"
STAGE_DIR = (
    ROOT
    / "outputs"
    / "PREP_ROOM_RENDER_CANVAS_DEEPEN_V1"
    / "1013R_R15_prep_room_unified_viewmodel_r0"
)
DOC_PATH = ROOT / "docs" / "1013R_R15_prep_room_unified_viewmodel.md"


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
    from backend.xiaobei_ai import prep_room_unified_viewmodel_1013R_R15 as unified_module

    errors: list[str] = []
    bundle = unified_module.build_viewmodel_sample_bundle()
    viewmodel = bundle.get("unified_viewmodel", {})
    render_slots = bundle.get("render_slots", [])
    slots_by_id = {item.get("slot_id"): item for item in render_slots if isinstance(item, dict)}
    boundary = bundle.get("boundary", {})
    doc = DOC_PATH.read_text(encoding="utf-8", errors="ignore") if DOC_PATH.exists() else ""

    if bundle.get("stage") != STAGE_ID:
        fail(errors, "stage_id_mismatch")
    if viewmodel.get("stage") != STAGE_ID:
        fail(errors, "viewmodel_stage_mismatch")
    if viewmodel.get("viewmodel_type") != "prep_room_unified_readonly_contract_viewmodel":
        fail(errors, "viewmodel_type_mismatch")
    if viewmodel.get("current_object", {}).get("title") != "2-1《色彩的渐变》":
        fail(errors, "current_object_not_preserved")

    required_top_fields = [
        "current_object",
        "lesson_viewmodel",
        "task_state",
        "action_gate",
        "render_surface_map",
        "render_slots",
        "source_policy",
        "renderer_contract",
        "boundary",
    ]
    for field in required_top_fields:
        if field not in viewmodel:
            fail(errors, f"top_field_missing:{field}")

    contracts = viewmodel.get("contracts_consumed", {})
    if contracts.get("r10_stage") != "1013R_R10_PREP_ROOM_SINGLE_LESSON_VIEWMODEL_READONLY_ENDPOINT":
        fail(errors, "r10_stage_not_consumed")
    if contracts.get("r13_contract_id") != "SHIWEI_TASK_STATE_CONTRACT_R0":
        fail(errors, "r13_contract_not_consumed")
    if contracts.get("r14_contract_id") != "SHIWEI_TEACHER_ACTION_GATE_CONTRACT_R0":
        fail(errors, "r14_contract_not_consumed")

    required_slots = [
        "current_object_card",
        "xiaojiao_task_state",
        "lesson_body",
        "teaching_process",
        "teacher_demo",
        "courseware_script",
        "classroom_display_screen",
        "worksheet",
        "assessment_rubric",
        "blackboard_design",
        "materials_list",
        "source_evidence",
        "confirm_actions",
        "bottom_composer",
    ]
    for slot_id in required_slots:
        if slot_id not in slots_by_id:
            fail(errors, f"render_slot_missing:{slot_id}")
    if len(render_slots) < 14:
        fail(errors, "render_slots_too_few")

    if "lesson_viewmodel.courseware_screens" not in slots_by_id.get("courseware_script", {}).get("payload_refs", []):
        fail(errors, "courseware_slot_payload_ref_missing")
    if "lesson_viewmodel.courseware_screens" not in slots_by_id.get("classroom_display_screen", {}).get("payload_refs", []):
        fail(errors, "display_slot_payload_ref_missing")
    if not slots_by_id.get("courseware_script", {}).get("available_actions"):
        fail(errors, "courseware_slot_actions_missing")
    if not slots_by_id.get("classroom_display_screen", {}).get("available_actions"):
        fail(errors, "display_slot_actions_missing")
    assessment_actions = slots_by_id.get("assessment_rubric", {}).get("available_actions", [])
    if not assessment_actions or any(item.get("allowed_now") for item in assessment_actions):
        fail(errors, "assessment_slot_should_only_have_blocked_actions")

    source_categories = set(viewmodel.get("source_policy", {}).get("source_categories", []))
    for category in ["textbook_anchor", "teacher_input", "ai_draft", "system_structure"]:
        if category not in source_categories:
            fail(errors, f"source_category_missing:{category}")
    if not viewmodel.get("source_policy", {}).get("ai_draft_may_not_be_standard"):
        fail(errors, "ai_draft_policy_missing")

    renderer_contract = viewmodel.get("renderer_contract", {})
    if not renderer_contract.get("single_entry"):
        fail(errors, "renderer_contract_not_single_entry")
    for field in required_top_fields:
        if field == "renderer_contract":
            continue
        if field not in renderer_contract.get("renderer_should_consume", []):
            fail(errors, f"renderer_should_consume_missing:{field}")
    for token in ["read_legacy_hydration_payload", "replace_visible_text_by_walker", "formal_apply"]:
        if token not in renderer_contract.get("renderer_must_not", []):
            fail(errors, f"renderer_must_not_missing:{token}")

    primary_render_text = json.dumps(
        {
            "current_object": viewmodel.get("current_object", {}),
            "lesson_viewmodel": viewmodel.get("lesson_viewmodel", {}),
            "task_state": viewmodel.get("task_state", {}),
            "render_slots": render_slots,
        },
        ensure_ascii=False,
    )
    for title in ["穿穿编编", "色彩的感觉"]:
        if title in primary_render_text:
            fail(errors, f"deprecated_title_leaked_into_unified_viewmodel:{title}")

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
        "route_registered",
    ]
    for flag in blocked_true_flags:
        if boundary.get(flag):
            fail(errors, f"readonly_boundary_broken:{flag}")
    if not boundary.get("unified_viewmodel_readonly"):
        fail(errors, "unified_viewmodel_readonly_not_marked")
    if not boundary.get("unified_viewmodel_defined"):
        fail(errors, "unified_viewmodel_defined_not_marked")

    if not DOC_PATH.exists():
        fail(errors, "r15_doc_missing")
    for token in ["prep_room_unified_readonly_contract_viewmodel", "render_slots", "formal_apply_performed=false"]:
        if token not in doc:
            fail(errors, f"r15_doc_token_missing:{token}")

    evidence = {
        "module": "backend.xiaobei_ai.prep_room_unified_viewmodel_1013R_R15",
        "viewmodel_type": viewmodel.get("viewmodel_type"),
        "current_object": viewmodel.get("current_object"),
        "contracts_consumed": contracts,
        "render_slot_count": len(render_slots),
        "source_categories": sorted(source_categories),
        "courseware_slot_actions": slots_by_id.get("courseware_script", {}).get("available_actions", []),
        "display_slot_actions": slots_by_id.get("classroom_display_screen", {}).get("available_actions", []),
        "assessment_slot_actions": assessment_actions,
        "renderer_contract": renderer_contract,
        "boundary": boundary,
    }
    result = {
        "stage_id": STAGE_ID,
        "status": "PASS" if not errors else "FAIL",
        "validator_pass": not errors,
        "created_at": now(),
        "checks": {
            "unified_viewmodel_defined": viewmodel.get("viewmodel_type")
            == "prep_room_unified_readonly_contract_viewmodel",
            "real_textbook_object_preserved": viewmodel.get("current_object", {}).get("title") == "2-1《色彩的渐变》",
            "contracts_consumed": not any(
                code in errors
                for code in ["r10_stage_not_consumed", "r13_contract_not_consumed", "r14_contract_not_consumed"]
            ),
            "render_slots_complete": len(render_slots) >= 14,
            "courseware_and_display_slots_bound": not any(
                code in errors
                for code in [
                    "courseware_slot_payload_ref_missing",
                    "display_slot_payload_ref_missing",
                    "courseware_slot_actions_missing",
                    "display_slot_actions_missing",
                ]
            ),
            "source_policy_embedded": all(
                category in source_categories for category in ["textbook_anchor", "teacher_input", "ai_draft", "system_structure"]
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
    from backend.xiaobei_ai import prep_room_unified_viewmodel_1013R_R15 as unified_module

    bundle = unified_module.build_viewmodel_sample_bundle()
    write_json(STAGE_DIR / "1013R_R15_result.json", result)
    write_json(STAGE_DIR / "prep_room_unified_viewmodel_sample_1013R_R15.json", bundle["unified_viewmodel"])
    write_json(STAGE_DIR / "render_slots_1013R_R15.json", bundle["render_slots"])
    write_json(STAGE_DIR / "prep_room_unified_viewmodel_evidence_1013R_R15.json", evidence)
    report = f"""# 1013R_R15 prep-room unified ViewModel

## 定位

本轮把 R10 lesson ViewModel、R13 小教任务状态合同、R14 教师确认门合同合成一份只读统一 ViewModel。

```text
stage_id={STAGE_ID}
viewmodel_type=prep_room_unified_readonly_contract_viewmodel
current_object=三年级第二单元第1课《色彩的渐变》
R36_modified=false
main_shell_modified=false
route_registered=false
provider_called=false
model_called=false
database_written=false
memory_written=false
vector_index_written=false
feishu_written=false
formal_apply_performed=false
```

## 已定义

- 页面未来可消费的单入口 ViewModel。
- 14 个 render_slots 的 payload/action/source 绑定。
- lesson_viewmodel、task_state、action_gate、source_policy 的顶层结构。
- renderer_should_consume 和 renderer_must_not。

## 验证

```text
validator_pass={str(result["validator_pass"]).lower()}
failed_checks={result["failed_checks"]}
```

## 下一步

```text
1013R_R16_SOURCE_POLICY_LIGHT_VALIDATOR_R0
```
"""
    write_text(STAGE_DIR / "1013R_R15_report.md", report)


def main() -> None:
    result, evidence, errors = validate()
    write_outputs(result, evidence)
    if errors:
        raise SystemExit("FAIL: " + ", ".join(errors))
    print("PASS: 1013R_R15 prep room unified viewmodel")


if __name__ == "__main__":
    main()
