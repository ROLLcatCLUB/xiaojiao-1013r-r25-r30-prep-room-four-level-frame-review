# 1013R_R13 Xiaojiao task-state contract and render surface map

## 定位

本轮定义小教任务状态合同和备课室内部渲染位索引。

```text
stage_id=1013R_R13_XIAOJIAO_TASK_STATE_CONTRACT_AND_RENDER_SURFACE_MAP
contract_id=SHIWEI_TASK_STATE_CONTRACT_R0
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

- 小教当前任务状态。
- 已知材料、缺口、预览候选、教师确认动作、阻断动作。
- 备课室 14 个主要渲染位。
- 大屏呈现与课件脚本分离。
- 教材依据、教师输入、AI 草案、系统结构的来源标签。

## 不做

- 不做完整渲染底座。
- 不注册新 route。
- 不写数据库、记忆、向量或飞书。
- 不调用模型或 provider。
- 不 formal apply。

## 验证

```text
validator_pass=true
failed_checks=[]
```

## 下一步

```text
1013R_R14_TEACHER_ACTION_GATE_CONTRACT_R0
```
