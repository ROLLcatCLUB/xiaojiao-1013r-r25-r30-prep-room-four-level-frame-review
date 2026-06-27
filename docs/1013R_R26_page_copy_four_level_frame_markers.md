# R26：R21 页面副本四级框架标记

```text
stage_id=1013R_R26_PAGE_COPY_FOUR_LEVEL_FRAME_MARKERS
marker_id=SHIWEI_PAGE_COPY_FOUR_LEVEL_FRAME_MARKERS_R0
consumes=1013R_R25_FOUR_LEVEL_FRAME_IMPLEMENTATION_MAP + 1013R_R21_PAGE_COPY_BINDS_UNIFIED_PACKAGE
```

R26 只在当前 R21 页面副本的运行时 DOM 上增加 `data-shiwei-frame-*` 标记，不重开页面，不改变可见布局，不注册后端 route。

## 标记规则

```text
data-shiwei-four-level-frame=true
data-shiwei-four-level-stage=1013R_R26_PAGE_COPY_FOUR_LEVEL_FRAME_MARKERS
data-shiwei-frame-route-rule=level_1_to_level_4_recursive
data-shiwei-current-room=prep_room
data-shiwei-frame-level=1|2|3|4
data-shiwei-frame-key=platform_shell|room_workspace|tool_frame|content_rendering
```

## 四级目标

```text
1级：.topbar / .xiaobei-chat-entry / #chatInput / #statusMain
2级：.canvas-stage / .render-layer / .nb-scene / .nb-binder
3级：.nb-panel / .nb-right-rail / .nb-drawer / .nb-state-bar / 章节动作工具
4级：.nb-workspace / .nb-doc-section / .nb-flow-step / .nb-step-detail-item / .r36-edit-bubble / .r6p-modal
```

## 边界

```text
runtime_dom_data_markers_added=true
visible_layout_modified=false
new_disconnected_page_created=false
R36_modified=false
main_shell_modified=false
route_registered=false
endpoint_registered=false
provider_called=false
model_called=false
database_written=false
memory_written=false
formal_apply_performed=false
```

## 下一步

```text
1013R_R27_XIAOJIAO_INTENT_FRAME_ROUTER_FIXTURE
```
