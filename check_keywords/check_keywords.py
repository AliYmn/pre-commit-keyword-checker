#!/usr/bin/env python3
import argparse
import os
import sys
import re


def main():
    parser = argparse.ArgumentParser(
        description="Check for specific keywords in the files before committing.")
    parser.add_argument("--exclude", type=str, nargs="?",
                        default=None, help="Directories to exclude")
    parser.add_argument("--keywords", type=str, nargs="*",
                        default=[], help="Keywords to look for")
    parser.add_argument("--exclude-files", type=str, nargs="*",
                        default=[], help="File extensions to exclude")
    args = parser.parse_args()

    exclude_pattern = args.exclude if args.exclude else []
    keywords = args.keywords if args.keywords else []
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
