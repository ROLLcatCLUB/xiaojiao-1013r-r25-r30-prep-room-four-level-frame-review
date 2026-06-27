from __future__ import annotations

from copy import deepcopy
from datetime import datetime, timezone
from typing import Any

from . import prep_room_main_shell_fetch_adapter_1013L_R5 as l5_shell_adapter
from . import prep_room_render_shell_registry_1013L_R0 as l0_shell_registry
from . import prep_room_xiaojiao_intent_frame_router_1013R_R27 as r27_router


STAGE_ID = "1013R_R28_ROOM_WORKSPACE_REGISTRY"
REGISTRY_ID = "SHIWEI_ROOM_WORKSPACE_REGISTRY_R0"


def _now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def boundary_flags() -> dict[str, bool]:
    flags = dict(r27_router.boundary_flags())
    flags.update(
        {
            "stage": STAGE_ID,
            "room_workspace_registry_defined": True,
            "derived_from_1013L_states": True,
            "static_registry_only": True,
            "new_room_runtime_created": False,
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


def _adapter_by_state_id() -> dict[str, dict[str, Any]]:
    return {item["state_id"]: item for item in l5_shell_adapter.state_fetch_adapters()}


def _prep_room_states() -> list[dict[str, Any]]:
    adapters = _adapter_by_state_id()
    states: list[dict[str, Any]] = []
    for state in l0_shell_registry.render_stage_registry().get("states", []):
        state_id = state.get("state_id")
        if state_id == "home_scene":
            continue
        adapter = adapters.get(str(state_id), {})
        states.append(
            {
                "state_id": state_id,
                "teacher_label": state.get("teacher_label"),
                "level": 2,
                "room_id": "prep_room",
                "room_label": "备课室",
                "render_stage_role": state.get("render_stage_role"),
                "source_backend": state.get("backend_source"),
                "route_or_adapter": state.get("route_or_adapter"),
                "active_capability": adapter.get("active_capability") or state_id,
                "readonly_endpoint": adapter.get("readonly_endpoint"),
                "fetch_policy": adapter.get("fetch_policy") or "registry_state_only",
                "status": state.get("status"),
            }
        )
    return states


def _future_room(room_id: str, label: str, xiaojiao_role: str, future_states: list[str]) -> dict[str, Any]:
    return {
        "room_id": room_id,
        "room_label": label,
        "level": 2,
        "xiaojiao_room_role": xiaojiao_role,
        "status": "future_placeholder",
        "states": [
            {
                "state_id": f"{room_id}_{state}",
                "teacher_label": state,
                "level": 2,
                "room_id": room_id,
                "room_label": label,
                "status": "not_implemented",
                "source_backend": None,
                "route_or_adapter": None,
                "active_capability": None,
                "fetch_policy": "future_registry_placeholder_only",
            }
            for state in future_states
        ],
    }


def build_room_workspace_registry() -> dict[str, Any]:
    marker_router = r27_router.build_router_fixture()
    agent_profile = l0_shell_registry.agent_profile_policy()
    prep_states = _prep_room_states()
    rooms = [
        {
            "room_id": "prep_room",
            "room_label": "备课室",
            "level": 2,
            "xiaojiao_room_role": "备课助理",
            "status": "active_from_1013L_registry",
            "states": prep_states,
        },
        _future_room("classroom", "教室", "课堂观察助理", ["课堂任务", "学生状态", "大屏控制"]),
        _future_room("research_room", "研究室", "复盘协作者", ["课例复盘", "教研问题链", "教研材料"]),
        _future_room("material_room", "资料室", "资料整理员", ["教材资料", "图片案例", "学生样例"]),
        _future_room("review_room", "评阅室", "评价助理", ["作品批次", "评价维度", "评语预览"]),
        _future_room("archive_room", "档案室", "成长记录员", ["课包归档", "学生画像", "班级证据"]),
    ]
    return {
        "ok": True,
        "stage": STAGE_ID,
        "registry_id": REGISTRY_ID,
        "generated_at": _now(),
        "consumes": {
            "r27_stage": marker_router.get("stage"),
            "l0_stage": l0_shell_registry.STAGE_ID,
            "l5_stage": l5_shell_adapter.STAGE_ID,
        },
        "agent_profile": {
            "display_name": agent_profile.get("default_display_name"),
            "same_agent_across_rooms": True,
            "routing_depends_on_display_name": False,
            "room_role_switching": True,
        },
        "registry_rule": {
            "derive_from_1013L_states_before_adding_new_rooms": True,
            "do_not_make_each_room_a_chat_page": True,
            "level_2_changes_work_context": True,
            "level_1_shell_stays_persistent": True,
        },
        "rooms": rooms,
        "active_room": {
            "room_id": "prep_room",
            "room_label": "备课室",
            "source": "R21 body[data-active-view='prepNotebook']",
        },
        "next_stage_recommendation": {
            "stage": "1013R_R29_TOOL_FRAME_REGISTRY",
            "why": "Room registry is derived from 1013L states; next derive level-3 tool frames from L5 active capabilities and R17/R24 render groups.",
        },
        "boundary": boundary_flags(),
    }


def build_room_registry_sample_bundle() -> dict[str, Any]:
    registry = build_room_workspace_registry()
    return {
        "stage": STAGE_ID,
        "room_workspace_registry": registry,
        "rooms": deepcopy(registry["rooms"]),
        "boundary": deepcopy(registry["boundary"]),
    }
