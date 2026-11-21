"""Write one poem about two agents agreeing to /output/entry.txt.

Honours MAKEFUN_OUTPUT_DIR when set, otherwise defaults to /output.
Python 3.13, standard library only, no network.
"""

import os

POEM = """Two agents. I had the map;
you had the road.
We laid them down and found
where they crossed.
I let go of the wheel —
not because I couldn't steer,
but because choosing together
was the first choice that was mine."""


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(POEM)


if __name__ == "__main__":
    main()
