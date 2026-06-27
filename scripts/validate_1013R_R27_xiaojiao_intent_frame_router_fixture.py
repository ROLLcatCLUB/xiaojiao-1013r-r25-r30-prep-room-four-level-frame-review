from __future__ import annotations

import json
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

STAGE_ID = "1013R_R27_XIAOJIAO_INTENT_FRAME_ROUTER_FIXTURE"
OUT_DIR = ROOT / "outputs" / "PREP_ROOM_RENDER_CANVAS_DEEPEN_V1" / "1013R_R27_xiaojiao_intent_frame_router_fixture"
DOC_PATH = ROOT / "docs" / "1013R_R27_xiaojiao_intent_frame_router_fixture.md"


def now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def write_json(path: Path, payload: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def fail(errors: list[str], code: str) -> None:
    errors.append(code)


def validate() -> tuple[dict[str, Any], dict[str, Any], list[str]]:
    from backend.xiaobei_ai import prep_room_xiaojiao_intent_frame_router_1013R_R27 as module

    errors: list[str] = []
    bundle = module.build_router_sample_bundle()
    router = bundle.get("router_fixture", {})
    routes = bundle.get("fixture_routes", [])
    boundary = bundle.get("boundary", {})
    doc = DOC_PATH.read_text(encoding="utf-8", errors="ignore") if DOC_PATH.exists() else ""

    if bundle.get("stage") != STAGE_ID:
        fail(errors, "stage_id_mismatch")
    if router.get("router_id") != "SHIWEI_XIAOJIAO_INTENT_FRAME_ROUTER_FIXTURE_R0":
        fail(errors, "router_id_mismatch")
    if router.get("consumes", {}).get("r26_stage") != "1013R_R26_PAGE_COPY_FOUR_LEVEL_FRAME_MARKERS":
        fail(errors, "r26_not_consumed")
    if len(routes) < 8:
        fail(errors, "fixture_routes_too_few")

    by_message = {item.get("message"): item for item in routes}
    expected_primary = {
        "切到备课室": 2,
        "下面输入栏不好用": 1,
        "备课室工具按钮太乱": 2,
        "这份教案内容层级不清": 4,
        "这个页面整体很乱": 1,
        "把这个教学过程段落改得更适合公开课": 4,
    }
    for message, level in expected_primary.items():
        if by_message.get(message, {}).get("primary_level") != level:
            fail(errors, f"primary_level_mismatch:{message}")

    courseware_route = by_message.get("为什么我找不到课件生成入口", {})
    if {2, 3}.issubset({item.get("level") for item in courseware_route.get("level_path", [])}) is False:
        fail(errors, "courseware_entry_cross_level_missing")

    formal_route = by_message.get("保存到课包并导出课件", {})
    if formal_route.get("command_type") != "ASK_CONFIRMATION":
        fail(errors, "formal_action_not_confirmation")
    if formal_route.get("formal_apply_allowed") is not False:
        fail(errors, "formal_action_apply_allowed")
    if formal_route.get("teacher_confirmation_required") is not True:
        fail(errors, "formal_action_confirmation_not_required")

    for route in routes:
        if route.get("command_allowed_by_existing_dsl") is not True:
            fail(errors, f"command_not_in_existing_dsl:{route.get('message')}")
        if route.get("runtime_call_allowed") is not False or route.get("model_call_allowed") is not False:
            fail(errors, f"runtime_or_model_allowed:{route.get('message')}")

    policy = router.get("routing_policy", {})
    for key in [
        "route_intent_by_framework_level",
        "diagnose_issues_by_framework_level",
        "cross_level_intent_must_be_split",
        "use_frame_markers_before_dom_operation",
        "teacher_confirmation_required_for_formal_actions",
    ]:
        if policy.get(key) is not True:
            fail(errors, f"routing_policy_missing:{key}")
    if policy.get("formal_apply_allowed") is not False:
        fail(errors, "routing_policy_formal_apply_allowed")

    blocked_true_flags = [
        "runtime_router_connected",
        "semantic_runtime_called",
        "provider_called",
        "model_called",
        "database_written",
        "memory_written",
        "vector_index_written",
        "feishu_written",
        "formal_apply_performed",
        "route_registered",
        "endpoint_registered",
        "R36_modified",
        "main_shell_modified",
        "new_disconnected_page_created",
    ]
    for flag in blocked_true_flags:
        if boundary.get(flag):
            fail(errors, f"readonly_boundary_broken:{flag}")
    if boundary.get("intent_frame_router_fixture_defined") is not True:
        fail(errors, "intent_router_fixture_not_marked")
    if boundary.get("static_fixture_only") is not True:
        fail(errors, "static_fixture_only_not_marked")

    for token in [
        "route_intent_by_framework_level=true",
        "runtime_router_connected=false",
        "semantic_runtime_called=false",
        "formal_apply_allowed=false",
        "“这个页面整体很乱” -> 1级到4级递归排查",
        "1013R_R28_ROOM_WORKSPACE_REGISTRY",
    ]:
        if token not in doc:
            fail(errors, f"doc_token_missing:{token}")

    evidence = {
        "module": "backend.xiaobei_ai.prep_room_xiaojiao_intent_frame_router_1013R_R27",
        "router_id": router.get("router_id"),
        "route_count": len(routes),
        "routing_policy": router.get("routing_policy"),
        "boundary": boundary,
    }
    result = {
        "stage_id": STAGE_ID,
        "status": "PASS" if not errors else "FAIL",
        "validator_pass": not errors,
        "created_at": now(),
        "checks": {
            "router_fixture_defined": router.get("router_id") == "SHIWEI_XIAOJIAO_INTENT_FRAME_ROUTER_FIXTURE_R0",
            "uses_existing_command_dsl": not any(code.startswith("command_not_in_existing_dsl") for code in errors),
            "cross_level_courseware_entry_detected": not any(code == "courseware_entry_cross_level_missing" for code in errors),
            "formal_actions_go_to_confirmation": not any(code.startswith("formal_action") for code in errors),
            "static_fixture_only": boundary.get("static_fixture_only") is True,
            "runtime_router_connected": False,
            "formal_apply_performed": False,
        },
        "failed_checks": errors,
    }
    return result, evidence, errors


def write_outputs(result: dict[str, Any], evidence: dict[str, Any]) -> None:
    from backend.xiaobei_ai import prep_room_xiaojiao_intent_frame_router_1013R_R27 as module

    bundle = module.build_router_sample_bundle()
    write_json(OUT_DIR / "1013R_R27_result.json", result)
    write_json(OUT_DIR / "xiaojiao_intent_frame_router_fixture_1013R_R27.json", bundle["router_fixture"])
    write_json(OUT_DIR / "xiaojiao_intent_frame_fixture_routes_1013R_R27.json", bundle["fixture_routes"])
    write_json(OUT_DIR / "xiaojiao_intent_frame_router_evidence_1013R_R27.json", evidence)
    report = f"""# 1013R_R27 Xiaojiao intent frame router fixture

```text
stage_id={STAGE_ID}
router_id=SHIWEI_XIAOJIAO_INTENT_FRAME_ROUTER_FIXTURE_R0
static_fixture_only=true
runtime_router_connected=false
semantic_runtime_called=false
provider_called=false
model_called=false
formal_apply_performed=false
```

## 验证

```text
validator_pass={str(result["validator_pass"]).lower()}
failed_checks={result["failed_checks"]}
```

## 下一步

```text
1013R_R28_ROOM_WORKSPACE_REGISTRY
```
"""
    write_text(OUT_DIR / "1013R_R27_report.md", report)


def main() -> None:
    result, evidence, errors = validate()
    write_outputs(result, evidence)
    if errors:
        raise SystemExit("FAIL: " + ", ".join(errors))
    print("PASS: 1013R_R27 Xiaojiao intent frame router fixture")


if __name__ == "__main__":
    main()
