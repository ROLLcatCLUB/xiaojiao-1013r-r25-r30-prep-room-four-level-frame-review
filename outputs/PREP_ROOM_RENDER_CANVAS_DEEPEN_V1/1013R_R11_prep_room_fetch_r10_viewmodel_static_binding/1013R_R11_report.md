# 1013R_R11 prep-room R9 fetch R10 ViewModel static binding

## 定位

本轮只在 R9 副本上建立 R10 只读 ViewModel 的静态绑定样板。

```text
stage_id=1013R_R11_PREP_ROOM_R9_FETCH_R10_VIEWMODEL_STATIC_BINDING
source_copy=1013R_R9_real_textbook_prep_page_sync
html=D:\Documents\SmartEdu\xiaobei-core\outputs\PREP_ROOM_RENDER_CANVAS_DEEPEN_V1\1013R_R11_prep_room_fetch_r10_viewmodel_static_binding\prep_room_render_canvas_deepen_v1_1013R_R11_prep_room_fetch_r10_viewmodel_static_binding.html
route=/api/prep-room/single-lesson-viewmodel/g3_u2_l1_color_gradient
task_object=三年级第二单元《多彩的世界》第1课《色彩的渐变》
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

## 风险点处理

- 旧 1013L 可见层 hydration 脚本在 R11 副本中已改为不可执行。
- 旧 R7 全文替换 walker 脚本在 R11 副本中已改为不可执行。
- 新 R11 绑定只读取 `/api/prep-room/single-lesson-viewmodel/g3_u2_l1_color_gradient`。
- 新 R11 绑定只做字段级映射，不执行保存、导出、写入或 formal apply。

## 验证

```text
validator_pass=true
failed_checks=[]
```
