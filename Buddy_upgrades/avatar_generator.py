#pip install Pillow

from PIL import Image

# Paths to the image layers. Each layer should be a transparent PNG.
face_shapes = ["face1.png", "face2.png", "face3.png"]
eye_types = ["eyes1.png", "eyes2.png", "eyes3.png"]
mouth_types = ["mouth1.png", "mouth2.png", "mouth3.png"]
hair_styles = ["hair1.png", "hair2.png", "hair3.png"]

# Function to create an avatar
def create_avatar(face, eyes, mouth, hair):
    # Start with the face shape
    avatar = Image.open(face)

    # Add eyes
    eyes_img = Image.open(eyes)
    avatar.paste(eyes_img, (0, 0), eyes_img)

    # Add mouth
    mouth_img = Image.open(mouth)
    avatar.paste(mouth_img, (0, 0), mouth_img)

    # Add hair
    hair_img = Image.open(hair)
    avatar.paste(hair_img, (0, 0), hair_img)

    return avatar

# Example usage: create an avatar with the first option from each feature
avatar = create_avatar(face_shapes[0], eye_types[0], mouth_types[0], hair_styles[0])
avatar.show()
