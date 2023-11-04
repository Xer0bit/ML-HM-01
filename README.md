# Image Operations Application

This Python application allows you to perform image operations using a graphical user interface (GUI). It provides two main features: inserting an image and creating an image. The inserted image is used to make predictions using a pre-trained deep learning model.

## Prerequisites

Before using this application, ensure that you have the required Python libraries installed. You can use the `requirements.txt` file to install these dependencies using `pip`.

```bash
pip install -r requirements.txt
```

Make sure you have Python 3.x installed on your system.
Usage

    To run the application, execute the following command:

```python main.py```

This will open a GUI window that allows you to insert an image and create an image.

    Click the "Insert Image" button to select an image file (e.g., PNG, JPG, JPEG, GIF, BMP, PPM) and make predictions using a pre-trained deep learning model. The predicted digit will be displayed in a new window.

    Click the "Create Image" button to create an image using the "paint.py" script. This image can be used for further operations.

Dependencies

The following Python libraries are required for this application. You can install them using the provided requirements.txt file:

    Pillow (PIL): Provides image processing capabilities.
    TensorFlow: Used for machine learning and deep learning tasks.
    NumPy: Provides support for numerical operations.

Files

    main.py: The main script that opens the GUI and controls the application.
    paint.py: A script for creating an image using a drawing interface.

Model

The application uses a pre-trained deep learning model to make predictions on inserted images. The model file is model.h5 located in the "Saved-Models" directory. If the model is not found, make sure it is present in the specified location.
License

This project is licensed under the MIT License. You can find more details in the LICENSE file.

Feel free to customize this README according to your project's specific details, such as installation instructions or additional documentation.
