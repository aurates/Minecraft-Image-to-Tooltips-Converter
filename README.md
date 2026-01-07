# Minecraft Image to Lore Converter

A Python script that converts images into Minecraft item lore format using colored unicode block characters (█). This allows you to display images as item tooltips on most of the modern Minecraft versions.

## Feature Highlights
- Converts images to Minecraft lore format using colored blocks
- Preview generated lore in a popup window
- Supports PNG, JPG, JPEG, BMP, and GIF formats
- Customizable output resolution

## 📋 Requirements

### Python Version
- Python 3.6 or higher

### Required Packages
Install the required package using pip:

```bash
pip install Pillow
```

Or create a `requirements.txt` file with:
```
Pillow
```

Then install with:
```bash
pip install -r requirements.txt
```

## 🎮 Compatibility

- **Minecraft Version**: 1.20.5+ (uses the new `minecraft:lore` component format)
- **Image Formats Supported**: PNG, JPG, JPEG, BMP, GIF

## 🚀 How to Use

### Basic Usage

1. Place your image file in the same directory as the script
2. Run the script:
   ```bash
   python converter.py
   ```
3. Enter the desired width and height when prompted (or press Enter for defaults: 75x64)
4. The script will generate a `{imagename}_lore.txt` file

### Example

```bash
python converter.py
```

Output:
```
Using image: image.png
Enter width (default 75): 
Enter height (default 64): 
Converting image: image.png
Generated 64 lines of lore
Successfully created image_lore.txt
```

## 📝 Output Format

The script generates a file containing the `minecraft:lore` component data in JSON format:

```json
{"minecraft:lore":['{"extra":[{"color":"#RRGGBB","text":"█████"},...]}', ...]}
```

## 🎯 Using in Minecraft

### Method 1: NBT Editor Mod
#### The latest version of this mod only supports up to 1.21.4, so I suggest you do everything on 1.21.4 and use creative hotbar to migrate them to other verisons.
Use the [NBT Editor mod](https://modrinth.com/mod/nbt-editor) to apply the lore to existing items in-game.

1. Install the NBT Editor mod
2. Hold the item you want to edit
3. Use the mod's commands/interface to edit the item's lore component
4. Paste the generated lore data

### Method 2: Find it yourself :D (I think you can do it with data pack)

## ⚙️ Configuration

### Image Resolution
- **Default Width**: 75 pixels
- **Default Height**: 64 pixels

**I would suggest you keep the aspect ratio as the origional image, so it doesn't look weird**

**Tips for best results:**
- Larger dimensions = more detail but longer lore text
- Too large may cause performance issues or exceed lore limits
- Recommended: Keep width between 50-100 for best balance

### Supported Image Formats
The script automatically detects image files with these extensions:
- `.png`
- `.jpg` / `.jpeg`
- `.bmp`
- `.gif`

## 👀 Tooltips Preview
After generating the lore file, there will be a preview option at the end of the cmd prompt. Type `y` and then a preview window will pop up to show you how the image looks like in Minecraft tooltips.

## 📁 File Structure

```
converter/
├── converter.py            # Main script
├── README.md               # This file
├── image.png               # Your input image
├── preview_lore.py        # Preview script
└── image_lore.txt          # Generated output

```

## 🔧 Troubleshooting

### "No image files found in current directory!"
- Ensure your image file is in the same folder as the script
- Check that the image has a supported extension (.png, .jpg, .jpeg, .bmp, .gif)

### "ModuleNotFoundError: No module named 'PIL'"
- Install Pillow: `pip install Pillow`

### Image looks distorted in-game
- Try different width/height ratios that match your source image's aspect ratio
- Use a smaller resolution for cleaner results

## 📜 License

MIT License

## 🤝 Contributing

Suggestions and improvements are welcome!

# Side Note

This project is mainly AI generated (including most part of this README.md), so I don't take much responsibility for any bugs because I didn't debug it myself. Feel free to modify and improve the code as needed! <3


