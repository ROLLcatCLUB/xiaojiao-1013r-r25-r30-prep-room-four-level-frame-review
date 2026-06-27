# 1013R_R15 prep-room unified ViewModel

## 定位

本轮把 R10 lesson ViewModel、R13 小教任务状态合同、R14 教师确认门合同合成一份只读统一 ViewModel。

```text
stage_id=1013R_R15_PREP_ROOM_UNIFIED_VIEWMODEL_R0
viewmodel_type=prep_room_unified_readonly_contract_viewmodel
current_object=三年级第二单元第1课《色彩的渐变》
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
```

## 已定义

- 页面未来可消费的单入口 ViewModel。
- 14 个 render_slots 的 payload/action/source 绑定。
- lesson_viewmodel、task_state、action_gate、source_policy 的顶层结构。
- renderer_should_consume 和 renderer_must_not。

## 验证

```text
validator_pass=true
failed_checks=[]
```

## 下一步

```text
1013R_R16_SOURCE_POLICY_LIGHT_VALIDATOR_R0
```
