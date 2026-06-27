from __future__ import annotations

from copy import deepcopy
from datetime import datetime, timezone
from typing import Any

from . import prep_room_task_state_contract_1013R_R13 as r13_contract


STAGE_ID = "1013R_R14_TEACHER_ACTION_GATE_CONTRACT_R0"
CONTRACT_ID = "SHIWEI_TEACHER_ACTION_GATE_CONTRACT_R0"


def _now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def boundary_flags() -> dict[str, bool]:
    flags = dict(r13_contract.boundary_flags())
    flags.update(
        {
            "stage": STAGE_ID,
            "teacher_action_gate_contract_readonly": True,
            "task_state_contract_consumed": True,
            "teacher_action_gate_defined": True,
            "unified_viewmodel_defined": False,
            "source_policy_validator_defined": False,
            "render_blocks_protocol_defined": False,
            "light_render_adapter_defined": False,
            "route_registered": False,
            "runtime_write_allowed": False,
            "provider_called": False,
            "model_called": False,
            "database_written": False,
            "memory_written": False,
            "vector_index_written": False,
            "feishu_written": False,
            "formal_apply_performed": False,
            "R36_modified": False,
            "main_shell_modified": False,
        }
    )
    return flags


def build_gate_types() -> list[dict[str, Any]]:
    return [
        {
            "gate_type": "view_only",
            "label": "只读查看",
            "allowed_effects": ["read_state", "open_detail"],
            "forbidden_effects": ["create_preview", "write_state", "export_file", "formal_apply"],
            "teacher_confirmation_required": False,
        },
        {
            "gate_type": "intent_preview_only",
            "label": "只识别意图",
            "allowed_effects": ["classify_teacher_input", "suggest_next_action"],
            "forbidden_effects": ["write_state", "export_file", "formal_apply"],
            "teacher_confirmation_required": False,
        },
        {
            "gate_type": "preview_then_confirm",
            "label": "先生成预览，再等确认",
            "allowed_effects": ["create_preview", "show_impact_scope", "show_source_badges"],
            "forbidden_effects": ["write_state", "export_file", "formal_apply"],
            "teacher_confirmation_required": True,
        },
        {
            "gate_type": "gate_required",
            "label": "必须经过教师确认门",
            "allowed_effects": ["show_confirm_dialog", "record_preview_decision"],
            "forbidden_effects": ["silent_write", "formal_apply_without_explicit_gate"],
            "teacher_confirmation_required": True,
        },
        {
            "gate_type": "blocked_until_teacher_dimension",
            "label": "缺少教师维度，暂时阻断",
            "allowed_effects": ["show_block_reason", "ask_for_missing_material"],
            "forbidden_effects": ["create_formal_assessment", "write_student_record", "formal_apply"],
            "teacher_confirmation_required": True,
        },
        {
            "gate_type": "future_only",
            "label": "未来能力",
            "allowed_effects": ["show_future_badge"],
            "forbidden_effects": ["execute_action", "write_state", "export_file", "formal_apply"],
            "teacher_confirmation_required": True,
        },
    ]


def _slot_gate(surface_map: list[dict[str, Any]]) -> dict[str, str]:
    return {
        str(item.get("slot_id")): str(item.get("action_gate"))
        for item in surface_map
        if item.get("slot_id") and item.get("action_gate")
    }


def _preview_action(candidate: dict[str, Any], slot_gates: dict[str, str]) -> dict[str, Any]:
    targets = list(candidate.get("targets", []))
    allowed_now = bool(candidate.get("allowed_now"))
    gate_type = "preview_then_confirm" if allowed_now else "blocked_until_teacher_dimension"
    return {
        "action_id": candidate.get("id"),
        "label": candidate.get("label"),
        "action_kind": "preview_candidate",
        "target_slots": targets,
        "target_slot_gates": {slot_id: slot_gates.get(slot_id, "unknown") for slot_id in targets},
        "gate_type": gate_type,
        "allowed_now": allowed_now,
        "requires_teacher_confirmation": True,
        "formal_apply_allowed": False,
        "write_effect": candidate.get("write_effect", "preview_only"),
        "blocked_by": list(candidate.get("blocked_by", [])),
        "must_show_before_confirm": [
            "preview_content",
            "impact_scope",
            "source_badges",
            "write_effect=preview_only",
        ],
    }


def _confirm_action(action: dict[str, Any], slot_gates: dict[str, str]) -> dict[str, Any]:
    targets = list(action.get("targets", []))
    return {
        "action_id": action.get("id"),
        "label": action.get("label"),
        "action_kind": "teacher_confirmation",
        "target_slots": targets,
        "target_slot_gates": {slot_id: slot_gates.get(slot_id, "unknown") for slot_id in targets},
        "gate_type": "gate_required",
        "allowed_now": bool(action.get("allowed_now")),
        "requires_teacher_confirmation": True,
        "formal_apply_allowed": bool(action.get("formal_apply_allowed")) and False,
        "write_effect": "record_preview_decision_only",
        "must_show_before_confirm": [
            "preview_diff_or_summary",
            "affected_slots",
            "source_policy_notes",
            "no_formal_apply_notice",
        ],
    }


