import os
import numpy as np
import pandas as pd
import cv2

train_csv = pd.read_csv('dataset/train.csv')
train_csv = train_csv[train_csv['Image'] != 'w_7489.jpg'] # one of the images specified in the dataframe is not present in the imgs folder, so remove it.
test_csv = pd.read_csv('dataset/sample_submission.csv')
test_image_names = test_csv['Image']

def load_train_images_to_dataframe(folder_path):
    # Initialize an empty list to store image information
    image_data = []

    # Get a list of all files in the folder
    files = os.listdir(folder_path)
    counter = 0
    # Iterate over each file
    for file_name in files:
        # Construct the full path to the file
        file_path = os.path.join(folder_path, file_name)
        
        # file_name_without_resized = file_name[8:]
        
        # To filter out the test images
        # if file_name_without_resized not in test_image_names.values:
        if file_name not in test_image_names.values:
            counter += 1
            # Read the image
            img = cv2.imread(file_path)
            
            # # Check if the image is loaded properly
            if img is None:
                print(f"Error: Image {file_name} not loaded!")
                continue
            
            image_data.append(img)

    # Create a DataFrame from the list of image information
    df = np.array(image_data)
    
    return df