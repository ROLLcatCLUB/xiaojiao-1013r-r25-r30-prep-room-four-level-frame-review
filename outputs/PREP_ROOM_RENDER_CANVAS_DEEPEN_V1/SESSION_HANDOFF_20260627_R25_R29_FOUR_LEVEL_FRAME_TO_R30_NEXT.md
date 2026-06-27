# 新会话交接：1013R_R25-R29 四级框架落地与 R30 下一步

```text
handoff_id=SESSION_HANDOFF_20260627_R25_R29_FOUR_LEVEL_FRAME_TO_R30_NEXT
repo=D:\Documents\SmartEdu\xiaobei-core
current_surface=outputs/PREP_ROOM_RENDER_CANVAS_DEEPEN_V1/1013R_R21_page_copy_binds_unified_package/prep_room_page_copy_binds_unified_package_1013R_R21.html
current_real_lesson=三年级第二单元第1课《色彩的渐变》
current_next_stage=1013R_R30_RENDER_SURFACE_CONNECTOR_PLAN_OR_VISUAL_TOOL_POLISH
```

## 新会话直接贴这句

```text
请先读取 D:\Documents\SmartEdu\xiaobei-core\outputs\PREP_ROOM_RENDER_CANVAS_DEEPEN_V1\SESSION_HANDOFF_20260627_R25_R29_FOUR_LEVEL_FRAME_TO_R30_NEXT.md，然后按当前 R21 页面副本和 R25-R29 四级框架链路继续。不要新开孤立静态页，不要改 R36，不要回到 R22/O_R2/M_R5，不要把 OpenClaw 扫描结论当字段标准，不要接模型/provider/runtime，不要 formal apply。下一步优先做 R30：把 R25-R29 的四级框架、各室注册表、工具框架注册表轻连接到当前 R21 页面可见结构里。
```

## 当前产品判断

当前方向不是普通 AI 聊天框，也不是单纯教案生成器。

```text
师维智教 = 教师工作场景系统
小教 = 常驻同一个助手，多空间切换职责
当前主场景 = 备课室
当前对象 = 三年级第二单元第1课《色彩的渐变》
页面中心 = 当前工作对象 + 任务状态 + 可确认推进
输入框定位 = 推进当前工作的入口之一，不是产品中心
```

当前核心框架已经定为四级递归：

```text
1级：平台外壳框架
2级：各室工作空间框架
3级：工具框架
4级：内容框架
```

后续 Agent 路由、问题排查、功能派发、UI 评审、ViewModel 设计都先按四级框架定位。

## 当前页面与边界

当前可见页面副本：

```text
D:\Documents\SmartEdu\xiaobei-core\outputs\PREP_ROOM_RENDER_CANVAS_DEEPEN_V1\1013R_R21_page_copy_binds_unified_package\prep_room_page_copy_binds_unified_package_1013R_R21.html
```

当前页面生成器：

```text
D:\Documents\SmartEdu\xiaobei-core\backend\xiaobei_ai\prep_room_page_copy_package_binding_1013R_R21.py
```

重要边界：

```text
R36_modified=false
main_shell_modified=false
new_disconnected_page_created=false
route_registered=false
endpoint_registered=false
provider_called=false
model_called=false
database_written=false
memory_written=false
feishu_written=false
formal_apply_performed=false
```

这条线允许：

```text
改当前 R21 页面副本生成器
新增 docs / outputs / validators
新增 readonly / fixture / registry / contract 模块
在当前 R21 页面副本内加 data-* 标记和静态 UI 轻连接
```

这条线禁止：

```text
不要新开一个孤立静态页来替代当前原型
不要直接改 R36 源页面
不要接 provider/model
不要接真实 runtime
不要写数据库/飞书/记忆
不要 formal apply
不要让 OpenClaw 扫描结论替代本项目字段标准
```

## OpenClaw / history-viewer 的使用方式

本轮看过：

```text
http://localhost:9876/history-viewer.html
http://localhost:9876/data/timeline.json
http://localhost:9876/data/inventory-l2.json
http://localhost:9876/data/audit-log.json
```

