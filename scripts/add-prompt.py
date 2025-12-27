import argparse
import datetime
from pathlib import Path


PROMPTS_MD = Path(__file__).resolve().parents[1] / "PROMPTS.md"


def ensure_file():
    if not PROMPTS_MD.exists():
        PROMPTS_MD.write_text("## Project Prompts Log\n\n")


def today_heading() -> str:
    return datetime.date.today().strftime("### %Y-%m-%d")


def append_prompt(note: str, link: str | None = None, section: str | None = None):
    ensure_file()
    content = PROMPTS_MD.read_text()

    lines = content.splitlines()
    heading = today_heading()

    # Ensure today's heading exists
    if heading not in content:
        lines.append(heading)

    entry = f"- {note}"
    if link:
        entry += f" ({link})"

    # Optional section subheading
    if section:
        sect_header = f"#### {section}"
        # Insert section header if missing under today's heading
        if sect_header not in content:
            lines.append(sect_header)
        lines.append(entry)
    else:
        lines.append(entry)

    PROMPTS_MD.write_text("\n".join(lines) + "\n")


def main():
    parser = argparse.ArgumentParser(description="Append a prompt entry to PROMPTS.md")
    parser.add_argument("--note", required=True, help="Prompt text or change note")
    parser.add_argument("--link", help="Optional file link or reference")
    parser.add_argument(
        "--section", help="Optional section name (e.g., Script Input Prompts)"
    )
    args = parser.parse_args()

    append_prompt(args.note, args.link, args.section)
    print(f"Appended prompt to {PROMPTS_MD}")


if __name__ == "__main__":
    main()
