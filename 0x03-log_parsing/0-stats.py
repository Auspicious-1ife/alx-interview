#!/usr/bin/python3
"""
Log Parsing Script

This script reads input from stdin, line by line, in the format of web server log entries and computes metrics based on the input. The script aggregates data and reports:

- Total file size of all processed log entries.
- The count of occurrences of specific HTTP status codes (200, 301, 400, 401, 403, 404, 405, 500).

The script processes data after every 10 lines and handles keyboard interruptions (CTRL + C), printing the final metrics before exiting.

Input format:
<IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>

Usage:
The script reads from stdin and prints output in the following format:

- Total file size: <total size>
- HTTP status code counts in ascending order (if applicable).

Sample output:
File size: 11320
200: 3
301: 2
400: 1
401: 2
403: 3
404: 4
405: 2
500: 3
"""

import sys
import signal

# Global variables
total_size = 0
status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0

def print_metrics():
    """
    Prints the aggregated metrics: total file size and status code counts.
    """
    global total_size, status_codes
    print(f"File size: {total_size}")
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print(f"{code}: {status_codes[code]}")

def handle_input_line(line):
    """
    Processes a single line of log input and updates the total file size and status code counts.

    Args:
        line (str): A line of input log data in the specified format.
    """
    global total_size, status_codes
    try:
        # Parse line based on expected format
        parts = line.split()
        if len(parts) > 6:
            file_size = int(parts[-1])
            status_code = int(parts[-2])
            
            # Update file size
            total_size += file_size

            # Update status code count if valid
            if status_code in status_codes:
                status_codes[status_code] += 1
    except (IndexError, ValueError):
        pass  # If the format is wrong, skip the line

def signal_handler(sig, frame):
    """
    Handles the keyboard interruption (CTRL + C) and prints metrics before exiting.
    """
    print_metrics()
    sys.exit(0)

# Attach signal handler to CTRL + C (SIGINT)
signal.signal(signal.SIGINT, signal_handler)

if __name__ == "__main__":
    try:
        for line in sys.stdin:
            handle_input_line(line)
            line_count += 1

            # Print metrics every 10 lines
            if line_count % 10 == 0:
                print_metrics()

    except KeyboardInterrupt:
        # Print final metrics if interrupted
        print_metrics()
        sys.exit(0)

    # Print final metrics after all input is processed
    print_metrics()

