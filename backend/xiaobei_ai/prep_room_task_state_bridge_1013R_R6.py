from __future__ import annotations

import json
from copy import deepcopy
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from flask import jsonify, request


STAGE_ID = "1013R_R6_PREP_ROOM_OLD_MATERIAL_RUNTIME_BRIDGE"
TASK_ID = "g3_u2_color_gradient"
TASK_ROUTE = f"/api/prep-room/task-state/{TASK_ID}"
ACTION_ROUTE = f"/api/prep-room/task-state/{TASK_ID}/action"


TEXTBOOK_CATALOG = [
    {
        "unit_no": 1,
        "unit_title": "记录生活",
        "lessons": [
            {"lesson_no": 1, "lesson_title": "画中的生活", "page": 1},
            {"lesson_no": 2, "lesson_title": "流淌的情感", "page": 4},
        ],
    },
    {
        "unit_no": 2,
        "unit_title": "多彩的世界",
        "lessons": [
            {"lesson_no": 1, "lesson_title": "色彩的渐变", "page": 6},
            {"lesson_no": 2, "lesson_title": "渐变的节奏", "page": 8},
            {"lesson_no": 3, "lesson_title": "多彩的生活", "page": 10},
        ],
    },
    {
        "unit_no": 3,
        "unit_title": "辽阔的海洋",
        "lessons": [
            {"lesson_no": 1, "lesson_title": "奇异的海洋生物", "page": 12},
            {"lesson_no": 2, "lesson_title": "跳动的蓝色心脏", "page": 14},
            {"lesson_no": 3, "lesson_title": "守护生命的摇篮", "page": 16},
        ],
    },
    {
        "unit_no": 4,
        "unit_title": "红领巾告诉我",
        "lessons": [
            {"lesson_no": 1, "lesson_title": "种下红色种子", "page": 18},
            {"lesson_no": 2, "lesson_title": "传承红色精神", "page": 20},
        ],
    },
    {
        "unit_no": "special",
        "unit_title": "青绿中国色",
        "lessons": [{"lesson_no": "theme", "lesson_title": "青绿中国色", "page": 22}],
        "page_span": "22-27",
    },
    {
        "unit_no": 5,
        "unit_title": "足下生辉",
        "lessons": [
            {"lesson_no": 1, "lesson_title": "走过四季", "page": 28},
            {"lesson_no": 2, "lesson_title": "魅力鞋汇", "page": 30},
            {"lesson_no": 3, "lesson_title": "时空“履”行", "page": 32},
        ],
    },
    {
        "unit_no": 6,
        "unit_title": "装点生活",
        "lessons": [
            {"lesson_no": 1, "lesson_title": "纹样有特点", "page": 34},
            {"lesson_no": 2, "lesson_title": "纹样的魅力", "page": 36},
        ],
    },
    {
        "unit_no": 7,
        "unit_title": "虎虎生威",
        "lessons": [
            {"lesson_no": 1, "lesson_title": "虎虎虎", "page": 38},
            {"lesson_no": 2, "lesson_title": "巧手做老虎", "page": 40},
        ],
    },
    {
        "unit_no": 8,
        "unit_title": "成长日记",
        "lessons": [
            {"lesson_no": 1, "lesson_title": "蓬勃的生命", "page": 42},
            {"lesson_no": 2, "lesson_title": "奔跑的少年", "page": 44},
            {"lesson_no": 3, "lesson_title": "未来的我们", "page": 46},
        ],
    },
    {
        "unit_no": "extension",
        "unit_title": "迁移拓展",
        "lessons": [{"lesson_no": "extension", "lesson_title": "迁移拓展", "page": 48}],
    },
]


def _repo_root() -> Path:
    return Path(__file__).resolve().parents[2]


def _now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def boundary_flags() -> dict[str, bool]:
    return {
        "old_material_runtime_bridge": True,
        "runtime_connected": True,
        "runtime_write_allowed": False,
        "reuse_previous_material_first": True,
        "new_system_created": False,
        "preview_only": True,
        "teacher_review_required": True,
        "textbook_catalog_rearranged": True,
        "textbook_ocr_available": False,
        "ai_generated_source_reference_only": True,
        "source_material_standard_alignment_allowed": False,
        "field_schema_standard_alignment_allowed": False,
        "provider_called": False,
        "model_called": False,
        "database_written": False,
        "memory_written": False,
        "vector_index_written": False,
        "feishu_written": False,
        "formal_apply_performed": False,
        "R36_modified": False,
        "main_shell_modified": False,
        "main_project_pushed": False,
    }


