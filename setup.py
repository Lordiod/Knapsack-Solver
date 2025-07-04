"""
Setup script for Knapsack Problem Solver
"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="knapsack-problem-solver",
    version="1.0.0",
    author="Knapsack Solver Contributors",
    author_email="",
    description="A professional GUI application for solving 0/1 and Fractional Knapsack problems",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/Knapsack-Solver",
    project_urls={
        "Bug Tracker": "https://github.com/yourusername/Knapsack-Solver/issues",
        "Documentation": "https://github.com/yourusername/Knapsack-Solver#readme",
        "Source Code": "https://github.com/yourusername/Knapsack-Solver",
    },
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Education",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Mathematics",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Education",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Environment :: X11 Applications",
        "Environment :: Win32 (MS Windows)",
        "Environment :: MacOS X",
    ],
    packages=find_packages(),
    python_requires=">=3.7",
    install_requires=requirements,
    extras_require={
        "dev": [
            "pytest>=6.0",
            "pytest-cov>=2.0",
            "black>=21.0",
            "flake8>=3.8",
            "mypy>=0.800",
        ],
    },
    entry_points={
        "console_scripts": [
            "knapsack-solver=main:main",
        ],
    },
    keywords=[
        "knapsack",
        "algorithm",
        "dynamic-programming",
        "optimization",
        "gui",
        "educational",
        "computer-science",
        "mathematics",
    ],
    include_package_data=True,
    zip_safe=False,
)
