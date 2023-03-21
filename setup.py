from setuptools import setup, find_packages

setup(
    name="pre-commit-keyword-checker",
    version="0.1.0",
    description="Pre-commit hook to detect specified keywords in files being committed",
    author="Ali Yaman",
    author_email="aliymn.db@gmail.com",
    packages=find_packages(),
    install_requires=["pre-commit"],
    entry_points={
        "console_scripts": ["check-keywords = check_keywords.main:main"],
    },
)
