# OpenCV Chessboard Generator

[![PyPI version](https://badge.fury.io/py/opencv-chessboard-generator.svg)](https://badge.fury.io/py/opencv-chessboard-generator)
[![Python versions](https://img.shields.io/pypi/pyversions/opencv-chessboard-generator.svg)](https://pypi.org/project/opencv-chessboard-generator/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A Python tool to generate high-quality chessboard patterns for OpenCV camera calibration.

## Features

- 🎯 Customizable grid dimensions (rows × columns)
- 📏 Configurable square size in centimeters
- 🖨️ Print-ready output with exact DPI settings
- 👁️ Preview before saving
- 📦 Easy to use Python API and CLI

## Installation

Install from PyPI:

```bash
pip install opencv-chessboard-generator
```

## Usage

### Command Line Interface

After installation, run the interactive CLI:

```bash
chessboard-generator
```

Follow the prompts to specify:

- Number of inner corner columns (e.g., 6)
- Number of inner corner rows (e.g., 9)
- Square size in centimeters (default: 3.0)
- DPI resolution for printing (default: 300)

### Python API

```python
from chessboard_generator import ChessboardGenerator

# Create a chessboard with 6x9 inner corners, 3cm squares, 300 DPI
generator = ChessboardGenerator(rows=9, cols=6, square_size_cm=3.0, dpi=300)

# Save to file
generator.save("my_chessboard.png")

# Or preview before saving
generator.preview()
```

### Recommended Settings for A3 Paper

For A3 paper (29.7 × 42 cm), we recommend:

- **13×8 inner corners** (landscape orientation)
- **Square size: 3.0 cm**
- **DPI: 300**

```python
generator = ChessboardGenerator(rows=8, cols=13, square_size_cm=3.0, dpi=300)
generator.save("chessboard_a3.png")
```

## Printing Instructions

⚠️ **IMPORTANT**: For accurate camera calibration, print settings matter!

1. Print at **EXACTLY** the specified DPI (no scaling)
2. Disable "Fit to page" in print settings
3. Use 100% scaling
4. Mount the printed chessboard on a flat, rigid surface
5. Measure the printed squares to verify they match your specified size

## OpenCV Integration

After generating your chessboard, use it with OpenCV:

```python
import cv2

# For a 6×9 inner corners chessboard
pattern_size = (6, 9)
square_size = 3.0  # cm

# Find chessboard corners in your calibration images
ret, corners = cv2.findChessboardCorners(image, pattern_size)
```

## Requirements

- Python >= 3.7
- OpenCV >= 4.5.0
- NumPy >= 1.19.0

## License

MIT License

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Development

For development setup and automated releases with GitHub Actions, see:
- [Quick Start Guide](QUICKSTART.md)
- [Detailed GitHub Actions Guide](GITHUB_ACTIONS_GUIDE.md)

## Author

Batuhan ÖKMEN (batuhanokmen@gmail.com)
