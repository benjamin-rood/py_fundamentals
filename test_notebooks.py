#!/usr/bin/env python3
"""
Execute all Jupyter notebooks in python_learning_notebooks/ to verify they
run without errors.

Usage:
    python test_notebooks.py                 # run all notebooks
    python test_notebooks.py 01_2            # run only notebooks matching "01_2"
    pytest test_notebooks.py -v              # run via pytest

No Jupyter installation required — notebooks are parsed as JSON and code
cells are executed sequentially using exec().

Cells whose metadata contains "raises-exception" in their tags list are
expected to raise an error (and it is a failure if they do NOT).

Cells containing input() calls are handled via a mock that returns canned
responses — see INPUT_RESPONSES.
"""

import json
import sys
from pathlib import Path
from unittest.mock import patch

NOTEBOOK_DIR = Path(__file__).parent / "python_learning_notebooks"

# Canned responses for input().
# 02_2_loops.ipynb uses input() for: a patient name, an age string, and a
# number-guessing game whose secret is random.randint(1, 20).  Supplying
# 1..20 guarantees a hit regardless of the secret.
INPUT_RESPONSES = ["Test Patient", "25"] + [str(i) for i in range(1, 21)]


# ---------------------------------------------------------------------------
# Core helpers
# ---------------------------------------------------------------------------

def extract_code_cells(notebook_path: Path) -> list[dict]:
    """Return non-empty code cells as dicts with source, expect_error, id."""
    with open(notebook_path) as f:
        nb = json.load(f)

    cells = []
    for cell in nb["cells"]:
        if cell["cell_type"] != "code":
            continue
        source = cell["source"]
        if isinstance(source, list):
            source = "".join(source)
        if not source.strip():
            continue
        tags = cell.get("metadata", {}).get("tags", [])
        cells.append(
            {
                "source": source,
                "expect_error": "raises-exception" in tags,
                "id": cell.get("id", "?"),
            }
        )
    return cells


def execute_notebook(notebook_path: Path) -> list[str]:
    """Execute every code cell in order.  Return a list of error strings
    (empty means the notebook passed)."""
    cells = extract_code_cells(notebook_path)
    namespace: dict = {"__name__": "__main__"}
    errors: list[str] = []
    input_iter = iter(INPUT_RESPONSES)

    with patch("builtins.input", side_effect=input_iter):
        for cell in cells:
            source = cell["source"]
            cell_id = cell["id"]
            label = f"{notebook_path.name}:{cell_id}"

            # --- compile ------------------------------------------------
            try:
                code = compile(source, label, "exec")
            except SyntaxError as exc:
                if cell["expect_error"]:
                    continue
                errors.append(
                    f"{cell_id} \u2014 SyntaxError: {exc}\n"
                    f"  Source:\n{_indent(source)}"
                )
                continue

            # --- execute ------------------------------------------------
            try:
                exec(code, namespace)  # noqa: S102
            except StopIteration:
                errors.append(f"{cell_id} \u2014 ran out of mock input() responses")
                break
            except Exception as exc:
                if cell["expect_error"]:
                    continue
                errors.append(
                    f"{cell_id} \u2014 {type(exc).__name__}: {exc}\n"
                    f"  Source:\n{_indent(source)}"
                )
            else:
                if cell["expect_error"]:
                    errors.append(
                        f"{cell_id} \u2014 expected an error but cell succeeded\n"
                        f"  Source:\n{_indent(source)}"
                    )

    return errors


def _indent(text: str, prefix: str = "    ") -> str:
    return "\n".join(prefix + line for line in text.splitlines())


# ---------------------------------------------------------------------------
# pytest interface
# ---------------------------------------------------------------------------

def _notebook_paths() -> list[Path]:
    return sorted(NOTEBOOK_DIR.glob("*.ipynb"))


try:
    import pytest

    @pytest.mark.parametrize(
        "notebook_path",
        _notebook_paths(),
        ids=[p.name for p in _notebook_paths()],
    )
    def test_notebook_executes(notebook_path: Path) -> None:
        errors = execute_notebook(notebook_path)
        if errors:
            pytest.fail("\n\n".join(errors))

except ImportError:
    pass


# ---------------------------------------------------------------------------
# Standalone CLI
# ---------------------------------------------------------------------------

def main() -> None:
    pattern = sys.argv[1] if len(sys.argv) > 1 else None
    notebooks = _notebook_paths()

    if pattern:
        notebooks = [p for p in notebooks if pattern in p.name]

    if not notebooks:
        msg = f"matching '{pattern}'" if pattern else f"in {NOTEBOOK_DIR}"
        print(f"No notebooks found {msg}")
        sys.exit(1)

    print(f"Testing {len(notebooks)} notebook(s)\n")

    failed: dict[str, list[str]] = {}
    for nb_path in notebooks:
        print(f"  {nb_path.name} ... ", end="", flush=True)
        errs = execute_notebook(nb_path)
        if errs:
            print("FAILED")
            failed[nb_path.name] = errs
        else:
            print("ok")

    print()
    if failed:
        for name, errs in failed.items():
            print(f"{'─' * 60}")
            print(f"FAIL: {name}\n")
            for e in errs:
                print(f"  {e}\n")
        print(f"{'─' * 60}")
        print(f"\n{len(failed)} of {len(notebooks)} notebook(s) failed")
        sys.exit(1)
    else:
        print(f"All {len(notebooks)} notebook(s) passed.")


if __name__ == "__main__":
    main()