def _read_json(relative_path: str) -> dict[str, Any]:
    path = _repo_root() / relative_path
    if not path.exists():
        return {}
    with path.open("r", encoding="utf-8-sig") as handle:
        payload = json.load(handle)
    return payload if isinstance(payload, dict) else {}


def _read_text(relative_path: str) -> str:
    path = _repo_root() / relative_path
    if not path.exists():
        return ""
    return path.read_text(encoding="utf-8-sig", errors="ignore")


def _keyword_lines(text: str, keywords: list[str], limit: int = 10) -> list[str]:
    lines: list[str] = []
    for raw in text.splitlines():
        line = raw.strip()
        if not line:
            continue
        if any(keyword in line for keyword in keywords):
            lines.append(line)
        if len(lines) >= limit:
            break
    return lines


def _source_card(
    *,
    source_id: str,
    relative_path: str,
    label: str,
    authority_status: str,
    source_status: str,
    usage: str,
    keywords: list[str],
) -> dict[str, Any]:
    text = _read_text(relative_path)
    return {
        "source_id": source_id,
        "label": label,
        "path": relative_path,
        "exists": bool(text),
        "char_count": len(text),
        "source_status": source_status,
        "authority_status": authority_status,
        "usage": usage,
        "excerpt_lines": _keyword_lines(text, keywords),
    }


def build_source_matrix() -> list[dict[str, Any]]:
    render_packet = _read_json("outputs/teaching_work_plan_content_0993B/readonly_render_packet_bundle_0993B.json")
    return [
        {
            "source_id": "user_provided_g3_textbook_catalog_photo",
            "label": "用户本轮提供的三年级教材目录照片",
            "path": "E:/学校工作/教学/教学资料/教材图片资料/三年级教材内容 - 图片/三年级目录.jpg",
            "exists": Path("E:/学校工作/教学/教学资料/教材图片资料/三年级目录.jpg").exists(),
            "source_status": "teacher_provided_textbook_photo_current_turn",
            "authority_status": "current_textbook_catalog_anchor",
            "usage": "用于纠正伪课题《色彩的感觉》，建立三年级真实教材目录与当前课题锚点。",
            "extracted_catalog": TEXTBOOK_CATALOG,
        },
        _source_card(
            source_id="kb_g3_textbook_image_index_no_ocr",
            label="知识库三年级教材图片索引",
            relative_path="knowledge-base/_parsed/kb_art_g3_textbook_images_20260427.txt",
            source_status="indexed_partial_no_ocr",
            authority_status="image_index_only_not_textbook_text",
            usage="只证明本地已有页图位置；该文件明确写着尚未完成 OCR，不能引用为教材原文。",
            keywords=["三年级美术教材图片包", "尚未完成 OCR", "三年级目录.jpg", "0.jpg", "23.jpg"],
        ),
        _source_card(
            source_id="work_plan_render_packet_0993B_real_catalog_hint",
            label="0993B 教学计划渲染包中的真实课题线索",
            relative_path="outputs/teaching_work_plan_content_0993B/readonly_render_packet_bundle_0993B.json",
            source_status="previous_runtime_fixture_reference",
            authority_status="planning_fixture_reference_only",
            usage="提供第二单元第1课《色彩的渐变》、第2课《渐变的节奏》、第3课《多彩的生活》的已有工程线索。",
            keywords=["第二单元第1课 色彩的渐变", "第二单元第2课 渐变的节奏", "第二单元第3课 多彩的生活"],
        ),
        {
            "source_id": "work_plan_render_packet_0993B_keys",
            "label": "0993B 渲染包结构索引",
            "path": "outputs/teaching_work_plan_content_0993B/readonly_render_packet_bundle_0993B.json",
            "exists": bool(render_packet),
            "source_status": "previous_runtime_fixture_reference",
            "authority_status": "planning_fixture_reference_only",
            "usage": "只读参考，不能替代教师目录照片。",
            "keys": sorted(render_packet.keys()) if render_packet else [],
        },
        _source_card(
            source_id="kb_g3_u1_old_ai_gradient_unit_doc",
            label="知识库旧 AI 第一单元《多变的色彩》备课文档",
            relative_path="knowledge-base/_parsed/kb_art_g3_lesson_case_lesson_8974535734.txt",
            source_status="kb_import_verified_but_reference_only",
            authority_status="ai_generated_reference_only",
            usage="旧 AI 教学设计中有渐变技法参考，但单元标题和教材目录不一致，不能作为标准对齐对象。",
            keywords=["第一单元", "多变的色彩", "渐变", "课时", "教学过程"],
        ),
        _source_card(
            source_id="kb_g3_u1_old_ai_lesson2_pigment_gradient_reference",
            label="知识库旧 AI 课时《颜料的渐变》参考教案",
            relative_path="knowledge-base/_parsed/kb_art_g3_lesson_case_2_07e719a809.txt",
            source_status="kb_import_verified_but_reference_only",
            authority_status="ai_generated_reference_only",
            usage="可参考水粉调色、加水形成明度变化等教学活动，但不改写真实课题《色彩的渐变》。",
            keywords=["颜料的渐变", "水粉", "加水", "色彩", "渐变"],
        ),
        _source_card(
            source_id="legacy_color_feeling_static_to_deprecate",
            label="前一版《色彩的感觉》静态原型",
            relative_path=(
                "outputs/PREP_ROOM_RENDER_CANVAS_DEEPEN_V1/"
                "1013I_R6P_single_lesson_reading_surface_inherits_big_unit_static_upgrade/"
                "prep_room_render_canvas_deepen_v1_R6P_single_lesson_inherits_big_unit.html"
            ),
            source_status="deprecated_prototype_reference",
            authority_status="not_a_textbook_lesson",
            usage="只保留为错误来源追踪；不得再作为当前教材锚点或任务对象。",
            keywords=["色彩的感觉", "课题仍需教师确认", "多变的色彩"],
        ),
    ]


