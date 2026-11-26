"""Print index.md with the sleeve table filled in, and refresh the tear sheets.

Metrics and sheets come from the live repo; anything missing fails the build.
Usage: python3 build/prepare_index.py > expanded.md
"""

import shutil
import sys
import tomllib
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CONFIG_PATH = ROOT / "build" / "sleeves.toml"
INDEX_PATH = ROOT / "index.md"

HEADER = (
    "| Signal | Description | Window | Sharpe (held) | In market "
    "| Max DD | Cost b/e |\n"
    "|:--|:--|--:|--:|--:|--:|--:|"
)


def render_row(sleeve: dict, metrics: dict, config: dict) -> str:
    """Render one markdown table row.

    Args:
        sleeve: Hand-written [[sleeve]] entry from the config.
        metrics: This sleeve's table from the metrics file.
        config: Full config, for the format table.

    Returns:
        The markdown row. A missing metric raises KeyError.
    """
    fmt = config["format"]
    window = f"{metrics['window_start_year']}–{metrics['window_end_year'] % 100:02d}"
    drawdown = f"{abs(metrics['max_drawdown_pct']):.{fmt['drawdown_decimals']}f}"
    cells = [
        f"[{sleeve['name']}](#{sleeve['anchor']})",
        sleeve["description"],
        window,
        f"{metrics['held_sharpe']:.{fmt['sharpe_decimals']}f}",
        f"{metrics['pct_time_in_market']:.{fmt['pct_time_decimals']}f}%",
        f"−{drawdown}%",
        f"{metrics['cost_breakeven_multiple']:.{fmt['breakeven_decimals']}f}×",
    ]
    return "| " + " | ".join(cells) + " |"


def main() -> None:
    """Refresh the sheets, then write the expanded markdown to stdout."""
    config = tomllib.loads(CONFIG_PATH.read_text(encoding="utf-8"))
    metrics_path = Path(config["metrics_path"]).expanduser()
    all_metrics = tomllib.loads(metrics_path.read_text(encoding="utf-8"))

    index = INDEX_PATH.read_text(encoding="utf-8")
    marker = config["marker"]
    if index.count(marker) != 1:
        sys.exit(f"index.md must contain {marker!r} exactly once")

    plots_dir = Path(config["plots_dir"]).expanduser()
    rows = []
    for sleeve in config["sleeve"]:
        rows.append(render_row(sleeve, all_metrics[sleeve["key"]], config))
        source = plots_dir / f"{sleeve['key']}.png"
        shutil.copy2(source, ROOT / config["sheets_dir"] / sleeve["sheet"])

    sys.stdout.write(index.replace(marker, HEADER + "\n" + "\n".join(rows)))


if __name__ == "__main__":
    main()
