import torch
from ultralytics import YOLO

# Ensure proper multiprocessing handling on Windows
if __name__ == '__main__':
    # Load a model
    model = YOLO("yolo11m.pt")

    # Train the model
    train_results = model.train(
        data="paths.yaml",  # path to dataset YAML
        epochs=100,  # number of training epochs
        workers=1,  # number of dataloader workers
        imgsz=640,  # training image size
        device=0,  # device to run on, e.g., device=0 or device=cpu
    )
