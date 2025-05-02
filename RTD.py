import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import requests
from io import BytesIO

def download_thumbnail():
    texture_id = entry.get().strip()
    
    if not texture_id.isdigit():
        messagebox.showerror("Error", "Texture ID must be a number.")
        return

    # Roblox Thumbnail API
    api_url = f"https://thumbnails.roblox.com/v1/assets?assetIds={texture_id}&size=420x420&format=Png&isCircular=false"

    try:
        api_response = requests.get(api_url).json()
        data = api_response.get("data", [])

        if not data or not data[0].get("imageUrl"):
            messagebox.showerror("Error", "No thumbnail found for this ID.")
            return

        image_url = data[0]["imageUrl"]
        image_response = requests.get(image_url)
        image_response.raise_for_status()

        # Load and display image preview
        img_data = BytesIO(image_response.content)
        img = Image.open(img_data)
        img = img.resize((200, 200))  # Resize for GUI display
        photo = ImageTk.PhotoImage(img)

        # Update label with image
        preview_label.config(image=photo)
        preview_label.image = photo  # Keep a reference!

        # Save image to file
        filename = f"texture_{texture_id}.png"
        with open(filename, 'wb') as f:
            f.write(image_response.content)

        messagebox.showinfo("Success", f"Texture saved as {filename}")

    except Exception as e:
        messagebox.showerror("Error", f"Something went wrong: {e}")

# GUI setup
root = tk.Tk()
root.title("Roblox Texture Downloader")

label = tk.Label(root, text="Enter Texture/Asset ID:")
label.pack(pady=5)

entry = tk.Entry(root, width=30)
entry.pack(pady=5)

btn = tk.Button(root, text="Download Texture", command=download_thumbnail)
btn.pack(pady=10)

preview_label = tk.Label(root)  # Placeholder for the image preview
preview_label.pack(pady=10)

root.mainloop()
