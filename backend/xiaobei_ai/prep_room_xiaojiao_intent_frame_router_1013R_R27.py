from __future__ import annotations

from copy import deepcopy
from datetime import datetime, timezone
from typing import Any

from . import prep_room_page_copy_four_level_markers_1013R_R26 as r26_markers
from .system_semantic_interaction_runtime import action_policy, command_dsl


STAGE_ID = "1013R_R27_XIAOJIAO_INTENT_FRAME_ROUTER_FIXTURE"
ROUTER_ID = "SHIWEI_XIAOJIAO_INTENT_FRAME_ROUTER_FIXTURE_R0"


FRAME_LEVELS = {
    1: {
        "level_key": "platform_shell",
        "teacher_name": "平台外壳框架",
        "target_marker": "data-shiwei-frame-level=1",
    },
    2: {
        "level_key": "room_workspace",
        "teacher_name": "各室工作空间框架",
        "target_marker": "data-shiwei-frame-level=2",
    },
    3: {
        "level_key": "tool_frame",
        "teacher_name": "工具框架",
        "target_marker": "data-shiwei-frame-level=3",
    },
    4: {
        "level_key": "content_rendering",
        "teacher_name": "内容框架",
        "target_marker": "data-shiwei-frame-level=4",
    },
}


def _now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def boundary_flags() -> dict[str, bool]:
    flags = dict(r26_markers.boundary_flags())
    flags.update(
        {
            "stage": STAGE_ID,
            "intent_frame_router_fixture_defined": True,
            "static_fixture_only": True,
            "runtime_router_connected": False,
            "semantic_runtime_called": False,
            "provider_called": False,
            "model_called": False,
            "database_written": False,
            "memory_written": False,
            "vector_index_written": False,
            "feishu_written": False,
            "formal_apply_performed": False,
            "route_registered": False,
            "endpoint_registered": False,
            "R36_modified": False,
            "main_shell_modified": False,
            "new_disconnected_page_created": False,
        }
    )
    return flags


def route_intent_static(message: str) -> dict[str, Any]:
    text = str(message or "").strip()
    state = {"candidate_exists": True}
    operation = action_policy.detect_operation(text, state)
    reasons: list[str] = []
    levels: list[int] = []

    if any(token in text for token in ["顶部", "下面输入栏", "输入栏", "搜索", "通知", "全局", "账号"]):
        levels.append(1)
        reasons.append("mentions_global_shell_or_bottom_entry")
    if any(token in text for token in ["备课室", "教室", "研究室", "教研室", "资料室", "知识馆", "评阅室", "档案室", "切到", "进入"]):
        levels.append(2)
        reasons.append("mentions_room_or_workspace_switch")
    if any(token in text for token in ["工具", "按钮", "入口", "课件", "大屏", "资料", "评价表", "学习单", "生成"]):
        levels.append(3)
        reasons.append("mentions_tool_or_action_frame")
    if any(token in text for token in ["教案", "段落", "章节", "教学过程", "本课依据", "学情", "目标", "内容", "这份"]):
        levels.append(4)
        reasons.append("mentions_rendered_lesson_content")
    if any(token in text for token in ["整体很乱", "页面整体", "很乱", "找不到"]):
        levels = [1, 2, 3, 4] if "很乱" in text or "页面整体" in text else sorted(set([2, 3] + levels))
        reasons.append("requires_recursive_diagnosis")
    if not levels:
        levels = [4]
        reasons.append("fallback_to_current_content_context")

    ordered_levels = []
    for level in [1, 2, 3, 4]:
        if level in levels and level not in ordered_levels:
            ordered_levels.append(level)

    primary = ordered_levels[0]
    command_type = {
        "formal_action": "ASK_CONFIRMATION",
        "modify": "MODIFY_CANDIDATE",
        "create": "GENERATE_CANDIDATE",
        "clarify_or_continue": "CLARIFY_KEY_SLOT" if primary in {2, 3} else "NOOP",
    }.get(operation, "NOOP")
    if "保存" in text or "导出" in text or "写入" in text or "正式" in text:
        command_type = "ASK_CONFIRMATION"

    return {
        "message": text,
        "operation": operation,
        "primary_level": primary,
        "primary_level_key": FRAME_LEVELS[primary]["level_key"],
        "level_path": [
            {
                "level": level,
                "level_key": FRAME_LEVELS[level]["level_key"],
                "teacher_name": FRAME_LEVELS[level]["teacher_name"],
                "target_marker": FRAME_LEVELS[level]["target_marker"],
            }
            for level in ordered_levels
        ],
        "route_reasons": reasons,
        "command_type": command_type,
        "command_allowed_by_existing_dsl": command_type in command_dsl.COMMAND_TYPE_SET,
        "teacher_confirmation_required": command_type == "ASK_CONFIRMATION",
        "formal_apply_allowed": False,
        "runtime_call_allowed": False,
        "model_call_allowed": False,
    }


def fixture_messages() -> list[str]:
    return [
        "切到备课室",
        "下面输入栏不好用",
        "备课室工具按钮太乱",
        "这份教案内容层级不清",
        "为什么我找不到课件生成入口",
        "这个页面整体很乱",
        "把这个教学过程段落改得更适合公开课",
        "保存到课包并导出课件",
    ]


def build_router_fixture() -> dict[str, Any]:
    marker_contract = r26_markers.build_marker_contract()
    routes = [route_intent_static(message) for message in fixture_messages()]
    return {
        "ok": True,
        "stage": STAGE_ID,
        "router_id": ROUTER_ID,
        "generated_at": _now(),
        "consumes": {
            "r26_stage": marker_contract.get("stage"),
            "marker_id": marker_contract.get("marker_id"),
            "command_dsl_command_types": deepcopy(command_dsl.COMMAND_TYPES),
            "action_policy_markers": {
                "formal_action_markers": deepcopy(action_policy.FORMAL_ACTION_MARKERS),
                "modify_markers": deepcopy(action_policy.MODIFY_MARKERS),
                "generate_markers": deepcopy(action_policy.GENERATE_MARKERS),
            },
        },
        "frame_levels": deepcopy(FRAME_LEVELS),
        "routing_policy": {
            "route_intent_by_framework_level": True,
            "diagnose_issues_by_framework_level": True,
            "recursive_order": [1, 2, 3, 4],
            "cross_level_intent_must_be_split": True,
            "use_frame_markers_before_dom_operation": True,
            "teacher_confirmation_required_for_formal_actions": True,
            "formal_apply_allowed": False,
        },
        "fixture_routes": routes,
        "next_stage_recommendation": {
            "stage": "1013R_R28_ROOM_WORKSPACE_REGISTRY",
            "why": "Intent can now route to frame levels in static fixture form; next derive room registry from the existing 1013L shell states.",
        },
        "boundary": boundary_flags(),
    }


def build_router_sample_bundle() -> dict[str, Any]:
    router = build_router_fixture()
    return {
        "stage": STAGE_ID,
        "router_fixture": router,
        "fixture_routes": deepcopy(router["fixture_routes"]),
        "boundary": deepcopy(router["boundary"]),
    }
