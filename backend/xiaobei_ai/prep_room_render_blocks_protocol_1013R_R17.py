from __future__ import annotations

from copy import deepcopy
from datetime import datetime, timezone
from typing import Any

from . import prep_room_source_policy_validator_1013R_R16 as r16_policy
from . import prep_room_unified_viewmodel_1013R_R15 as r15_viewmodel


STAGE_ID = "1013R_R17_RENDER_BLOCKS_PROTOCOL_R0"
PROTOCOL_ID = "SHIWEI_RENDER_BLOCKS_PROTOCOL_R0"


def _now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def boundary_flags() -> dict[str, bool]:
    flags = dict(r16_policy.boundary_flags())
    flags.update(
        {
            "stage": STAGE_ID,
            "render_blocks_protocol_readonly": True,
            "render_blocks_protocol_defined": True,
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


BLOCK_TYPE_BY_SLOT = {
    "current_object_card": "object_summary",
    "xiaojiao_task_state": "task_state",
    "lesson_body": "document_sections",
    "teaching_process": "process_steps",
    "teacher_demo": "derivative_placeholder",
    "courseware_script": "courseware_preview",
    "classroom_display_screen": "display_preview",
    "worksheet": "worksheet_placeholder",
    "assessment_rubric": "assessment_blocked",
    "blackboard_design": "blackboard_placeholder",
    "materials_list": "materials_preview",
    "source_evidence": "source_policy",
    "confirm_actions": "action_gate",
    "bottom_composer": "composer_prompt",
}


def _block_content_ref(slot: dict[str, Any]) -> dict[str, Any]:
    refs = list(slot.get("payload_refs", []))
    return {
        "payload_refs": refs,
        "primary_ref": refs[0] if refs else None,
        "requires_runtime_resolution": False,
    }


def _source_badges(slot: dict[str, Any]) -> list[str]:
    refs = slot.get("source_refs", {})
    if isinstance(refs, dict):
        policy = refs.get("source_policy")
        source_ids = refs.get("source_ids", [])
        badges = [str(policy)] if policy else []
        badges.extend(str(item) for item in source_ids[:2])
        return badges
    return []


def build_render_blocks(viewmodel: dict[str, Any] | None = None) -> list[dict[str, Any]]:
    if viewmodel is None:
        viewmodel = r15_viewmodel.build_unified_viewmodel()
    blocks: list[dict[str, Any]] = []
    for index, slot in enumerate(viewmodel.get("render_slots", []), start=1):
        slot_id = str(slot.get("slot_id"))
        block = {
            "block_id": f"rb_{index:02d}_{slot_id}",
            "slot_id": slot_id,
            "block_type": BLOCK_TYPE_BY_SLOT.get(slot_id, "generic_slot"),
            "title": slot.get("human_name"),
            "order": index,
            "render_state": slot.get("render_state"),
            "gate_type": slot.get("action_gate"),
            "content_ref": _block_content_ref(slot),
            "source_badges": _source_badges(slot),
            "available_actions": deepcopy(slot.get("available_actions", [])),
            "future_actions": deepcopy(slot.get("future_actions", [])),
            "teacher_visible": True,
            "formal_apply_allowed": False,
        }
        blocks.append(block)
    return blocks


def build_render_blocks_protocol() -> dict[str, Any]:
    viewmodel = r15_viewmodel.build_unified_viewmodel()
    source_policy = r16_policy.build_source_policy_result(viewmodel)
    blocks = build_render_blocks(viewmodel)
    return {
        "ok": source_policy.get("ok") is True,
        "stage": STAGE_ID,
        "protocol_id": PROTOCOL_ID,
        "protocol_version": "0.1.0",
        "generated_at": _now(),
        "consumes": {
            "unified_viewmodel_stage": viewmodel.get("stage"),
            "source_policy_stage": source_policy.get("stage"),
            "current_object": deepcopy(viewmodel.get("current_object", {})),
        },
        "render_blocks": blocks,
        "block_groups": [
            {
                "group_id": "lesson_core",
                "label": "备课核心",
                "slot_ids": ["current_object_card", "xiaojiao_task_state", "lesson_body", "teaching_process"],
            },
            {
                "group_id": "derivatives",
                "label": "课堂派生物",
                "slot_ids": [
                    "teacher_demo",
                    "courseware_script",
                    "classroom_display_screen",
                    "worksheet",
                    "assessment_rubric",
                    "blackboard_design",
                ],
            },
            {
                "group_id": "governance",
                "label": "来源与确认",
                "slot_ids": ["materials_list", "source_evidence", "confirm_actions", "bottom_composer"],
            },
        ],
        "renderer_requirements": {
            "stable_order": True,
            "must_render_block_title": True,
            "must_show_gate_state": True,
            "must_show_source_badges": True,
            "must_not_formal_apply": True,
            "must_not_call_provider": True,
        },
        "next_stage_recommendation": {
            "stage": "1013R_R18_LIGHT_RENDER_ADAPTER_SAMPLE",
            "why": "render_blocks 协议已定义，可用轻量适配器验证页面未来如何按 block 渲染。",
        },
        "boundary": boundary_flags(),
    }


def build_protocol_sample_bundle() -> dict[str, Any]:
    protocol = build_render_blocks_protocol()
    return {
        "stage": STAGE_ID,
        "render_blocks_protocol": protocol,
        "render_blocks": deepcopy(protocol["render_blocks"]),
        "boundary": deepcopy(protocol["boundary"]),
    }
