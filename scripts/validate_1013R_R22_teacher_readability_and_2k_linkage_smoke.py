from __future__ import annotations

import json
import shutil
import struct
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

STAGE_ID = "1013R_R22_TEACHER_READABILITY_AND_2K_LINKAGE_SMOKE"
STAGE_DIR = ROOT / "outputs" / "PREP_ROOM_RENDER_CANVAS_DEEPEN_V1" / "1013R_R22_teacher_readability_and_2k_linkage_smoke"
DOC_PATH = ROOT / "docs" / "1013R_R22_teacher_readability_and_2k_linkage_smoke.md"
HTML_PATH = STAGE_DIR / "prep_room_page_copy_for_r22_teacher_readability.html"
SCREENSHOT_PATH = STAGE_DIR / "1013R_R22_2k_teacher_readability_check.png"


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


def chrome_path() -> str | None:
    candidates = [
        shutil.which("chrome"),
        shutil.which("chrome.exe"),
        shutil.which("msedge"),
        shutil.which("msedge.exe"),
        r"C:\Program Files\Google\Chrome\Application\chrome.exe",
        r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
        r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
        r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
    ]
    for candidate in candidates:
        if candidate and Path(candidate).exists():
            return candidate
    return None


def capture_screenshot(html_path: Path, screenshot_path: Path) -> tuple[bool, str]:
    browser = chrome_path()
    if browser is None:
        return False, "chrome_or_edge_not_found"
    screenshot_path.parent.mkdir(parents=True, exist_ok=True)
    cmd = [
        browser,
        "--headless=new",
        "--disable-gpu",
        "--hide-scrollbars",
        "--window-size=2560,1440",
        f"--screenshot={screenshot_path}",
        html_path.resolve().as_uri(),
    ]
    completed = subprocess.run(cmd, cwd=str(ROOT), text=True, capture_output=True, timeout=60)
    if completed.returncode != 0:
        return False, (completed.stderr or completed.stdout or "chrome_screenshot_failed").strip()
    return screenshot_path.exists(), "ok" if screenshot_path.exists() else "screenshot_missing"


def png_size(path: Path) -> tuple[int | None, int | None]:
    if not path.exists():
        return None, None
    with path.open("rb") as fh:
        header = fh.read(24)
    if len(header) < 24 or header[:8] != b"\x89PNG\r\n\x1a\n":
        return None, None
    width, height = struct.unpack(">II", header[16:24])
    return width, height


def validate() -> tuple[dict[str, Any], dict[str, Any], list[str]]:
    from backend.xiaobei_ai import prep_room_teacher_readability_smoke_1013R_R22 as module

    errors: list[str] = []
    bundle = module.build_smoke_sample_bundle()
    smoke = bundle.get("teacher_readability_smoke", {})
    html = bundle.get("html", "")
    boundary = bundle.get("boundary", {})
    doc = DOC_PATH.read_text(encoding="utf-8", errors="ignore") if DOC_PATH.exists() else ""

    if bundle.get("stage") != STAGE_ID:
        fail(errors, "stage_id_mismatch")
    if smoke.get("smoke_id") != "SHIWEI_PREP_ROOM_TEACHER_READABILITY_2K_SMOKE_R0":
        fail(errors, "smoke_id_mismatch")
    if smoke.get("consumes", {}).get("r21_stage") != "1013R_R21_PAGE_COPY_BINDS_UNIFIED_PACKAGE":
        fail(errors, "r21_page_copy_not_consumed")
    if smoke.get("ok") is not True:
        fail(errors, "teacher_readability_static_checks_failed")

    HTML_PATH.parent.mkdir(parents=True, exist_ok=True)
    write_text(HTML_PATH, html)
    screenshot_ok, screenshot_message = capture_screenshot(HTML_PATH, SCREENSHOT_PATH)
    if not screenshot_ok:
        fail(errors, f"screenshot_failed:{screenshot_message[:120]}")
    width, height = png_size(SCREENSHOT_PATH)
    if (width, height) != (2560, 1440):
        fail(errors, f"screenshot_size_mismatch:{width}x{height}")

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
        "R36_modified",
        "main_shell_modified",
        "existing_page_modified",
    ]
    for flag in blocked_true_flags:
        if boundary.get(flag):
            fail(errors, f"readonly_boundary_broken:{flag}")
    if not boundary.get("teacher_readability_smoke_defined"):
        fail(errors, "teacher_readability_smoke_not_marked")

    for token in ["2K 截图", "R36_modified=false", "route_registered=false", "formal_apply_performed=false"]:
        if token not in doc:
            fail(errors, f"r22_doc_token_missing:{token}")

    evidence = {
        "module": "backend.xiaobei_ai.prep_room_teacher_readability_smoke_1013R_R22",
        "smoke_id": smoke.get("smoke_id"),
        "consumes": smoke.get("consumes"),
        "static_checks": smoke.get("checks"),
        "html_path": str(HTML_PATH),
        "screenshot_path": str(SCREENSHOT_PATH),
        "screenshot_size": {"width": width, "height": height},
        "screenshot_message": screenshot_message,
        "boundary": boundary,
    }
    result = {
        "stage_id": STAGE_ID,
        "status": "PASS" if not errors else "FAIL",
        "validator_pass": not errors,
        "created_at": now(),
        "checks": {
            "teacher_readability_static_checks_pass": smoke.get("ok") is True,
            "screenshot_created": screenshot_ok,
            "screenshot_2k_size": (width, height) == (2560, 1440),
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
    from backend.xiaobei_ai import prep_room_teacher_readability_smoke_1013R_R22 as module

    bundle = module.build_smoke_sample_bundle()
    write_json(STAGE_DIR / "1013R_R22_result.json", result)
    write_json(STAGE_DIR / "teacher_readability_smoke_1013R_R22.json", bundle["teacher_readability_smoke"])
    write_json(STAGE_DIR / "teacher_readability_evidence_1013R_R22.json", evidence)
    report = f"""# 1013R_R22 teacher readability and 2K linkage smoke

```text
stage_id={STAGE_ID}
smoke_id=SHIWEI_PREP_ROOM_TEACHER_READABILITY_2K_SMOKE_R0
current_object=三年级第二单元第1课《色彩的渐变》
html_path={HTML_PATH}
screenshot_path={SCREENSHOT_PATH}
screenshot_size={evidence.get("screenshot_size", {}).get("width")}x{evidence.get("screenshot_size", {}).get("height")}
R36_modified=false
main_shell_modified=false
existing_page_modified=false
route_registered=false
endpoint_registered=false
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
1013R_R23_PREP_ROOM_TEACHER_WALKTHROUGH_SCRIPT
```
"""
    write_text(STAGE_DIR / "1013R_R22_report.md", report)


def main() -> None:
    result, evidence, errors = validate()
    write_outputs(result, evidence)
    if errors:
        raise SystemExit("FAIL: " + ", ".join(errors))
    print("PASS: 1013R_R22 teacher readability and 2K linkage smoke")


if __name__ == "__main__":
    main()
