import gradio as gr
import face_recognition
import os
from PIL import Image

def compare_faces_in_folder(known_image_path, folder_path, tolerance=0.6):
    # Load the known image and encode its face
    known_image = face_recognition.load_image_file(known_image_path)
    known_encoding = face_recognition.face_encodings(known_image)[0]

    # Initialize an empty list to store matching image filenames
    matching_images = []

    # Iterate through every file in the folder
    for file in os.listdir(folder_path):
        if file.endswith(".jpg") or file.endswith(".png"):
            # Load the image from the folder
            unknown_image = face_recognition.load_image_file(os.path.join(folder_path, file))

            # Attempt to locate faces in the image and get their encodings
            try:
                unknown_encoding = face_recognition.face_encodings(unknown_image)[0]
            except IndexError:
                continue

            # Compare faces
            results = face_recognition.compare_faces([known_encoding], unknown_encoding, tolerance=tolerance)

            # If a match was found, add the filename to the list
            if results[0]:
                matching_images.append(file)

    return matching_images

def search_faces(folder_path, known_image):
    # Save the known image to a temporary file
    known_image_path = "temp_known_image.jpg"
    known_image.save(known_image_path)

    # Perform face comparison
    matching_images = compare_faces_in_folder(known_image_path, folder_path)

    # Load and return the matching images
    matching_pics = [Image.open(os.path.join(folder_path, img)) for img in matching_images]

    return matching_images, matching_pics

with gr.Blocks() as demo:
    folder_path = gr.Textbox(label="Folder Path", placeholder="Enter the path to the folder containing images")
    known_image = gr.Image(label="Upload Sample Image", type="pil")
    search_button = gr.Button("Search for Matching Faces")

    matching_images = gr.Textbox(label="Matching Image Filenames", interactive=False)
    matching_pics = gr.Gallery(label="Matching Images", columns=3, object_fit="contain")

    search_button.click(search_faces, inputs=[folder_path, known_image], outputs=[matching_images, matching_pics])

demo.launch()
