"""Load volleyball passing-stats JSON exports and build a self-contained HTML report.

Usage:  python analyze.py [json_dir] [output.html]
Defaults: JSON files in this folder, output report.html alongside.

Each JSON is one session export: metadata.date/time plus players[] (name, attempts, average).
Players with 0 attempts in a session have no rating (shown as a gap).
Players are ordered by season average (attempt-weighted across sessions).
Team rating = attempt-weighted average across all players in the session.
"""
import json
import sys
from collections import OrderedDict
from pathlib import Path


def load(json_dir: Path):
    """Return (sessions, players): sessions = sorted list of labels,
    players = {name: {label: (attempts, avg)}}."""
    players = OrderedDict()
    sessions = set()
    for path in sorted(json_dir.glob("*.json")):
        with path.open(encoding="utf-8-sig") as f:
            data = json.load(f)
        meta = data["metadata"]
        label = f"{meta['date']} {meta['time']}".strip()
        sessions.add(label)
        for p in data["players"]:
            players.setdefault(p["name"].strip(), {})[label] = (
                int(p["attempts"]),
                float(p["average"]),
            )
    return sorted(sessions), players


def build_data(sessions, players):
    series = {}
    for name, by_session in players.items():
        series[name] = {
            "ratings": [
                by_session[s][1] if s in by_session and by_session[s][0] > 0 else None
                for s in sessions
            ],
            "attempts": [by_session[s][0] if s in by_session else 0 for s in sessions],
        }
        total = sum(a for a, _ in by_session.values())
        series[name]["season_avg"] = (
            round(sum(a * r for a, r in by_session.values()) / total, 2) if total else None
        )
    # Highest season average first (players with no attempts last)
    series = dict(sorted(series.items(),
                         key=lambda kv: (kv[1]["season_avg"] is None, -(kv[1]["season_avg"] or 0))))
    team, team_attempts = [], []
    for s in sessions:
        total = sum(p[s][0] for p in players.values() if s in p)
        pts = sum(p[s][0] * p[s][1] for p in players.values() if s in p)
        team.append(round(pts / total, 2) if total else None)
        team_attempts.append(total)
    return {"sessions": sessions, "players": series,
            "team": {"ratings": team, "attempts": team_attempts}}


TEMPLATE = Path(__file__).with_name("report_template.html")


def main():
    here = Path(__file__).parent
    json_dir = Path(sys.argv[1]) if len(sys.argv) > 1 else here
    out = Path(sys.argv[2]) if len(sys.argv) > 2 else here / "report.html"
    sessions, players = load(json_dir)
    if not sessions:
        sys.exit(f"No JSON data found in {json_dir}")
    data = build_data(sessions, players)
    html = TEMPLATE.read_text(encoding="utf-8").replace("__DATA__", json.dumps(data))
    out.write_text(html, encoding="utf-8")
    print(f"{len(players)} players, {len(sessions)} sessions -> {out}")


if __name__ == "__main__":
    main()
