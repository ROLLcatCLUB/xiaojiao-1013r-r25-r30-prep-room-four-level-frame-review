# 1013R_R25-R30 本地规划审核包

```text
package_id=1013R_R25_R30_GPT_PLANNING_REVIEW_LOCAL_PACKAGE_20260627
repo=D:\Documents\SmartEdu\xiaobei-core
current_surface=outputs/PREP_ROOM_RENDER_CANVAS_DEEPEN_V1/1013R_R21_page_copy_binds_unified_package/prep_room_page_copy_binds_unified_package_1013R_R21.html
next_stage=1013R_R30_RENDER_SURFACE_CONNECTOR_PLAN_OR_VISUAL_TOOL_POLISH
```

## 给 GPT 的审核请求

请把这个目录当作本地 review area，不是完整源码仓库。

重点判断：

```text
1. R13-R29 这些协议、样板、页面副本、注册表是否足够支撑 R30。
2. R30 是否应该优先做“四级框架 -> 当前 R21 页面可见结构”的轻连接。
3. 当前页面有没有继续退化成普通静态页、普通教案页或聊天框的风险。
4. 当前工具框架、各室框架、内容渲染框架之间是否断裂。
5. 哪些资料可以复用为底座，哪些只能作为参考，哪些应该摒弃或归档。
6. 后续是否应先做渲染表面连接，再做大屏/课件/学习单/评价表联动，而不是先做完整 runtime。
```

## 必须先读

```text
outputs/PREP_ROOM_RENDER_CANVAS_DEEPEN_V1/SESSION_HANDOFF_20260627_R25_R29_FOUR_LEVEL_FRAME_TO_R30_NEXT.md
outputs/PREP_ROOM_RENDER_CANVAS_DEEPEN_V1/SESSION_HANDOFF_20260627_R25_R29_FOUR_LEVEL_FRAME_TO_R30_NEXT.index.json
PACKAGE_MANIFEST.json
```

## 当前产品判断

```text
师维智教 = 教师工作场景系统
小教 = 常驻同一个助手，多空间切换职责
当前主场景 = 备课室
当前真实课题 = 三年级第二单元第1课《色彩的渐变》
页面中心 = 当前工作对象 + 任务状态 + 可确认推进
输入框 = 推进当前工作的入口之一，不是产品中心
```

## 四级递归框架

后续路由、诊断、UI 评审、ViewModel 设计、组件拆分都按四级框架定位：

```text
1级：平台外壳框架
2级：各室工作空间框架
3级：工具框架
4级：内容框架
```

当前目标不是另做一张漂亮静态页，而是把已有页面和底座按四级框架接起来。

## 本包内容结构

```text
docs/
  1013R_product_frame_four_level.md
  1013R_R13-R29*.md
  guides/github_review_upload_prompt_template_for_gpt.md
  handoff/xiaojiao_teacher_jarvis_workbench_1000A_to_new_planning_line_handoff_20260612.md
  audit/openclaw_import_allowlist_067D.md
  audit/capability_executor_coverage_inventory_067E.md

backend/xiaobei_ai/
  1013L 壳层底座
  1013K 大单元/课件参考底座
  1013R_R13-R29 备课室协议、页面副本、注册表、路由 fixture
  system_semantic_interaction_runtime/action_policy.py
  system_semantic_interaction_runtime/command_dsl.py

scripts/
  validate_1013R_product_frame_four_level.py
  validate_1013R_R13-R29*.py

outputs/PREP_ROOM_RENDER_CANVAS_DEEPEN_V1/
  R13-R29 result/report/json/html/png
  当前 R21 页面副本
  R22 2K 截图
  R25-R29 新会话 handoff
```

## 当前边界

请按这些边界审核，不要要求本包完成 runtime：

```text
do_not_create_disconnected_static_page
do_not_modify_R36
do_not_return_to_R22_O_R2_M_R5
do_not_connect_model_or_provider
do_not_connect_runtime
do_not_formal_apply
do_not_write_database_feishu_memory
do_not_treat_openclaw_scan_as_field_standard
```

允许：

```text
在当前 R21 页面副本生成器内继续轻连接
新增 docs / outputs / validators
新增 readonly / fixture / registry / contract 模块
给当前页面加 data-shiwei-* 标记
把工具入口静态映射到内容渲染区
```

禁止：

```text
另开孤立静态页
直接改 R36
接 provider/model/runtime
正式保存/导出/归档
写数据库/飞书/记忆
把 OpenClaw 扫描结论当字段标准
```

## 建议审核顺序

```text
1. 先读 handoff md，确认最新上下文。
2. 读 index json，确认机器索引和 GitHub review 链路。
3. 读 docs/1013R_product_frame_four_level.md，确认四级框架。
4. 读 R13-R17，确认任务状态、确认门、ViewModel、来源规则、render_blocks。
5. 读 R18-R24，确认页面副本、可读性、组件边界。
6. 读 R25-R29，确认四级框架、意图路由、各室、工具注册表。
7. 打开 R21 HTML 和 R22 2K 截图，看当前页面实际状态。
8. 给出 R30 是否可推进、如何推进、先做什么、不做什么。
```

## 建议 GPT 输出格式

```text
一、是否同意进入 R30
二、R30 应该做什么
三、R30 不应该做什么
四、当前资料中可复用底座
五、当前资料中只能参考/应归档的内容
六、当前最大风险
七、建议的 R30-R33 路线
八、是否建议上传 GitHub review repo
```

## GitHub 审核递交

如果需要上传 GitHub，沿用本包 handoff 中的“小型独立 review repo”方式：

```text
不要推整个 xiaobei-core
只推本 review package 中的必要文件
repo 建议：
ROLLcatCLUB/xiaojiao-1013r-r25-r30-prep-room-four-level-frame-review
```

可直接参考：

```text
docs/guides/github_review_upload_prompt_template_for_gpt.md
```
