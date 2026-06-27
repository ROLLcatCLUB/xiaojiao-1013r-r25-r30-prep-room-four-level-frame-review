from __future__ import annotations

from copy import deepcopy
from datetime import datetime, timezone
from typing import Any

from . import prep_room_page_copy_package_binding_1013R_R21 as r21_binding


STAGE_ID = "1013R_R22_TEACHER_READABILITY_AND_2K_LINKAGE_SMOKE"
SMOKE_ID = "SHIWEI_PREP_ROOM_TEACHER_READABILITY_2K_SMOKE_R0"


def _now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def boundary_flags() -> dict[str, bool]:
    flags = dict(r21_binding.boundary_flags())
    flags.update(
        {
            "stage": STAGE_ID,
            "teacher_readability_smoke_defined": True,
            "visual_2k_check_expected": True,
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


def build_teacher_readability_smoke(html: str | None = None) -> dict[str, Any]:
    if html is None:
        html = r21_binding.build_page_copy_html()
    checks = [
        {
            "check_id": "current_object_first_screen",
            "label": "第一眼知道当前课题",
            "pass": "2-1《色彩的渐变》" in html and "备课室" in html,
        },
        {
            "check_id": "xiaojiao_task_state_visible",
            "label": "第一眼知道小教正在判断备课任务",
            "pass": "小教任务状态" in html and "小教判断" in html,
        },
        {
            "check_id": "known_missing_suggested_visible",
            "label": "已知材料 / 缺口 / 动作可见",
            "pass": all(token in html for token in ["已知材料", "还缺", "教师确认动作"]),
        },
        {
            "check_id": "render_blocks_visible",
            "label": "render_blocks 不是只躺在 JSON 里",
            "pass": '"render_blocks"' in html and "model.views.prepNotebook.current_lesson" in html,
        },
        {
            "check_id": "prototype_base_preserved",
            "label": "页面仍在原型里，不另起静态页，也不外贴协议带",
            "pass": "data-1013j-prep-start=\"true\"" in html
            and "script-1013R-R21-internal-prototype-binding" in html
            and "r21-prototype-protocol-band" not in html
            and len(html.encode("utf-8")) >= 900000,
        },
        {
            "check_id": "derivatives_visible",
            "label": "课件 / 大屏 / 学习单 / 评价表都有可见入口",
            "pass": all(token in html for token in ["课件", "大屏", "学习单", "评价表"])
            and "derivative_linkage" in html
            and ".nb-flow-step" in html
            and "r21-derived-mini" in html,
        },
        {
            "check_id": "teaching_process_expanded",
            "label": "教学过程不是一行摘要，已恢复多微环节",
            "pass": all(
                token in html
                for token in [
                    "restoreProcessStepDetails",
                    "data-r21-process-restored",
                    "readable_details",
                    "展现差异",
                    "指认方向",
                    "学生试色",
                    "保留调整",
                    "同伴反馈",
                ]
            ),
        },
        {
            "check_id": "big_unit_edit_card_grammar",
            "label": "大单元编辑也复用修改卡片语法",
            "pass": all(
                token in html
                for token in [
                    "ensureBigUnitEditActions",
                    "enhanceBigUnitParagraphRows",
                    "openBigUnitSingleLessonBubble",
                    "rememberBigUnitRowIntent",
                    "bindBigUnitRowIntentCapture",
                    "activeBigUnitItemForEdit",
                    "renderBigUnitEditModal",
                    "polishBigUnitEditModal",
                    "data-r21-big-unit-lines",
                    "data-r21-big-unit-row",
                    "data-r21-big-unit-numbered-rows",
                    "r21-big-unit-line",
                    "data-r21-big-unit-before",
                    "data-r21-big-unit-after",
                    "data-r21-big-unit-advice",
                    "data-r21-big-unit-actions",
                    "r6p-modal-impact-help",
                ]
            ),
        },
        {
            "check_id": "source_policy_quiet_visible",
            "label": "来源提示能看见但不压过主任务",
            "pass": "资料来源轻校验" in html and "source_policy_checks" in html,
        },
        {
            "check_id": "not_chatbox",
            "label": "不是 AI 聊天框",
            "pass": "请输入你的问题" not in html and "告诉小教你要推进哪一步" in html,
        },
    ]
    return {
        "ok": all(item["pass"] for item in checks),
        "stage": STAGE_ID,
        "smoke_id": SMOKE_ID,
        "generated_at": _now(),
        "consumes": {
            "r21_stage": r21_binding.STAGE_ID,
            "r21_binding_id": r21_binding.BINDING_ID,
        },
        "checks": checks,
        "failed_checks": [item["check_id"] for item in checks if not item["pass"]],
        "visual_expectation": {
            "viewport": "2560x1440",
            "should_capture_screenshot": True,
            "should_not_require_dev_server": True,
        },
        "next_stage_recommendation": {
            "stage": "1013R_R23_PREP_ROOM_TEACHER_WALKTHROUGH_SCRIPT",
            "why": "R22 已从老师视角检查可读性与可见联动；下一步应把老师怎么走一遍备课室流程写成走查脚本。",
        },
        "boundary": boundary_flags(),
    }


def build_smoke_sample_bundle() -> dict[str, Any]:
    html = r21_binding.build_page_copy_html()
    smoke = build_teacher_readability_smoke(html)
    return {
        "stage": STAGE_ID,
        "teacher_readability_smoke": smoke,
        "html": html,
        "boundary": deepcopy(smoke["boundary"]),
    }
