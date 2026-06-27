from __future__ import annotations

import json
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

STAGE_ID = "1013R_R14_TEACHER_ACTION_GATE_CONTRACT_R0"
STAGE_DIR = (
    ROOT
    / "outputs"
    / "PREP_ROOM_RENDER_CANVAS_DEEPEN_V1"
    / "1013R_R14_teacher_action_gate_contract_r0"
)
DOC_PATH = ROOT / "docs" / "1013R_R14_teacher_action_gate_contract.md"


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
    from backend.xiaobei_ai import prep_room_teacher_action_gate_contract_1013R_R14 as gate_module

    errors: list[str] = []
    bundle = gate_module.build_contract_sample_bundle()
    contract = bundle.get("teacher_action_gate_contract", {})
    action_matrix = bundle.get("action_matrix", [])
    boundary = bundle.get("boundary", {})
    doc = DOC_PATH.read_text(encoding="utf-8", errors="ignore") if DOC_PATH.exists() else ""
    actions_by_id = {item.get("action_id"): item for item in action_matrix if isinstance(item, dict)}

    if bundle.get("stage") != STAGE_ID:
        fail(errors, "stage_id_mismatch")
    if contract.get("stage") != STAGE_ID:
        fail(errors, "contract_stage_mismatch")
    if contract.get("contract_id") != "SHIWEI_TEACHER_ACTION_GATE_CONTRACT_R0":
        fail(errors, "contract_id_mismatch")
    if contract.get("consumes", {}).get("task_state_contract_id") != "SHIWEI_TASK_STATE_CONTRACT_R0":
        fail(errors, "r13_task_state_contract_not_consumed")
    if contract.get("consumes", {}).get("current_object", {}).get("title") != "2-1《色彩的渐变》":
        fail(errors, "current_object_not_preserved")

    required_gate_types = [
        "view_only",
        "intent_preview_only",
        "preview_then_confirm",
        "gate_required",
        "blocked_until_teacher_dimension",
        "future_only",
    ]
    gate_types = {item.get("gate_type") for item in contract.get("gate_types", [])}
    for gate_type in required_gate_types:
        if gate_type not in gate_types:
            fail(errors, f"gate_type_missing:{gate_type}")

    required_actions = [
        "preview_lesson_body_refinement",
        "preview_courseware_script",
        "preview_display_screen",
        "preview_worksheet",
        "preview_assessment_rubric",
        "confirm_refine_lesson_body_preview",
        "confirm_generate_courseware_preview",
        "confirm_generate_display_preview",
        "confirm_generate_worksheet_preview",
        "formal_save_to_lesson_package",
        "write_student_assessment",
        "export_courseware_file",
        "write_memory_or_archive",
    ]
    for action_id in required_actions:
        if action_id not in actions_by_id:
            fail(errors, f"action_missing:{action_id}")

    if actions_by_id.get("preview_courseware_script", {}).get("target_slots") != ["courseware_script"]:
        fail(errors, "courseware_preview_target_mismatch")
    if actions_by_id.get("preview_display_screen", {}).get("target_slots") != ["classroom_display_screen"]:
        fail(errors, "display_preview_target_mismatch")
    if actions_by_id.get("preview_worksheet", {}).get("target_slots") != ["worksheet"]:
        fail(errors, "worksheet_preview_target_mismatch")
    if actions_by_id.get("preview_assessment_rubric", {}).get("allowed_now"):
        fail(errors, "assessment_preview_should_be_blocked")
    if actions_by_id.get("preview_assessment_rubric", {}).get("gate_type") != "blocked_until_teacher_dimension":
        fail(errors, "assessment_preview_gate_mismatch")

    for action in action_matrix:
        if action.get("formal_apply_allowed"):
            fail(errors, f"formal_apply_allowed_in_action:{action.get('action_id')}")
        if action.get("allowed_now") and action.get("gate_type") in {"preview_then_confirm", "gate_required"}:
            if not action.get("requires_teacher_confirmation"):
                fail(errors, f"confirmation_missing_for_allowed_action:{action.get('action_id')}")
        if action.get("write_effect") not in {"preview_only", "record_preview_decision_only", "none"}:
            fail(errors, f"unexpected_write_effect:{action.get('action_id')}:{action.get('write_effect')}")

    rule_ids = {item.get("rule_id") for item in contract.get("confirmation_rules", [])}
    for rule_id in [
        "show_preview_before_confirm",
        "show_impact_scope",
        "show_source_badges",
        "no_silent_write",
        "formal_apply_separate_gate",
    ]:
        if rule_id not in rule_ids:
            fail(errors, f"confirmation_rule_missing:{rule_id}")

    receipt_schema = contract.get("confirmation_receipt_schema", {})
    if receipt_schema.get("formal_apply_performed") is not False:
        fail(errors, "receipt_schema_does_not_force_formal_apply_false")

    groups = {item.get("group_id"): item for item in contract.get("teacher_visible_groups", [])}
    if "can_preview_now" not in groups:
        fail(errors, "can_preview_now_group_missing")
    if "blocked_now" not in groups:
        fail(errors, "blocked_now_group_missing")
    if "preview_assessment_rubric" not in groups.get("blocked_now", {}).get("action_ids", []):
        fail(errors, "blocked_assessment_not_visible")
    if "write_memory_or_archive" not in groups.get("blocked_now", {}).get("action_ids", []):
        fail(errors, "blocked_memory_not_visible")

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
    if not boundary.get("teacher_action_gate_contract_readonly"):
        fail(errors, "teacher_action_gate_contract_readonly_not_marked")
    if not boundary.get("task_state_contract_consumed"):
        fail(errors, "task_state_contract_consumed_not_marked")

    if not DOC_PATH.exists():
        fail(errors, "r14_doc_missing")
    for token in ["SHIWEI_TEACHER_ACTION_GATE_CONTRACT_R0", "preview_then_confirm", "formal_apply_performed=false"]:
        if token not in doc:
            fail(errors, f"r14_doc_token_missing:{token}")

    evidence = {
        "module": "backend.xiaobei_ai.prep_room_teacher_action_gate_contract_1013R_R14",
        "contract_id": contract.get("contract_id"),
        "consumes": contract.get("consumes"),
        "gate_type_count": len(contract.get("gate_types", [])),
        "action_count": len(action_matrix),
        "allowed_action_count": len([item for item in action_matrix if item.get("allowed_now")]),
        "blocked_action_count": len([item for item in action_matrix if not item.get("allowed_now")]),
        "formal_apply_allowed_count": len([item for item in action_matrix if item.get("formal_apply_allowed")]),
        "teacher_visible_groups": contract.get("teacher_visible_groups", []),
        "boundary": boundary,
    }
    result = {
        "stage_id": STAGE_ID,
        "status": "PASS" if not errors else "FAIL",
        "validator_pass": not errors,
        "created_at": now(),
        "checks": {
            "teacher_action_gate_contract_defined": contract.get("contract_id")
            == "SHIWEI_TEACHER_ACTION_GATE_CONTRACT_R0",
            "r13_task_state_consumed": contract.get("consumes", {}).get("task_state_contract_id")
            == "SHIWEI_TASK_STATE_CONTRACT_R0",
            "courseware_and_display_actions_separated": not any(
                code in errors for code in ["courseware_preview_target_mismatch", "display_preview_target_mismatch"]
            ),
            "assessment_action_blocked": not any(
                code in errors for code in ["assessment_preview_should_be_blocked", "assessment_preview_gate_mismatch"]
            ),
            "no_action_allows_formal_apply": evidence["formal_apply_allowed_count"] == 0,
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
    from backend.xiaobei_ai import prep_room_teacher_action_gate_contract_1013R_R14 as gate_module

    bundle = gate_module.build_contract_sample_bundle()
    write_json(STAGE_DIR / "1013R_R14_result.json", result)
    write_json(STAGE_DIR / "teacher_action_gate_contract_sample_1013R_R14.json", bundle["teacher_action_gate_contract"])
    write_json(STAGE_DIR / "action_matrix_1013R_R14.json", bundle["action_matrix"])
    write_json(STAGE_DIR / "teacher_action_gate_evidence_1013R_R14.json", evidence)
    report = f"""# 1013R_R14 teacher action gate contract

## 定位

本轮定义教师确认门合同，不执行任何动作。

```text
stage_id={STAGE_ID}
contract_id=SHIWEI_TEACHER_ACTION_GATE_CONTRACT_R0
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

- 6 种动作门控类型。
- 预览候选、教师确认动作和阻断动作的统一 action matrix。
- 确认前必须显示预览、影响范围、来源标签和无 formal apply 提示。
- 确认回执 schema。

## 验证

```text
validator_pass={str(result["validator_pass"]).lower()}
failed_checks={result["failed_checks"]}
```

## 下一步

```text
1013R_R15_PREP_ROOM_UNIFIED_VIEWMODEL_R0
```
"""
    write_text(STAGE_DIR / "1013R_R14_report.md", report)


def main() -> None:
    result, evidence, errors = validate()
    write_outputs(result, evidence)
    if errors:
        raise SystemExit("FAIL: " + ", ".join(errors))
    print("PASS: 1013R_R14 teacher action gate contract")


if __name__ == "__main__":
    main()
