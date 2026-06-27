from __future__ import annotations

from copy import deepcopy
from datetime import datetime, timezone
from typing import Any

from . import prep_room_derivative_static_linkage_1013R_R19 as r19_linkage
from . import prep_room_render_blocks_protocol_1013R_R17 as r17_blocks
from . import prep_room_source_policy_validator_1013R_R16 as r16_policy
from . import prep_room_unified_viewmodel_1013R_R15 as r15_viewmodel


STAGE_ID = "1013R_R20_PREP_ROOM_UNIFIED_PACKAGE_READONLY_EXPORT_R0"
PACKAGE_ID = "SHIWEI_PREP_ROOM_UNIFIED_PACKAGE_READONLY_EXPORT_R0"
PACKAGE_TYPE = "prep_room_unified_protocol_package_readonly_export"


def _now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def boundary_flags() -> dict[str, bool]:
    flags = dict(r19_linkage.boundary_flags())
    flags.update(
        {
            "stage": STAGE_ID,
            "unified_package_readonly_export": True,
            "static_json_export_allowed": True,
            "route_registered": False,
            "endpoint_registered": False,
            "runtime_write_allowed": False,
            "existing_page_modified": False,
            "provider_called": False,
            "model_called": False,
            "database_written": False,
            "memory_written": False,
            "vector_index_written": False,
            "feishu_written": False,
            "formal_apply_performed": False,
            "courseware_export_created": False,
            "worksheet_export_created": False,
            "assessment_written": False,
            "R36_modified": False,
            "main_shell_modified": False,
        }
    )
    return flags


def _render_block_linkage_index(linkage: dict[str, Any]) -> dict[str, Any]:
    return {
        "courseware_script": {
            "derivative_object_id": "courseware_script",
            "linked_process_step_ids": [item.get("process_step_id") for item in linkage.get("process_derivative_links", [])],
        },
        "classroom_display_screen": {
            "derivative_object_id": "classroom_display_screen",
            "linked_process_step_ids": [item.get("process_step_id") for item in linkage.get("process_derivative_links", [])],
        },
        "worksheet": {
            "derivative_object_id": "worksheet",
            "linked_process_step_ids": [
                item.get("process_step_id")
                for item in linkage.get("process_derivative_links", [])
                if item.get("worksheet", {}).get("render_state") in {"preview", "placeholder"}
            ],
        },
        "assessment_rubric": {
            "derivative_object_id": "assessment_rubric",
            "linked_process_step_ids": [item.get("process_step_id") for item in linkage.get("process_derivative_links", [])],
            "render_state": "blocked_until_teacher_dimension",
        },
    }


def build_unified_package() -> dict[str, Any]:
    viewmodel = r15_viewmodel.build_unified_viewmodel()
    source_policy_result = r16_policy.build_source_policy_result(viewmodel)
    render_blocks_protocol = r17_blocks.build_render_blocks_protocol()
    derivative_linkage = r19_linkage.build_derivative_linkage(viewmodel)
    render_block_linkage_index = _render_block_linkage_index(derivative_linkage)

    return {
        "ok": True,
        "stage": STAGE_ID,
        "package_id": PACKAGE_ID,
        "package_type": PACKAGE_TYPE,
        "generated_at": _now(),
        "human_name": "R20：备课室统一协议包只读出口",
        "current_object": deepcopy(viewmodel.get("current_object", {})),
        "task_state": deepcopy(viewmodel.get("task_state", {})),
        "teacher_action_gate": deepcopy(viewmodel.get("action_gate", {})),
        "source_policy_result": source_policy_result,
        "render_blocks": deepcopy(render_blocks_protocol.get("render_blocks", [])),
        "render_block_groups": deepcopy(render_blocks_protocol.get("block_groups", [])),
        "render_block_linkage_index": render_block_linkage_index,
        "derivative_linkage": derivative_linkage,
        "lesson_viewmodel": deepcopy(viewmodel.get("lesson_viewmodel", {})),
        "package_contract": {
            "page_should_consume": [
                "current_object",
                "task_state",
                "teacher_action_gate",
                "source_policy_result",
                "render_blocks",
                "render_block_linkage_index",
                "derivative_linkage",
            ],
            "page_must_not": [
                "register_route",
                "call_provider",
                "write_database",
                "write_memory",
                "formal_apply",
                "treat_ai_draft_as_standard",
            ],
            "route_or_endpoint_status": "not_registered_static_readonly_export_only",
        },
        "contracts_consumed": {
            "r15_stage": viewmodel.get("stage"),
            "r16_stage": source_policy_result.get("stage"),
            "r17_stage": render_blocks_protocol.get("stage"),
            "r19_stage": derivative_linkage.get("stage"),
        },
        "next_stage_recommendation": {
            "stage": "1013R_R21_PAGE_COPY_BINDS_UNIFIED_PACKAGE",
            "why": "统一协议包已合成；下一步只做页面副本读取这个包，验证老师能看到任务状态、来源、确认门和派生对象联动。",
        },
        "boundary": boundary_flags(),
    }


def build_package_sample_bundle() -> dict[str, Any]:
    package = build_unified_package()
    return {
        "stage": STAGE_ID,
        "unified_package": package,
        "render_blocks": deepcopy(package["render_blocks"]),
        "derivative_linkage": deepcopy(package["derivative_linkage"]),
        "boundary": deepcopy(package["boundary"]),
    }