def build_task_state() -> dict[str, Any]:
    return {
        "ok": True,
        "stage": STAGE_ID,
        "runtime_mode": "local_readonly_task_state_bridge",
        "generated_at": _now(),
        "route": {
            "task_state": TASK_ROUTE,
            "action": ACTION_ROUTE,
        },
        "task_object": {
            "task_object_id": "PREP-G3-U2-L1-COLOR-GRADIENT",
            "object_type": "lesson_plan",
            "title": "三年级《色彩的渐变》",
            "grade": "三年级",
            "subject": "美术",
            "unit_no": 2,
            "unit_title": "第二单元《多彩的世界》",
            "lesson_no": 1,
            "lesson_title": "色彩的渐变",
            "textbook_page": 6,
            "status": "runtime_readonly_preview",
            "current_focus": "reanchor_previous_color_line_to_real_textbook_catalog",
            "teacher_confirmation_required": True,
            "write_allowed": False,
        },
        "base_context": {
            "textbook_catalog": {
                "grade": "三年级",
                "source_status": "teacher_provided_catalog_photo_current_turn",
                "ocr_status": "not_available_in_kb",
                "catalog": TEXTBOOK_CATALOG,
            },
            "unit_package": {
                "unit_title": "第二单元《多彩的世界》",
                "unit_thread": "认识色彩明度与纯度 > 探究渐变秩序与节奏 > 用渐变装点校园与生活",
                "source_status": "teacher_provided_catalog_photo_and_page_images",
                "authority_status": "current_textbook_catalog_anchor",
            },
            "lesson_chain": [
                {
                    "lesson_code": "2-1",
                    "lesson_title": "色彩的渐变",
                    "textbook_page": 6,
                    "role": "认识明度、纯度和渐变排列，做调色/排列实验。",
                    "source_status": "current_textbook_catalog_anchor",
                },
                {
                    "lesson_code": "2-2",
                    "lesson_title": "渐变的节奏",
                    "textbook_page": 8,
                    "role": "把色彩明度或纯度渐变用于画面节奏和旋律表达。",
                    "source_status": "current_textbook_catalog_anchor",
                },
                {
                    "lesson_code": "2-3",
                    "lesson_title": "多彩的生活",
                    "textbook_page": 10,
                    "role": "用渐变组织空间、装置或校园生活表达。",
                    "source_status": "current_textbook_catalog_anchor",
                },
            ],
            "deprecation_notice": {
                "deprecated_lesson_title": "色彩的感觉",
                "reason": "该标题不在本轮教师提供的三年级教材目录中。",
                "replacement": "第二单元第1课《色彩的渐变》",
                "must_not_use_as_textbook_anchor": True,
            },
            "knowledge_base_policy": {
                "textbook_images_in_kb_have_ocr": False,
                "ai_lesson_design_can_be_used_as_reference": True,
                "ai_lesson_design_can_be_used_as_standard": False,
                "field_schema_can_be_used_as_standard": False,
            },
        },
        "xiaojiao_task_state": {
            "judgement": "教材锚点已纠偏，正在重新备课",
            "known_materials": [
                "年级：三年级",
                "真实单元：第二单元《多彩的世界》",
                "当前任务对象：第1课《色彩的渐变》",
                "教材目录页显示第1课《色彩的渐变》/6，第2课《渐变的节奏》/8，第3课《多彩的生活》/10",
                "本地知识库三年级教材图片只有索引，未完成 OCR",
            ],
            "missing_items": [
                "把第6-11页教材图做正式 OCR 或人工摘录",
                "把旧 AI《多变的色彩》资料降级为技法参考",
                "按第二单元真实课题重排备课室左侧目录和当前工作对象",
                "决定先接任务状态、学习单预览还是课件屏预览",
            ],
            "suggested_action": "先用只读 runtime 跑真实教材锚点《色彩的渐变》，再接正文候选和课件预览。",
            "available_preview": [
                "真实教材目录",
                "当前课题锚点",
                "第二单元课时链",
                "旧资料降级说明",
                "确认动作",
            ],
        },
        "source_matrix": build_source_matrix(),
        "runtime_actions": [
            {
                "action_id": "continue_refine",
                "teacher_label": "继续精修",
                "result_state": "preview_state_patch_only",
                "write_allowed": False,
            },
            {
                "action_id": "generate_courseware_preview",
                "teacher_label": "生成课件预览",
                "result_state": "courseware_preview_request_only",
                "write_allowed": False,
            },
            {
                "action_id": "build_learning_sheet_preview",
                "teacher_label": "做学习单预览",
                "result_state": "learning_sheet_preview_request_only",
                "write_allowed": False,
            },
            {
                "action_id": "confirm_real_textbook_anchor",
                "teacher_label": "确认按色彩的渐变重排",
                "result_state": "real_textbook_anchor_confirmed_in_runtime_only",
                "write_allowed": False,
            },
        ],
        "boundary": boundary_flags(),
    }


