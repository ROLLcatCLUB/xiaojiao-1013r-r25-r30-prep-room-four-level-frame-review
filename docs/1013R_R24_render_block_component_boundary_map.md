# R24：渲染块组件边界表

```text
stage_id=1013R_R24_RENDER_BLOCK_COMPONENT_BOUNDARY_MAP
boundary_id=SHIWEI_RENDER_BLOCK_COMPONENT_BOUNDARY_MAP_R0
```

R24 只定义 render_blocks 到未来组件的边界，不实现组件，不接底座，不注册 route。

## 四级框架约束

组件边界必须先服从四级产品框架：

```text
framework_reference=docs/1013R_product_frame_four_level.md
level_1=平台外壳框架
level_2=各室工作空间框架
level_3=工具框架
level_4=内容框架
```

R24 当前只处理四级内容组件与部分三级工具入口，不定义一级全局壳，也不把各室结构写死在单个组件里。

## 组件边界

```text
object_summary -> PrepRoomObjectHeader
task_state -> XiaojiaoTaskStatePanel
document_sections -> LessonSectionStack
process_steps -> TeachingProcessTimeline
courseware_preview -> CoursewareScriptPreview
display_preview -> ClassroomDisplayPreview
worksheet_placeholder -> WorksheetPreviewSlot
assessment_blocked -> AssessmentBlockedPanel
source_policy -> SourceEvidencePanel
action_gate -> TeacherActionGatePanel
composer_prompt -> XiaojiaoComposerPrompt
```

所有组件都必须遵守：

```text
may_save_or_export=false
may_call_provider=false
must_respect_gate_type=true
must_not_promote_ai_draft_to_standard=true
```

## 边界

```text
component_implementation_created=false
R36_modified=false
route_registered=false
endpoint_registered=false
provider_called=false
model_called=false
database_written=false
memory_written=false
formal_apply_performed=false
```
