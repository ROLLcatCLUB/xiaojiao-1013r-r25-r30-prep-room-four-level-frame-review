# R20：备课室统一协议包只读出口

```text
stage_id=1013R_R20_PREP_ROOM_UNIFIED_PACKAGE_READONLY_EXPORT_R0
package_id=SHIWEI_PREP_ROOM_UNIFIED_PACKAGE_READONLY_EXPORT_R0
```

R20 的边界修正：它不是正式 route，也不是 endpoint 注册。它只是把 R15 / R16 / R17 / R19 合成一个页面可消费的只读协议包。

## 输入

```text
R15 unified_viewmodel
R16 source_policy_result
R17 render_blocks
R19 derivative_object_linkage
```

## 输出

```text
prep_room_unified_package_1013R_R20.json
```

页面后续只应该读取这份包里的稳定字段：

```text
current_object
task_state
teacher_action_gate
source_policy_result
render_blocks
render_block_linkage_index
derivative_linkage
lesson_viewmodel
```

## 边界

```text
route_registered=false
endpoint_registered=false
R36_modified=false
main_shell_modified=false
existing_page_modified=false
provider_called=false
model_called=false
database_written=false
memory_written=false
vector_index_written=false
feishu_written=false
formal_apply_performed=false
```

## 下一步

```text
R21：页面副本绑定 R20 协议包
```
