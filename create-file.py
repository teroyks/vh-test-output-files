"""Create a file with dummy content.

Add current date and time to the file name to make browsing the list easier.
"""

from datetime import datetime as dt

import valohai

OUTPUT_DIR = "output_files"


def create_file(filename):
    """Create a file with dummy content."""
    with open(filename, "w") as f:
        f.write(dt.now().strftime("%Y-%m-%d %H:%M:%S"))


def current_datetime():
    """Return current date and time."""
    return dt.now().strftime("%Y-%m-%d_%H-%M")


if __name__ == "__main__":
    # Create a file using valohai utils
    output_path = valohai.outputs(OUTPUT_DIR).path(f"dummy_{current_datetime()}.txt")
    print(f"Creating file: {output_path}")
    create_file(output_path)

    # Create a file using the plain path
    plain_output_path = f"/valohai/outputs/{OUTPUT_DIR}/plain_{current_datetime()}.txt"
    print(f"Creating file: {plain_output_path}")
    create_file(plain_output_path)
