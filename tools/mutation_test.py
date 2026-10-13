"""Pengujian mutasi sederhana. Tiap mutan dijalankan di salinan terpisah,
jadi pricing.py asli tidak pernah berubah."""
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

MUTANTS = {
    "M1: hapus diskon": (
        "return subtotal * (1 - MEMBER_DISCOUNT_RATE)",
        "return subtotal",
    ),
    "M2: pajak 0.11 -> 0.10": (
        "TAX_RATE = 0.11",
        "TAX_RATE = 0.10",
    ),
    "M3: hapus validasi kuantitas": (
        '    if quantity <= 0:\n        raise ValueError("quantity must be positive")\n',
        "",
    ),
}


def run_mutant(old, new):
    source = (ROOT / "pricing.py").read_text(encoding="utf-8")
    assert old in source
    mutated = source.replace(old, new, 1)

    with tempfile.TemporaryDirectory() as tmp:
        work = Path(tmp)
        shutil.copytree(ROOT / "tests", work / "tests")
        shutil.copy(ROOT / "pytest.ini", work / "pytest.ini")
        (work / "pricing.py").write_text(mutated, encoding="utf-8")
        result = subprocess.run(
            [sys.executable, "-m", "pytest", "-q", "--tb=no", "-rf",
             "-p", "no:cacheprovider"],
            cwd=work, capture_output=True, text=True,
        )

    return [
        line.split(" ")[1].split("::")[-1]
        for line in result.stdout.splitlines()
        if line.startswith("FAILED")
    ]


if __name__ == "__main__":
    for name, (old, new) in MUTANTS.items():
        failed = run_mutant(old, new)
        print(name)
        for test_name in failed or ["(tidak ada, mutan lolos)"]:
            print(f"    gagal: {test_name}")
        print()
