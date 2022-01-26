"""CSV Data and Weather Project."""

__author__ = "730329298"

import sys

from csv import DictReader

from typing import List, Dict

SOD: str = "SOD  "
NUMBER_OF_READINGS: float = 7.0

def main() -> None:
    args: Dict[str, str] = read_args()
    results: List[float] = list(args["file_path"], args["column"])
    if sys.argv[3] == "min":
        new_results = min(results)
    if sys.argv[3] == "max":
        new_results = max(results)
    if sys.argv[3] == "avg":
        new_results = sum(results)/NUMBER_OF_READINGS
    print(new_results)


def read_args() -> Dict[str, str]:
    """Check for valid CLI arguments and return them in a dictionary."""
    if len(sys.argv) != 4:
        print("Usage: python -m projects.pj01.weather [file] [column] [operation]")
        exit()
    return {
        "file_path": sys.argv[1],
        "column": sys.argv[2],
        "operation": sys.argv[3]
        }


def list(file_path: str, column: str) -> List[float]:
    file_handle = open(FILE, "r", encoding="utf8")
    csv_reader = DictReader(file_handle)
    sod_data: List[float] = []
    for row in csv_reader:
        if row['REPORT_TYPE'] == SOD:
            try:
                sod_data.append(float(row[column]))
            except ValueError:
                ... # Ignore an invalid value
    return(sod_data)


if __name__ == "__main__":
    main()


