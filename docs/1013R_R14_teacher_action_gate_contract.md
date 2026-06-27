# 1013R_R14 教师确认门合同

```text
stage_id=1013R_R14_TEACHER_ACTION_GATE_CONTRACT_R0
contract_id=SHIWEI_TEACHER_ACTION_GATE_CONTRACT_R0
current_space=备课室
current_object=2-1《色彩的渐变》
```

## 定位

R14 解决的问题：

```text
小教建议的动作，哪些现在能预览？
哪些必须由老师确认？
哪些当前阻断？
哪些只是未来能力？
```

R14 不执行动作，只定义门控。

## 门控类型

| gate_type | 人话 | 允许 | 禁止 |
| --- | --- | --- | --- |
| `view_only` | 只读查看 | 读状态、看详情 | 生成、写入、导出 |
| `intent_preview_only` | 只识别意图 | 判断老师想推进哪一步 | 写入、导出、正式应用 |
| `preview_then_confirm` | 先预览后确认 | 生成预览、显示影响范围、显示来源 | 写入、导出、正式应用 |
| `gate_required` | 必须经过教师确认门 | 显示确认、记录预览态决定 | 静默写入、无门应用 |
| `blocked_until_teacher_dimension` | 缺教师维度时阻断 | 显示阻断原因、要求补材料 | 正式评价、学生记录写入 |
| `future_only` | 未来能力 | 显示未来标记 | 执行动作 |

## 确认前必须显示

任何 `preview_then_confirm` 或 `gate_required` 动作，在老师确认前都必须显示：

```text
preview_content=预览内容
impact_scope=影响哪些渲染位
source_badges=资料来源标签
write_effect=本次只产生预览/回执，不 formal apply
```

## 当前动作组

### 现在可以先预览

```text
preview_lesson_body_refinement
preview_courseware_script
preview_display_screen
preview_worksheet
```

### 当前阻断

```text
preview_assessment_rubric
formal_save_to_lesson_package
write_student_assessment
export_courseware_file
write_memory_or_archive
```

阻断原因：

```text
评价表缺少学生作品样例和教师确认的评价维度。
正式保存缺少 formal apply gate。
课件导出缺少 export contract。
记忆/档案写入必须等待记忆策略和来源校验。
```

## 确认回执

后续真正执行时，确认回执至少包含：

```text
receipt_id
action_id
teacher_decision
target_slots
preview_summary
source_badges
write_effect
formal_apply_performed=false
created_at
```

## 边界

```text
R36_modified=false
main_shell_modified=false
route_registered=false
provider_called=false
model_called=false
database_written=false
memory_written=false
vector_index_written=false
feishu_written=false
formal_apply_performed=false
runtime_write_allowed=false
```

## 下一步

```text
1013R_R15_PREP_ROOM_UNIFIED_VIEWMODEL_R0
```

原因：

```text
R13 已定义任务状态和渲染位。
R14 已定义动作门控。
R15 应把 lesson_viewmodel、task_state、action_gate、source_policy、render_surface_map 合成一份统一 ViewModel。
```
