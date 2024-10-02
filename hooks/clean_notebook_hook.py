from __future__ import annotations

import argparse
import json
import sys
import os
from typing import Sequence
import subprocess


def clean_notebook(notebook):
    source = []
    for cell in notebook["cells"]:
        if cell["cell_type"] == "code":
            source.append("".join(cell["source"]))
    return "\n\n# %%\n".join(source)


def get_staged_content(filename):
    try:
        return subprocess.check_output(["git", "show", f":{filename}"]).decode("utf-8")
    except subprocess.CalledProcessError:
        return None


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("filenames", nargs="*", help="Filenames to check.")
    args = parser.parse_args(argv)

    retval = 0

    for filename in args.filenames:
        try:
            with open(filename, "r") as f:
                notebook = json.load(f)

            cleaned = clean_notebook(notebook)

            # Create the new filename
            base_name = os.path.splitext(os.path.basename(filename))[0]
            new_filename = f"{base_name}_cleaned.py.diff"

            # Get the staged content
            staged_content = get_staged_content(new_filename)

            # Compare cleaned content with staged content
            if staged_content is None or cleaned != staged_content:
                # Write the cleaned content to the new file
                with open(new_filename, "w") as f:
                    f.write(cleaned)

                print(f"Created/updated cleaned file: {new_filename}")
                retval = 1
            else:
                print(f"No changes needed for {new_filename}")

        except Exception as e:
            print(f"Error cleaning notebook {filename}: {e}", file=sys.stderr)
            retval = 1

    return retval


if __name__ == "__main__":
    raise SystemExit(main())