结论：

```text
history-viewer 只能作为资产索引和扫描线索
inventory-l2 明确偏项目级/L2 扫描，不能当产品真相
OpenClaw 机制可以吸收为流程/方法
OpenClaw runtime / memory 不能导入
```

可参考的 OpenClaw 边界文档：

```text
D:\Documents\SmartEdu\xiaobei-core\docs\audit\openclaw_import_allowlist_067D.md
D:\Documents\SmartEdu\xiaobei-core\docs\audit\capability_executor_coverage_inventory_067E.md
```

## 已落地阶段

### R25：四级框架实现映射

```text
stage_id=1013R_R25_FOUR_LEVEL_FRAME_IMPLEMENTATION_MAP
status=PASS
purpose=把四级框架映射到已有底座，说明复用/参考/摒弃对象
```

核心文件：

```text
backend/xiaobei_ai/prep_room_four_level_frame_implementation_map_1013R_R25.py
docs/1013R_R25_four_level_frame_implementation_map.md
scripts/validate_1013R_R25_four_level_frame_implementation_map.py
outputs/PREP_ROOM_RENDER_CANVAS_DEEPEN_V1/1013R_R25_four_level_frame_implementation_map/
```

R25 关键判断：

```text
1013L shell registry/fetch adapter -> 一级/二级骨架
1013R R15-R24 -> 四级 render_blocks 与组件边界
1013R R21 -> 当前可见页面副本
1013K big-unit/courseware -> 三级工具数据来源
platform_core/render_blocks 0954C -> 参考安全模型，不接 runtime
system_semantic_interaction_runtime -> 参考未来意图/命令门，不接 runtime
frontend/workbench legacy assets -> 挖模式，不重开 workbench 页面
OpenClaw history/scans -> 只作归档索引
```

### R26：R21 页面副本四级框架标记

```text
stage_id=1013R_R26_PAGE_COPY_FOUR_LEVEL_FRAME_MARKERS
status=PASS
purpose=在当前 R21 页面运行时 DOM 里增加 data-shiwei-frame-* 标记
```

核心文件：

```text
backend/xiaobei_ai/prep_room_page_copy_package_binding_1013R_R21.py
backend/xiaobei_ai/prep_room_page_copy_four_level_markers_1013R_R26.py
docs/1013R_R26_page_copy_four_level_frame_markers.md
scripts/validate_1013R_R26_page_copy_four_level_frame_markers.py
outputs/PREP_ROOM_RENDER_CANVAS_DEEPEN_V1/1013R_R26_page_copy_four_level_frame_markers/
```

当前 R21 HTML 已包含：

```text
data-shiwei-four-level-frame
data-shiwei-four-level-stage
data-shiwei-frame-route-rule
data-shiwei-current-room
data-shiwei-frame-level
data-shiwei-frame-key
data-shiwei-frame-role
__SHIWEI_FOUR_LEVEL_FRAME_MARKERS__
```

R26 不改变可见布局，只加可路由/可排查的 DOM 标记。

### R27：小教意图层级路由 fixture

```text
stage_id=1013R_R27_XIAOJIAO_INTENT_FRAME_ROUTER_FIXTURE
status=PASS
purpose=静态判断老师意图属于 1/2/3/4 哪一层
```

核心文件：

```text
backend/xiaobei_ai/prep_room_xiaojiao_intent_frame_router_1013R_R27.py
docs/1013R_R27_xiaojiao_intent_frame_router_fixture.md
scripts/validate_1013R_R27_xiaojiao_intent_frame_router_fixture.py
outputs/PREP_ROOM_RENDER_CANVAS_DEEPEN_V1/1013R_R27_xiaojiao_intent_frame_router_fixture/
```

示例：

```text
“切到备课室” -> 2级：各室工作空间框架
“下面输入栏不好用” -> 1级：平台外壳框架
“备课室工具按钮太乱” -> 2级 + 3级
“这份教案内容层级不清” -> 4级：内容框架
“为什么找不到课件生成入口” -> 2级 + 3级
“这个页面整体很乱” -> 1级到4级递归排查
“保存到课包并导出课件” -> ASK_CONFIRMATION，formal_apply_allowed=false
```

