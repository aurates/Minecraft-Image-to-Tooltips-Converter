# 99% of the code is done by vibe coding <3
import os
import json
from PIL import Image

def rgb_to_hex_color(r, g, b):
    """Convert RGB to hex color format #RRGGBB"""
    return f"#{r:02X}{g:02X}{b:02X}"

def image_to_minecraft_lore(image_path, width=75, height=64):
    """Convert image to Minecraft lore format with hex colors"""
    img = Image.open(image_path)
    img = img.convert('RGB')
    img = img.resize((width, height), Image.Resampling.LANCZOS)
    
    lore_lines = []
    
    for y in range(height):
        # Start building the line
        line_parts = []
        current_color = None
        count = 0
        
        for x in range(width):
            r, g, b = img.getpixel((x, y))
            hex_color = rgb_to_hex_color(r, g, b)
            
            # If color changes, save the previous color run
            if hex_color != current_color:
                if current_color is not None:
                    line_parts.append({
                        "color": current_color,
                        "text": "█" * count
                    })
                current_color = hex_color
                count = 1
            else:
                count += 1
        
        # Add the last color run
        if current_color is not None:
            line_parts.append({
                "color": current_color,
                "text": "█" * count
            })
        
        # Format the line in Minecraft lore format as JSON
        lore_object = {
            "extra": line_parts,
            "italic": False,
            "text": ""
        }
        lore_lines.append(json.dumps(lore_object, separators=(',', ':'), ensure_ascii=False))
    
    return lore_lines

def create_lore_txt(image_path, output_path=None, img_width=75, img_height=64):
    """Create a txt file with Minecraft lore format"""
    
    if output_path is None:
        script_dir = os.path.dirname(os.path.abspath(__file__)) if '__file__' in globals() else os.getcwd()
        base_name = os.path.splitext(os.path.basename(image_path))[0]
        output_path = os.path.join(script_dir, f'{base_name}_lore.txt')
    
    print(f"Converting image: {image_path}")
    lore_lines = image_to_minecraft_lore(image_path, img_width, img_height)
    print(f"Generated {len(lore_lines)} lines of lore")
    
    # Format as custom JSON with minecraft:lore key and single-quoted array elements
    lore_array = ",".join([f"'{line}'" for line in lore_lines])
    output_text = f'{{"minecraft:lore":[{lore_array}]}}'
    
    # Write to file
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(output_text)
    
    print(f"\nSuccessfully created {output_path}")
    print(f"File saved at: {os.path.abspath(output_path)}")
    print(f"\nYou can copy this lore data and use it in your Minecraft item components")

if __name__ == "__main__":
    # List image files in current directory
    image_files = [f for f in os.listdir('.') if f.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif'))]
    
    if not image_files:
        print("No image files found in current directory!")
        exit(1)
    
    # Use the first image found
    image_path = image_files[0]
    print(f"Using image: {image_path}")
    
    # Optional: customize resolution
    width = input("Enter width (default 75): ").strip()
    height = input("Enter height (default 64): ").strip()
    
    width = int(width) if width else 75
    height = int(height) if height else 64
    

    create_lore_txt(image_path, img_width=width, img_height=height)
