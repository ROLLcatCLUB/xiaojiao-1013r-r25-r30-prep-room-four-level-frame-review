# 1013R_R16 资料来源轻校验

```text
stage_id=1013R_R16_SOURCE_POLICY_LIGHT_VALIDATOR_R0
validator_id=SHIWEI_SOURCE_POLICY_LIGHT_VALIDATOR_R0
current_object=2-1《色彩的渐变》
```

## 定位

R16 不做完整资料库，也不做真实来源回写。

它只在进入 `render_blocks` 前做轻量检查：

```text
当前课题必须来自教材锚点
AI 草案不能作为教材标准
来源分类必须齐全
评价表缺学生作品和评价维度时必须阻断
记忆写入必须后置
```

## 来源分层

```text
textbook_anchor=教材依据
teacher_input=教师输入
ai_draft=AI 草案
system_structure=系统结构
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
```

## 下一步

```text
1013R_R17_RENDER_BLOCKS_PROTOCOL_R0
```