def _blocked_action(action: dict[str, Any]) -> dict[str, Any]:
    return {
        "action_id": action.get("id"),
        "label": action.get("label"),
        "action_kind": "blocked_action",
        "target_slots": [],
        "gate_type": "future_only" if action.get("id") in {"export_courseware_file", "write_memory_or_archive"} else "blocked_until_teacher_dimension",
        "allowed_now": False,
        "requires_teacher_confirmation": True,
        "formal_apply_allowed": False,
        "write_effect": "none",
        "blocked_reason": action.get("blocked_reason"),
        "unblock_requires": list(action.get("unblock_requires", [])),
    }


def build_action_matrix(task_contract: dict[str, Any] | None = None) -> list[dict[str, Any]]:
    if task_contract is None:
        task_contract = r13_contract.build_task_state_contract()
    slot_gates = _slot_gate(task_contract.get("render_surface_map", []))
    actions: list[dict[str, Any]] = []
    actions.extend(_preview_action(item, slot_gates) for item in task_contract.get("preview_candidates", []))
    actions.extend(_confirm_action(item, slot_gates) for item in task_contract.get("teacher_confirm_actions", []))
    actions.extend(_blocked_action(item) for item in task_contract.get("blocked_actions", []))
    return actions


def build_confirmation_receipt_schema() -> dict[str, Any]:
    return {
        "receipt_id": "string",
        "action_id": "string",
        "teacher_decision": ["confirm_preview", "revise_preview", "reject_preview", "defer"],
        "target_slots": ["string"],
        "preview_summary": "string",
        "source_badges": ["textbook_anchor", "teacher_input", "ai_draft", "system_structure"],
        "write_effect": ["preview_only", "record_preview_decision_only", "none"],
        "formal_apply_performed": False,
        "created_at": "iso8601",
    }


def build_gate_contract() -> dict[str, Any]:
    task_contract = r13_contract.build_task_state_contract()
    action_matrix = build_action_matrix(task_contract)
    return {
        "ok": True,
        "stage": STAGE_ID,
        "contract_id": CONTRACT_ID,
        "contract_version": "0.1.0",
        "generated_at": _now(),
        "consumes": {
            "task_state_contract_stage": task_contract.get("stage"),
            "task_state_contract_id": task_contract.get("contract_id"),
            "current_object": deepcopy(task_contract.get("current_object", {})),
            "render_surface_slot_count": len(task_contract.get("render_surface_map", [])),
        },
        "gate_types": build_gate_types(),
        "action_matrix": action_matrix,
        "confirmation_rules": [
            {
                "rule_id": "show_preview_before_confirm",
                "label": "确认前必须先显示预览",
                "must_hold": True,
            },
            {
                "rule_id": "show_impact_scope",
                "label": "确认前必须显示影响哪些渲染位",
                "must_hold": True,
            },
            {
                "rule_id": "show_source_badges",
                "label": "确认前必须显示资料来源标签",
                "must_hold": True,
            },
            {
                "rule_id": "no_silent_write",
                "label": "不得静默写入数据库、记忆、飞书、向量或正式课包",
                "must_hold": True,
            },
            {
                "rule_id": "formal_apply_separate_gate",
                "label": "formal apply 必须是后续独立门，不得混入 R14",
                "must_hold": True,
            },
        ],
        "confirmation_receipt_schema": build_confirmation_receipt_schema(),
        "teacher_visible_groups": [
            {
                "group_id": "can_preview_now",
                "label": "现在可以先预览",
                "action_ids": [
                    item["action_id"]
                    for item in action_matrix
                    if item["action_kind"] == "preview_candidate" and item["allowed_now"]
                ],
            },
            {
                "group_id": "need_teacher_confirm",
                "label": "需要教师确认",
                "action_ids": [
                    item["action_id"]
                    for item in action_matrix
                    if item["requires_teacher_confirmation"] and item["allowed_now"]
                ],
            },
            {
                "group_id": "blocked_now",
                "label": "当前阻断",
                "action_ids": [item["action_id"] for item in action_matrix if not item["allowed_now"]],
            },
        ],
        "audit_receipt": {
            "created_by_stage": STAGE_ID,
            "r13_task_state_contract_stage": task_contract.get("stage"),
            "readonly": True,
            "formal_apply_performed": False,
            "no_write_flags": boundary_flags(),
        },
        "next_stage_recommendation": {
            "stage": "1013R_R15_PREP_ROOM_UNIFIED_VIEWMODEL_R0",
            "why": "R13 定义任务状态和渲染位，R14 定义动作门控；下一步应把 lesson_viewmodel、task_state、action_gate、source_policy 和 render_surface_map 合成统一 ViewModel。",
        },
        "boundary": boundary_flags(),
    }


def build_contract_sample_bundle() -> dict[str, Any]:
    contract = build_gate_contract()
    return {
        "stage": STAGE_ID,
        "teacher_action_gate_contract": contract,
        "action_matrix": deepcopy(contract["action_matrix"]),
        "confirmation_receipt_schema": deepcopy(contract["confirmation_receipt_schema"]),
        "boundary": deepcopy(contract["boundary"]),
    }
