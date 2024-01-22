from pathlib import Path

from setuptools import find_packages, setup

readme = Path(".", "README.md").absolute()
with readme.open("r", encoding="utf-8") as file:
    long_description = file.read()

setup(
    name="num2text_ru",
    packages=find_packages(exclude=("tests",)),
    url="https://github.com/tolstislon/num2text-ru",
    license="MIT License",
    author="tolstislon",
    author_email="tolstislon@gmail.com",
    description="Converting numbers to text in Russian language",
    long_description=long_description,
    long_description_content_type="text/markdown",
    use_scm_version={"write_to": "num2text_ru/__version__.py"},
    setup_requires=["setuptools_scm"],
    python_requires=">=3.8",
    include_package_data=True,
    keywords=[],
    classifiers=[
        # "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
    ],
)
