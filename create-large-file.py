"""Generate a file large enough to trigger a multipart upload.

550 MB should do it.
The lower limit for S3 multipart uploads is 5 TiB / 10_000,
approximately 549.8 MB.
"""

from datetime import datetime as dt
from pathlib import Path
import valohai

MEGABYTE = 1_000_000
OUTPUT_DIR = "output_files"


def generate_large_file(filename: str, size_mb: int) -> None:
    size_in_bytes = size_mb * MEGABYTE
    chunk_size = MEGABYTE
    with open(filename, "wb") as f:
        for _ in range(size_in_bytes // chunk_size):
            f.write(b"\x00" * chunk_size)
        remaining_bytes = size_in_bytes % chunk_size
        if remaining_bytes:
            f.write(b"\x00" * remaining_bytes)
        print(f"File size: {f.tell()} bytes")
    print(f"Wrote {size_in_bytes} bytes to {filename}")
    file = Path(filename)
    print(f"File size: {file.stat().st_size} bytes")


def current_datetime():
    """Return current date and time."""
    return dt.now().strftime("%Y-%m-%d_%H-%M")


if __name__ == "__main__":
    output_path = valohai.outputs(OUTPUT_DIR).path(f"large_{current_datetime()}.bin")
    print(f"Creating large file: {output_path}")
    generate_large_file(output_path, 550)
