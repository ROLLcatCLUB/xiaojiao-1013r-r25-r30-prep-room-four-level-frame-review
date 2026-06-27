# R27：小教意图层级路由 Fixture

```text
stage_id=1013R_R27_XIAOJIAO_INTENT_FRAME_ROUTER_FIXTURE
router_id=SHIWEI_XIAOJIAO_INTENT_FRAME_ROUTER_FIXTURE_R0
consumes=1013R_R26_PAGE_COPY_FOUR_LEVEL_FRAME_MARKERS
```

R27 把“小教先判断问题属于哪一层”落成静态 fixture。它复用现有 `system_semantic_interaction_runtime` 的 `action_policy` 和 `command_dsl` 词表，但不调用运行时、不接模型。

## 路由原则

```text
route_intent_by_framework_level=true
diagnose_issues_by_framework_level=true
recursive_order=1,2,3,4
cross_level_intent_must_be_split=true
use_frame_markers_before_dom_operation=true
teacher_confirmation_required_for_formal_actions=true
formal_apply_allowed=false
```

## 示例

```text
“切到备课室” -> 2级：各室工作空间框架
“下面输入栏不好用” -> 1级：平台外壳框架
“备课室工具按钮太乱” -> 3级：工具框架
“这份教案内容层级不清” -> 4级：内容框架
“为什么找不到课件生成入口” -> 2级 + 3级
“这个页面整体很乱” -> 1级到4级递归排查
“保存到课包并导出课件” -> ASK_CONFIRMATION，formal_apply_allowed=false
```

## 边界

```text
static_fixture_only=true
runtime_router_connected=false
semantic_runtime_called=false
provider_called=false
model_called=false
database_written=false
memory_written=false
route_registered=false
endpoint_registered=false
formal_apply_performed=false
```

## 下一步

```text
1013R_R28_ROOM_WORKSPACE_REGISTRY
```