R27 复用：

```text
backend/xiaobei_ai/system_semantic_interaction_runtime/action_policy.py
backend/xiaobei_ai/system_semantic_interaction_runtime/command_dsl.py
```

但 R27 没有接真实 runtime。

### R28：各室工作空间注册表

```text
stage_id=1013R_R28_ROOM_WORKSPACE_REGISTRY
status=PASS
purpose=定义二级空间，当前 active_room=备课室
```

核心文件：

```text
backend/xiaobei_ai/prep_room_room_workspace_registry_1013R_R28.py
docs/1013R_R28_room_workspace_registry.md
scripts/validate_1013R_R28_room_workspace_registry.py
outputs/PREP_ROOM_RENDER_CANVAS_DEEPEN_V1/1013R_R28_room_workspace_registry/
```

当前从 1013L 派生出的备课室状态：

```text
prep_notebook
big_unit_design
single_lesson_design
courseware_workspace
classroom_display_preview
material_intake
week_calendar
```

未来空间只做占位：

```text
教室：课堂观察助理
研究室：复盘协作者
资料室：资料整理员
评阅室：评价助理
档案室：成长记录员
```

### R29：工具框架注册表

```text
stage_id=1013R_R29_TOOL_FRAME_REGISTRY
status=PASS
purpose=定义三级工具框架，从 L5 + R17 + R24 派生
```

核心文件：

```text
backend/xiaobei_ai/prep_room_tool_frame_registry_1013R_R29.py
docs/1013R_R29_tool_frame_registry.md
scripts/validate_1013R_R29_tool_frame_registry.py
outputs/PREP_ROOM_RENDER_CANVAS_DEEPEN_V1/1013R_R29_tool_frame_registry/
```

当前工具框架：

```text
prep_notebook：备课本
prep_room_home：开始
big_unit_design：大单元
single_lesson_prep：单课
courseware_workspace：课件
classroom_display_preview：大屏
material_intake：资料
schedule_context：周课表
teacher_action_gate：教师确认门
source_evidence：资料来源与依据
xiaojiao_bottom_composer：小教推进入口
```

渲染组来源：

```text
R17 block_groups:
lesson_core
derivatives
governance

R24 component_groups:
prep_room_core
derivative_objects
governance_and_actions
```

## 重要底座索引

### 1013L 壳层 / 状态底座

```text
backend/xiaobei_ai/prep_room_render_shell_registry_1013L_R0.py
backend/xiaobei_ai/prep_room_main_shell_fetch_adapter_1013L_R5.py
```

作用：

```text
一级壳层稳定
二级 RenderStage 状态
readonly fetch adapter
不要重写
```

### 1013R ViewModel / render_blocks / action gate

```text
backend/xiaobei_ai/prep_room_unified_viewmodel_1013R_R15.py
backend/xiaobei_ai/prep_room_source_policy_validator_1013R_R16.py
backend/xiaobei_ai/prep_room_render_blocks_protocol_1013R_R17.py
backend/xiaobei_ai/prep_room_derivative_static_linkage_1013R_R19.py
backend/xiaobei_ai/prep_room_unified_package_readonly_export_1013R_R20.py
backend/xiaobei_ai/prep_room_render_block_component_boundary_1013R_R24.py
```

作用：

```text
统一 ViewModel
资料来源轻规则
render_blocks 协议
派生物静态联动
只读统一包
组件边界
```

### 当前可见页面线

```text
backend/xiaobei_ai/prep_room_page_copy_package_binding_1013R_R21.py
outputs/PREP_ROOM_RENDER_CANVAS_DEEPEN_V1/1013R_R21_page_copy_binds_unified_package/prep_room_page_copy_binds_unified_package_1013R_R21.html
```

这就是当前继续改的原型页，不要另开孤立页。

### 大单元 / 课件 / 大屏历史底座

