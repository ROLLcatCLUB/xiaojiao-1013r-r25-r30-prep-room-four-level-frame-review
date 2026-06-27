from __future__ import annotations

from copy import deepcopy
from datetime import datetime, timezone
from typing import Any

from flask import jsonify, request

from . import prep_room_task_state_bridge_1013R_R6 as task_state_bridge


STAGE_ID = "1013R_R10_PREP_ROOM_SINGLE_LESSON_VIEWMODEL_READONLY_ENDPOINT"
TASK_ID = "g3_u2_l1_color_gradient"
VIEWMODEL_ROUTE = f"/api/prep-room/single-lesson-viewmodel/{TASK_ID}"
ACTION_ROUTE = f"/api/prep-room/single-lesson-viewmodel/{TASK_ID}/action"


def _now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def boundary_flags() -> dict[str, bool]:
    flags = dict(task_state_bridge.boundary_flags())
    flags.update(
        {
            "stage": STAGE_ID,
            "single_lesson_viewmodel_readonly": True,
            "render_hydration_ready": True,
            "text_replace_bridge_only": False,
            "runtime_connected": True,
            "runtime_write_allowed": False,
            "formal_frontend_binding_performed": False,
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


def build_lesson_tree() -> list[dict[str, Any]]:
    tree: list[dict[str, Any]] = []
    for unit in task_state_bridge.TEXTBOOK_CATALOG:
        unit_no = unit["unit_no"]
        unit_code = f"u{unit_no}" if isinstance(unit_no, int) else str(unit_no)
        tree.append(
            {
                "id": unit_code,
                "label": unit["unit_title"],
                "type": "unit",
                "unit_no": unit_no,
                "lessons": [
                    {
                        "id": f"{unit_code}_l{lesson['lesson_no']}",
                        "code": f"{lesson['lesson_no']}",
                        "title": lesson["lesson_title"],
                        "page": lesson["page"],
                        "active": unit_no == 2 and lesson["lesson_no"] == 1,
                    }
                    for lesson in unit["lessons"]
                ],
            }
        )
    return tree


def build_current_lesson() -> dict[str, Any]:
    return {
        "id": TASK_ID,
        "title": "2-1《色彩的渐变》",
        "eyebrow": "第二单元 多彩的世界",
        "textbook_page": "教材第6-7页",
        "status": "待确认",
        "flow": ["教材锚点", "备课正文", "课堂大屏", "学习单", "作品证据", "教师确认"],
        "badges": [
            "真实教材锚点",
            "教材第6-7页图像",
            "旧 AI 资料降级为参考",
            "只读 runtime",
        ],
        "sections": [
            {
                "id": "basis",
                "title": "一、本课依据",
                "items": [
                    "本课对应三年级第二单元《多彩的世界》第1课《色彩的渐变》，教材页码为第6页。",
                    "教材呈现自然中的色彩渐变、色彩明度与纯度变化、渐变排列游戏和学生作品。",
                    "本地旧 AI 教学资料只能作为渐变技法参考，不能作为教材标准或字段标准。",
                ],
            },
            {
                "id": "analysis",
                "title": "二、学情分析",
                "items": [
                    "三年级学生能直观看到颜色深浅、浓淡和鲜灰差异，但容易把渐变理解为把几种颜色并排涂上去。",
                    "他们需要通过色卡排列、颜料试色或纸条排序，把颜色慢慢变化的规律变成可操作步骤。",
                    "本版学情是备课预设，后续应接入课堂记录和教师确认修正。",
                ],
            },
            {
                "id": "goals",
                "title": "三、教学目标",
                "items": [
                    "观察自然和作品中的色彩渐变，知道明度、纯度会影响渐变效果。",
                    "能用调色、拼摆或绘画方式表现有秩序的色彩渐变。",
                    "感受色彩渐变带来的节奏、层次和视觉美感。",
                ],
            },
            {
                "id": "keypoints",
                "title": "四、教学重难点",
                "items": [
                    "重点：发现色彩由深到浅、由鲜到灰、由一种颜色逐步过渡到另一种颜色的变化。",
                    "难点：让渐变有规律、有层次，不变成随意涂色或简单排色。",
                ],
            },
            {
                "id": "preparation",
                "title": "五、教学准备",
                "items": [
                    "教师准备教材页图、渐变色阶示例、试色纸和可视化调色步骤。",
                    "学生准备水彩笔、油画棒或水粉材料，保留试色过程作为证据。",
                ],
            },
            {
                "id": "assessment",
                "title": "六、学习单与评价",
                "items": [
                    "学习单只记录色阶顺序、调色发现和一次修改理由。",
                    "评价看试色证据、渐变秩序、作品应用和表达说明，不只看画面是否漂亮。",
                ],
            },
            {
                "id": "reflection",
                "title": "七、教师待确认",
                "items": [
                    "是否优先用颜料调色，还是用纸条拼摆降低操作难度。",
                    "是否把第2课《渐变的节奏》和第3课《多彩的生活》作为本课延展预告。",
                ],
            },
        ],
        "process_steps": [
            {
                "id": "intro",
                "title": "看见渐变",
                "teacher_action": "出示自然图片和教材页，引导学生找从明到暗、从鲜到灰的变化。",
                "student_action": "用手指沿色带说出颜色怎样慢慢变化。",
                "screen_seed": "一张自然渐变图 + 5格色阶",
                "evidence": "学生能指出变化方向。",
            },
            {
                "id": "sense",
                "title": "比较明度与纯度",
                "teacher_action": "用同一种颜色加入白色、黑色或灰色，展示明度和纯度变化。",
                "student_action": "比较哪一格更亮、哪一格更灰，并尝试排序。",
                "screen_seed": "明度变化 / 纯度变化 对照",
                "evidence": "学生完成色阶排序。",
            },
            {
                "id": "explore",
                "title": "做渐变实验",
                "teacher_action": "示范少量多次加色，提醒每一步只改变一点点。",
                "student_action": "在试色纸上完成3到5格渐变色阶。",
                "screen_seed": "调色步骤：原色 -> 加白/加水 -> 逐格变化",
                "evidence": "试色纸保留过程。",
            },
            {
                "id": "make",
                "title": "把渐变用到画面",
                "teacher_action": "提示把渐变用于动物、植物、建筑或校园空间。",
                "student_action": "选择一个对象，把渐变规律转化为画面层次。",
                "screen_seed": "学生作品参考：鸟、鲸、纸构空间",
                "evidence": "作品中出现清晰渐变区域。",
            },
            {
                "id": "share",
                "title": "说出修改理由",
                "teacher_action": "组织学生用一句话说明自己的渐变方向和调整原因。",
                "student_action": "展示作品和试色纸，说出保留或修改的一处。",
                "screen_seed": "我用了__到__的渐变，因为__。",
                "evidence": "学生能用证据说明作品。",
            },
        ],
        "big_screen_short_text": [
            "颜色慢慢变，层次就出现。",
            "每一步只变一点点。",
            "试色纸也是作品证据。",
        ],
    }


def build_courseware_screens() -> list[dict[str, Any]]:
    return [
        {"screen_no": 1, "title": "色彩的渐变", "role": "本课方向", "status": "已有文字"},
        {"screen_no": 2, "title": "看色彩图片", "role": "导入观察", "status": "待补图"},
        {"screen_no": 3, "title": "比较两组颜色", "role": "比较变化", "status": "待补图"},
        {"screen_no": 4, "title": "感觉词卡", "role": "比较变化", "status": "已有文字"},
        {"screen_no": 5, "title": "色彩实验任务", "role": "色彩实验", "status": "待补图"},
        {"screen_no": 6, "title": "白板试色", "role": "色彩实验", "status": "可白板"},
        {"screen_no": 7, "title": "学生作品展示", "role": "展示评价", "status": "待学生作品"},
        {"screen_no": 8, "title": "总结回看", "role": "展示评价", "status": "已有文字"},
    ]


def build_single_lesson_viewmodel() -> dict[str, Any]:
    task_state = task_state_bridge.build_task_state()
    return {
        "ok": True,
        "stage": STAGE_ID,
        "viewmodel_type": "prep_room_single_lesson_readonly",
        "viewmodel_id": TASK_ID,
        "generated_at": _now(),
        "route": {
            "viewmodel": VIEWMODEL_ROUTE,
            "action": ACTION_ROUTE,
            "task_state_source": task_state_bridge.TASK_ROUTE,
        },
        "render_contract": {
            "target_stage": "existing_page_static_preview_hydration_next",
            "renderer_should_consume": [
                "task_object",
                "prep_view_patch.lesson_tree",
                "prep_view_patch.current_lesson",
                "courseware_screen_patch",
                "source_matrix",
                "runtime_actions",
                "boundary",
            ],
            "renderer_must_not": [
                "replace_visible_text_by_walker",
                "treat_ai_reference_as_standard",
                "write_database_or_memory",
                "formal_apply",
            ],
        },
        "task_object": deepcopy(task_state["task_object"]),
        "prep_view_patch": {
            "active_view": "prepNotebook",
            "active_node_id": "u2_l1",
            "grade": "三年级",
            "term": "2025学年第二学期",
            "lesson_tree": build_lesson_tree(),
            "current_lesson": build_current_lesson(),
        },
        "courseware_screen_patch": build_courseware_screens(),
        "source_matrix": task_state_bridge.build_source_matrix(),
        "runtime_actions": deepcopy(task_state["runtime_actions"]),
        "boundary": boundary_flags(),
    }


def handle_viewmodel_request() -> tuple[dict[str, Any], int]:
    return build_single_lesson_viewmodel(), 200


def handle_action_request(payload: Any) -> tuple[dict[str, Any], int]:
    if not isinstance(payload, dict):
        payload = {}
    action_id = str(payload.get("action_id") or "").strip()
    viewmodel = build_single_lesson_viewmodel()
    known_actions = {item["action_id"]: item for item in viewmodel["runtime_actions"]}
    if action_id not in known_actions:
        return {
            "ok": False,
            "stage": STAGE_ID,
            "error_code": "UNKNOWN_SINGLE_LESSON_VIEWMODEL_ACTION",
            "known_action_ids": sorted(known_actions),
            "boundary": boundary_flags(),
        }, 400
    return {
        "ok": True,
        "stage": STAGE_ID,
        "accepted_action": deepcopy(known_actions[action_id]),
        "state_patch_preview": {
            "viewmodel_id": TASK_ID,
            "last_action_id": action_id,
            "write_allowed": False,
            "formal_apply_performed": False,
            "teacher_confirmation_required": True,
            "message": "已生成只读状态补丁预览，尚未写入 R36、数据库、记忆或正式主壳。",
        },
        "boundary": boundary_flags(),
    }, 200


def register_routes(bp, cors_preflight):
    @bp.route(VIEWMODEL_ROUTE, methods=["GET", "OPTIONS"])
    def prep_room_single_lesson_viewmodel_color_gradient_1013r_r10():
        if request.method == "OPTIONS":
            return cors_preflight()
        response, status_code = handle_viewmodel_request()
        return jsonify(response), status_code

    @bp.route(ACTION_ROUTE, methods=["POST", "OPTIONS"])
    def prep_room_single_lesson_viewmodel_action_color_gradient_1013r_r10():
        if request.method == "OPTIONS":
            return cors_preflight()
        payload = request.get_json(silent=True)
        response, status_code = handle_action_request(payload)
        return jsonify(response), status_code
