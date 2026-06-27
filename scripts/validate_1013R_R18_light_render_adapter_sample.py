from __future__ import annotations

import json
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

STAGE_ID = "1013R_R18_LIGHT_RENDER_ADAPTER_SAMPLE"
STAGE_DIR = ROOT / "outputs" / "PREP_ROOM_RENDER_CANVAS_DEEPEN_V1" / "1013R_R18_light_render_adapter_sample"
DOC_PATH = ROOT / "docs" / "1013R_R18_light_render_adapter_sample.md"


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
    from backend.xiaobei_ai import prep_room_light_render_adapter_1013R_R18 as module

    errors: list[str] = []
    bundle = module.build_adapter_sample_bundle()
    sample = bundle.get("light_render_adapter_sample", {})
    html = bundle.get("html", "")
    boundary = bundle.get("boundary", {})
    doc = DOC_PATH.read_text(encoding="utf-8", errors="ignore") if DOC_PATH.exists() else ""

    if bundle.get("stage") != STAGE_ID:
        fail(errors, "stage_id_mismatch")
    if sample.get("stage") != STAGE_ID:
        fail(errors, "sample_stage_mismatch")
    if sample.get("adapter_id") != "SHIWEI_LIGHT_RENDER_ADAPTER_SAMPLE_R0":
        fail(errors, "adapter_id_mismatch")
    if sample.get("consumes", {}).get("render_blocks_protocol_stage") != "1013R_R17_RENDER_BLOCKS_PROTOCOL_R0":
        fail(errors, "r17_render_blocks_protocol_not_consumed")
    if sample.get("consumes", {}).get("block_count", 0) < 14:
        fail(errors, "render_block_count_too_small")
    for token in ["备课室轻量渲染适配样板", "2-1《色彩的渐变》", "data-slot=\"courseware_script\"", "data-slot=\"classroom_display_screen\""]:
        if token not in html:
            fail(errors, f"html_token_missing:{token}")
    if html.count('class="r18-block"') < 14:
        fail(errors, "html_block_count_too_small")

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
        "existing_page_modified",
    ]
    for flag in blocked_true_flags:
        if boundary.get(flag):
            fail(errors, f"readonly_boundary_broken:{flag}")
    if not boundary.get("light_render_adapter_readonly"):
        fail(errors, "light_render_adapter_readonly_not_marked")
    if not boundary.get("light_render_adapter_defined"):
        fail(errors, "light_render_adapter_defined_not_marked")

    if not DOC_PATH.exists():
        fail(errors, "r18_doc_missing")
    for token in ["SHIWEI_LIGHT_RENDER_ADAPTER_SAMPLE_R0", "existing_page_modified=false", "formal_apply_performed=false"]:
        if token not in doc:
            fail(errors, f"r18_doc_token_missing:{token}")

    evidence = {
        "module": "backend.xiaobei_ai.prep_room_light_render_adapter_1013R_R18",
        "adapter_id": sample.get("adapter_id"),
        "consumes": sample.get("consumes"),
        "html_length": len(html),
        "html_block_count": html.count('class="r18-block"'),
        "boundary": boundary,
    }
    result = {
        "stage_id": STAGE_ID,
        "status": "PASS" if not errors else "FAIL",
        "validator_pass": not errors,
        "created_at": now(),
        "checks": {
            "r17_render_blocks_consumed": sample.get("consumes", {}).get("render_blocks_protocol_stage")
            == "1013R_R17_RENDER_BLOCKS_PROTOCOL_R0",
            "html_sample_created": bool(html),
            "major_slots_rendered": all(
                token in html for token in ['data-slot="courseware_script"', 'data-slot="classroom_display_screen"']
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
    from backend.xiaobei_ai import prep_room_light_render_adapter_1013R_R18 as module

    bundle = module.build_adapter_sample_bundle()
    write_json(STAGE_DIR / "1013R_R18_result.json", result)
    write_json(STAGE_DIR / "light_render_adapter_sample_1013R_R18.json", bundle["light_render_adapter_sample"])
    write_json(STAGE_DIR / "light_render_adapter_evidence_1013R_R18.json", evidence)
    write_text(STAGE_DIR / "prep_room_light_render_adapter_sample_1013R_R18.html", bundle["html"])
    report = f"""# 1013R_R18 light render adapter sample

```text
stage_id={STAGE_ID}
adapter_id=SHIWEI_LIGHT_RENDER_ADAPTER_SAMPLE_R0
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
formal_apply_performed=false
```

## 验证

```text
validator_pass={str(result["validator_pass"]).lower()}
failed_checks={result["failed_checks"]}
```

## 下一步

```text
1013R_R19_DERIVATIVE_OBJECT_STATIC_LINKAGE_SAMPLE
```
"""
    write_text(STAGE_DIR / "1013R_R18_report.md", report)


def main() -> None:
    result, evidence, errors = validate()
    write_outputs(result, evidence)
    if errors:
        raise SystemExit("FAIL: " + ", ".join(errors))
    print("PASS: 1013R_R18 light render adapter sample")


if __name__ == "__main__":
    main()
