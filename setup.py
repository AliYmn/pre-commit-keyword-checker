from setuptools import setup, find_packages
import sys

if sys.version_info[0] < 3:
    with open('README.md') as f:
        README = f.read()
else:
    with open('README.md', encoding='utf-8') as f:
        README = f.read()

setup(
    name="pre-commit-keyword-checker",
    version="1.5.0",
    license="MIT",
    long_description_content_type="text/markdown",
    long_description=README,
    description="A pre-commit hook for checking specified keywords in the files being committed.",
    author="Ali Yaman",
    author_email="aliymn.db@gmail.com",
    url="https://github.com/AliYmn/pre-commit-keyword-checker",
    packages=find_packages(),
    install_requires=["pre-commit"],
    entry_points={
        "console_scripts": ["check-keywords = check_keywords.check_keywords:main"],
    },
)
