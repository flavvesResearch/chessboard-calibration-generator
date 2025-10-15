"""
Setup configuration for chessboard-generator package
"""

from setuptools import setup, find_packages
from pathlib import Path

# Read the README file
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text(encoding='utf-8')

setup(
    name="opencv-chessboard-generator",
    version="1.0.0",
    author="batuhan ÖKMEN",
    author_email="batuhanokmen@gmail.com",
    description="A tool to generate chessboard patterns for OpenCV camera calibration",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/flavvesResearch/chessboard-calibration-generator",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Image Recognition",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
    install_requires=[
        "opencv-python>=4.5.0",
        "numpy>=1.19.0",
    ],
    entry_points={
        'console_scripts': [
            'chessboard-generator=chessboard_generator.__main__:main',
        ],
    },
    keywords="opencv calibration chessboard camera computer-vision",
    project_urls={
        "Bug Reports": "https://github.com/flavvesResearch/chessboard-calibration-generator/issues",
        "Source": "https://github.com/flavvesResearch/chessboard-calibration-generator",
    },
)
