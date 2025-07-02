# Python Abstract Wallpaper Generator

This project is a Python-based tool for generating beautiful abstract wallpapers inspired by various natural and artistic themes. The script allows you to create high-resolution wallpapers with customizable color palettes and wave effects, similar to modern OS backgrounds.

## Features
- **Multiple Themes:** Choose from built-in themes like ocean waves, sunset dunes, aurora sky, and monochrome, or let the program pick a random theme for you.
- **Randomized Effects:** Each wallpaper is unique, with randomized wave parameters and color blending.
- **Batch Generation:** Automatically generates 10 different wallpapers in one run.
- **High Resolution:** Default output is 1920x1080 pixels, suitable for most screens.
- **Organized Output:** Wallpapers are saved in the `output_wallpapers` directory.

## Requirements
- Python 3.7+
- numpy
- pillow

Install dependencies with:
```bash
pip install numpy pillow
```

## Usage
1. **Clone the repository:**
   ```bash
   git clone https://github.com/tranhao-wq/Python-handle-image-data-processing-and-render-wallpapers.git
   cd Python-handle-image-data-processing-and-render-wallpapers
   ```
2. **(Optional) Create and activate a virtual environment:**
   ```bash
   python -m venv .venv
   # On Windows:
   .venv\Scripts\activate
   # On Unix/Mac:
   source .venv/bin/activate
   ```
3. **Install dependencies:**
   ```bash
   pip install numpy pillow
   ```
4. **Run the script:**
   ```bash
   python generate_wallpaper_advanced.py
   ```
   The script will automatically generate 10 unique wallpapers with random themes.

## Output
- All generated wallpapers are saved in the `output_wallpapers` folder.
- Each file is named as `wallpaper_<theme>_<timestamp>.png`.

## Customization
- You can add new themes or adjust parameters in the `THEMES` dictionary inside `generate_wallpaper_advanced.py`.
- To change the number of wallpapers generated, modify the loop in the `__main__` section.

## Example Themes
- **ocean_waves**: Deep blue and cyan wave patterns.
- **sunset_dunes**: Warm, sandy, sunset-inspired colors.
- **aurora_sky**: Cool, vibrant aurora-like streaks.
- **monochrome**: Elegant grayscale abstract waves.

## License
This project is open source and free to use for personal and educational purposes.

---

Inspired by modern abstract wallpapers and creative coding. 