# RTD - Roblox Texture Dowloader
<p align="center">
    <img src="https://skillicons.dev/icons?i=py" />
</p>
Roblox Texture Downloader (RTD) is a lightweight Python-based GUI application that allows users to download Roblox asset thumbnails by simply entering their asset ID.<br/>
It uses Roblox’s public thumbnail API and provides an instant preview before saving the texture locally.

# Key Features
- Simple Interface – Minimal, intuitive UI using `tkinter`.
- Live Preview – Displays the texture thumbnail before saving.
- Error Handling – Built-in validation and error messaging for invalid IDs or missing assets.
- Automatic Saving – Downloads and saves the texture as a `.png` file in the local directory.
- Lightweight & Fast – No installation required beyond Python and a few dependencies.
# How To Use
1. Make sure you have Python 3.7+ installed.
2. Install required dependencies with:<br/>
`pip install pillow requests`
3. Run the script:<br/>
`python rtd.py`
4.In the application window:
- Enter a valid Roblox Asset ID.
- Click "Download Texture".
- A preview will appear, and the image will be saved locally as `texture_<ID>.png`.

# Credits
- Developed by: [Klaudiusz Wojtyczka](https://github.com/DragoCam) & [Nightzy](https://github.com/NightzyStudios)
- Libraries Used:
- [Tkinter](https://docs.python.org/3/library/tkinter.html)
- [Pillow (PIL)](https://pillow.readthedocs.io/)
- [Requests](https://docs.python-requests.org/)
