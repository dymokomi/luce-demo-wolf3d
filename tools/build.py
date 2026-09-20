#!/usr/bin/env python3
import argparse
import os
from pathlib import Path
import shutil
import subprocess

ROOT = Path(__file__).resolve().parents[1]
SUFFIX = ".exe" if os.name == "nt" else ""
parser = argparse.ArgumentParser(description="Build luce-demo-wolf3d natively from Base sources.")
parser.add_argument("--base", type=Path, default=ROOT.parent / f"luce-base/build/luce-base{SUFFIX}")
parser.add_argument("--opt", type=int, choices=range(4), default=1)
parser.add_argument("-o", "--output", type=Path, default=ROOT / f"build/wolf3d{SUFFIX}")
args = parser.parse_args()
output = args.output.resolve()
output.parent.mkdir(parents=True, exist_ok=True)
subprocess.run([str(args.base.resolve()), "build", str(ROOT / "src/main.lucb"),
                "--native", "--opt", str(args.opt), "-o", str(output)],
               cwd=ROOT, check=True)
# Original Wolf3D loads VSWAP.WL1 / GAMEMAPS.WL1 / MAPHEAD.WL1 from the exe directory.
for name in ["MAPHEAD.WL1", "GAMEMAPS.WL1", "VSWAP.WL1",
             "VGAHEAD.WL1", "VGAGRAPH.WL1", "VGADICT.WL1",
             "AUDIOHED.WL1", "AUDIOT.WL1"]:
    source = ROOT / "data" / name
    if source.exists():
        shutil.copy2(source, output.parent / name)
