# Photo-Lookalike

This project is a face recognition tool that searches for matching faces within a folder of images. It uses the `face_recognition` library to compare a known image with images in a specified folder and returns the filenames and the images that match the known image.

## Features

- Upload a sample image for face comparison.
- Specify a folder containing images to search for matching faces.
- Display filenames and images of the matches found.

## Requirements

- Python 3.x
- `face_recognition` library
- `gradio` library
- `PIL` (Python Imaging Library)

## Installation

1. Clone the repository:

```bash
git clone https://github.com/Nikil-D-Gr8/Photo-Lookalike.git
cd Photo_Lookalike
```

2. Install the required libraries:

```bash
pip install face_recognition gradio pillow
```

## Usage

1. Run the application:

```bash
python app.py
```

2. Open your web browser and go to the port in which the app is running usualy shown after the python code is executed..

3. Enter the path to the folder containing the images you want to search relative to the path of the python file or the absolute path in your system.

4. Upload the sample image for comparison.

5. Click the "Search for Matching Faces" button to start the search.

6. View the matching image filenames and images in the output section.

## Code Overview

### Function Definitions

- **compare_faces_in_folder(known_image_path, folder_path, tolerance=0.6)**:
  - Loads the known image and encodes its face.
  - Iterates through all images in the specified folder and encodes their faces.
  - Compares the known face encoding with each image in the folder.
  - Returns a list of filenames of the matching images.

- **search_faces(folder_path, known_image)**:
  - Saves the known image to a temporary file.
  - Calls `compare_faces_in_folder` to find matching images.
  - Loads and returns the matching images.

### Gradio Interface

- **folder_path**: Textbox to input the path to the folder containing images.
- **known_image**: Image component to upload the sample image for comparison.
- **search_button**: Button to trigger the search process.
- **matching_images**: Textbox to display the filenames of matching images.
- **matching_pics**: Gallery to display the matching images.


## Contributing

1. Fork the repository.
2. Create your feature branch: `git checkout -b feature/your-feature`.
3. Commit your changes: `git commit -m 'Add some feature'`.
4. Push to the branch: `git push origin feature/your-feature`.
5. Open a pull request.

## Acknowledgements

- [face_recognition](https://github.com/ageitgey/face_recognition) - The world's simplest facial recognition API for Python and the command line.
- [Gradio](https://gradio.app) - Create UIs for your machine learning model in Python.

Feel free to contribute and improve this project. For any issues or suggestions, please open an issue or create a pull request.

---

Happy coding!
