# 067E Capability -> Executor Coverage Inventory

日期：2026-05-17

## 结论

067E 后，Workbench 的能力覆盖关系收敛为：

```text
capability -> skill -> route intent -> executor -> output contract -> safety gate
```

本次没有接入 OPENCLAW memory、小教 runtime、小评 runtime、飞书写回、数据库写入、知识库正式写入、正式评分或真实导出。

换句话说，067E 没有做 OPENCLAW memory 导入，也没有把外部 OPENCLAW 能力接成默认流程。

## Capability 覆盖表

| capability_id | write_allowed | skill | route_intent | executor | executor_status | output_contract | risk | action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `ask_clarifying_question` | false | `ask_clarifying_question` | clarification/topic_selection/unknown | `workbench_dry_run.clarification` | implemented_preview_executor | `workbench_agent_turn_response_v1` | 低 | 保留 |
| `show_course_catalog_if_available` | false | `course_catalog_query` | course_catalog_query | `runtime_reply_only` | implemented_preview_executor | `workbench_agent_turn_response_v1` | 低 | 保留 |
| `ask_teacher_to_choose_topic` | false | `course_catalog_query` | course_catalog_query/topic_selection | `runtime_reply_only` | implemented_preview_executor | `workbench_agent_turn_response_v1` | 低 | 保留 |
| `ask_for_textbook_or_grade_plan` | false | `course_catalog_query` | planning_info_query | `runtime_reply_only` | implemented_preview_executor | `workbench_agent_turn_response_v1` | 低 | 保留 |
| `acknowledge_feedback_and_explain` | false | `issue_capture` | teacher_feedback_or_quality_complaint | `runtime_reply_only` | implemented_preview_executor | `workbench_agent_turn_response_v1` | 低 | 保留 |
| `revise_current_candidate_using_teacher_content` | false | `issue_capture` | teacher_feedback_or_quality_complaint | `runtime_reply_only` | implemented_preview_executor | `workbench_agent_turn_response_v1` | 中 | 只保留信息，不生成候选 |
| `start_semester_schedule_planning` | false | `semester_schedule_start` | new_topic/semester_plan_request | `runtime_semester_schedule_start` | implemented_preview_executor | `workbench_agent_turn_response_v1` | 低 | 保留 |
| `update_context_only` | false | `task_object_update` | scope_correction/lesson_count_update | `workbench_agent_state_reducer` | implemented_preview_executor | `workbench_agent_state_patch_v1` | 低 | 保留 |
| `generate_unit_brief_candidate` | false | `create_unit_candidate` | new_topic/scope_correction/unit_brief_request | `workbench_dry_run.unit_brief` | implemented_preview_executor | `candidate_card_update` | 中 | candidate only |
| `update_task_object_memory` | false | `task_object_update` | task_object_update | `runtime_task_object_memory_update` | implemented_preview_executor | `workbench_task_object_memory_v1` | 中 | state preview only |
| `split_lesson_components` | false | `split_unit_lessons` | lesson_component_split_request | `runtime_lesson_component_split` | implemented_preview_executor | `lesson_component_split_candidate_v1` | 中 | candidate only |
| `ask_which_field_to_edit` | false | `edit_unit_field` | field_edit_request | `runtime_field_edit_selector` | implemented_preview_executor | `workbench_agent_turn_response_v1` | 低 | selector only |
| `generate_semester_plan_candidate` | false | `task_object_create` | legacy semester_plan_request | `workbench_dry_run.semester_plan` | deprecated | `candidate_card_update` | 中 | 默认改走课务协商 |
| `generate_lesson_brief_candidate` | false | `create_lesson_candidate` | new_topic/lesson_brief_request | `workbench_dry_run.lesson_brief` | implemented_preview_executor | `candidate_card_update` | 中 | candidate only |
| `refine_activity_candidate` | false | `activity_refine` | activity_refine_request | `workbench_dry_run.activity_refine` | implemented_preview_executor | `candidate_card_update` | 中 | candidate only |
| `generate_task_sheet_candidate` | false | `generate_task_sheet` | task_sheet_request | `workbench_dry_run.task_sheet` | implemented_preview_executor | `candidate_card_update` | 中 | candidate only |
| `open_resource_cards` | false | `resource_preview` | resource_request | `workbench_dry_run.resources` | implemented_preview_executor | `preview_card_update` | 低 | 067E 补齐声明 |
| `open_package_check` | false | `package_preview` | package_check_request | `workbench_dry_run.package_check` | implemented_preview_executor | `preview_card_update` | 低 | 067E 补齐声明 |
| `apply_last_candidate_to_preview` | false | `accept_candidate` | accept/write/apply candidate | `workbench_dry_run.apply_last_candidate` | implemented_preview_executor | `preview_card_update` | 中 | preview only |
| `reject_last_candidate` | false | `discard_candidate` | reject_last_candidate | `runtime_candidate_reject` | implemented_preview_executor | `workbench_agent_turn_response_v1` | 低 | 保留 |
| `modify_last_candidate` | false | `candidate_modify` | modify_last_candidate | `runtime_reply_only` | declarative_only | `workbench_agent_turn_response_v1` | 中 | 067E1 runtime guard 直接阻断，router 改走字段选择 |
| `start_official_field_question_flow` | false | `official_field_question` | official_field_question_start | `runtime_field_question_start` | implemented_preview_executor | `field_question_state_update` | 中 | field preview only |
| `answer_official_field` | false | `official_field_question` | field_answer | `runtime_field_answer` | implemented_preview_executor | `field_question_state_update` | 中 | field preview only |
| `skip_official_field_with_fallback` | false | `official_field_question` | field_skip | `runtime_field_skip` | implemented_preview_executor | `field_question_state_update` | 中 | fallback candidate only |
| `open_package_preview` | false | `package_preview` | package_preview_request | `workbench_dry_run.package_check` | implemented_preview_executor | `preview_card_update` | 低 | no export |
| `open_export_gate` | false | `export_gate_check` | export_gate_request | `runtime_export_gate_preview` | draft_only_executor | `export_gate_preview` | 中 | gate preview only |
| `create_export_record_preview` | false | `export_gate_check` | export_gate_request | `runtime_export_record_preview` | draft_only_executor | `export_record_preview` | 中 | preview only, no real export |
| `reply_only` | false | several reply skills | continue/unknown/fallback | `runtime_reply_only` | implemented_preview_executor | `workbench_agent_turn_response_v1` | 低 | 保留 |
| `answer_from_current_context` | false | `resource_preview` | context_probe | `runtime_context_probe` | implemented_preview_executor | `workbench_agent_turn_response_v1` | 低 | reply/card preview only |

