from __future__ import annotations

import json
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

STAGE_ID = "1013R_R13_XIAOJIAO_TASK_STATE_CONTRACT_AND_RENDER_SURFACE_MAP"
STAGE_DIR = (
    ROOT
    / "outputs"
    / "PREP_ROOM_RENDER_CANVAS_DEEPEN_V1"
    / "1013R_R13_xiaojiao_task_state_contract_and_render_surface_map"
)
DOC_CONTRACT_PATH = ROOT / "docs" / "1013R_R13_xiaojiao_task_state_contract.md"
DOC_SURFACE_MAP_PATH = ROOT / "docs" / "prep-room-render-surface-map.md"


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
    from backend.xiaobei_ai import prep_room_task_state_contract_1013R_R13 as contract_module

    errors: list[str] = []
    bundle = contract_module.build_contract_sample_bundle()
    contract = bundle.get("task_state_contract", {})
    surface_map = bundle.get("render_surface_map", [])
    surface_by_id = {item.get("slot_id"): item for item in surface_map if isinstance(item, dict)}
    boundary = bundle.get("boundary", {})
    contract_doc = DOC_CONTRACT_PATH.read_text(encoding="utf-8", errors="ignore") if DOC_CONTRACT_PATH.exists() else ""
    surface_doc = DOC_SURFACE_MAP_PATH.read_text(encoding="utf-8", errors="ignore") if DOC_SURFACE_MAP_PATH.exists() else ""

    if bundle.get("stage") != STAGE_ID:
        fail(errors, "stage_id_mismatch")
    if contract.get("stage") != STAGE_ID:
        fail(errors, "contract_stage_mismatch")
    if contract.get("contract_id") != "SHIWEI_TASK_STATE_CONTRACT_R0":
        fail(errors, "contract_id_mismatch")
    if contract.get("space", {}).get("id") != "prep_room":
        fail(errors, "space_not_prep_room")
    if contract.get("current_object", {}).get("title") != "2-1《色彩的渐变》":
        fail(errors, "current_object_not_real_textbook_lesson")
    forbidden_titles = ["穿穿编编", "色彩的感觉"]
    primary_render_payload = {
        "current_object": contract.get("current_object", {}),
        "task_state": contract.get("task_state", {}),
        "known_materials": contract.get("known_materials", []),
        "preview_candidates": contract.get("preview_candidates", []),
        "teacher_confirm_actions": contract.get("teacher_confirm_actions", []),
        "render_surface_map": surface_map,
    }
    primary_render_text = json.dumps(primary_render_payload, ensure_ascii=False)
    for title in forbidden_titles:
        if title in primary_render_text:
            fail(errors, f"deprecated_title_leaked_into_primary_render_contract:{title}")

    required_contract_fields = [
        "space",
        "current_object",
        "task_state",
        "known_materials",
        "missing_materials",
        "preview_candidates",
        "teacher_confirm_actions",
        "blocked_actions",
        "render_surface_map",
        "source_policy_notes",
        "audit_receipt",
    ]
    for field in required_contract_fields:
        if field not in contract:
            fail(errors, f"contract_field_missing:{field}")

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
        if slot_id not in surface_by_id:
            fail(errors, f"render_slot_missing:{slot_id}")

    if len(surface_map) < 14:
        fail(errors, "render_surface_map_too_small")
    if surface_by_id.get("courseware_script", {}).get("slot_id") == surface_by_id.get("classroom_display_screen", {}).get("slot_id"):
        fail(errors, "courseware_and_display_not_separated")
    if surface_by_id.get("courseware_script", {}).get("human_name") == surface_by_id.get("classroom_display_screen", {}).get("human_name"):
        fail(errors, "courseware_and_display_names_not_separated")
    if surface_by_id.get("assessment_rubric", {}).get("action_gate") != "blocked_until_teacher_dimension":
        fail(errors, "assessment_rubric_not_blocked_without_dimension")

    if len(contract.get("known_materials", [])) < 5:
        fail(errors, "known_materials_too_few")
    missing_ids = {item.get("id") for item in contract.get("missing_materials", [])}
    for missing_id in ["student_work_samples", "assessment_dimensions", "official_textbook_ocr", "classroom_constraints"]:
        if missing_id not in missing_ids:
            fail(errors, f"missing_material_not_declared:{missing_id}")
    candidate_ids = {item.get("id") for item in contract.get("preview_candidates", [])}
    for candidate_id in [
        "preview_lesson_body_refinement",
        "preview_courseware_script",
        "preview_display_screen",
        "preview_worksheet",
        "preview_assessment_rubric",
    ]:
        if candidate_id not in candidate_ids:
            fail(errors, f"preview_candidate_missing:{candidate_id}")

    blocked_ids = {item.get("id") for item in contract.get("blocked_actions", [])}
    for blocked_id in [
        "formal_save_to_lesson_package",
        "write_student_assessment",
        "export_courseware_file",
        "write_memory_or_archive",
    ]:
        if blocked_id not in blocked_ids:
            fail(errors, f"blocked_action_missing:{blocked_id}")

    source_categories = {item.get("category") for item in contract.get("source_policy_notes", [])}
    for category in ["textbook_anchor", "teacher_input", "ai_draft", "system_structure"]:
        if category not in source_categories:
            fail(errors, f"source_policy_category_missing:{category}")

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
    if not boundary.get("task_state_contract_readonly"):
        fail(errors, "task_state_contract_readonly_not_marked")
    if not boundary.get("render_surface_map_defined"):
        fail(errors, "render_surface_map_defined_not_marked")

    if not DOC_CONTRACT_PATH.exists():
        fail(errors, "contract_doc_missing")
    if not DOC_SURFACE_MAP_PATH.exists():
        fail(errors, "surface_map_doc_missing")
    for token in ["SHIWEI_TASK_STATE_CONTRACT_R0", "2-1《色彩的渐变》", "formal_apply_performed=false"]:
        if token not in contract_doc:
            fail(errors, f"contract_doc_token_missing:{token}")
    for token in ["courseware_script", "classroom_display_screen", "assessment_rubric", "bottom_composer"]:
        if token not in surface_doc:
            fail(errors, f"surface_doc_token_missing:{token}")

    evidence = {
        "module": "backend.xiaobei_ai.prep_room_task_state_contract_1013R_R13",
        "contract_id": contract.get("contract_id"),
        "current_object": contract.get("current_object"),
        "task_state": contract.get("task_state"),
        "known_material_count": len(contract.get("known_materials", [])),
        "missing_material_count": len(contract.get("missing_materials", [])),
        "preview_candidate_count": len(contract.get("preview_candidates", [])),
        "teacher_confirm_action_count": len(contract.get("teacher_confirm_actions", [])),
        "blocked_action_count": len(contract.get("blocked_actions", [])),
        "render_surface_slot_count": len(surface_map),
        "required_slots_present": all(slot_id in surface_by_id for slot_id in required_slots),
        "courseware_and_display_separated": (
            surface_by_id.get("courseware_script", {}).get("human_name")
            != surface_by_id.get("classroom_display_screen", {}).get("human_name")
        ),
        "boundary": boundary,
    }
    result = {
        "stage_id": STAGE_ID,
        "status": "PASS" if not errors else "FAIL",
        "validator_pass": not errors,
        "created_at": now(),
        "checks": {
            "task_state_contract_defined": contract.get("contract_id") == "SHIWEI_TASK_STATE_CONTRACT_R0",
            "real_textbook_object_preserved": contract.get("current_object", {}).get("title") == "2-1《色彩的渐变》",
            "render_surface_map_defined": len(surface_map) >= 14,
            "major_derivative_slots_present": all(
                slot_id in surface_by_id
                for slot_id in ["courseware_script", "classroom_display_screen", "worksheet", "assessment_rubric"]
            ),
            "courseware_and_display_separated": evidence["courseware_and_display_separated"],
            "source_policy_categories_embedded": all(
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
    from backend.xiaobei_ai import prep_room_task_state_contract_1013R_R13 as contract_module

    bundle = contract_module.build_contract_sample_bundle()
    write_json(STAGE_DIR / "1013R_R13_result.json", result)
    write_json(STAGE_DIR / "task_state_contract_sample_1013R_R13.json", bundle["task_state_contract"])
    write_json(STAGE_DIR / "render_surface_map_1013R_R13.json", bundle["render_surface_map"])
    write_json(STAGE_DIR / "task_state_contract_evidence_1013R_R13.json", evidence)
    report = f"""# 1013R_R13 Xiaojiao task-state contract and render surface map

## 定位

本轮定义小教任务状态合同和备课室内部渲染位索引。

```text
stage_id={STAGE_ID}
contract_id=SHIWEI_TASK_STATE_CONTRACT_R0
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

- 小教当前任务状态。
- 已知材料、缺口、预览候选、教师确认动作、阻断动作。
- 备课室 14 个主要渲染位。
- 大屏呈现与课件脚本分离。
- 教材依据、教师输入、AI 草案、系统结构的来源标签。

## 不做

- 不做完整渲染底座。
- 不注册新 route。
- 不写数据库、记忆、向量或飞书。
- 不调用模型或 provider。
- 不 formal apply。

## 验证

```text
validator_pass={str(result["validator_pass"]).lower()}
failed_checks={result["failed_checks"]}
```

## 下一步

```text
1013R_R14_TEACHER_ACTION_GATE_CONTRACT_R0
```
"""
    write_text(STAGE_DIR / "1013R_R13_report.md", report)


def main() -> None:
    result, evidence, errors = validate()
    write_outputs(result, evidence)
    if errors:
        raise SystemExit("FAIL: " + ", ".join(errors))
    print("PASS: 1013R_R13 xiaojiao task-state contract and render surface map")


if __name__ == "__main__":
    main()
