from __future__ import annotations

import json
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

STAGE_ID = "1013R_R20_PREP_ROOM_UNIFIED_PACKAGE_READONLY_EXPORT_R0"
STAGE_DIR = ROOT / "outputs" / "PREP_ROOM_RENDER_CANVAS_DEEPEN_V1" / "1013R_R20_prep_room_unified_package_readonly_export_r0"
DOC_PATH = ROOT / "docs" / "1013R_R20_prep_room_unified_package_readonly_export.md"


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
    from backend.xiaobei_ai import prep_room_unified_package_readonly_export_1013R_R20 as module

    errors: list[str] = []
    bundle = module.build_package_sample_bundle()
    package = bundle.get("unified_package", {})
    boundary = bundle.get("boundary", {})
    doc = DOC_PATH.read_text(encoding="utf-8", errors="ignore") if DOC_PATH.exists() else ""

    if bundle.get("stage") != STAGE_ID:
        fail(errors, "stage_id_mismatch")
    if package.get("stage") != STAGE_ID:
        fail(errors, "package_stage_mismatch")
    if package.get("package_id") != "SHIWEI_PREP_ROOM_UNIFIED_PACKAGE_READONLY_EXPORT_R0":
        fail(errors, "package_id_mismatch")
    if package.get("current_object", {}).get("title") != "2-1《色彩的渐变》":
        fail(errors, "current_object_not_preserved")
    if "穿穿编编" in json.dumps(package, ensure_ascii=False):
        fail(errors, "deprecated_object_chuanchuanbianbian_present")
    if package.get("current_object", {}).get("title") == "色彩的感觉":
        fail(errors, "deprecated_object_color_feeling_as_current")

    consumed = package.get("contracts_consumed", {})
    expected = {
        "r15_stage": "1013R_R15_PREP_ROOM_UNIFIED_VIEWMODEL_R0",
        "r16_stage": "1013R_R16_SOURCE_POLICY_LIGHT_VALIDATOR_R0",
        "r17_stage": "1013R_R17_RENDER_BLOCKS_PROTOCOL_R0",
        "r19_stage": "1013R_R19_DERIVATIVE_OBJECT_STATIC_LINKAGE_SAMPLE",
    }
    for key, value in expected.items():
        if consumed.get(key) != value:
            fail(errors, f"contract_not_consumed:{key}")

    for field in [
        "current_object",
        "task_state",
        "teacher_action_gate",
        "source_policy_result",
        "render_blocks",
        "render_block_linkage_index",
        "derivative_linkage",
    ]:
        if field not in package:
            fail(errors, f"package_field_missing:{field}")
    if len(package.get("render_blocks", [])) < 14:
        fail(errors, "render_blocks_too_few")
    for slot in ["courseware_script", "classroom_display_screen", "worksheet", "assessment_rubric"]:
        if slot not in package.get("render_block_linkage_index", {}):
            fail(errors, f"render_block_linkage_missing:{slot}")
    if package.get("source_policy_result", {}).get("ok") is not True:
        fail(errors, "source_policy_not_ok")
    if package.get("derivative_linkage", {}).get("static_linkage_summary", {}).get("assessment_blocked") is not True:
        fail(errors, "assessment_not_blocked")

    blocked_true_flags = [
        "route_registered",
        "endpoint_registered",
        "provider_called",
        "model_called",
        "database_written",
        "memory_written",
        "vector_index_written",
        "feishu_written",
        "formal_apply_performed",
        "courseware_export_created",
        "worksheet_export_created",
        "assessment_written",
        "R36_modified",
        "main_shell_modified",
        "runtime_write_allowed",
        "existing_page_modified",
    ]
    for flag in blocked_true_flags:
        if boundary.get(flag):
            fail(errors, f"readonly_boundary_broken:{flag}")
    if not boundary.get("unified_package_readonly_export"):
        fail(errors, "unified_package_readonly_export_not_marked")
    if not boundary.get("static_json_export_allowed"):
        fail(errors, "static_json_export_not_allowed")

    for token in ["不是正式 route", "route_registered=false", "endpoint_registered=false", "formal_apply_performed=false"]:
        if token not in doc:
            fail(errors, f"r20_doc_token_missing:{token}")

    evidence = {
        "module": "backend.xiaobei_ai.prep_room_unified_package_readonly_export_1013R_R20",
        "package_id": package.get("package_id"),
        "contracts_consumed": consumed,
        "current_object": package.get("current_object"),
        "render_block_count": len(package.get("render_blocks", [])),
        "derivative_linkage_summary": package.get("derivative_linkage", {}).get("static_linkage_summary"),
        "boundary": boundary,
    }
    result = {
        "stage_id": STAGE_ID,
        "status": "PASS" if not errors else "FAIL",
        "validator_pass": not errors,
        "created_at": now(),
        "checks": {
            "unified_package_created": package.get("package_id") == "SHIWEI_PREP_ROOM_UNIFIED_PACKAGE_READONLY_EXPORT_R0",
            "r15_r16_r17_r19_consumed": not any(code.startswith("contract_not_consumed") for code in errors),
            "render_blocks_and_derivatives_linked": not any(code.startswith("render_block_linkage_missing") for code in errors),
            "not_route_or_endpoint": boundary.get("route_registered") is False and boundary.get("endpoint_registered") is False,
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
    from backend.xiaobei_ai import prep_room_unified_package_readonly_export_1013R_R20 as module

    bundle = module.build_package_sample_bundle()
    write_json(STAGE_DIR / "1013R_R20_result.json", result)
    write_json(STAGE_DIR / "prep_room_unified_package_1013R_R20.json", bundle["unified_package"])
    write_json(STAGE_DIR / "render_blocks_1013R_R20.json", bundle["render_blocks"])
    write_json(STAGE_DIR / "derivative_linkage_1013R_R20.json", bundle["derivative_linkage"])
    write_json(STAGE_DIR / "unified_package_evidence_1013R_R20.json", evidence)
    report = f"""# 1013R_R20 prep room unified package readonly export

```text
stage_id={STAGE_ID}
package_id=SHIWEI_PREP_ROOM_UNIFIED_PACKAGE_READONLY_EXPORT_R0
current_object=三年级第二单元第1课《色彩的渐变》
route_registered=false
endpoint_registered=false
R36_modified=false
main_shell_modified=false
existing_page_modified=false
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
1013R_R21_PAGE_COPY_BINDS_UNIFIED_PACKAGE
```
"""
    write_text(STAGE_DIR / "1013R_R20_report.md", report)


def main() -> None:
    result, evidence, errors = validate()
    write_outputs(result, evidence)
    if errors:
        raise SystemExit("FAIL: " + ", ".join(errors))
    print("PASS: 1013R_R20 unified package readonly export")


if __name__ == "__main__":
    main()