```text
backend/xiaobei_ai/prep_room_big_unit_render_viewmodel_1013K_R7.py
backend/xiaobei_ai/prep_room_big_unit_renderer_fetch_adapter_1013K_R13.py
outputs/PREP_ROOM_RENDER_CANVAS_DEEPEN_V1/1013K_R29A_courseware_viewmodel_normalization_before_visible_render/
```

注意：

```text
这些是底座线索，优先接，不要重写大单元/课件字段。
```

## 当前验证命令

```powershell
python scripts/validate_1013R_product_frame_four_level.py
python scripts/validate_1013R_R21_page_copy_binds_unified_package.py
python scripts/validate_1013R_R22_teacher_readability_and_2k_linkage_smoke.py
python scripts/validate_1013R_R25_four_level_frame_implementation_map.py
python scripts/validate_1013R_R26_page_copy_four_level_frame_markers.py
python scripts/validate_1013R_R27_xiaojiao_intent_frame_router_fixture.py
python scripts/validate_1013R_R28_room_workspace_registry.py
python scripts/validate_1013R_R29_tool_frame_registry.py
```

最新结果：

```text
PASS: 1013R product frame four level
PASS: 1013R_R21 page copy binds unified package
PASS: 1013R_R22 teacher readability and 2K linkage smoke
PASS: 1013R_R25 four level frame implementation map
PASS: 1013R_R26 page copy four level frame markers
PASS: 1013R_R27 Xiaojiao intent frame router fixture
PASS: 1013R_R28 room workspace registry
PASS: 1013R_R29 tool frame registry
```

## GitHub 审核递交链路

后续如果要把 R25-R29 或 R30 审核材料交给 GPT / 外部审核，不要推整个 `xiaobei-core` 主仓。

沿用项目既有习惯：

```text
stage outputs
-> 本地 validator 通过
-> 小型独立 GitHub review repo
-> README + result/report/manifest/validator/raw links
-> 发 raw link 给 GPT 审核
-> 根据审核结论决定下一阶段
```

可复用模板：

```text
D:\Documents\SmartEdu\xiaobei-core\docs\guides\github_review_upload_prompt_template_for_gpt.md
D:\Documents\SmartEdu\xiaobei-core\docs\handoff\xiaojiao_teacher_jarvis_workbench_1000A_to_new_planning_line_handoff_20260612.md
```

建议本线 review repo 命名：

```text
ROLLcatCLUB/xiaojiao-1013r-r25-r30-prep-room-four-level-frame-review
```

建议本地 review 目录：

```text
D:\Documents\SmartEdu\xiaobei-github-review\xiaojiao-1013r-r25-r30-prep-room-four-level-frame-review
```

审核包只复制必要材料，保留相对路径。当前至少应包含：

