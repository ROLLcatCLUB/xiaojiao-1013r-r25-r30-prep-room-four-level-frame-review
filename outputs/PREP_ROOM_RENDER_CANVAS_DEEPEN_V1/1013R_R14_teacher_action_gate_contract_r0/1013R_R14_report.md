# 1013R_R14 teacher action gate contract

## 定位

本轮定义教师确认门合同，不执行任何动作。

```text
stage_id=1013R_R14_TEACHER_ACTION_GATE_CONTRACT_R0
contract_id=SHIWEI_TEACHER_ACTION_GATE_CONTRACT_R0
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

- 6 种动作门控类型。
- 预览候选、教师确认动作和阻断动作的统一 action matrix。
- 确认前必须显示预览、影响范围、来源标签和无 formal apply 提示。
- 确认回执 schema。

## 验证

```text
validator_pass=true
failed_checks=[]
```

## 下一步

```text
1013R_R15_PREP_ROOM_UNIFIED_VIEWMODEL_R0
```
