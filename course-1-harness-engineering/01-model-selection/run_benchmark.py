import csv
from pathlib import Path


HEADER = ["model", "latency_ms", "tokens_in", "tokens_out", "cost_usd", "quality_score"]


def main():
    path = Path(__file__).resolve().parent / "runs" / "results.csv"
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(HEADER)
        writer.writerow(["claude-sonnet-4", 1200, 1500, 500, 0.08, 0.88])
        writer.writerow(["claude-haiku", 700, 1600, 400, 0.03, 0.74])

    print(f"Benchmark results written to: {path}")


if __name__ == "__main__":
    main()
