# 师维页面四级产品框架

```text
framework_id=SHIWEI_FOUR_LEVEL_PRODUCT_FRAME_R0
applies_to=师维智教 / 小教常驻教师工作台
current_reference_page=R21 备课室页面副本
```

这是后续页面设计、渲染底座、工具布局和各室扩展的重点框架。所有新页面和新功能先判断自己属于哪一级，再设计数据、交互和组件。

## 四级结构

```text
一级：平台外壳框架
二级：各室工作空间框架
三级：工具框架
四级：内容框架
```

### 一级：平台外壳框架

一级是最外层的师维平台壳。

它包含：

```text
顶部全局栏
底部小教输入栏 / 状态入口
全局身份、搜索、通知、账号、一级导航
```

一级框架不随单个功能频繁改变。老师从备课室切到教室、研究室、资料室时，一级框架保持稳定，只改变当前空间和内容。

设计规则：

```text
top_shell_persistent=true
bottom_xiaojiao_entry_persistent=true
global_identity_persistent=true
do_not_put_room_specific_content_in_level_1=true
```

### 二级：各室工作空间框架

二级是老师进入的具体工作空间。

当前规划包括：

```text
备课室
教室
研究室 / 教研室
资料室 / 知识馆
评阅室
档案室
```

进入不同“室”时，二级结构改变。备课室可以是备课本、课件、大屏、资料依据；教室可以是课堂控制、学生状态、投屏任务；研究室可以是课例复盘、教研材料、问题链。

设计规则：

```text
room_is_level_2=true
room_changes_main_work_context=true
xiaojiao_same_agent_different_room_role=true
do_not_make_every_room_a_chat_page=true
```

### 三级：工具框架

三级是在某个工作空间内，为当前工作提供操作的工具框架。

以备课室为例：

```text
备课本工具
课件工具
大屏工具
资料工具
评价工具
编辑 / 查看 / 确认工具
```

三级框架决定“老师现在用什么工具做事”，但不直接等同于正文内容。工具可以改变四级内容的形态，例如从备课正文切到大屏草稿、课件脚本、学习单、评价表。

设计规则：

```text
tool_frame_is_level_3=true
tool_frame_controls_content_mode=true
tool_actions_must_respect_teacher_confirmation_gate=true
do_not_mix_tool_controls_into_document_body=true
```

### 四级：内容框架

四级是具体被阅读、编辑、预览或确认的内容。

以当前备课室为例：

```text
课题信息
大单元章节
单课备课正文
教学过程
课件脚本
大屏草稿
学习单
评价表
资料来源
修改前 / 修改后 / 小教建议
```

四级内容可以随工具和对象变化。小教生成、修改、预览、阻断提示都应该落在四级内容里，并通过三级工具和确认门推进。

设计规则：

```text
content_is_level_4=true
content_can_change_by_room_and_tool=true
preview_before_apply=true
teacher_confirmation_required_for_write_export_archive_assessment=true
```

## 当前 R21 页面的映射

```text
一级：
  顶部师维全局栏
  底部小教输入栏

二级：
  备课室

三级：
  备课本 / 大屏草稿 / 课件制作 / 资料与依据 / 查看编辑动作

四级：
  三年级第二单元第1课《色彩的渐变》
  大单元章节
  本课依据、学情分析、教学目标、教学过程
  右侧大屏草稿条目
  弹出修改卡片中的修改前、修改后、小教建议
```

## 后续设计判定

后续任何新需求先问四个问题：

```text
1. 它是否改变一级平台外壳？
2. 它是否新增或切换二级工作空间？
3. 它是否只是某个空间内的三级工具？
4. 它是否只是工具下面变化的四级内容？
```

如果没有回答清楚，不进入视觉实现和底座实现。

## 禁止混层

```text
不要把四级内容做成一级全局框架。
不要把三级工具做成独立页面。
不要把二级各室都做成聊天框。
不要让底部小教输入栏替代工作空间。
不要因为某个内容复杂，就破坏一级和二级框架稳定性。
```

一句话原则：

```text
一级定平台稳定感，二级定工作场景，三级定工具能力，四级承载具体内容。
```

## 递归实现规则

四级框架不是只给 UI 排版用的，它也是 Agent 路由、问题定位、功能派发、组件拆分和 ViewModel 设计的底层递归规则。

标准递归顺序：

```text
先判断：是不是一级壳层问题？
不是 ->
再判断：是不是二级空间结构问题？
不是 ->
再判断：是不是三级工具框架问题？
不是 ->
再判断：是不是四级内容渲染问题？
```

工程化表达：

```text
route_intent_by_framework_level=true
diagnose_issues_by_framework_level=true
assign_features_by_framework_level=true
implement_recursively_by_framework_level=true
```

## 小教路由规则

小教收到老师意图后，不应直接回答或直接操作，而应先判断这个意图属于哪一层。

```text
用户说“切到备课室” -> 二级：各室空间
用户说“下面输入栏不好用” -> 一级：全局壳层
用户说“备课室工具按钮太乱” -> 三级：工具框架
用户说“这份教案内容层级不清” -> 四级：内容渲染
用户说“为什么找不到课件生成入口” -> 二级空间 + 三级工具
用户说“这个页面整体很乱” -> 从一级到四级递归排查
```

如果一个问题跨层，必须拆开处理：

```text
问题A：一级壳层
问题B：三级工具
问题C：四级内容
```

不能混在一起改，也不能因为四级内容问题去重做一级壳层。

## 后续开发规则

```text
一级壳层稳定
二级空间切换
三级工具随功能变化
四级内容随任务变化
```

后续无论是：

```text
Agent 路由
功能设计
问题排查
Codex 任务派发
UI 评审
ViewModel 设计
组件拆分
交互改造
```

都必须先按四级框架定位，再进入实现。