## Skill Registry 盘点

| skill 类型 | skill_id | coverage |
| --- | --- | --- |
| 已接 preview executor | `ask_clarifying_question`, `course_catalog_query`, `semester_schedule_start`, `task_object_update`, `create_unit_candidate`, `create_lesson_candidate`, `split_unit_lessons`, `edit_unit_field`, `accept_candidate`, `discard_candidate`, `official_field_question`, `activity_refine`, `generate_task_sheet`, `resource_preview`, `package_preview`, `issue_capture` | 可执行但仍为 preview/candidate/teacher review |
| 声明型子技能 | `semester_basic_info_collect`, `semester_constraint_collect`, `unit_lesson_allocate`, `weekly_schedule_generate`, `schedule_conflict_check`, `schedule_adjust`, `schedule_confirm`, `semester_work_plan_preview_generate`, `doc_preview`, `replay_test` | declarative_only，不允许 UI 宣称已接安全 executor |
| 旧别名/重复声明 | `unit_brief_candidate`, `lesson_component_split`, `field_edit_request`, `candidate_apply`, `candidate_reject`, `task_sheet_generate`, `package_check` | declarative_only，实际走对应 selector 绑定 skill |
| 草稿门禁 | `export_gate_check` | draft_only_executor，只做 gate preview，不真实导出 |

