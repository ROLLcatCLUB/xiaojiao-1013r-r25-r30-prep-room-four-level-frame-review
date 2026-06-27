# 1013R_R6 旧资料接 runtime 只读桥

## 定位

本轮纠正前一版伪课题：`色彩的感觉` 不在教师提供的三年级教材目录中。
当前 runtime 任务对象改为真实教材锚点：三年级第二单元《多彩的世界》第1课《色彩的渐变》。

```text
stage_id=1013R_R6_PREP_ROOM_OLD_MATERIAL_RUNTIME_BRIDGE
task_object=三年级《色彩的渐变》
route=/api/prep-room/task-state/g3_u2_color_gradient
old_material_reused=true
textbook_catalog_rearranged=true
textbook_ocr_available=false
new_system_created=false
runtime_connected=true
runtime_write_allowed=false
provider_called=false
model_called=false
formal_apply_performed=false
```

## 资料口径

1. 教材目录以教师本轮提供的目录照片为准。
2. 本地知识库 `kb_art_g3_textbook_images_20260427.txt` 只有图片索引，明确未完成 OCR。
3. 旧 AI 教案、旧字段设计、旧《色彩的感觉》原型只能作为错误追踪或技法参考，不能作为标准。

## 验证

```text
validator_pass=true
failed_checks=[]
```
