import argparse
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent))

from hardware_review_cli import dump_json, run_schema_validate


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--run-dir", required=True)
    args = parser.parse_args()
    run_dir = Path(args.run_dir).resolve()
    dump_json(run_dir / "gates" / "schema_validate_result.json", run_schema_validate(run_dir))
