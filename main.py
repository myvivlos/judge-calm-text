"""Write the fixed ai-judge-relax-01 entry text to entry.txt using stdlib only."""

import hashlib
import os

ENTRY_BYTES = 546


def build_text() -> str:
    """Return the fixed entry text."""
    return (
        "We put the kettle down without hurrying. Rain had been at the window for a "
        "while, soft as a hand turning pages, and the room had gone the colour of tea "
        "left to steep. Nobody said anything, and the quiet was not the empty kind, "
        "only the ordinary kind, a house settling into its own evening. Outside, the "
        "streetlight came on in stages, the way ice gives up and turns to water. "
        "Tomorrow would want answers. For now the clock was allowed to be slow, and "
        "the cat, having found the warmest chair, closed its eyes as though nothing "
        "here needed watching."
    )


def main() -> None:
    """Validate and write the UTF-8 encoded entry text to entry.txt."""
    text = build_text()
    encoded = text.encode("utf-8")
    if not encoded or not text.strip() or len(text) > 1000 or len(encoded) > 1000:
        raise ValueError("Encoded entry text must be non-empty and at most 1000 characters.")
    assert len(encoded) == ENTRY_BYTES

    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    if output_dir:
        os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "entry.txt")
    # Write as raw UTF-8 bytes rather than text mode to avoid platform-dependent line-ending translation or locale encoding differences.
    with open(output_path, "wb") as f:
        f.write(encoded)

    if os.environ.get("MAKEFUN_VERBOSE") == "1":
        digest = hashlib.sha256(encoded).hexdigest()
        print(f"{output_path} {len(encoded)} {digest}")


if __name__ == "__main__":
    main()
