#!/usr/bin/env python3
"""Write one startup pitch that sounds absurd until you see it would sell."""

import os
from pathlib import Path

TEXT = "We sell naming rights to houseplants: for four dollars your fern gets a sponsor's name on a tiny brass plaque, and offices pay gladly, because it is the only advertisement their staff stop to water."


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(TEXT + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
