# 1013R_R17 render_blocks 协议

```text
stage_id=1013R_R17_RENDER_BLOCKS_PROTOCOL_R0
protocol_id=SHIWEI_RENDER_BLOCKS_PROTOCOL_R0
current_object=2-1《色彩的渐变》
```

## 定位

R17 把 R15 的 `render_slots` 转成稳定的 `render_blocks`。

后续渲染底座不直接读临时页面字段，而是读：

```text
render_blocks[]
```

## 四级框架约束

render_blocks 只属于四级内容框架，不能反向改写一级平台外壳、二级各室结构或三级工具框架。

```text
framework_reference=docs/1013R_product_frame_four_level.md
render_blocks_level=4
room_frame_level=2
tool_frame_level=3
```

每个 block 必须包含：

```text
block_id
slot_id
block_type
title
order
render_state
gate_type
content_ref
source_badges
available_actions
formal_apply_allowed=false
```

## 分组

```text
lesson_core=当前对象、小教状态、备课正文、教学过程
derivatives=教师示范、课件脚本、大屏、学习单、评价表、板书
governance=材料、来源、确认动作、小教输入
```

## 渲染要求

```text
must_render_block_title=true
must_show_gate_state=true
must_show_source_badges=true
must_not_formal_apply=true
must_not_call_provider=true
```

## 下一步

```text
1013R_R18_LIGHT_RENDER_ADAPTER_SAMPLE
```
