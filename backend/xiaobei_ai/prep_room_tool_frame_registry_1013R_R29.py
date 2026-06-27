from __future__ import annotations

from copy import deepcopy
from datetime import datetime, timezone
from typing import Any

from . import prep_room_main_shell_fetch_adapter_1013L_R5 as l5_shell_adapter
from . import prep_room_render_block_component_boundary_1013R_R24 as r24_component_boundary
from . import prep_room_render_blocks_protocol_1013R_R17 as r17_render_blocks
from . import prep_room_render_shell_registry_1013L_R0 as l0_shell_registry
from . import prep_room_room_workspace_registry_1013R_R28 as r28_room_registry


STAGE_ID = "1013R_R29_TOOL_FRAME_REGISTRY"
REGISTRY_ID = "SHIWEI_TOOL_FRAME_REGISTRY_R0"


def _now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def boundary_flags() -> dict[str, bool]:
    flags = dict(r28_room_registry.boundary_flags())
    flags.update(
        {
            "stage": STAGE_ID,
            "tool_frame_registry_defined": True,
            "derived_from_l5_and_r17_r24": True,
            "static_registry_only": True,
            "tool_behavior_implemented": False,
            "new_disconnected_page_created": False,
            "route_registered": False,
            "endpoint_registered": False,
            "runtime_connected": False,
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


def _l0_state_by_id() -> dict[str, dict[str, Any]]:
    return {item["state_id"]: item for item in l0_shell_registry.render_stage_registry().get("states", [])}


def _capability_to_tool_frame(adapter: dict[str, Any]) -> dict[str, Any]:
    active_capability = adapter.get("active_capability") or adapter.get("state_id")
    return {
        "tool_id": active_capability,
        "tool_label": adapter.get("teacher_label"),
        "level": 3,
        "room_id": "prep_room",
        "source_state_id": adapter.get("state_id"),
        "render_slot": adapter.get("render_slot"),
        "readonly_endpoint": adapter.get("readonly_endpoint"),
        "source_endpoint": adapter.get("source_endpoint"),
        "source_fixture": adapter.get("source_fixture"),
        "fetch_policy": adapter.get("fetch_policy"),
        "controls_level_4_content": True,
        "formal_apply_allowed": False,
        "may_call_provider": False,
        "teacher_confirmation_required_for_write": True,
    }


def _missing_l5_tool_from_l0(state_id: str, tool_id: str, label: str) -> dict[str, Any]:
    state = _l0_state_by_id().get(state_id, {})
    return {
        "tool_id": tool_id,
        "tool_label": label,
        "level": 3,
        "room_id": "prep_room",
        "source_state_id": state_id,
        "render_slot": "stage_body",
        "readonly_endpoint": None,
        "source_endpoint": None,
        "source_fixture": state.get("route_or_adapter"),
        "fetch_policy": "l0_state_static_mapping",
        "controls_level_4_content": True,
        "formal_apply_allowed": False,
        "may_call_provider": False,
        "teacher_confirmation_required_for_write": True,
    }


def _governance_tools() -> list[dict[str, Any]]:
    return [
        {
            "tool_id": "teacher_action_gate",
            "tool_label": "教师确认门",
            "level": 3,
            "room_id": "prep_room",
            "source_state_id": "confirm_actions",
            "render_slot": "governance",
            "source_endpoint": None,
            "source_fixture": "1013R_R17 slot_id=confirm_actions",
            "fetch_policy": "render_block_slot_mapping",
            "controls_level_4_content": True,
            "formal_apply_allowed": False,
            "may_call_provider": False,
            "teacher_confirmation_required_for_write": True,
        },
        {
            "tool_id": "source_evidence",
            "tool_label": "资料来源与依据",
            "level": 3,
            "room_id": "prep_room",
            "source_state_id": "source_evidence",
            "render_slot": "governance",
            "source_endpoint": None,
            "source_fixture": "1013R_R17 slot_id=source_evidence",
            "fetch_policy": "render_block_slot_mapping",
            "controls_level_4_content": True,
            "formal_apply_allowed": False,
            "may_call_provider": False,
            "teacher_confirmation_required_for_write": True,
        },
        {
            "tool_id": "xiaojiao_bottom_composer",
            "tool_label": "小教推进入口",
            "level": 3,
            "room_id": "prep_room",
            "source_state_id": "bottom_composer",
            "render_slot": "global_bottom",
            "source_endpoint": None,
            "source_fixture": "1013R_R17 slot_id=bottom_composer",
            "fetch_policy": "composer_prompt_mapping",
            "controls_level_4_content": False,
            "formal_apply_allowed": False,
            "may_call_provider": False,
            "teacher_confirmation_required_for_write": True,
        },
    ]


def build_tool_frame_registry() -> dict[str, Any]:
    room_registry = r28_room_registry.build_room_workspace_registry()
    render_protocol = r17_render_blocks.build_render_blocks_protocol()
    component_boundary = r24_component_boundary.build_component_boundary_map()
    l5_tools = [_capability_to_tool_frame(adapter) for adapter in l5_shell_adapter.state_fetch_adapters()]
    tool_frames = [
        _missing_l5_tool_from_l0("prep_notebook", "prep_notebook", "备课本"),
        *l5_tools,
        *_governance_tools(),
    ]
    return {
        "ok": True,
        "stage": STAGE_ID,
        "registry_id": REGISTRY_ID,
        "generated_at": _now(),
        "consumes": {
            "r28_stage": room_registry.get("stage"),
            "l5_stage": l5_shell_adapter.STAGE_ID,
            "r17_stage": render_protocol.get("stage"),
            "r24_stage": component_boundary.get("stage"),
        },
        "registry_rule": {
            "derive_from_l5_active_capabilities": True,
            "derive_content_modes_from_r17_block_groups": True,
            "derive_component_boundaries_from_r24": True,
            "tool_frame_controls_level_4_content": True,
            "tool_actions_must_respect_teacher_confirmation_gate": True,
            "do_not_make_tool_frame_a_new_page": True,
            "formal_apply_allowed": False,
        },
        "tool_frames": tool_frames,
        "render_group_bindings": deepcopy(render_protocol.get("block_groups", [])),
        "component_group_bindings": deepcopy(component_boundary.get("component_groups", [])),
        "content_slot_bindings": [
            {
                "slot_id": block.get("slot_id"),
                "block_type": block.get("block_type"),
                "tool_frame_hint": (
                    "governance"
                    if block.get("slot_id") in {"source_evidence", "confirm_actions", "bottom_composer"}
                    else "derivative"
                    if block.get("slot_id") in {"courseware_script", "classroom_display_screen", "worksheet", "assessment_rubric", "blackboard_design"}
                    else "lesson_core"
                ),
                "formal_apply_allowed": False,
            }
            for block in render_protocol.get("render_blocks", [])
        ],
        "next_stage_recommendation": {
            "stage": "1013R_R30_RENDER_SURFACE_CONNECTOR_PLAN_OR_VISUAL_TOOL_POLISH",
            "why": "Rooms and tools are now registered from existing assets; next can either plan a connector or polish visible tool grouping inside the current page copy.",
        },
        "boundary": boundary_flags(),
    }


def build_tool_registry_sample_bundle() -> dict[str, Any]:
    registry = build_tool_frame_registry()
    return {
        "stage": STAGE_ID,
        "tool_frame_registry": registry,
        "tool_frames": deepcopy(registry["tool_frames"]),
        "render_group_bindings": deepcopy(registry["render_group_bindings"]),
        "component_group_bindings": deepcopy(registry["component_group_bindings"]),
        "boundary": deepcopy(registry["boundary"]),
    }