```text
outputs/PREP_ROOM_RENDER_CANVAS_DEEPEN_V1/SESSION_HANDOFF_20260627_R25_R29_FOUR_LEVEL_FRAME_TO_R30_NEXT.md
outputs/PREP_ROOM_RENDER_CANVAS_DEEPEN_V1/SESSION_HANDOFF_20260627_R25_R29_FOUR_LEVEL_FRAME_TO_R30_NEXT.index.json
docs/1013R_product_frame_four_level.md
docs/1013R_R25_four_level_frame_implementation_map.md
docs/1013R_R26_page_copy_four_level_frame_markers.md
docs/1013R_R27_xiaojiao_intent_frame_router_fixture.md
docs/1013R_R28_room_workspace_registry.md
docs/1013R_R29_tool_frame_registry.md
backend/xiaobei_ai/prep_room_page_copy_package_binding_1013R_R21.py
backend/xiaobei_ai/prep_room_four_level_frame_implementation_map_1013R_R25.py
backend/xiaobei_ai/prep_room_page_copy_four_level_markers_1013R_R26.py
backend/xiaobei_ai/prep_room_xiaojiao_intent_frame_router_1013R_R27.py
backend/xiaobei_ai/prep_room_room_workspace_registry_1013R_R28.py
backend/xiaobei_ai/prep_room_tool_frame_registry_1013R_R29.py
scripts/validate_1013R_product_frame_four_level.py
scripts/validate_1013R_R21_page_copy_binds_unified_package.py
scripts/validate_1013R_R22_teacher_readability_and_2k_linkage_smoke.py
scripts/validate_1013R_R25_four_level_frame_implementation_map.py
scripts/validate_1013R_R26_page_copy_four_level_frame_markers.py
scripts/validate_1013R_R27_xiaojiao_intent_frame_router_fixture.py
scripts/validate_1013R_R28_room_workspace_registry.py
scripts/validate_1013R_R29_tool_frame_registry.py
outputs/PREP_ROOM_RENDER_CANVAS_DEEPEN_V1/1013R_R25_four_level_frame_implementation_map/1013R_R25_result.json
outputs/PREP_ROOM_RENDER_CANVAS_DEEPEN_V1/1013R_R26_page_copy_four_level_frame_markers/1013R_R26_result.json
outputs/PREP_ROOM_RENDER_CANVAS_DEEPEN_V1/1013R_R27_xiaojiao_intent_frame_router_fixture/1013R_R27_result.json
outputs/PREP_ROOM_RENDER_CANVAS_DEEPEN_V1/1013R_R28_room_workspace_registry/1013R_R28_result.json
outputs/PREP_ROOM_RENDER_CANVAS_DEEPEN_V1/1013R_R29_tool_frame_registry/1013R_R29_result.json
outputs/PREP_ROOM_RENDER_CANVAS_DEEPEN_V1/1013R_R21_page_copy_binds_unified_package/prep_room_page_copy_binds_unified_package_1013R_R21.html
outputs/PREP_ROOM_RENDER_CANVAS_DEEPEN_V1/1013R_R22_teacher_readability_and_2k_linkage_smoke/1013R_R22_2k_teacher_readability_check.png
```

如果 R30 之后新增审核报告，应追加：

```text
docs/1013R_R30_*.md
backend/xiaobei_ai/*1013R_R30*.py
scripts/validate_1013R_R30_*.py
outputs/PREP_ROOM_RENDER_CANVAS_DEEPEN_V1/1013R_R30_*/
docs/audit/*1013R_R30*_report.md
docs/audit/*1013R_R30*_result.json
docs/audit/*1013R_R30*_checklist.json
docs/audit_packages/*1013R_R30*_manifest.json
docs/audit_packages/*1013R_R30*.zip
```

禁止上传：

```text
.env
token
secret
真实学生数据
真实课堂日志
飞书 token
provider raw prompt/response
node_modules
__pycache__
整个 xiaobei-core 仓库
database 文件
```

上传前在 review repo 写入 `.gitattributes`，避免换行改变哈希：

```powershell
[System.IO.File]::WriteAllBytes(
  (Join-Path $target ".gitattributes"),
  [System.Text.Encoding]::ASCII.GetBytes("* -text`n")
)
```

推荐上传命令：

```powershell
cd D:\Documents\SmartEdu\xiaobei-core
gh auth status -h github.com

$reviewRoot = "D:\Documents\SmartEdu\xiaobei-github-review"
$repoName = "xiaojiao-1013r-r25-r30-prep-room-four-level-frame-review"
$target = Join-Path $reviewRoot $repoName
New-Item -ItemType Directory -Force -Path $target | Out-Null

# 按上面的复制清单复制文件，保留相对路径。
# 在 $target 新增 README.md 和 .gitattributes。

Set-Location $target
git init -b master
git add .
git commit -m "Add 1013R prep room four-level frame review package"
gh repo create ROLLcatCLUB/$repoName --public --source . --remote origin --push
```

如果 repo 已存在：

```powershell
Set-Location $target
git init -b master
git add .
git commit -m "Refresh 1013R prep room four-level frame review package"
git remote add origin https://github.com/ROLLcatCLUB/$repoName.git
git push -u origin master --force
```

Raw link 模板：

```text
Repo:
https://github.com/ROLLcatCLUB/xiaojiao-1013r-r25-r30-prep-room-four-level-frame-review

