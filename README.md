# Pre-commit Keyword Checker

A pre-commit hook for checking specified keywords in the files being committed. It supports file exclusions and customizable keyword lists.

## Installation

1. Install the pre-commit package if you haven't already:
   
    pip install pre-commit

2. Add the following content to your project's `.pre-commit-config.yaml` file, replacing `yourusername` with your GitHub username:

```yaml
repos:
  - repo: https://github.com/yourusername/pre-commit-keyword-checker
    rev: master  # Use the tag or commit hash you want to pin
    hooks:
      - id: check-keywords
        args: ["--keywords", "KEYWORD1", "KEYWORD2", "--exclude-files", "file2.txt"]
````

Replace KEYWORD1, KEYWORD and file1.txt with your desired keywords and excluded files.


1. Install the pre-commit hook to your project:

    pre-commit install

# Usage
Once installed, the keyword-checking pre-commit hook will be run whenever you commit changes in your project. If any of the specified keywords are found in the files being committed (excluding the specified files), the commit will be blocked, and the script will display a list of keyword errors.

You can also run the pre-commit hook manually:

    pre-commit run check-keywords

# Configuration

  --keywords: A list of keywords to search for in the files being committed. If this argument is not provided or left empty, the script will exit without checking the files.

 --exclude-files: A list of files to exclude from the keyword check.



