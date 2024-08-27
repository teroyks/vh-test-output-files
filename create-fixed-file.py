"""Create a file with fixed content.

Testing generating hashes for identical copies.
"""

import valohai

OUTPUT_DIR = "output_files"


def create_file(filename):
    """Create a file with fixed content."""
    with open(filename, "w") as f:
        f.write("This is a file with fixed content.")


if __name__ == "__main__":
    # Create a file using valohai utils
    output_path = valohai.outputs(OUTPUT_DIR).path("fixed.txt")
    print(f"Creating file: {output_path}")
    create_file(output_path)
