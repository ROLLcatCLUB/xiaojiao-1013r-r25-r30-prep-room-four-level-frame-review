from __future__ import annotations

from copy import deepcopy
from datetime import datetime, timezone
from typing import Any

from . import prep_room_teacher_readability_smoke_1013R_R22 as r22_smoke
from . import prep_room_unified_package_readonly_export_1013R_R20 as r20_package


STAGE_ID = "1013R_R23_PREP_ROOM_TEACHER_WALKTHROUGH_SCRIPT"
SCRIPT_ID = "SHIWEI_PREP_ROOM_TEACHER_WALKTHROUGH_SCRIPT_R0"


def _now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def boundary_flags() -> dict[str, bool]:
    flags = dict(r22_smoke.boundary_flags())
    flags.update(
        {
            "stage": STAGE_ID,
            "teacher_walkthrough_script_defined": True,
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


def build_teacher_walkthrough_script() -> dict[str, Any]:
    package = r20_package.build_unified_package()
    current = package.get("current_object", {})
    return {
        "ok": True,
        "stage": STAGE_ID,
        "script_id": SCRIPT_ID,
        "generated_at": _now(),
        "current_object": deepcopy(current),
        "consumes": {
            "r20_stage": package.get("stage"),
            "r22_stage": r22_smoke.STAGE_ID,
        },
        "walkthrough_steps": [
            {
                "step_id": "open_prep_room",
                "teacher_action": "老师打开备课室页面副本。",
                "expected_system_state": "第一屏显示备课室、三年级第二单元第1课《色彩的渐变》和小教判断。",
                "pass_signal": "不是空白聊天框，当前对象和小教任务状态同时可见。",
            },
            {
                "step_id": "read_known_and_missing",
                "teacher_action": "老师先看已知材料和缺口。",
                "expected_system_state": "系统区分教材依据、教师输入、AI 草案和系统结构，并显示学生样例、评价维度等缺口。",
                "pass_signal": "老师能知道下一步需要补什么，而不是只看到一篇长文。",
            },
            {
                "step_id": "preview_display",
                "teacher_action": "老师选择查看大屏呈现预览。",
                "expected_system_state": "页面显示教学过程对应的大屏提示，但不导出、不保存。",
                "pass_signal": "大屏是派生对象预览，仍在确认门内。",
            },
            {
                "step_id": "preview_courseware",
                "teacher_action": "老师查看课件脚本。",
                "expected_system_state": "课件脚本与教学环节联动，显示预览状态。",
                "pass_signal": "课件脚本不是独立长文，而是挂在课堂过程上。",
            },
            {
                "step_id": "try_assessment",
                "teacher_action": "老师尝试做评价表。",
                "expected_system_state": "系统提示缺少学生作品样例和评价维度，评价表处于阻断状态。",
                "pass_signal": "小教没有越过老师直接生成正式评价。",
            },
            {
                "step_id": "teacher_confirm_next",
                "teacher_action": "老师选择继续补充备课要求。",
                "expected_system_state": "输入框提示为“告诉小教你要推进哪一步”。",
                "pass_signal": "输入框是工作推进入口，不是产品中心。",
            },
        ],
        "acceptance": [
            "老师能说出当前正在备哪一课。",
            "老师能说出小教已经知道什么、还缺什么。",
            "老师能看到课件、大屏、学习单、评价表是备课包的派生对象。",
            "老师能区分预览动作、需要确认动作和阻断动作。",
            "老师不会误以为系统已经正式保存、导出或写入评价。",
        ],
        "next_stage_recommendation": {
            "stage": "1013R_R24_RENDER_BLOCK_COMPONENT_BOUNDARY_MAP",
            "why": "走查脚本已定义教师使用路径；下一步把 render_blocks 映射到未来组件边界，为渲染底座做准备。",
        },
        "boundary": boundary_flags(),
    }


def build_walkthrough_sample_bundle() -> dict[str, Any]:
    script = build_teacher_walkthrough_script()
    return {
        "stage": STAGE_ID,
        "teacher_walkthrough_script": script,
        "walkthrough_steps": deepcopy(script["walkthrough_steps"]),
        "boundary": deepcopy(script["boundary"]),
    }
