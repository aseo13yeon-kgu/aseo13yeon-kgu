import json
import re
import datetime
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
README = ROOT / "README.md"
IDIOMS = ROOT / "idioms.json"

START = "<!-- IDIOM:START -->"
END = "<!-- IDIOM:END -->"


def main():
    idioms = json.loads(IDIOMS.read_text(encoding="utf-8"))
    day_index = datetime.date.today().timetuple().tm_yday
    idiom = idioms[day_index % len(idioms)]

    block = (
        f"{START}\n"
        f"> **{idiom['hanzi']} ({idiom['korean_reading']})**  \n"
        f"> {idiom['meaning_ko']}  \n"
        f"> {idiom['meaning_zh']}\n"
        f"{END}"
    )

    text = README.read_text(encoding="utf-8")
    pattern = re.compile(re.escape(START) + r".*?" + re.escape(END), re.DOTALL)
    if not pattern.search(text):
        raise SystemExit("README.md에서 IDIOM 마커를 찾을 수 없습니다.")

    README.write_text(pattern.sub(block, text), encoding="utf-8")


if __name__ == "__main__":
    main()
