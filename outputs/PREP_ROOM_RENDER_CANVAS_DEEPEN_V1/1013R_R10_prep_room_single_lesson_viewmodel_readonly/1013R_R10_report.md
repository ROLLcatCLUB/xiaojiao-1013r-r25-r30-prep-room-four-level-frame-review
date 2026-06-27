# 1013R_R10 prep-room single lesson ViewModel readonly endpoint

## 定位

本轮只把三年级第二单元第1课《色彩的渐变》的备课页数据沉到后端 ViewModel。

```text
stage_id=1013R_R10_PREP_ROOM_SINGLE_LESSON_VIEWMODEL_READONLY_ENDPOINT
route=/api/prep-room/single-lesson-viewmodel/g3_u2_l1_color_gradient
action_route=/api/prep-room/single-lesson-viewmodel/g3_u2_l1_color_gradient/action
R36_modified=false
main_shell_modified=false
provider_called=false
model_called=false
database_written=false
memory_written=false
vector_index_written=false
feishu_written=false
formal_apply_performed=false
```

## 渲染关系

- R9 仍是静态渲染页。
- R10 提供渲染页可消费的只读 ViewModel。
- 下一步页面副本应 fetch R10，而不是继续靠可见文字替换。

## 验证

```text
validator_pass=true
failed_checks=[]
```
