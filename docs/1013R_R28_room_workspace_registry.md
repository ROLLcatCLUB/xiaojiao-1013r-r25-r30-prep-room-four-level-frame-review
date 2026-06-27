# R28：各室工作空间注册表

```text
stage_id=1013R_R28_ROOM_WORKSPACE_REGISTRY
registry_id=SHIWEI_ROOM_WORKSPACE_REGISTRY_R0
consumes=1013R_R27_XIAOJIAO_INTENT_FRAME_ROUTER_FIXTURE + 1013L_R0 + 1013L_R5
```

R28 定义二级“各室工作空间框架”。它从 1013L 壳层状态派生当前可用的备课室状态，不另起一套房间系统。

## 当前可用空间

```text
active_room=备课室
source=1013L render_stage_registry + 1013L state_fetch_adapters + R21 prepNotebook
```

备课室当前承接：

```text
prep_notebook
big_unit_design
single_lesson_design
courseware_workspace
classroom_display_preview
material_intake
week_calendar
```

## 未来空间占位

```text
教室：课堂观察助理
研究室：复盘协作者
资料室：资料整理员
评阅室：评价助理
档案室：成长记录员
```

这些暂时只是 registry placeholder，不做 runtime、不做页面、不做真实数据写入。

## 规则

```text
derive_from_1013L_states_before_adding_new_rooms=true
do_not_make_each_room_a_chat_page=true
level_2_changes_work_context=true
level_1_shell_stays_persistent=true
same_agent_across_rooms=true
```

## 边界

```text
static_registry_only=true
new_room_runtime_created=false
new_disconnected_page_created=false
route_registered=false
endpoint_registered=false
runtime_connected=false
provider_called=false
model_called=false
database_written=false
memory_written=false
formal_apply_performed=false
```

## 下一步

```text
1013R_R29_TOOL_FRAME_REGISTRY
```
