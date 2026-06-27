# 1013R_R15 备课室统一 ViewModel

```text
stage_id=1013R_R15_PREP_ROOM_UNIFIED_VIEWMODEL_R0
viewmodel_type=prep_room_unified_readonly_contract_viewmodel
current_object=2-1《色彩的渐变》
```

## 定位

R15 把前面三条线合成一份页面将来可消费的统一数据：

```text
R10 lesson ViewModel
R13 小教任务状态合同
R14 教师确认门合同
```

合成后，后续页面和渲染底座不应该继续东拼西凑读临时字段，而应该优先吃：

```text
current_object
lesson_viewmodel
task_state
action_gate
render_surface_map
render_slots
source_policy
boundary
```

## 顶层结构

| 字段 | 含义 |
| --- | --- |
| `current_object` | 当前课题与教材对象 |
| `lesson_viewmodel` | 课题树、当前课正文、教学过程、课件屏幕 |
| `task_state` | 小教判断、已知材料、缺口、预览候选 |
| `action_gate` | 动作门控、确认规则、确认回执 schema |
| `render_surface_map` | 备课室所有主要渲染位 |
| `render_slots` | 渲染位和 payload/action/source 的绑定 |
| `source_policy` | 来源矩阵和来源分类规则 |
| `renderer_contract` | 后续渲染底座应消费/禁止消费的字段 |
| `boundary` | 只读边界 |

## 渲染位绑定

`render_slots` 是 R15 的关键。

每个 slot 都要说明：

```text
slot_id
human_name
render_state
action_gate
payload_refs
source_refs
available_actions
future_actions
```

这样后续轻量渲染底座不需要理解所有业务细节，只要按 slot 渲染。

## Renderer Contract

后续页面应该消费：

```text
current_object
lesson_viewmodel
task_state
action_gate
render_surface_map
render_slots
source_policy
boundary
```

后续页面禁止：

```text
read_legacy_hydration_payload
replace_visible_text_by_walker
treat_ai_reference_as_standard
write_database_or_memory
formal_apply
```

## 当前边界

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
1013R_R16_SOURCE_POLICY_LIGHT_VALIDATOR_R0
```

原因：

```text
R15 已经把页面数据合成单入口。
在进入 render_blocks 或轻量渲染底座之前，需要先做轻量来源校验，防止教材依据、教师输入、AI 草案和系统结构混在一起。
```
