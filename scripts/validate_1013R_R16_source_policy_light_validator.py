from __future__ import annotations

import json
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

STAGE_ID = "1013R_R16_SOURCE_POLICY_LIGHT_VALIDATOR_R0"
STAGE_DIR = ROOT / "outputs" / "PREP_ROOM_RENDER_CANVAS_DEEPEN_V1" / "1013R_R16_source_policy_light_validator_r0"
DOC_PATH = ROOT / "docs" / "1013R_R16_source_policy_light_validator.md"


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
    from backend.xiaobei_ai import prep_room_source_policy_validator_1013R_R16 as module

    errors: list[str] = []
    bundle = module.build_validator_sample_bundle()
    result_payload = bundle.get("source_policy_result", {})
    boundary = bundle.get("boundary", {})
    doc = DOC_PATH.read_text(encoding="utf-8", errors="ignore") if DOC_PATH.exists() else ""

    if bundle.get("stage") != STAGE_ID:
        fail(errors, "stage_id_mismatch")
    if result_payload.get("stage") != STAGE_ID:
        fail(errors, "result_stage_mismatch")
    if result_payload.get("validator_id") != "SHIWEI_SOURCE_POLICY_LIGHT_VALIDATOR_R0":
        fail(errors, "validator_id_mismatch")
    if result_payload.get("consumes", {}).get("unified_viewmodel_stage") != "1013R_R15_PREP_ROOM_UNIFIED_VIEWMODEL_R0":
        fail(errors, "r15_unified_viewmodel_not_consumed")
    if result_payload.get("consumes", {}).get("current_object", {}).get("title") != "2-1《色彩的渐变》":
        fail(errors, "current_object_not_preserved")
    if not result_payload.get("ok"):
        fail(errors, "source_policy_result_not_ok")
    for item in result_payload.get("checks", []):
        if item.get("status") != "pass":
            fail(errors, f"source_policy_check_failed:{item.get('check_id')}")

    required_checks = {
        "current_object_has_textbook_anchor",
        "ai_draft_not_standard",
        "source_categories_present",
        "assessment_blocked_until_materials",
        "memory_write_blocked",
    }
    check_ids = {item.get("check_id") for item in result_payload.get("checks", [])}
    for check_id in required_checks:
        if check_id not in check_ids:
            fail(errors, f"source_policy_check_missing:{check_id}")

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
    if not boundary.get("source_policy_light_validator_readonly"):
        fail(errors, "source_policy_light_validator_readonly_not_marked")
    if not boundary.get("source_policy_validator_defined"):
        fail(errors, "source_policy_validator_defined_not_marked")

    if not DOC_PATH.exists():
        fail(errors, "r16_doc_missing")
    for token in ["SHIWEI_SOURCE_POLICY_LIGHT_VALIDATOR_R0", "AI 草案", "formal_apply_performed=false"]:
        if token not in doc:
            fail(errors, f"r16_doc_token_missing:{token}")

    evidence = {
        "module": "backend.xiaobei_ai.prep_room_source_policy_validator_1013R_R16",
        "validator_id": result_payload.get("validator_id"),
        "consumes": result_payload.get("consumes"),
        "checks": result_payload.get("checks"),
        "failed_checks": result_payload.get("failed_checks"),
        "boundary": boundary,
    }
    result = {
        "stage_id": STAGE_ID,
        "status": "PASS" if not errors else "FAIL",
        "validator_pass": not errors,
        "created_at": now(),
        "checks": {
            "r15_unified_viewmodel_consumed": result_payload.get("consumes", {}).get("unified_viewmodel_stage")
            == "1013R_R15_PREP_ROOM_UNIFIED_VIEWMODEL_R0",
            "source_policy_ok": result_payload.get("ok") is True,
            "assessment_blocked": "assessment_blocked_until_materials" in check_ids,
            "memory_write_blocked": "memory_write_blocked" in check_ids,
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
    from backend.xiaobei_ai import prep_room_source_policy_validator_1013R_R16 as module

    bundle = module.build_validator_sample_bundle()
    write_json(STAGE_DIR / "1013R_R16_result.json", result)
    write_json(STAGE_DIR / "source_policy_result_1013R_R16.json", bundle["source_policy_result"])
    write_json(STAGE_DIR / "source_policy_evidence_1013R_R16.json", evidence)
    report = f"""# 1013R_R16 source policy light validator

```text
stage_id={STAGE_ID}
validator_id=SHIWEI_SOURCE_POLICY_LIGHT_VALIDATOR_R0
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
1013R_R17_RENDER_BLOCKS_PROTOCOL_R0
```
"""
    write_text(STAGE_DIR / "1013R_R16_report.md", report)


def main() -> None:
    result, evidence, errors = validate()
    write_outputs(result, evidence)
    if errors:
        raise SystemExit("FAIL: " + ", ".join(errors))
    print("PASS: 1013R_R16 source policy light validator")


if __name__ == "__main__":
    main()
