from __future__ import annotations

import json
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

STAGE_ID = "1013R_R17_RENDER_BLOCKS_PROTOCOL_R0"
STAGE_DIR = ROOT / "outputs" / "PREP_ROOM_RENDER_CANVAS_DEEPEN_V1" / "1013R_R17_render_blocks_protocol_r0"
DOC_PATH = ROOT / "docs" / "1013R_R17_render_blocks_protocol.md"


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
    from backend.xiaobei_ai import prep_room_render_blocks_protocol_1013R_R17 as module

    errors: list[str] = []
    bundle = module.build_protocol_sample_bundle()
    protocol = bundle.get("render_blocks_protocol", {})
    blocks = bundle.get("render_blocks", [])
    boundary = bundle.get("boundary", {})
    doc = DOC_PATH.read_text(encoding="utf-8", errors="ignore") if DOC_PATH.exists() else ""
    blocks_by_slot = {item.get("slot_id"): item for item in blocks if isinstance(item, dict)}

    if bundle.get("stage") != STAGE_ID:
        fail(errors, "stage_id_mismatch")
    if protocol.get("stage") != STAGE_ID:
        fail(errors, "protocol_stage_mismatch")
    if protocol.get("protocol_id") != "SHIWEI_RENDER_BLOCKS_PROTOCOL_R0":
        fail(errors, "protocol_id_mismatch")
    if protocol.get("consumes", {}).get("unified_viewmodel_stage") != "1013R_R15_PREP_ROOM_UNIFIED_VIEWMODEL_R0":
        fail(errors, "r15_unified_viewmodel_not_consumed")
    if protocol.get("consumes", {}).get("source_policy_stage") != "1013R_R16_SOURCE_POLICY_LIGHT_VALIDATOR_R0":
        fail(errors, "r16_source_policy_not_consumed")
    if protocol.get("consumes", {}).get("current_object", {}).get("title") != "2-1《色彩的渐变》":
        fail(errors, "current_object_not_preserved")
    if len(blocks) < 14:
        fail(errors, "render_blocks_too_few")

    required_slots = [
        "lesson_body",
        "courseware_script",
        "classroom_display_screen",
        "worksheet",
        "assessment_rubric",
        "source_evidence",
        "confirm_actions",
    ]
    for slot_id in required_slots:
        if slot_id not in blocks_by_slot:
            fail(errors, f"block_missing_for_slot:{slot_id}")
    if blocks_by_slot.get("courseware_script", {}).get("block_type") != "courseware_preview":
        fail(errors, "courseware_block_type_mismatch")
    if blocks_by_slot.get("classroom_display_screen", {}).get("block_type") != "display_preview":
        fail(errors, "display_block_type_mismatch")
    if blocks_by_slot.get("assessment_rubric", {}).get("block_type") != "assessment_blocked":
        fail(errors, "assessment_block_type_mismatch")

    for block in blocks:
        for field in ["block_id", "slot_id", "block_type", "title", "order", "render_state", "gate_type", "content_ref"]:
            if field not in block:
                fail(errors, f"block_field_missing:{block.get('slot_id')}:{field}")
        if block.get("formal_apply_allowed"):
            fail(errors, f"block_allows_formal_apply:{block.get('slot_id')}")
        if not block.get("source_badges"):
            fail(errors, f"block_source_badges_missing:{block.get('slot_id')}")

    requirements = protocol.get("renderer_requirements", {})
    for key in ["stable_order", "must_render_block_title", "must_show_gate_state", "must_show_source_badges", "must_not_formal_apply", "must_not_call_provider"]:
        if not requirements.get(key):
            fail(errors, f"renderer_requirement_missing:{key}")

    blocked_true_flags = [
        "provider_called",
        "model_called",
        "database_written",
        "memory_written",
        "vector_index_written",
        "feishu_written",
        "formal_apply_performed",
        "R36_modified",
        "main_shell_modified",
        "runtime_write_allowed",
        "route_registered",
    ]
    for flag in blocked_true_flags:
        if boundary.get(flag):
            fail(errors, f"readonly_boundary_broken:{flag}")
    if not boundary.get("render_blocks_protocol_readonly"):
        fail(errors, "render_blocks_protocol_readonly_not_marked")
    if not boundary.get("render_blocks_protocol_defined"):
        fail(errors, "render_blocks_protocol_defined_not_marked")

    if not DOC_PATH.exists():
        fail(errors, "r17_doc_missing")
    for token in ["SHIWEI_RENDER_BLOCKS_PROTOCOL_R0", "render_blocks", "must_not_formal_apply=true"]:
        if token not in doc:
            fail(errors, f"r17_doc_token_missing:{token}")

    evidence = {
        "module": "backend.xiaobei_ai.prep_room_render_blocks_protocol_1013R_R17",
        "protocol_id": protocol.get("protocol_id"),
        "block_count": len(blocks),
        "block_groups": protocol.get("block_groups"),
        "requirements": requirements,
        "boundary": boundary,
    }
    result = {
        "stage_id": STAGE_ID,
        "status": "PASS" if not errors else "FAIL",
        "validator_pass": not errors,
        "created_at": now(),
        "checks": {
            "render_blocks_protocol_defined": protocol.get("protocol_id") == "SHIWEI_RENDER_BLOCKS_PROTOCOL_R0",
            "r15_and_r16_consumed": not any(code in errors for code in ["r15_unified_viewmodel_not_consumed", "r16_source_policy_not_consumed"]),
            "major_blocks_present": all(slot_id in blocks_by_slot for slot_id in required_slots),
            "no_block_allows_formal_apply": not any(code.startswith("block_allows_formal_apply") for code in errors),
            "readonly_boundaries_intact": not any(code.startswith("readonly_boundary_broken") for code in errors),
            "R36_modified": False,
            "provider_called": False,
            "model_called": False,
            "formal_apply_performed": False,
        },
        "failed_checks": errors,
    }
    return result, evidence, errors


def write_outputs(result: dict[str, Any], evidence: dict[str, Any]) -> None:
    from backend.xiaobei_ai import prep_room_render_blocks_protocol_1013R_R17 as module

    bundle = module.build_protocol_sample_bundle()
    write_json(STAGE_DIR / "1013R_R17_result.json", result)
    write_json(STAGE_DIR / "render_blocks_protocol_1013R_R17.json", bundle["render_blocks_protocol"])
    write_json(STAGE_DIR / "render_blocks_1013R_R17.json", bundle["render_blocks"])
    write_json(STAGE_DIR / "render_blocks_evidence_1013R_R17.json", evidence)
    report = f"""# 1013R_R17 render_blocks protocol

```text
stage_id={STAGE_ID}
protocol_id=SHIWEI_RENDER_BLOCKS_PROTOCOL_R0
current_object=三年级第二单元第1课《色彩的渐变》
R36_modified=false
main_shell_modified=false
route_registered=false
provider_called=false
model_called=false
database_written=false
memory_written=false
vector_index_written=false
feishu_written=false
formal_apply_performed=false
```

## 验证

```text
validator_pass={str(result["validator_pass"]).lower()}
failed_checks={result["failed_checks"]}
```

## 下一步

```text
1013R_R18_LIGHT_RENDER_ADAPTER_SAMPLE
```
"""
    write_text(STAGE_DIR / "1013R_R17_report.md", report)


def main() -> None:
    result, evidence, errors = validate()
    write_outputs(result, evidence)
    if errors:
        raise SystemExit("FAIL: " + ", ".join(errors))
    print("PASS: 1013R_R17 render_blocks protocol")


if __name__ == "__main__":
    main()
