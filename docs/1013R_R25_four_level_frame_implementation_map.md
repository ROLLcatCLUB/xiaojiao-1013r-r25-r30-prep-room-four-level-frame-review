# R25：四级框架实现映射

```text
stage_id=1013R_R25_FOUR_LEVEL_FRAME_IMPLEMENTATION_MAP
map_id=SHIWEI_FOUR_LEVEL_FRAME_IMPLEMENTATION_MAP_R0
framework_reference=docs/1013R_product_frame_four_level.md
```

R25 不改页面，不注册 route，不接 runtime。它只把“师维四级递归框架”落成一张实现映射表，说明后续 R26-R29 应该接哪些已有底座、哪些只作为参考、哪些必须摒弃。

## 当前判断

```text
history_viewer_used_as_index_only=true
OpenClaw_runtime_imported=false
OpenClaw_memory_imported=false
new_disconnected_page_created=false
R36_modified=false
provider_called=false
model_called=false
formal_apply_performed=false
```

`http://localhost:9876/history-viewer.html` 只能作为归档入口和资产线索。它的 `inventory-l2.json` 已说明自己是项目级扫描，并未深读所有代码，所以不能直接当产品真相或字段标准。

## 四级实现映射

### 一级：平台外壳框架

复用：

```text
1013L_R0 shell_shape.top_shell_persistent
1013L_R0 shell_shape.bottom_agent_bar_persistent
1013L_R5 main shell ViewModel adapter
R21 当前顶部栏和底部小教输入栏
```

R26 只在当前 R21 页面副本里加标记，不新开页面。

### 二级：各室工作空间框架

复用：

```text
1013L_R0 render_stage_registry
1013L_R5 state_fetch_adapters
R21 body[data-active-view='prepNotebook']
```

R28 各室注册表必须从 1013L 的已有状态派生，不另起一套房间列表。

### 三级：工具框架

复用：

```text
1013L_R5 active_capability
1013R_R17 block_groups
1013R_R24 component_groups
R21 右侧栏 / 章节动作 / 查看编辑按钮
```

R29 工具框架注册表必须从 L5 的 state_fetch_adapters 与 R17/R24 的渲染组派生。

### 四级：内容框架

复用：

```text
1013R_R15 render_slots
1013R_R17 render_blocks
1013R_R20 unified package
1013R_R24 component_boundary_entries
1013R_R21 R36 edit bubble reuse and big-unit row binding
```

内容层承载单课备课正文、大单元章节、教学过程步骤、大屏草稿、课件脚本、资料来源、修改卡片和小教建议。

## 资产决策

```text
1013L shell registry/fetch adapter -> 接入一级和二级骨架
1013R R15-R24 -> 接入四级 render_blocks 与组件边界
1013R R21 -> 保持为当前可见页面副本
1013K big-unit/courseware -> 接入三级工具数据来源
platform_core/render_blocks 0954C -> 参考安全模型，不接 runtime
system_semantic_interaction_runtime -> 参考未来意图/命令门，不接 runtime
frontend/workbench legacy assets -> 挖模式，不重开 workbench 页面
OpenClaw history/scans -> 只作归档索引，不导入 runtime/memory
```

## 后续顺序

```text
R26：在当前 R21 页面副本内加四级框架标记
R27：小教意图层级路由 fixture，静态不接模型
R28：各室工作空间注册表，派生自 1013L 状态
R29：工具框架注册表，派生自 L5 与 R17/R24
```

## 禁止

```text
不要新开孤立静态页
不要把 OpenClaw 扫描结论当字段标准
不要导入 OpenClaw runtime 或 memory
不要接 provider/model
不要写库、写飞书、写记忆
不要 formal apply
不要绕过教师确认门
```
