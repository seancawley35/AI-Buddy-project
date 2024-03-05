#pip install Pillow

from PIL import Image
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

# Paths to the image layers. Each layer should be a transparent PNG.
face_shapes = ["face1.png", "face2.png", "face3.png"]
eye_types = ["eyes1.png", "eyes2.png", "eyes3.png"]
mouth_types = ["mouth1.png", "mouth2.png", "mouth3.png"]
hair_styles = ["hair1.png", "hair2.png", "hair3.png"]

# Function to create an avatar
def create_avatar(face, eyes, mouth, hair):
    # Start with the face shape
    avatar = Image.open(face_shapes[face])

    # Add eyes
    eyes_img = Image.open(eye_types[eyes])
    avatar.paste(eyes_img, (0, 0), eyes_img)

    # Add mouth
    mouth_img = Image.open(mouth_types[mouth])
    avatar.paste(mouth_img, (0, 0), mouth_img)

    # Add hair
    hair_img = Image.open(hair_styles[hair])
    avatar.paste(hair_img, (0, 0), hair_img)

    return avatar

# Function to update the avatar preview
def update_preview(*args):
    avatar = create_avatar(face_var.get(), eyes_var.get(), mouth_var.get(), hair_var.get())
    avatar_image = ImageTk.PhotoImage(avatar)
    preview_label.configure(image=avatar_image)
    preview_label.image = avatar_image

# Set up the main application window
root = tk.Tk()
root.title("Avatar Generator")

# Create variables to hold the feature choice
face_var = tk.IntVar(value=0)
eyes_var = tk.IntVar(value=0)
mouth_var = tk.IntVar(value=0)
hair_var = tk.IntVar(value=0)

# Create the dropdown menus for feature selection
face_menu = ttk.Combobox(root, textvariable=face_var, values=list(range(len(face_shapes))))
eyes_menu = ttk.Combobox(root, textvariable=eyes_var, values=list(range(len(eye_types))))
mouth_menu = ttk.Combobox(root, textvariable=mouth_var, values=list(range(len(mouth_types))))
hair_menu = ttk.Combobox(root, textvariable=hair_var

