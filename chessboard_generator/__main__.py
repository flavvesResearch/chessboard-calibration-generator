"""
Command-line interface for chessboard generator
"""

from pathlib import Path
from .generator import ChessboardGenerator


def main():
    """
    Main function with interactive menu for chessboard generation.
    """
    print("=" * 60)
    print("Chessboard Generator for Camera Calibration")
    print("=" * 60)
    print()
    
    # Get user input
    try:
        cols = int(input("Enter number of inner corner COLUMNS (e.g., 6): ").strip() or "6")
        rows = int(input("Enter number of inner corner ROWS (e.g., 9): ").strip() or "9")
        square_size = float(input("Enter square size in cm (default: 3.0): ").strip() or "3.0")
        dpi = int(input("Enter DPI resolution (default: 300): ").strip() or "300")
        
        # Create output directory if it doesn't exist
        output_dir = Path("generated_chessboards")
        output_dir.mkdir(exist_ok=True)
        
        # Generate filename
        filename = output_dir / f"chessboard_{cols}x{rows}_{square_size}cm_{dpi}dpi.png"
        
        print("\n" + "-" * 60)
        print("Generating chessboard with following parameters:")
        print(f"  - Inner corners: {cols}x{rows}")
        print(f"  - Square size: {square_size} cm")
        print(f"  - DPI: {dpi}")
        print("-" * 60)
        print()
        
        # Create generator and save
        generator = ChessboardGenerator(rows=rows, cols=cols, 
                                       square_size_cm=square_size, dpi=dpi)
        
        # Ask if user wants to preview
        preview = input("\nWould you like to preview before saving? (y/n): ").strip().lower()
        if preview == 'y':
            generator.preview()
        
        # Save the chessboard
        generator.save(str(filename))
        
        print("\n" + "=" * 60)
        print("IMPORTANT PRINTING INSTRUCTIONS:")
        print("=" * 60)
        print(f"1. Print at EXACTLY {dpi} DPI (no scaling)")
        print("2. Disable 'Fit to page' in print settings")
        print("3. Use 100% scaling")
        print("4. Mount on a flat, rigid surface")
        print("5. Measure the printed squares to verify size")
        print(f"   (Each square should be {square_size} cm x {square_size} cm)")
        print("=" * 60)
        
    except ValueError as e:
        print(f"\n✗ Invalid input: {e}")
        return
    except Exception as e:
        print(f"\n✗ Error: {e}")
        return


if __name__ == "__main__":
    main()