## Route -> Capability 覆盖

| route intent | capability | executor_status |
| --- | --- | --- |
| `new_topic` | unit/lesson candidate 或 semester schedule start | implemented_preview_executor |
| `continue_current` | reply 或当前 scope candidate | implemented_preview_executor |
| `scope_correction` / `lesson_count_update` | `generate_unit_brief_candidate` / `update_context_only` | implemented_preview_executor |
| `semester_plan_request` | `start_semester_schedule_planning` | implemented_preview_executor |
| `unit_brief_request` / `lesson_brief_request` | `generate_unit_brief_candidate` / `generate_lesson_brief_candidate` | implemented_preview_executor |
| `course_catalog_query` / `planning_info_query` | course catalog reply capabilities | implemented_preview_executor |
| `task_object_update` | `update_task_object_memory` | implemented_preview_executor |
| `lesson_component_split_request` | `split_lesson_components` | implemented_preview_executor |
| `field_edit_request` | `ask_which_field_to_edit` | implemented_preview_executor |
| `teacher_feedback_or_quality_complaint` | feedback acknowledgement capabilities | implemented_preview_executor |
| `official_field_question_start` | `start_official_field_question_flow` | implemented_preview_executor |
| `activity_refine_request` | `refine_activity_candidate` | implemented_preview_executor |
| `task_sheet_request` | `generate_task_sheet_candidate` | implemented_preview_executor |
| `resource_request` | `open_resource_cards` | implemented_preview_executor |
| `package_check_request` | `open_package_check` | implemented_preview_executor |
| candidate accept/reject/modify | apply/reject/field selector；直接 `modify_last_candidate` action 为 declarative_only | implemented_preview_executor or declarative_only |

## 067E1 Runtime Guard 加硬

067E1 将 coverage executor status 绑定到 runtime guard：

```text
backend/xiaobei_ai/workbench_agent_capability_registry.py::ACTION_EXECUTOR_STATUS
backend/xiaobei_ai/workbench_agent_runtime.py::_runtime_guard
```

阻断状态：

```text
declarative_only
missing_executor
blocked_by_design
```

因此：

```text
modify_last_candidate action -> declarative_only -> guard accepted=false
modify_last_candidate intent -> ask_which_field_to_edit -> implemented_preview_executor
missing_executor_probe -> missing_executor -> guard accepted=false
feishu_writeback/database_write/formal_scoring/real_export -> blocked_by_design -> guard accepted=false
```

blocked response 仍保持：

```text
execution_status=blocked
execution_success=false
write_allowed=false
```

## Blocked By Design

| capability_id | status | reason |
| --- | --- | --- |
| `feishu_writeback` | blocked_by_design | 067E 不写飞书。 |
| `database_write` | blocked_by_design | 067E 不写数据库。 |
| `formal_scoring` | blocked_by_design | 067E 不启用正式评分。 |
| `real_export` | blocked_by_design | 067E 不真实导出。 |
| `openclaw_memory_import` | blocked_by_design | 068A 前不导入 OPENCLAW memory。 |
| `xiaojiao_runtime` | declarative_only | 067E 不接小教 runtime。 |
| `xiaoping_runtime` | declarative_only | 067E 不接小评 runtime。 |
| `missing_executor_probe` | missing_executor | validator 用于确认 runtime guard 会阻断未知 action。 |

## 安全边界

所有 coverage 项保持：

```text
write_allowed=false
external_write_allowed=false
formal_scoring_allowed=false
real_export_allowed=false
teacher_review_required=true
```

067E 没有把 declarative_only 或 missing_executor 伪装成 implemented。
