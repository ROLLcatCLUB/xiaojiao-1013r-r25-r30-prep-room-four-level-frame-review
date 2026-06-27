from __future__ import annotations

from copy import deepcopy
from datetime import datetime, timezone
from typing import Any

from . import prep_room_single_lesson_viewmodel_1013R_R10 as r10_viewmodel


STAGE_ID = "1013R_R13_XIAOJIAO_TASK_STATE_CONTRACT_AND_RENDER_SURFACE_MAP"
CONTRACT_ID = "SHIWEI_TASK_STATE_CONTRACT_R0"
TASK_ID = "g3_u2_l1_color_gradient"


def _now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def boundary_flags() -> dict[str, bool]:
    flags = dict(r10_viewmodel.boundary_flags())
    flags.update(
        {
            "stage": STAGE_ID,
            "task_state_contract_readonly": True,
            "render_surface_map_defined": True,
            "teacher_action_gate_defined": False,
            "unified_viewmodel_defined": False,
            "source_policy_validator_defined": False,
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


def _source_refs(source_ids: list[str], source_policy: str = "mixed_reference") -> dict[str, Any]:
    return {
        "source_ids": source_ids,
        "source_policy": source_policy,
        "must_show_source_badge": True,
        "ai_draft_may_not_be_standard": True,
    }


def build_render_surface_map() -> list[dict[str, Any]]:
    return [
        {
            "slot_id": "current_object_card",
            "human_name": "当前课题卡",
            "teacher_visible_purpose": "让老师一眼知道当前正在备哪一课。",
            "data_source": ["task_object", "prep_view_patch.current_lesson"],
            "render_state": "bound",
            "action_gate": "view_only",
            "source_refs": _source_refs(["user_provided_g3_textbook_catalog_photo"], "textbook_anchor"),
            "future_actions": ["switch_lesson_after_gate"],
        },
        {
            "slot_id": "xiaojiao_task_state",
            "human_name": "小教任务状态",
            "teacher_visible_purpose": "显示小教判断、已知材料、缺口和建议下一步。",
            "data_source": ["xiaojiao_task_state_contract"],
            "render_state": "contract_ready",
            "action_gate": "view_only",
            "source_refs": _source_refs(["task_state_contract_1013R_R13"], "system_structure"),
            "future_actions": ["add_material", "choose_preview_candidate"],
        },
        {
            "slot_id": "lesson_body",
            "human_name": "备课本正文",
            "teacher_visible_purpose": "承载教学目标、重难点、准备、过程和评价建议。",
            "data_source": ["prep_view_patch.current_lesson.sections"],
            "render_state": "bound",
            "action_gate": "preview_then_confirm",
            "source_refs": _source_refs(
                [
                    "user_provided_g3_textbook_catalog_photo",
                    "work_plan_render_packet_0993B_real_catalog_hint",
                    "kb_g3_u1_old_ai_gradient_unit_doc",
                ],
                "textbook_anchor_plus_reference",
            ),
            "future_actions": ["refine_section", "preview_patch", "teacher_confirm_patch"],
        },
        {
            "slot_id": "teaching_process",
            "human_name": "教学过程",
            "teacher_visible_purpose": "把课堂环节拆成可检查的教师动作、学生活动、大屏提示和证据。",
            "data_source": ["prep_view_patch.current_lesson.process_steps"],
            "render_state": "bound",
            "action_gate": "preview_then_confirm",
            "source_refs": _source_refs(["prep_view_patch.current_lesson.process_steps"], "system_structure"),
            "future_actions": ["refine_process_step", "link_display_screen", "create_evidence_check"],
        },
        {
            "slot_id": "teacher_demo",
            "human_name": "教师示范",
            "teacher_visible_purpose": "沉淀示范步骤、注意点和可上屏的示范语。",
            "data_source": ["prep_view_patch.current_lesson.process_steps", "courseware_screen_patch"],
            "render_state": "placeholder",
            "action_gate": "preview_then_confirm",
            "source_refs": _source_refs(["teacher_input_required"], "teacher_input_required"),
            "future_actions": ["generate_demo_preview", "confirm_demo_script"],
        },
        {
            "slot_id": "courseware_script",
            "human_name": "课件脚本",
            "teacher_visible_purpose": "定义 PPT/课件的屏幕顺序、标题、课堂作用和素材状态。",
            "data_source": ["courseware_screen_patch"],
            "render_state": "bound_as_preview",
            "action_gate": "preview_then_confirm",
            "source_refs": _source_refs(["courseware_screen_patch"], "system_structure"),
            "future_actions": ["generate_courseware_script", "export_courseware_after_gate"],
        },
        {
            "slot_id": "classroom_display_screen",
            "human_name": "大屏呈现",
            "teacher_visible_purpose": "定义上课时投屏给学生看的文字、图像、白板和任务提示。",
            "data_source": ["prep_view_patch.current_lesson.big_screen_short_text", "courseware_screen_patch"],
            "render_state": "bound_as_preview",
            "action_gate": "preview_then_confirm",
            "source_refs": _source_refs(["courseware_screen_patch"], "system_structure"),
            "future_actions": ["generate_display_screen_preview", "link_screen_to_process_step"],
        },
        {
            "slot_id": "worksheet",
            "human_name": "学习单",
            "teacher_visible_purpose": "记录学生试色、排序、发现和修改理由。",
            "data_source": ["prep_view_patch.current_lesson.sections.assessment"],
            "render_state": "placeholder",
            "action_gate": "preview_then_confirm",
            "source_refs": _source_refs(["teacher_input_required"], "teacher_input_required"),
            "future_actions": ["generate_worksheet_preview", "confirm_worksheet"],
        },
        {
            "slot_id": "assessment_rubric",
            "human_name": "评价表",
            "teacher_visible_purpose": "定义课堂评价维度、证据和教师确认后的评价用语。",
            "data_source": ["prep_view_patch.current_lesson.sections.assessment"],
            "render_state": "placeholder",
            "action_gate": "blocked_until_teacher_dimension",
            "source_refs": _source_refs(["teacher_input_required"], "teacher_input_required"),
            "future_actions": ["define_assessment_dimension", "preview_rubric"],
        },
        {
            "slot_id": "blackboard_design",
            "human_name": "板书设计",
            "teacher_visible_purpose": "承载本课核心概念、步骤和学生可见的课堂结构。",
            "data_source": ["prep_view_patch.current_lesson.flow", "teacher_input_required"],
            "render_state": "placeholder",
            "action_gate": "preview_then_confirm",
            "source_refs": _source_refs(["teacher_input_required"], "teacher_input_required"),
            "future_actions": ["generate_blackboard_preview"],
        },
        {
            "slot_id": "materials_list",
            "human_name": "材料清单",
            "teacher_visible_purpose": "列出教材页、色卡、试色纸、颜料、学生作品样例等材料。",
            "data_source": ["prep_view_patch.current_lesson.sections.preparation", "source_matrix"],
            "render_state": "bound_as_preview",
            "action_gate": "preview_then_confirm",
            "source_refs": _source_refs(["source_matrix"], "mixed_reference"),
            "future_actions": ["check_missing_materials", "add_teacher_material"],
        },
        {
            "slot_id": "source_evidence",
            "human_name": "资料来源与证据",
            "teacher_visible_purpose": "区分教材依据、教师输入、AI 草案、外部参考和系统结构。",
            "data_source": ["source_matrix", "source_policy_notes"],
            "render_state": "contract_ready",
            "action_gate": "view_only",
            "source_refs": _source_refs(["source_matrix"], "source_policy"),
            "future_actions": ["open_source_detail", "run_source_policy_validator"],
        },
        {
            "slot_id": "confirm_actions",
            "human_name": "教师确认动作",
            "teacher_visible_purpose": "列出可预览、需确认、阻断和未来动作。",
            "data_source": ["runtime_actions", "preview_candidates", "teacher_confirm_actions", "blocked_actions"],
            "render_state": "contract_ready",
            "action_gate": "gate_required",
            "source_refs": _source_refs(["runtime_actions"], "system_structure"),
            "future_actions": ["confirm_preview", "reject_preview", "defer_action"],
        },
        {
            "slot_id": "bottom_composer",
            "human_name": "底部小教输入",
            "teacher_visible_purpose": "作为推进当前工作的入口，而不是普通聊天框。",
            "data_source": ["task_state", "suggested_teacher_prompts"],
            "render_state": "bound_as_prompt",
            "action_gate": "intent_preview_only",
            "source_refs": _source_refs(["task_state_contract_1013R_R13"], "system_structure"),
            "future_actions": ["submit_teacher_requirement", "classify_intent"],
        },
    ]


def build_known_materials(viewmodel: dict[str, Any]) -> list[dict[str, Any]]:
    task_object = viewmodel.get("task_object", {})
    lesson = viewmodel.get("prep_view_patch", {}).get("current_lesson", {})
    return [
        {
            "id": "grade_term",
            "label": "年级与学期",
            "value": f"{task_object.get('grade', '三年级')} · {task_object.get('term', '2025学年第二学期')}",
            "source_category": "system_structure",
        },
        {
            "id": "lesson_anchor",
            "label": "当前课题",
            "value": lesson.get("title", "2-1《色彩的渐变》"),
            "source_category": "textbook_anchor",
        },
        {
            "id": "unit_anchor",
            "label": "单元位置",
            "value": lesson.get("eyebrow", "第二单元 多彩的世界"),
            "source_category": "textbook_anchor",
        },
        {
            "id": "textbook_page",
            "label": "教材页码",
            "value": lesson.get("textbook_page", "教材第6-7页"),
            "source_category": "textbook_anchor",
        },
        {
            "id": "courseware_screen_patch",
            "label": "课件屏幕草案",
            "value": f"{len(viewmodel.get('courseware_screen_patch', []))} 屏预览",
            "source_category": "system_structure",
        },
    ]


def build_missing_materials() -> list[dict[str, Any]]:
    return [
        {
            "id": "student_work_samples",
            "label": "学生作品样例",
            "why_needed": "评价表和展示评价需要真实作品证据，不能只靠 AI 设想。",
            "blocks_slots": ["assessment_rubric", "classroom_display_screen"],
            "severity": "medium",
        },
        {
            "id": "assessment_dimensions",
            "label": "评价维度",
            "why_needed": "正式评价和评语必须由教师确认维度后才能推进。",
            "blocks_slots": ["assessment_rubric"],
            "severity": "high",
        },
        {
            "id": "official_textbook_ocr",
            "label": "教材第6-7页正式 OCR",
            "why_needed": "当前有教材锚点和页面位置，但不能把 AI 草案当教材原文。",
            "blocks_slots": ["source_evidence"],
            "severity": "medium",
        },
        {
            "id": "classroom_constraints",
            "label": "课堂条件",
            "why_needed": "颜料、水粉、纸条拼摆和白板演示会影响教学过程和材料清单。",
            "blocks_slots": ["teacher_demo", "materials_list"],
            "severity": "medium",
        },
    ]


def build_preview_candidates() -> list[dict[str, Any]]:
    return [
        {
            "id": "preview_lesson_body_refinement",
            "label": "精修备课本正文",
            "targets": ["lesson_body", "teaching_process"],
            "allowed_now": True,
            "requires_teacher_confirmation": True,
            "write_effect": "preview_only",
        },
        {
            "id": "preview_courseware_script",
            "label": "生成课件脚本预览",
            "targets": ["courseware_script"],
            "allowed_now": True,
            "requires_teacher_confirmation": True,
            "write_effect": "preview_only",
        },
        {
            "id": "preview_display_screen",
            "label": "生成大屏呈现预览",
            "targets": ["classroom_display_screen"],
            "allowed_now": True,
            "requires_teacher_confirmation": True,
            "write_effect": "preview_only",
        },
        {
            "id": "preview_worksheet",
            "label": "生成学习单预览",
            "targets": ["worksheet"],
            "allowed_now": True,
            "requires_teacher_confirmation": True,
            "write_effect": "preview_only",
        },
        {
            "id": "preview_assessment_rubric",
            "label": "生成评价表预览",
            "targets": ["assessment_rubric"],
            "allowed_now": False,
            "requires_teacher_confirmation": True,
            "blocked_by": ["assessment_dimensions", "student_work_samples"],
            "write_effect": "preview_only",
        },
    ]


def build_teacher_confirm_actions() -> list[dict[str, Any]]:
    return [
        {
            "id": "confirm_refine_lesson_body_preview",
            "label": "确认精修备课正文预览",
            "targets": ["lesson_body", "teaching_process"],
            "allowed_now": True,
            "formal_apply_allowed": False,
        },
        {
            "id": "confirm_generate_courseware_preview",
            "label": "确认生成课件脚本预览",
            "targets": ["courseware_script"],
            "allowed_now": True,
            "formal_apply_allowed": False,
        },
        {
            "id": "confirm_generate_display_preview",
            "label": "确认生成大屏预览",
            "targets": ["classroom_display_screen"],
            "allowed_now": True,
            "formal_apply_allowed": False,
        },
        {
            "id": "confirm_generate_worksheet_preview",
            "label": "确认生成学习单预览",
            "targets": ["worksheet"],
            "allowed_now": True,
            "formal_apply_allowed": False,
        },
    ]


def build_blocked_actions() -> list[dict[str, Any]]:
    return [
        {
            "id": "formal_save_to_lesson_package",
            "label": "保存到正式课包",
            "blocked_reason": "当前只有只读合同和预览态，没有 formal apply gate。",
            "unblock_requires": ["TEACHER_ACTION_GATE_CONTRACT_R0", "formal_apply_authorization"],
        },
        {
            "id": "write_student_assessment",
            "label": "正式评价学生作品",
            "blocked_reason": "缺少学生作品样例和教师确认的评价维度。",
            "unblock_requires": ["student_work_samples", "assessment_dimensions", "teacher_confirmation"],
        },
        {
            "id": "export_courseware_file",
            "label": "导出课件文件",
            "blocked_reason": "当前只定义课件脚本预览，不生成正式文件。",
            "unblock_requires": ["render_blocks_protocol", "export_contract", "teacher_confirmation"],
        },
        {
            "id": "write_memory_or_archive",
            "label": "写入记忆或档案",
            "blocked_reason": "记忆底座后置，当前避免污染教师偏好和历史记录。",
            "unblock_requires": ["memory_policy_contract", "source_policy_validator"],
        },
    ]


def build_source_policy_notes(viewmodel: dict[str, Any]) -> list[dict[str, Any]]:
    source_matrix = viewmodel.get("source_matrix", [])
    return [
        {
            "category": "textbook_anchor",
            "label": "教材依据",
            "rule": "可作为当前课题、单元、页码和教材对象依据。",
            "current_source_ids": [
                item.get("source_id")
                for item in source_matrix
                if item.get("authority_status") == "current_textbook_catalog_anchor"
            ],
        },
        {
            "category": "teacher_input",
            "label": "教师输入",
            "rule": "可作为当前任务输入和课堂条件依据，但需要保留来源。",
            "current_source_ids": ["teacher_input_required"],
        },
        {
            "category": "ai_draft",
            "label": "AI 草案",
            "rule": "只能作为草稿或参考，不能升格为教材标准、字段标准或正式评价依据。",
            "current_source_ids": [
                item.get("source_id")
                for item in source_matrix
                if item.get("authority_status") == "ai_generated_reference_only"
            ],
        },
        {
            "category": "system_structure",
            "label": "系统结构",
            "rule": "用于页面渲染、状态表达和操作门控，不等同于教学内容依据。",
            "current_source_ids": ["task_state_contract_1013R_R13", "courseware_screen_patch"],
        },
    ]


def build_task_state_contract() -> dict[str, Any]:
    viewmodel = r10_viewmodel.build_single_lesson_viewmodel()
    lesson = viewmodel.get("prep_view_patch", {}).get("current_lesson", {})
    task_object = viewmodel.get("task_object", {})
    surface_map = build_render_surface_map()
    missing = build_missing_materials()
    return {
        "ok": True,
        "stage": STAGE_ID,
        "contract_id": CONTRACT_ID,
        "contract_version": "0.1.0",
        "generated_at": _now(),
        "space": {
            "id": "prep_room",
            "label": "备课室",
            "xiaojiao_role": "备课助理",
        },
        "current_object": {
            "id": TASK_ID,
            "type": "single_lesson",
            "grade": task_object.get("grade", "三年级"),
            "term": task_object.get("term", "2025学年第二学期"),
            "unit": lesson.get("eyebrow", "第二单元 多彩的世界"),
            "title": lesson.get("title", "2-1《色彩的渐变》"),
            "textbook_page": lesson.get("textbook_page", "教材第6-7页"),
            "status": lesson.get("status", "待确认"),
        },
        "task_state": {
            "state_id": "prep_preview_in_progress",
            "teacher_visible_label": "小教判断：正在备课",
            "current_step": "教学判断与结构化预览",
            "known_material_count": 5,
            "missing_material_count": len(missing),
            "recommended_next_action_id": "preview_lesson_body_refinement",
            "should_not_long_chat": True,
            "teacher_visible_summary": "小教已定位三年级第二单元第1课《色彩的渐变》，当前处于备课预览态；后续保存、导出、评价和归档都需要教师确认门。",
        },
        "known_materials": build_known_materials(viewmodel),
        "missing_materials": missing,
        "preview_candidates": build_preview_candidates(),
        "teacher_confirm_actions": build_teacher_confirm_actions(),
        "blocked_actions": build_blocked_actions(),
        "render_surface_map": surface_map,
        "source_policy_notes": build_source_policy_notes(viewmodel),
        "suggested_teacher_prompts": [
            "帮我先精修教学过程。",
            "先生成大屏呈现预览。",
            "把学习单做成轻量版。",
            "我补充学生作品样例后再做评价表。",
        ],
        "evidence_summary": {
            "real_textbook_anchor": "2-1《色彩的渐变》",
            "deprecated_objects": ["《穿穿编编》", "《色彩的感觉》"],
            "source_matrix_count": len(viewmodel.get("source_matrix", [])),
            "surface_slot_count": len(surface_map),
            "policy": "教材依据、教师输入、AI 草案、外部参考和系统结构必须分层显示。",
        },
        "audit_receipt": {
            "created_by_stage": STAGE_ID,
            "r10_viewmodel_stage": viewmodel.get("stage"),
            "r10_viewmodel_route": viewmodel.get("route", {}).get("viewmodel"),
            "readonly": True,
            "no_write_flags": boundary_flags(),
        },
        "next_stage_recommendation": {
            "stage": "1013R_R14_TEACHER_ACTION_GATE_CONTRACT_R0",
            "why": "R13 已定义小教当前任务状态和渲染位，下一步需要把可预览、需确认、阻断和未来动作做成教师确认门合同。",
        },
        "boundary": boundary_flags(),
    }


def build_contract_sample_bundle() -> dict[str, Any]:
    contract = build_task_state_contract()
    return {
        "stage": STAGE_ID,
        "task_state_contract": contract,
        "render_surface_map": deepcopy(contract["render_surface_map"]),
        "boundary": deepcopy(contract["boundary"]),
    }
