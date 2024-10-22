import cv2
import os


directory = r"S:\Downloads\Vision\images\train"


for name in os.listdir(directory):
    file_path = os.path.join(directory, name)
    
    if name.lower().endswith(('.png', '.jpg', '.jpeg')):
        print(f"Processing image file: '{name}'")

        img_grayscale = cv2.imread(file_path, 0)
        cv2.imshow('Grayscale Image', img_grayscale)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    else:

        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            print(f"Content of '{name}'")
            print(f.read())
    print()
