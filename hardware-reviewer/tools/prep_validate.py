import argparse
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent))

from hardware_review_cli import dump_json, run_prep_validate


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--run-dir", required=True)
    args = parser.parse_args()
    run_dir = Path(args.run_dir).resolve()
    dump_json(run_dir / "gates" / "prep_validate_result.json", run_prep_validate(run_dir))
