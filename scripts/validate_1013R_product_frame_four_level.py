from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOC_PATH = ROOT / "docs" / "1013R_product_frame_four_level.md"
R21_DOC = ROOT / "docs" / "1013R_R21_page_copy_binds_unified_package.md"
R17_DOC = ROOT / "docs" / "1013R_R17_render_blocks_protocol.md"
R24_DOC = ROOT / "docs" / "1013R_R24_render_block_component_boundary_map.md"
OUT_DIR = ROOT / "outputs" / "PREP_ROOM_RENDER_CANVAS_DEEPEN_V1" / "1013R_product_frame_four_level"


def now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore") if path.exists() else ""


def write_json(path: Path, payload: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def main() -> None:
    errors: list[str] = []
    frame = read(DOC_PATH)
    r21 = read(R21_DOC)
    r17 = read(R17_DOC)
    r24 = read(R24_DOC)

    required_frame_tokens = [
        "framework_id=SHIWEI_FOUR_LEVEL_PRODUCT_FRAME_R0",
        "一级：平台外壳框架",
        "二级：各室工作空间框架",
        "三级：工具框架",
        "四级：内容框架",
        "顶部全局栏",
        "底部小教输入栏",
        "备课室",
        "教室",
        "研究室",
        "资料室",
        "tool_frame_controls_content_mode=true",
        "preview_before_apply=true",
        "递归实现规则",
        "小教路由规则",
        "route_intent_by_framework_level=true",
        "diagnose_issues_by_framework_level=true",
        "assign_features_by_framework_level=true",
        "implement_recursively_by_framework_level=true",
        "一级壳层稳定",
        "二级空间切换",
        "三级工具随功能变化",
        "四级内容随任务变化",
        "从一级到四级递归排查",
        "一级定平台稳定感，二级定工作场景，三级定工具能力，四级承载具体内容。",
    ]
    for token in required_frame_tokens:
        if token not in frame:
            errors.append(f"frame_token_missing:{token}")

    for label, text in [
        ("r21", r21),
        ("r17", r17),
        ("r24", r24),
    ]:
        if "docs/1013R_product_frame_four_level.md" not in text:
            errors.append(f"{label}_framework_reference_missing")

    result = {
        "stage_id": "1013R_PRODUCT_FRAME_FOUR_LEVEL",
        "status": "PASS" if not errors else "FAIL",
        "validator_pass": not errors,
        "created_at": now(),
        "checks": {
            "framework_doc_exists": DOC_PATH.exists(),
            "level_1_shell_defined": "一级：平台外壳框架" in frame,
            "level_2_room_defined": "二级：各室工作空间框架" in frame,
            "level_3_tool_defined": "三级：工具框架" in frame,
            "level_4_content_defined": "四级：内容框架" in frame,
            "r21_references_framework": "docs/1013R_product_frame_four_level.md" in r21,
            "r17_references_framework": "docs/1013R_product_frame_four_level.md" in r17,
            "r24_references_framework": "docs/1013R_product_frame_four_level.md" in r24,
            "recursive_rule_defined": "implement_recursively_by_framework_level=true" in frame,
            "agent_routing_rule_defined": "route_intent_by_framework_level=true" in frame and "小教路由规则" in frame,
            "diagnosis_rule_defined": "diagnose_issues_by_framework_level=true" in frame,
        },
        "failed_checks": errors,
    }
    write_json(OUT_DIR / "1013R_product_frame_four_level_result.json", result)
    if errors:
        raise SystemExit("FAIL: " + ", ".join(errors))
    print("PASS: 1013R product frame four level")


if __name__ == "__main__":
    main()
