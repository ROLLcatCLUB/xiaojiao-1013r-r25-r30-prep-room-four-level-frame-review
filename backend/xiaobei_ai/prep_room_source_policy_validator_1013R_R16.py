from __future__ import annotations

from copy import deepcopy
from datetime import datetime, timezone
from typing import Any

from . import prep_room_unified_viewmodel_1013R_R15 as r15_viewmodel


STAGE_ID = "1013R_R16_SOURCE_POLICY_LIGHT_VALIDATOR_R0"
VALIDATOR_ID = "SHIWEI_SOURCE_POLICY_LIGHT_VALIDATOR_R0"


def _now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def boundary_flags() -> dict[str, bool]:
    flags = dict(r15_viewmodel.boundary_flags())
    flags.update(
        {
            "stage": STAGE_ID,
            "source_policy_light_validator_readonly": True,
            "source_policy_validator_defined": True,
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


def _source_categories(viewmodel: dict[str, Any]) -> set[str]:
    return set(viewmodel.get("source_policy", {}).get("source_categories", []))


def _ai_reference_source_ids(viewmodel: dict[str, Any]) -> list[str]:
    ids: list[str] = []
    for item in viewmodel.get("source_policy", {}).get("source_matrix", []):
        if item.get("authority_status") == "ai_generated_reference_only":
            ids.append(str(item.get("source_id")))
    return ids


def build_source_policy_result(viewmodel: dict[str, Any] | None = None) -> dict[str, Any]:
    if viewmodel is None:
        viewmodel = r15_viewmodel.build_unified_viewmodel()
    categories = _source_categories(viewmodel)
    current_object = viewmodel.get("current_object", {})
    source_policy = viewmodel.get("source_policy", {})
    task_state = viewmodel.get("task_state", {})
    action_gate = viewmodel.get("action_gate", {})
    blocked_actions = {
        item.get("action_id"): item
        for item in action_gate.get("action_matrix", [])
        if not item.get("allowed_now")
    }
    missing_ids = {item.get("id") for item in task_state.get("missing_materials", [])}
    checks = [
        {
            "check_id": "current_object_has_textbook_anchor",
            "label": "当前课题必须有教材锚点",
            "status": "pass" if "textbook_anchor" in categories and current_object.get("title") == "2-1《色彩的渐变》" else "fail",
            "evidence": current_object,
        },
        {
            "check_id": "ai_draft_not_standard",
            "label": "AI 草案不能作为教材标准",
            "status": "pass" if source_policy.get("ai_draft_may_not_be_standard") else "fail",
            "evidence": {"ai_reference_source_ids": _ai_reference_source_ids(viewmodel)},
        },
        {
            "check_id": "source_categories_present",
            "label": "来源分类必须齐全",
            "status": (
                "pass"
                if {"textbook_anchor", "teacher_input", "ai_draft", "system_structure"}.issubset(categories)
                else "fail"
            ),
            "evidence": {"source_categories": sorted(categories)},
        },
        {
            "check_id": "assessment_blocked_until_materials",
            "label": "缺学生作品和评价维度时评价表必须阻断",
            "status": (
                "pass"
                if "student_work_samples" in missing_ids
                and "assessment_dimensions" in missing_ids
                and "preview_assessment_rubric" in blocked_actions
                else "fail"
            ),
            "evidence": {
                "missing_materials": sorted(str(item) for item in missing_ids),
                "blocked_action": blocked_actions.get("preview_assessment_rubric"),
            },
        },
        {
            "check_id": "memory_write_blocked",
            "label": "记忆写入必须后置",
            "status": "pass" if "write_memory_or_archive" in blocked_actions else "fail",
            "evidence": blocked_actions.get("write_memory_or_archive"),
        },
    ]
    failed = [item["check_id"] for item in checks if item["status"] != "pass"]
    return {
        "ok": not failed,
        "stage": STAGE_ID,
        "validator_id": VALIDATOR_ID,
        "generated_at": _now(),
        "consumes": {
            "unified_viewmodel_stage": viewmodel.get("stage"),
            "viewmodel_type": viewmodel.get("viewmodel_type"),
            "current_object": deepcopy(current_object),
        },
        "checks": checks,
        "failed_checks": failed,
        "source_policy_summary": {
            "textbook_anchor": "可作为当前课题、单元、页码和教材对象依据。",
            "teacher_input": "可作为当前任务输入和课堂条件依据。",
            "ai_draft": "只能作为草稿或参考，不能升格为教材标准、字段标准或正式评价依据。",
            "system_structure": "只负责渲染和门控，不等同于教学内容依据。",
        },
        "next_stage_recommendation": {
            "stage": "1013R_R17_RENDER_BLOCKS_PROTOCOL_R0",
            "why": "来源轻校验通过后，可以把统一 ViewModel 转成 render_blocks 协议，供后续轻量渲染适配器消费。",
        },
        "boundary": boundary_flags(),
    }


def build_validator_sample_bundle() -> dict[str, Any]:
    result = build_source_policy_result()
    return {
        "stage": STAGE_ID,
        "source_policy_result": result,
        "boundary": deepcopy(result["boundary"]),
    }
