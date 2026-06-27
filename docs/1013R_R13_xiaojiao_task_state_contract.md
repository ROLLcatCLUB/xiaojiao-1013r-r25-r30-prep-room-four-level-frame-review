# 1013R_R13 小教任务状态合同

```text
stage_id=1013R_R13_XIAOJIAO_TASK_STATE_CONTRACT_AND_RENDER_SURFACE_MAP
contract_id=SHIWEI_TASK_STATE_CONTRACT_R0
current_product=师维智教
current_agent_name=小教
current_space=备课室
current_object=三年级第二单元第1课《色彩的渐变》
```

## 定位

R13 不做完整底座，不做正式写入，也不把页面继续扩成静态长文。

R13 要解决的是：

```text
小教现在到底在推进什么？
页面内部有哪些主要渲染位？
每个渲染位吃什么数据？
每个动作是可预览、需确认、阻断，还是未来能力？
```

## 合同字段

| 字段 | 人话含义 | 当前要求 |
| --- | --- | --- |
| `space` | 当前工作空间 | 必须是备课室 |
| `current_object` | 当前处理对象 | 必须是 `2-1《色彩的渐变》` |
| `task_state` | 小教判断老师正在做什么 | 必须说明正在备课、处于预览态 |
| `known_materials` | 已知材料 | 至少包含年级、学期、单元、课题、教材页、课件草案 |
| `missing_materials` | 缺口 | 至少包含学生作品样例、评价维度、正式 OCR、课堂条件 |
| `preview_candidates` | 可先生成的预览 | 包含备课正文、课件脚本、大屏、学习单、评价表 |
| `teacher_confirm_actions` | 需要教师确认的动作 | 只允许预览确认，不允许 formal apply |
| `blocked_actions` | 当前不能做的动作 | 保存正式课包、正式评价、导出、写记忆都阻断 |
| `render_surface_map` | 备课室渲染位地图 | 定义当前对象、小教状态、正文、大屏、课件等渲染位 |
| `source_policy_notes` | 资料来源规则 | 区分教材依据、教师输入、AI 草案和系统结构 |
| `audit_receipt` | 可追踪记录 | 必须记录 R10 来源和只读边界 |

## 当前任务状态

```text
state_id=prep_preview_in_progress
teacher_visible_label=小教判断：正在备课
current_step=教学判断与结构化预览
recommended_next_action=精修备课本正文
```

小教当前不应该表现为聊天机器人，而应该表现为：

```text
当前空间：备课室
当前对象：2-1《色彩的渐变》
已知材料：年级、学期、单元、课题、教材页、课件屏草案
缺口：学生作品样例、评价维度、正式 OCR、课堂条件
建议动作：先生成或精修备课预览
```

## 动作分层

```text
view_only=只看状态，不推进
preview_then_confirm=可以生成预览，但需要教师确认
gate_required=必须经过教师确认门
blocked_until_teacher_dimension=缺少教师维度，暂时阻断
future_only=未来能力，不在当前阶段执行
```

## 当前硬边界

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

R13 完成后，不直接进入大底座。

下一阶段建议：

```text
1013R_R14_TEACHER_ACTION_GATE_CONTRACT_R0
```

原因：

```text
R13 已经说明小教当前在做什么，以及页面有哪些渲染位；
R14 应该把可预览、需确认、阻断、未来动作做成教师确认门合同。
```
