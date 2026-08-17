import re, unicodedata, hashlib
from ftfy import fix_text

BOILERPLATE = {
    "home  products  pricing  contact",
    "was this article helpful?",
    "copyright 2026 acme inc. all rights reserved.",
}

def clean_text(raw_text: str) -> str:
    # Fix encoding and normalize Unicode
    text = unicodedata.normalize("NFKC", fix_text(raw_text))
    out = []

    for line in text.splitlines():
        # Normalize whitespace
        line = re.sub(r"\s+", " ", line).strip()
        low = line.lower()

        # Strip boilerplate
        if not line or low in BOILERPLATE:
            continue 

        # Drop low-value lines
        if len(line) < 15 and not re.search(r"[a-zA-Z]", line):
            continue

        out.append(line)

    return "\n".join(out)

seen = set()

# Drop exact duplicates by content hash
def dedup(chunks: list[str]) -> list[str]:
    kept = []

    for char in chunks:
        hashed_char = hashlib.sha256(char.encode()).hexdigest()

        if hashed_char not in seen:
            seen.add(hashed_char)
            kept.append(char)

    return kept