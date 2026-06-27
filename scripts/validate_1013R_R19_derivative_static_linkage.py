from __future__ import annotations

import json
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

STAGE_ID = "1013R_R19_DERIVATIVE_OBJECT_STATIC_LINKAGE_SAMPLE"
STAGE_DIR = ROOT / "outputs" / "PREP_ROOM_RENDER_CANVAS_DEEPEN_V1" / "1013R_R19_derivative_object_static_linkage_sample"
DOC_PATH = ROOT / "docs" / "1013R_R19_derivative_object_static_linkage.md"


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
    from backend.xiaobei_ai import prep_room_derivative_static_linkage_1013R_R19 as module

    errors: list[str] = []
    bundle = module.build_linkage_sample_bundle()
    linkage = bundle.get("derivative_linkage", {})
    links = bundle.get("process_derivative_links", [])
    boundary = bundle.get("boundary", {})
    doc = DOC_PATH.read_text(encoding="utf-8", errors="ignore") if DOC_PATH.exists() else ""

    if bundle.get("stage") != STAGE_ID:
        fail(errors, "stage_id_mismatch")
    if linkage.get("stage") != STAGE_ID:
        fail(errors, "linkage_stage_mismatch")
    if linkage.get("linkage_id") != "SHIWEI_PREP_ROOM_DERIVATIVE_OBJECT_LINKAGE_R0":
        fail(errors, "linkage_id_mismatch")
    if linkage.get("consumes", {}).get("unified_viewmodel_stage") != "1013R_R15_PREP_ROOM_UNIFIED_VIEWMODEL_R0":
        fail(errors, "r15_unified_viewmodel_not_consumed")
    if linkage.get("consumes", {}).get("light_render_adapter_stage") != "1013R_R18_LIGHT_RENDER_ADAPTER_SAMPLE":
        fail(errors, "r18_adapter_not_consumed")
    if linkage.get("consumes", {}).get("current_object", {}).get("title") != "2-1《色彩的渐变》":
        fail(errors, "current_object_not_preserved")

    derivative_ids = {item.get("object_id") for item in linkage.get("derivative_objects", [])}
    for object_id in ["courseware_script", "classroom_display_screen", "worksheet", "assessment_rubric"]:
        if object_id not in derivative_ids:
            fail(errors, f"derivative_object_missing:{object_id}")
    if len(links) < 5:
        fail(errors, "process_derivative_links_too_few")
    for link in links:
        for field in ["process_step_id", "courseware_screen", "classroom_display", "worksheet", "assessment_rubric"]:
            if field not in link:
                fail(errors, f"link_field_missing:{link.get('link_id')}:{field}")
        if link.get("assessment_rubric", {}).get("render_state") != "blocked_until_teacher_dimension":
            fail(errors, f"assessment_not_blocked_in_link:{link.get('link_id')}")

    summary = linkage.get("static_linkage_summary", {})
    if summary.get("exports_created"):
        fail(errors, "exports_created_should_be_false")
    if not summary.get("assessment_blocked"):
        fail(errors, "assessment_blocked_not_marked")
    if summary.get("linked_step_count") != len(links):
        fail(errors, "linked_step_count_mismatch")

    blocked_true_flags = [
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
        "route_registered",
        "existing_page_modified",
    ]
    for flag in blocked_true_flags:
        if boundary.get(flag):
            fail(errors, f"readonly_boundary_broken:{flag}")
    if not boundary.get("derivative_object_linkage_readonly"):
        fail(errors, "derivative_object_linkage_readonly_not_marked")
    if not boundary.get("derivative_static_linkage_defined"):
        fail(errors, "derivative_static_linkage_defined_not_marked")

    if not DOC_PATH.exists():
        fail(errors, "r19_doc_missing")
    for token in [
        "SHIWEI_PREP_ROOM_DERIVATIVE_OBJECT_LINKAGE_R0",
        "assessment_written=false",
        "R36_modified=false",
        "1013R_R20_PREP_ROOM_UNIFIED_PACKAGE_READONLY_EXPORT_R0",
    ]:
        if token not in doc:
            fail(errors, f"r19_doc_token_missing:{token}")

    evidence = {
        "module": "backend.xiaobei_ai.prep_room_derivative_static_linkage_1013R_R19",
        "linkage_id": linkage.get("linkage_id"),
        "consumes": linkage.get("consumes"),
        "derivative_objects": linkage.get("derivative_objects"),
        "link_count": len(links),
        "summary": summary,
        "boundary": boundary,
    }
    result = {
        "stage_id": STAGE_ID,
        "status": "PASS" if not errors else "FAIL",
        "validator_pass": not errors,
        "created_at": now(),
        "checks": {
            "derivative_linkage_defined": linkage.get("linkage_id")
            == "SHIWEI_PREP_ROOM_DERIVATIVE_OBJECT_LINKAGE_R0",
            "r15_and_r18_consumed": not any(code in errors for code in ["r15_unified_viewmodel_not_consumed", "r18_adapter_not_consumed"]),
            "major_derivatives_present": all(
                object_id in derivative_ids
                for object_id in ["courseware_script", "classroom_display_screen", "worksheet", "assessment_rubric"]
            ),
            "assessment_blocked": summary.get("assessment_blocked") is True,
            "no_exports_or_writes": not any(
                code in errors for code in ["exports_created_should_be_false"] if code
            ),
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
    from backend.xiaobei_ai import prep_room_derivative_static_linkage_1013R_R19 as module

    bundle = module.build_linkage_sample_bundle()
    write_json(STAGE_DIR / "1013R_R19_result.json", result)
    write_json(STAGE_DIR / "derivative_object_linkage_1013R_R19.json", bundle["derivative_linkage"])
    write_json(STAGE_DIR / "process_derivative_links_1013R_R19.json", bundle["process_derivative_links"])
    write_json(STAGE_DIR / "derivative_linkage_evidence_1013R_R19.json", evidence)
    report = f"""# 1013R_R19 derivative object static linkage sample

```text
stage_id={STAGE_ID}
linkage_id=SHIWEI_PREP_ROOM_DERIVATIVE_OBJECT_LINKAGE_R0
current_object=三年级第二单元第1课《色彩的渐变》
R36_modified=false
main_shell_modified=false
existing_page_modified=false
route_registered=false
provider_called=false
model_called=false
database_written=false
memory_written=false
vector_index_written=false
feishu_written=false
courseware_export_created=false
worksheet_export_created=false
assessment_written=false
formal_apply_performed=false
```

## 验证

```text
validator_pass={str(result["validator_pass"]).lower()}
failed_checks={result["failed_checks"]}
```

## 下一步

```text
1013R_R20_PREP_ROOM_UNIFIED_PACKAGE_READONLY_EXPORT_R0
```
"""
    write_text(STAGE_DIR / "1013R_R19_report.md", report)


def main() -> None:
    result, evidence, errors = validate()
    write_outputs(result, evidence)
    if errors:
        raise SystemExit("FAIL: " + ", ".join(errors))
    print("PASS: 1013R_R19 derivative object static linkage")


if __name__ == "__main__":
    main()
