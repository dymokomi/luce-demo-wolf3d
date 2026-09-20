#!/usr/bin/env python3
"""CPU contracts for the Wolf3D port. File I/O lives in a small main, not `test` blocks."""
import os
from pathlib import Path
import subprocess

ROOT = Path(__file__).resolve().parents[1]
parser_base = ROOT.parent / ("luce-base/build/luce-base.exe" if os.name == "nt" else "luce-base/build/luce-base")
import argparse
parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("--base", type=Path, default=parser_base)
args = parser.parse_args()
env = dict(os.environ)
subprocess.run([str(args.base.resolve()), "test", str(ROOT / "src/id_ca.lucb"), "--native"],
               check=True, cwd=ROOT, env=env, timeout=120)
print("PASS luce-demo-wolf3d Carmack/RLEW")
