from __future__ import annotations

from copy import deepcopy
from datetime import datetime, timezone
from typing import Any

from . import prep_room_render_blocks_protocol_1013R_R17 as r17_blocks
from . import prep_room_teacher_walkthrough_script_1013R_R23 as r23_walkthrough
from . import prep_room_unified_package_readonly_export_1013R_R20 as r20_package


STAGE_ID = "1013R_R24_RENDER_BLOCK_COMPONENT_BOUNDARY_MAP"
BOUNDARY_ID = "SHIWEI_RENDER_BLOCK_COMPONENT_BOUNDARY_MAP_R0"


def _now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def boundary_flags() -> dict[str, bool]:
    flags = dict(r23_walkthrough.boundary_flags())
    flags.update(
        {
            "stage": STAGE_ID,
            "render_block_component_boundary_defined": True,
            "component_implementation_created": False,
            "route_registered": False,
            "endpoint_registered": False,
            "R36_modified": False,
            "main_shell_modified": False,
            "existing_page_modified": False,
            "provider_called": False,
            "model_called": False,
            "database_written": False,
            "memory_written": False,
            "vector_index_written": False,
            "feishu_written": False,
            "formal_apply_performed": False,
        }
    )
    return flags


COMPONENT_BY_BLOCK_TYPE = {
    "object_summary": "PrepRoomObjectHeader",
    "task_state": "XiaojiaoTaskStatePanel",
    "document_sections": "LessonSectionStack",
    "process_steps": "TeachingProcessTimeline",
    "derivative_placeholder": "DerivativePreviewPlaceholder",
    "courseware_preview": "CoursewareScriptPreview",
    "display_preview": "ClassroomDisplayPreview",
    "worksheet_placeholder": "WorksheetPreviewSlot",
    "assessment_blocked": "AssessmentBlockedPanel",
    "blackboard_placeholder": "BlackboardDesignPreview",
    "materials_preview": "MaterialsListPanel",
    "source_policy": "SourceEvidencePanel",
    "action_gate": "TeacherActionGatePanel",
    "composer_prompt": "XiaojiaoComposerPrompt",
}


def _component_props(block: dict[str, Any]) -> list[str]:
    base = ["block_id", "slot_id", "title", "render_state", "gate_type", "source_badges"]
    slot_id = block.get("slot_id")
    extra = {
        "current_object_card": ["current_object"],
        "xiaojiao_task_state": ["task_state.known_materials", "task_state.missing_materials"],
        "lesson_body": ["lesson_viewmodel.current_lesson.sections"],
        "teaching_process": ["lesson_viewmodel.current_lesson.process_steps", "derivative_linkage.process_derivative_links"],
        "courseware_script": ["lesson_viewmodel.courseware_screens", "render_block_linkage_index.courseware_script"],
        "classroom_display_screen": ["render_block_linkage_index.classroom_display_screen"],
        "worksheet": ["render_block_linkage_index.worksheet"],
        "assessment_rubric": ["render_block_linkage_index.assessment_rubric", "task_state.missing_materials"],
        "source_evidence": ["source_policy_result.checks"],
        "confirm_actions": ["teacher_action_gate.action_matrix"],
        "bottom_composer": ["task_state.suggested_teacher_prompts"],
    }
    return base + extra.get(str(slot_id), list(block.get("content_ref", {}).get("payload_refs", [])))


def build_component_boundary_map() -> dict[str, Any]:
    package = r20_package.build_unified_package()
    blocks = package.get("render_blocks", [])
    entries: list[dict[str, Any]] = []
    for block in blocks:
        block_type = str(block.get("block_type"))
        entries.append(
            {
                "slot_id": block.get("slot_id"),
                "block_type": block_type,
                "human_name": block.get("title"),
                "future_component": COMPONENT_BY_BLOCK_TYPE.get(block_type, "GenericRenderBlock"),
                "props_contract": _component_props(block),
                "allowed_interaction_boundary": {
                    "may_expand_preview": True,
                    "may_emit_teacher_intent": bool(block.get("available_actions")),
                    "may_save_or_export": False,
                    "may_call_provider": False,
                    "must_respect_gate_type": block.get("gate_type"),
                },
                "source_policy_boundary": {
                    "must_show_source_badges": True,
                    "must_not_promote_ai_draft_to_standard": True,
                },
            }
        )
    return {
        "ok": True,
        "stage": STAGE_ID,
        "boundary_id": BOUNDARY_ID,
        "generated_at": _now(),
        "consumes": {
            "r17_stage": r17_blocks.STAGE_ID,
            "r20_stage": package.get("stage"),
            "r23_stage": r23_walkthrough.STAGE_ID,
            "current_object": deepcopy(package.get("current_object", {})),
        },
        "component_boundary_entries": entries,
        "component_groups": [
            {
                "group_id": "prep_room_core",
                "components": ["PrepRoomObjectHeader", "XiaojiaoTaskStatePanel", "LessonSectionStack", "TeachingProcessTimeline"],
            },
            {
                "group_id": "derivative_objects",
                "components": [
                    "CoursewareScriptPreview",
                    "ClassroomDisplayPreview",
                    "WorksheetPreviewSlot",
                    "AssessmentBlockedPanel",
                    "BlackboardDesignPreview",
                ],
            },
            {
                "group_id": "governance_and_actions",
                "components": ["SourceEvidencePanel", "TeacherActionGatePanel", "XiaojiaoComposerPrompt"],
            },
        ],
        "next_stage_recommendation": {
            "stage": "1013R_R25_READONLY_ROUTE_REGISTRATION_GATE",
            "why": "组件边界已定义；下一步才评估 R20 统一协议包是否允许进入 dev 只读 route 注册门禁。",
        },
        "boundary": boundary_flags(),
    }


def build_boundary_sample_bundle() -> dict[str, Any]:
    boundary_map = build_component_boundary_map()
    return {
        "stage": STAGE_ID,
        "component_boundary_map": boundary_map,
        "component_boundary_entries": deepcopy(boundary_map["component_boundary_entries"]),
        "boundary": deepcopy(boundary_map["boundary"]),
    }
