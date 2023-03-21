from setuptools import setup, find_packages

setup(
    name="pre-commit-keyword-checker",
    version="0.2.1",
    description="A pre-commit hook for checking specified keywords in the files being committed.",
    author="Ali Yaman",
    author_email="aliymn.db@gmail.com",
    url="https://github.com/AliYmn/pre-commit-keyword-checker",
    packages=find_packages(),
    install_requires=["pre-commit"],
    entry_points={
        "console_scripts": ["check-keywords = check_keywords.main:main"],
    },
)
