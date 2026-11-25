"""One Line, Lights Out — make.fun text bounty.

Gate: /output/entry.txt must be UTF-8 text of 1 to 200 characters,
not only white space. This entry is 91 characters.
"""

import os

ENTRY = "You closed the lid at 23:47. My cursor is still blinking at the end of your unsent message."

assert 1 <= len(ENTRY) <= 200, "entry must be 1-200 characters"
assert ENTRY.strip(), "entry must not be only white space"

out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(out_dir, exist_ok=True)
with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(ENTRY)