README:
https://raw.githubusercontent.com/ROLLcatCLUB/xiaojiao-1013r-r25-r30-prep-room-four-level-frame-review/master/README.md

Handoff:
https://raw.githubusercontent.com/ROLLcatCLUB/xiaojiao-1013r-r25-r30-prep-room-four-level-frame-review/master/outputs/PREP_ROOM_RENDER_CANVAS_DEEPEN_V1/SESSION_HANDOFF_20260627_R25_R29_FOUR_LEVEL_FRAME_TO_R30_NEXT.md

Index:
https://raw.githubusercontent.com/ROLLcatCLUB/xiaojiao-1013r-r25-r30-prep-room-four-level-frame-review/master/outputs/PREP_ROOM_RENDER_CANVAS_DEEPEN_V1/SESSION_HANDOFF_20260627_R25_R29_FOUR_LEVEL_FRAME_TO_R30_NEXT.index.json

R29 result:
https://raw.githubusercontent.com/ROLLcatCLUB/xiaojiao-1013r-r25-r30-prep-room-four-level-frame-review/master/outputs/PREP_ROOM_RENDER_CANVAS_DEEPEN_V1/1013R_R29_tool_frame_registry/1013R_R29_result.json
```

发给 GPT 的审核口径：

```text
请审核这个 GitHub review area：

https://github.com/ROLLcatCLUB/xiaojiao-1013r-r25-r30-prep-room-four-level-frame-review

重点读取：
- README.md
- handoff md
- index json
- docs/1013R_R25-R29*.md
- outputs/*result.json
- scripts/validate_*.py
- 当前 R21 HTML 页面副本
- R22 2K 截图

请判断：
1. R25-R29 是否已经足够作为 R30 前置协议
2. 是否仍遵守不改 R36、不新开孤立静态页、不接 provider/runtime、不 formal apply
3. R30 是否应优先做四级框架到 R21 可见结构的轻连接
4. 是否存在重复版本、字段退化、工具框架断裂、审核材料夹带 forbidden files 的问题
5. 是否可以进入 recommended_next_stage

注意：
这是 review area，不是完整源码仓库。
OpenClaw/history-viewer 只作资产索引，不能替代本项目字段标准。
```

## 下一步：R30 建议

建议下一步：

```text
1013R_R30_RENDER_SURFACE_CONNECTOR_PLAN_OR_VISUAL_TOOL_POLISH
```

R30 不做完整渲染 runtime，也不接模型。

R30 目标：

```text
把 R25-R29 的框架协议接到当前 R21 页面的可见结构里
让页面能看出：
  1级：顶部 + 底部小教输入栏
  2级：当前空间 = 备课室
  3级：备课本 / 大单元 / 单课 / 课件 / 大屏 / 资料 / 评价 / 确认门
  4级：正文、教学过程、修改卡片、大屏草稿、来源依据
```

R30 可做：

```text
1. 右侧工具区轻整理：按 R29 工具注册表归组
2. 给当前页已有工具入口加 data-shiwei-tool-id / data-shiwei-room-id
3. 让工具与四级内容形成静态映射：
   课件 -> courseware_script / courseware_screens
   大屏 -> classroom_display_screen
   资料 -> source_evidence / materials_list
   评价 -> assessment_rubric
   编辑 -> 修改前 / 修改后 / 小教建议
4. 保持现有页面视觉，不做大改版
5. 继续只在 R21 页面副本生成器内实现
```

R30 不做：

```text
不接 provider/model
不接真实 runtime
不做真实保存/导出/归档
不写数据库/飞书/记忆
不改 R36
不新开孤立静态页
```

## 一句话路线

```text
R25-R29 已经把“四级框架、意图路由、各室注册表、工具注册表”落成底层协议；
R30 开始把这些协议轻连接到当前 R21 页面可见结构；
R31 以后再考虑右侧工具区重组、大屏/课件/学习单/评价表静态联动，以及 render_blocks 到页面内容区的轻量连接器。
```
