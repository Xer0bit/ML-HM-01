
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageDraw
from PPImage import ImagePP
import tensorflow as tf
import numpy as np
import os

model = tf.keras.models.load_model('Saved-Models/model.h5')

if model is None:
    print("Model not found")
else:
    print("Model loaded")


# Create a function to insert an image
def insert_image():
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png *.jpg *.jpeg *.gif *.bmp *.ppm")])
    if file_path:
        # Insert the image into the window
        print("Selected image:", file_path)
        # image = Image.open(file_path)
        image = ImagePP(file_path)
        predictions = model.predict(image)
        # Get the predicted class
        predicted_class = np.argmax(predictions)
        print("Predicted digit:", predicted_class)
        #create a new window that show the predicted digit
        root2 = tk.Tk()
        root2.title("Predicted Digit")
        root2.geometry("700x200")
        label = tk.Label(root2, text="Predicted Digit: " + str(predicted_class), font=("Arial Bold", 50))
        label.pack(fill=tk.BOTH, expand=True)
        root2.mainloop()
    else:
        print("No image selected")
        
# Create a function to create an image
def create_image():
    os.system("python3 paint.py")
    root.destroy()
    os.system("python3 main.py")

# Create the main application window
root = tk.Tk()
root.title("Image Operations")

# Create Insert Image and Create Image buttons
insert_button = tk.Button(root, text="Insert Image", command=insert_image)
create_button = tk.Button(root, text="Create Image", command=create_image)

# Pack the buttons into the window
insert_button.pack()
create_button.pack()

# Start the main application loop
root.mainloop()