def handle_task_state_request() -> tuple[dict[str, Any], int]:
    return build_task_state(), 200


def handle_action_request(payload: Any) -> tuple[dict[str, Any], int]:
    if not isinstance(payload, dict):
        payload = {}
    action_id = str(payload.get("action_id") or "").strip()
    task_state = build_task_state()
    known_actions = {item["action_id"]: item for item in task_state["runtime_actions"]}
    if action_id not in known_actions:
        return {
            "ok": False,
            "stage": STAGE_ID,
            "error_code": "UNKNOWN_TASK_STATE_ACTION",
            "teacher_visible_message": "这个动作还没有接入，只能先查看《色彩的渐变》的任务状态。",
            "known_action_ids": sorted(known_actions),
            "boundary": boundary_flags(),
        }, 400
    return {
        "ok": True,
        "stage": STAGE_ID,
        "runtime_mode": "local_readonly_task_state_bridge",
        "task_object_id": task_state["task_object"]["task_object_id"],
        "accepted_action": deepcopy(known_actions[action_id]),
        "state_patch_preview": {
            "last_action_id": action_id,
            "candidate_status": "preview_requested",
            "write_allowed": False,
            "teacher_confirmation_required": True,
            "next_suggested_action": "在备课室页面中查看《色彩的渐变》预览，再决定是否继续接正文候选或课件预览。",
        },
        "boundary": boundary_flags(),
    }, 200


def register_routes(bp, cors_preflight):
    @bp.route(TASK_ROUTE, methods=["GET", "OPTIONS"])
    def prep_room_task_state_color_gradient_1013r_r6():
        if request.method == "OPTIONS":
            return cors_preflight()
        response, status_code = handle_task_state_request()
        return jsonify(response), status_code

    @bp.route(ACTION_ROUTE, methods=["POST", "OPTIONS"])
    def prep_room_task_state_action_color_gradient_1013r_r6():
        if request.method == "OPTIONS":
            return cors_preflight()
        payload = request.get_json(silent=True)
        response, status_code = handle_action_request(payload)
        return jsonify(response), status_code
