# Avis Drone Labs - Vulcan Project

This repository holds my work for the **Avis Drone Labs - Vulcan Project**, focused on developing a computer vision solution for search and rescue missions using drones.

## Project Overview

The goal of the Vulcan Project is to leverage drones equipped with advanced machine learning models to detect human shapes from a bird's-eye view. This project will aid in search and rescue operations, enhancing efficiency and safety in critical missions.

### Key Components
1. **YOLOv8 Classification Model**  
   - A YOLOv8 model has been trained to detect human shapes from aerial footage (bird's-eye view). This is particularly useful in identifying people in difficult-to-reach areas during search and rescue missions.
   - The YOLOv8 model is integrated with the **OpenCV** Python library to perform image classification tasks.

2. **Color Thresholding Algorithm (Debatable Redundancy)**  
   - A color thresholding algorithm was introduced, though its necessity is still under debate.  
   - **Purpose:** It could serve as a redundancy system for detecting people based on clothing color (e.g., a person wearing a red jacket).  
   - **Current Status:** The YOLOv8 model appears promising without requiring early-stage color manipulation from the camera feed, though the color thresholding may remain as a fallback.

3. **Displacement Vector Calculation**  
   - Currently working on calculating the **displacement vector** from the center of the image to the bounding box of the classified object (human) in the image frame.
   - This vector will be communicated to **ArduPilot** using **pymavlink** to guide the drone towards the detected human.

## Technologies Used

- **YOLOv8**: Deep learning model for object detection and classification.
- **OpenCV**: Open-source computer vision library for image processing and analysis.
