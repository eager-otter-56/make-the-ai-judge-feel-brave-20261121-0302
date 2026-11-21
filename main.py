import os

TEXT = (
    "The harbor is still dark when you reach the dock. "
    "Frost on the rope, cold in your hands \u2014 and under your fingers, "
    "the knot gives, strand by strand, the way it always has. "
    "The water holds the boat. It held it all night. "
    "Step in. The oars are where you left them."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
