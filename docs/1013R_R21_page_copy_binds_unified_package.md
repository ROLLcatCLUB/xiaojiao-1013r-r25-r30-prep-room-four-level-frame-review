# R21：备课室页面副本读取统一协议包

```text
stage_id=1013R_R21_PAGE_COPY_BINDS_UNIFIED_PACKAGE
binding_id=SHIWEI_PREP_ROOM_PAGE_COPY_PACKAGE_BINDING_R0
```

R21 只做页面副本，不改主壳，不改 R36。页面副本必须以 R11 原型页为基底，保留旧页作为回滚版本；禁止另起一个脱离原型的新静态页，也禁止在原型外部贴一条新的协议工作带。

## 四级产品框架约束

R21 页面必须服从：

```text
docs/1013R_product_frame_four_level.md
```

当前页面映射为：

```text
一级：顶部师维全局栏 + 底部小教输入栏
二级：备课室
三级：备课本 / 大屏草稿 / 课件制作 / 资料与依据 / 查看编辑动作
四级：当前课题、大单元章节、单课正文、教学过程、弹出修改卡片等具体内容
```

后续设计不得把三级工具做成独立页面，也不得把四级内容提升成一级全局框架。

R20 字段必须进入原型内部已有字段位：

```text
current_object -> 原型课题区 / current_lesson
task_state -> 原型小教判断 / reasoning_trace / 右侧状态卡
known_materials / missing_materials -> 原型右侧材料状态卡
teacher_action_gate -> 原型右侧确认动作卡
source_policy_result -> 原型依据/来源提示
render_blocks -> 原型备课正文、教学过程、大屏、课件、学习单、评价区
derivative_linkage -> 原型教学过程节点与课件/大屏/学习单/评价表联动
composer prompt -> 原型底部小教输入框
```

## 页面必须可见

```text
当前对象：三年级第二单元第1课《色彩的渐变》
小教任务状态
已知材料 / 缺口
教师确认动作
资料来源轻校验
render_blocks
教学过程与课件 / 大屏 / 学习单 / 评价表联动
```

## 边界

```text
R36_modified=false
main_shell_modified=false
existing_page_modified=false
route_registered=false
endpoint_registered=false
provider_called=false
model_called=false
database_written=false
memory_written=false
formal_apply_performed=false
new_blank_static_page_created=false
source_prototype_modified=false
external_protocol_band_created=false
internal_prototype_binding=true
```

## 下一步

```text
R22：教师可读性 + 2K 视觉验证 + 派生对象可见联动
```
