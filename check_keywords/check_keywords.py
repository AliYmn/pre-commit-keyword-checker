#!/usr/bin/env python3
import argparse
import os
import sys
import re


def main():
    parser = argparse.ArgumentParser(
        description="Check keywords in the files being committed")
    parser.add_argument("--exclude", type=str, help="File pattern to exclude")
    parser.add_argument("--keywords", nargs="+",
                        help="Keywords to search for in the files")
    parser.add_argument("--exclude-files", nargs="+",
                        help="List of files to exclude from the keyword check")
    args = parser.parse_args()

    if not args.keywords:
        sys.exit(0)

    exclude_pattern = args.exclude
    keywords = args.keywords
    exclude_files_list = args.exclude_files if args.exclude_files else []

    modified_files = os.popen(
        "git diff --name-only --cached").read().splitlines()
    excluded_files = (
        os.popen(
            f"git diff --name-only --cached | grep -E '{exclude_pattern}'").read().splitlines()
        if exclude_pattern
        else []
    )

    keyword_errors = []

    for modified_file in modified_files:
        if (
            modified_file in excluded_files
            or modified_file in [".pre-commit-config.yaml", "check_keywords.py"]
            or modified_file in exclude_files_list
        ):
            continue

        file_content = os.popen(f"git show :{modified_file}").read()
        for keyword in keywords:
            if re.search(fr"\b{re.escape(keyword)}\b", file_content, re.IGNORECASE):
                keyword_errors.append((keyword, modified_file))

    if keyword_errors:
        print("\nKeyword Errors:")
        for keyword, file in keyword_errors:
            print(f"  - Keyword '{keyword}' found in {file}.")
        sys.exit(1)
    else:
        print("\nFiles passed keyword check.")
        sys.exit(0)


if __name__ == "__main__":
    main()
