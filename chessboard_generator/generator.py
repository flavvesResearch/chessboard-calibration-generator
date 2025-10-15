"""
Chessboard Generator Module
Creates chessboard patterns with customizable dimensions for OpenCV calibration
"""

import cv2
import numpy as np
from pathlib import Path


class ChessboardGenerator:
    """
    A class to generate chessboard patterns for camera calibration.
    
    Attributes:
        rows (int): Number of inner corner rows (squares - 1)
        cols (int): Number of inner corner columns (squares - 1)
        square_size_cm (float): Size of each square in centimeters
        dpi (int): Dots per inch for printing resolution
    """
    
    def __init__(self, rows=9, cols=6, square_size_cm=3.0, dpi=300):
        """
        Initialize the chessboard generator.
        
        Args:
            rows (int): Number of inner corner rows (e.g., 9 for 10x7 board)
            cols (int): Number of inner corner columns (e.g., 6 for 10x7 board)
            square_size_cm (float): Size of each square in cm (default: 3.0)
            dpi (int): Resolution in dots per inch (default: 300)
        """
        self.rows = rows
        self.cols = cols
        self.square_size_cm = square_size_cm
        self.dpi = dpi
        
        # Calculate pixel size based on DPI
        # 1 inch = 2.54 cm
        self.pixels_per_cm = dpi / 2.54
        self.square_size_pixels = int(square_size_cm * self.pixels_per_cm)
        
    def generate_chessboard(self):
        """
        Generate a chessboard pattern.
        
        Returns:
            numpy.ndarray: The generated chessboard image
        """
        # Total number of squares (including outer squares)
        total_rows = self.rows + 1
        total_cols = self.cols + 1
        
        # Calculate image dimensions
        height = total_rows * self.square_size_pixels
        width = total_cols * self.square_size_pixels
        
        # Create empty white image
        chessboard = np.ones((height, width), dtype=np.uint8) * 255
        
        # Fill in black squares
        for i in range(total_rows):
            for j in range(total_cols):
                # Checkerboard pattern: alternate colors
                if (i + j) % 2 == 1:
                    y_start = i * self.square_size_pixels
                    y_end = (i + 1) * self.square_size_pixels
                    x_start = j * self.square_size_pixels
                    x_end = (j + 1) * self.square_size_pixels
                    chessboard[y_start:y_end, x_start:x_end] = 0
        
        return chessboard
    
    def add_border_and_info(self, chessboard, border_size=50):
        """
        Add a white border and information text to the chessboard.
        
        Args:
            chessboard (numpy.ndarray): The chessboard image
            border_size (int): Size of the border in pixels (default: 50)
            
        Returns:
            numpy.ndarray: Chessboard with border and info
        """
        # Add white border
        bordered = cv2.copyMakeBorder(
            chessboard,
            border_size, border_size, border_size, border_size,
            cv2.BORDER_CONSTANT,
            value=255
        )
        
        return bordered
    
    def save(self, filename="chessboard.png", add_info=True):
        """
        Generate and save the chessboard pattern.
        
        Args:
            filename (str): Output filename (default: "chessboard.png")
            add_info (bool): Whether to add border and information text
            
        Returns:
            bool: True if saved successfully, False otherwise
        """
        # Generate chessboard
        chessboard = self.generate_chessboard()
        
        # Add border and info if requested
        if add_info:
            chessboard = self.add_border_and_info(chessboard)
        
        # Save the image
        success = cv2.imwrite(filename, chessboard)
        
        if success:
            print(f"[OK] Chessboard saved successfully: {filename}")
            print(f"  - Inner corners: {self.cols}x{self.rows}")
            print(f"  - Square size: {self.square_size_cm} cm")
            print(f"  - Image size: {chessboard.shape[1]}x{chessboard.shape[0]} pixels")
            print(f"  - Resolution: {self.dpi} DPI")
            print(f"\nFor OpenCV calibration, use:")
            print(f"  pattern_size = ({self.cols}, {self.rows})")
            print(f"  square_size = {self.square_size_cm}  # cm")
        else:
            print(f"[ERROR] Failed to save chessboard: {filename}")
        
        return success
    
    def preview(self):
        """
        Generate and display the chessboard pattern in a window.
        Press any key to close the window.
        """
        chessboard = self.generate_chessboard()
        chessboard_with_info = self.add_border_and_info(chessboard)
        
        # Resize for display if too large
        max_display_size = 1200
        if max(chessboard_with_info.shape) > max_display_size:
            scale = max_display_size / max(chessboard_with_info.shape)
            new_width = int(chessboard_with_info.shape[1] * scale)
            new_height = int(chessboard_with_info.shape[0] * scale)
            display_img = cv2.resize(chessboard_with_info, (new_width, new_height))
        else:
            display_img = chessboard_with_info
        
        cv2.imshow('Chessboard Preview', display_img)
        print("Press any key to close the preview window...")
        cv2.waitKey(0)
        cv2.destroyAllWindows()
