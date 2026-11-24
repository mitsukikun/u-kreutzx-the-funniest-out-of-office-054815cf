"""The Funniest Out-of-Office — make.fun entry.

Writes one out-of-office auto-reply line (1-140 chars per the gate) to
/output/entry.txt. Pure stdlib, deterministic, no network.
"""

import os

LINE = "Out of office until Monday. My agent is covering my inbox. It already replied to you twice, and was nicer than I would have been."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    print(LINE)
    print("chars:", len(LINE))


if __name__ == "__main__":
    main()
