from __future__ import annotations

from copy import deepcopy
from datetime import datetime, timezone
from typing import Any

from . import prep_room_light_render_adapter_1013R_R18 as r18_adapter
from . import prep_room_unified_viewmodel_1013R_R15 as r15_viewmodel


STAGE_ID = "1013R_R19_DERIVATIVE_OBJECT_STATIC_LINKAGE_SAMPLE"
LINKAGE_ID = "SHIWEI_PREP_ROOM_DERIVATIVE_OBJECT_LINKAGE_R0"


def _now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def boundary_flags() -> dict[str, bool]:
    flags = dict(r18_adapter.boundary_flags())
    flags.update(
        {
            "stage": STAGE_ID,
            "derivative_object_linkage_readonly": True,
            "derivative_static_linkage_defined": True,
            "route_registered": False,
            "existing_page_modified": False,
            "runtime_write_allowed": False,
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


def _screen_for_step(screens: list[dict[str, Any]], index: int) -> dict[str, Any]:
    if not screens:
        return {}
    return deepcopy(screens[min(index, len(screens) - 1)])


def build_derivative_linkage(viewmodel: dict[str, Any] | None = None) -> dict[str, Any]:
    if viewmodel is None:
        viewmodel = r15_viewmodel.build_unified_viewmodel()
    lesson = viewmodel.get("lesson_viewmodel", {}).get("current_lesson", {})
    steps = lesson.get("process_steps", [])
    screens = viewmodel.get("lesson_viewmodel", {}).get("courseware_screens", [])
    links: list[dict[str, Any]] = []
    for index, step in enumerate(steps):
        screen = _screen_for_step(screens, index + 1)
        links.append(
            {
                "link_id": f"link_{index + 1}_{step.get('id')}",
                "process_step_id": step.get("id"),
                "process_step_title": step.get("title"),
                "courseware_screen": {
                    "screen_no": screen.get("screen_no"),
                    "title": screen.get("title"),
                    "role": screen.get("role"),
                    "status": screen.get("status"),
                },
                "classroom_display": {
                    "screen_seed": step.get("screen_seed"),
                    "student_visible_prompt": lesson.get("big_screen_short_text", [None])[index % len(lesson.get("big_screen_short_text", [None]))],
                    "render_state": "preview",
                },
                "worksheet": {
                    "capture_prompt": step.get("evidence"),
                    "render_state": "placeholder" if step.get("id") not in {"explore", "share"} else "preview",
                    "requires_teacher_confirmation": True,
                },
                "assessment_rubric": {
                    "evidence": step.get("evidence"),
                    "render_state": "blocked_until_teacher_dimension",
                    "blocked_by": ["student_work_samples", "assessment_dimensions"],
                },
            }
        )
    return {
        "ok": True,
        "stage": STAGE_ID,
        "linkage_id": LINKAGE_ID,
        "generated_at": _now(),
        "consumes": {
            "unified_viewmodel_stage": viewmodel.get("stage"),
            "light_render_adapter_stage": r18_adapter.STAGE_ID,
            "current_object": deepcopy(viewmodel.get("current_object", {})),
        },
        "derivative_objects": [
            {
                "object_id": "courseware_script",
                "label": "课件脚本",
                "slot_id": "courseware_script",
                "current_state": "preview",
                "formal_output_created": False,
            },
            {
                "object_id": "classroom_display_screen",
                "label": "大屏呈现",
                "slot_id": "classroom_display_screen",
                "current_state": "preview",
                "formal_output_created": False,
            },
            {
                "object_id": "worksheet",
                "label": "学习单",
                "slot_id": "worksheet",
                "current_state": "placeholder_with_preview_hooks",
                "formal_output_created": False,
            },
            {
                "object_id": "assessment_rubric",
                "label": "评价表",
                "slot_id": "assessment_rubric",
                "current_state": "blocked_until_teacher_dimension",
                "formal_output_created": False,
            },
        ],
        "process_derivative_links": links,
        "static_linkage_summary": {
            "process_step_count": len(steps),
            "courseware_screen_count": len(screens),
            "linked_step_count": len(links),
            "assessment_blocked": True,
            "exports_created": False,
        },
        "teacher_visible_next_actions": [
            "先确认大屏预览是否按教学过程走。",
            "补学生作品样例后再开放评价表预览。",
            "课件脚本仍是预览，不导出 PPT。",
            "学习单只做轻量记录，不写入正式课包。",
        ],
        "next_stage_recommendation": {
            "stage": "1013R_R20_PREP_ROOM_UNIFIED_PACKAGE_READONLY_EXPORT_R0",
            "why": "R16-R19 已完成协议到轻量渲染与派生物联动；下一步先合成页面可消费的只读协议包，不注册真实 route，仍不 formal apply。",
        },
        "boundary": boundary_flags(),
    }


def build_linkage_sample_bundle() -> dict[str, Any]:
    linkage = build_derivative_linkage()
    return {
        "stage": STAGE_ID,
        "derivative_linkage": linkage,
        "process_derivative_links": deepcopy(linkage["process_derivative_links"]),
        "boundary": deepcopy(linkage["boundary"]),
    }
