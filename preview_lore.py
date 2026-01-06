"""
Preview module for Minecraft lore output.
Displays the lore as square blocks with visible grid lines.
Uses Pillow for fast image rendering.
"""

import json
import tkinter as tk
from PIL import Image, ImageTk, ImageDraw


def hex_to_rgb(hex_color):
    """Convert hex color #RRGGBB to RGB tuple"""
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))


def show_preview(lore_lines):
    """Open a window to preview the lore output with colored square blocks and grid lines"""
    # Calculate dimensions
    num_rows = len(lore_lines)
    num_cols = 0

    # Parse lore to find width and build pixel data
    pixel_data = []
    for lore_json in lore_lines:
        lore_data = json.loads(lore_json)
        row_pixels = []
        if "extra" in lore_data:
            for part in lore_data["extra"]:
                color = part.get("color", "#FFFFFF")
                text = part.get("text", "")
                # Each █ character represents one pixel
                for _ in text:
                    row_pixels.append(color)
        pixel_data.append(row_pixels)
        num_cols = max(num_cols, len(row_pixels))

    # Determine pixel size to fit all pixels within a reasonable window size
    max_width = 900
    max_height = 700
    pixel_size = max(1, min(max_width // num_cols, max_height // num_rows))

    # Create image using Pillow (much faster than canvas rectangles)
    img_width = num_cols * pixel_size
    img_height = num_rows * pixel_size

    # Create base image from pixel data at 1:1 scale first
    base_img = Image.new('RGB', (num_cols, num_rows), color=(26, 26, 46))

    for y, row in enumerate(pixel_data):
        for x, color in enumerate(row):
            base_img.putpixel((x, y), hex_to_rgb(color))

    # Scale up using NEAREST to keep sharp pixels (no blending)
    scaled_img = base_img.resize((img_width, img_height), Image.Resampling.NEAREST)

    # Draw grid lines if pixel size is large enough to see them
    if pixel_size >= 3:
        draw = ImageDraw.Draw(scaled_img)
        grid_color = (26, 26, 26)  # Dark grid lines

        # Draw vertical lines
        for x in range(0, img_width + 1, pixel_size):
            draw.line([(x, 0), (x, img_height)], fill=grid_color, width=1)

        # Draw horizontal lines
        for y in range(0, img_height + 1, pixel_size):
            draw.line([(0, y), (img_width, y)], fill=grid_color, width=1)

    # Create tkinter window
    root = tk.Tk()
    root.title("Lore Preview")
    root.configure(bg='#2b2b2b')
    root.resizable(False, False)  # Fixed size window

    # Convert to PhotoImage for tkinter
    photo = ImageTk.PhotoImage(scaled_img)

    # Create label to display image (faster than canvas for static images)
    img_label = tk.Label(root, image=photo, bg='#2b2b2b')
    img_label.image = photo  # Keep reference to prevent garbage collection
    img_label.pack()

    # Add info label
    info_label = tk.Label(root, text=f"Size: {num_cols}x{num_rows} | Block: {pixel_size}px | Close window to exit",
                          bg='#2b2b2b', fg='white')
    info_label.pack(pady=5)

    # Center the window
    root.update_idletasks()
    x = (root.winfo_screenwidth() // 2) - (root.winfo_width() // 2)
    y = (root.winfo_screenheight() // 2) - (root.winfo_height() // 2)
    root.geometry(f"+{x}+{y}")

    root.mainloop()


if __name__ == "__main__":
    # Can also be run standalone by reading a lore file
    import sys

    if len(sys.argv) < 2:
        print("Usage: python preview_lore.py <lore_file.txt>")
        print("Or import and call show_preview(lore_lines) from another script")
        exit(1)

    lore_file = sys.argv[1]

    # Read and parse the lore file
    with open(lore_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Extract lore lines from the minecraft:lore format
    # Format: {"minecraft:lore":['line1','line2',...]}
    import re
    # Find all single-quoted JSON strings
    matches = re.findall(r"'({[^']+})'", content)

    if matches:
        show_preview(matches)
    else:
        print("Could not parse lore data from file")

