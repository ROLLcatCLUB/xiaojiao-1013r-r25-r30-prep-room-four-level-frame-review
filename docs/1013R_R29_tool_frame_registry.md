# R29：工具框架注册表

```text
stage_id=1013R_R29_TOOL_FRAME_REGISTRY
registry_id=SHIWEI_TOOL_FRAME_REGISTRY_R0
consumes=1013R_R28_ROOM_WORKSPACE_REGISTRY + 1013L_R5 + 1013R_R17 + 1013R_R24
```

R29 定义三级“工具框架”。它从 L5 的 `active_capability`、R17 的 `block_groups` 和 R24 的 `component_groups` 派生，不实现按钮行为，不新开页面。

## 当前工具框架

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

## 渲染组来源

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

## 规则

```text
derive_from_l5_active_capabilities=true
derive_content_modes_from_r17_block_groups=true
derive_component_boundaries_from_r24=true
tool_frame_controls_level_4_content=true
tool_actions_must_respect_teacher_confirmation_gate=true
do_not_make_tool_frame_a_new_page=true
formal_apply_allowed=false
```

## 边界

```text
static_registry_only=true
tool_behavior_implemented=false
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
1013R_R30_RENDER_SURFACE_CONNECTOR_PLAN_OR_VISUAL_TOOL_POLISH
```
