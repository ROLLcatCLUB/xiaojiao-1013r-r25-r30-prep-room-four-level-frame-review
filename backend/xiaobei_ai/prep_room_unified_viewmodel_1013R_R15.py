from __future__ import annotations

from copy import deepcopy
from datetime import datetime, timezone
from typing import Any

from . import prep_room_single_lesson_viewmodel_1013R_R10 as r10_viewmodel
from . import prep_room_task_state_contract_1013R_R13 as r13_contract
from . import prep_room_teacher_action_gate_contract_1013R_R14 as r14_gate


STAGE_ID = "1013R_R15_PREP_ROOM_UNIFIED_VIEWMODEL_R0"
VIEWMODEL_TYPE = "prep_room_unified_readonly_contract_viewmodel"
VIEWMODEL_ID = "g3_u2_l1_color_gradient_unified"


def _now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def boundary_flags() -> dict[str, bool]:
    flags = dict(r14_gate.boundary_flags())
    flags.update(
        {
            "stage": STAGE_ID,
            "unified_viewmodel_readonly": True,
            "unified_viewmodel_defined": True,
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


def _actions_for_slot(action_matrix: list[dict[str, Any]], slot_id: str) -> list[dict[str, Any]]:
    actions: list[dict[str, Any]] = []
    for action in action_matrix:
        if slot_id not in action.get("target_slots", []):
            continue
        actions.append(
            {
                "action_id": action.get("action_id"),
                "label": action.get("label"),
                "gate_type": action.get("gate_type"),
                "allowed_now": action.get("allowed_now"),
                "write_effect": action.get("write_effect"),
            }
        )
    return actions


def _payload_ref_for_slot(slot_id: str) -> list[str]:
    refs = {
        "current_object_card": ["current_object", "lesson_viewmodel.current_lesson"],
        "xiaojiao_task_state": ["task_state"],
        "lesson_body": ["lesson_viewmodel.current_lesson.sections"],
        "teaching_process": ["lesson_viewmodel.current_lesson.process_steps"],
        "teacher_demo": ["lesson_viewmodel.current_lesson.process_steps", "lesson_viewmodel.courseware_screens"],
        "courseware_script": ["lesson_viewmodel.courseware_screens"],
        "classroom_display_screen": [
            "lesson_viewmodel.current_lesson.big_screen_short_text",
            "lesson_viewmodel.courseware_screens",
        ],
        "worksheet": ["lesson_viewmodel.current_lesson.sections.assessment"],
        "assessment_rubric": ["lesson_viewmodel.current_lesson.sections.assessment", "task_state.missing_materials"],
        "blackboard_design": ["lesson_viewmodel.current_lesson.flow"],
        "materials_list": ["lesson_viewmodel.current_lesson.sections.preparation", "source_policy"],
        "source_evidence": ["source_policy"],
        "confirm_actions": ["action_gate"],
        "bottom_composer": ["task_state.suggested_teacher_prompts"],
    }
    return refs.get(slot_id, [])


def build_render_slots(
    surface_map: list[dict[str, Any]],
    action_matrix: list[dict[str, Any]],
) -> list[dict[str, Any]]:
    slots: list[dict[str, Any]] = []
    for slot in surface_map:
        slot_id = slot.get("slot_id")
        slots.append(
            {
                "slot_id": slot_id,
                "human_name": slot.get("human_name"),
                "render_state": slot.get("render_state"),
                "action_gate": slot.get("action_gate"),
                "payload_refs": _payload_ref_for_slot(str(slot_id)),
                "source_refs": deepcopy(slot.get("source_refs", {})),
                "available_actions": _actions_for_slot(action_matrix, str(slot_id)),
                "future_actions": deepcopy(slot.get("future_actions", [])),
            }
        )
    return slots


def _section_index(sections: list[dict[str, Any]]) -> dict[str, dict[str, Any]]:
    return {str(item.get("id")): deepcopy(item) for item in sections if item.get("id")}


def build_unified_viewmodel() -> dict[str, Any]:
    r10 = r10_viewmodel.build_single_lesson_viewmodel()
    task_contract = r13_contract.build_task_state_contract()
    gate_contract = r14_gate.build_gate_contract()
    current_lesson = deepcopy(r10.get("prep_view_patch", {}).get("current_lesson", {}))
    action_matrix = deepcopy(gate_contract.get("action_matrix", []))
    surface_map = deepcopy(task_contract.get("render_surface_map", []))
    source_policy = deepcopy(task_contract.get("source_policy_notes", []))

    return {
        "ok": True,
        "stage": STAGE_ID,
        "viewmodel_type": VIEWMODEL_TYPE,
        "viewmodel_id": VIEWMODEL_ID,
        "generated_at": _now(),
        "current_object": deepcopy(task_contract.get("current_object", {})),
        "lesson_viewmodel": {
            "active_view": r10.get("prep_view_patch", {}).get("active_view"),
            "active_node_id": r10.get("prep_view_patch", {}).get("active_node_id"),
            "lesson_tree": deepcopy(r10.get("prep_view_patch", {}).get("lesson_tree", [])),
            "current_lesson": current_lesson,
            "section_index": _section_index(current_lesson.get("sections", [])),
            "courseware_screens": deepcopy(r10.get("courseware_screen_patch", [])),
        },
        "task_state": {
            "space": deepcopy(task_contract.get("space", {})),
            "task_state": deepcopy(task_contract.get("task_state", {})),
            "known_materials": deepcopy(task_contract.get("known_materials", [])),
            "missing_materials": deepcopy(task_contract.get("missing_materials", [])),
            "preview_candidates": deepcopy(task_contract.get("preview_candidates", [])),
            "suggested_teacher_prompts": deepcopy(task_contract.get("suggested_teacher_prompts", [])),
        },
        "action_gate": {
            "contract_id": gate_contract.get("contract_id"),
            "gate_types": deepcopy(gate_contract.get("gate_types", [])),
            "action_matrix": action_matrix,
            "confirmation_rules": deepcopy(gate_contract.get("confirmation_rules", [])),
            "confirmation_receipt_schema": deepcopy(gate_contract.get("confirmation_receipt_schema", {})),
            "teacher_visible_groups": deepcopy(gate_contract.get("teacher_visible_groups", [])),
        },
        "render_surface_map": surface_map,
        "render_slots": build_render_slots(surface_map, action_matrix),
        "source_policy": {
            "source_matrix": deepcopy(r10.get("source_matrix", [])),
            "source_policy_notes": source_policy,
            "source_categories": [item.get("category") for item in source_policy],
            "ai_draft_may_not_be_standard": True,
            "textbook_anchor_required_for_current_object": True,
        },
        "contracts_consumed": {
            "r10_stage": r10.get("stage"),
            "r13_stage": task_contract.get("stage"),
            "r13_contract_id": task_contract.get("contract_id"),
            "r14_stage": gate_contract.get("stage"),
            "r14_contract_id": gate_contract.get("contract_id"),
        },
        "renderer_contract": {
            "single_entry": True,
            "renderer_should_consume": [
                "current_object",
                "lesson_viewmodel",
                "task_state",
                "action_gate",
                "render_surface_map",
                "render_slots",
                "source_policy",
                "boundary",
            ],
            "renderer_must_not": [
                "read_legacy_hydration_payload",
                "replace_visible_text_by_walker",
                "treat_ai_reference_as_standard",
                "write_database_or_memory",
                "formal_apply",
            ],
        },
        "next_stage_recommendation": {
            "stage": "1013R_R16_SOURCE_POLICY_LIGHT_VALIDATOR_R0",
            "why": "统一 ViewModel 已合并页面、任务状态和动作门控；下一步应先轻量校验资料来源，避免 render_blocks 之前混淆教材依据、教师输入和 AI 草案。",
        },
        "boundary": boundary_flags(),
    }


def build_viewmodel_sample_bundle() -> dict[str, Any]:
    viewmodel = build_unified_viewmodel()
    return {
        "stage": STAGE_ID,
        "unified_viewmodel": viewmodel,
        "render_slots": deepcopy(viewmodel["render_slots"]),
        "boundary": deepcopy(viewmodel["boundary"]),
    }
