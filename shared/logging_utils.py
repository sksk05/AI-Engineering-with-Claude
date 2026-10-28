import json
from datetime import datetime, timezone
from pathlib import Path


def jsonl_logger(path: str | Path):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)

    def log(event: dict):
        entry = {
            "timestamp": datetime.now(timezone.utc).isoformat(),
            **event,
        }
        with path.open("a", encoding="utf-8") as f:
            f.write(json.dumps(entry) + "\n")

    return log
