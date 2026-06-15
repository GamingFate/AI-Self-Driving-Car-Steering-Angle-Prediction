# 🏗️ System Design & Architecture

This directory contains the architectural diagrams, conceptual designs, preprocessing workflows, and implementation visualizations used during the development of the **AI-Based Self-Driving Car Simulator for Steering Angle Prediction Using Computer Vision and Deep Learning**.

These diagrams provide a high-level understanding of the system's design, data flow, deep learning architecture, and autonomous driving pipeline.

---

# 📁 Directory Contents

| File                                         | Description                                              |
| -------------------------------------------- | -------------------------------------------------------- |
| `autonomous-driving-system-architecture.png` | Overall architecture of the autonomous driving system    |
| `behavioral-cloning.png`                     | Behavioral Cloning approach used for end-to-end learning |
| `cnn-model-architecture.jpg`                 | NVIDIA CNN architecture for steering angle prediction    |
| `camera-angles.png`                          | Multi-camera data collection setup                       |
| `data-preprocessing-pipeline.png`            | Image preprocessing and augmentation workflow            |
| `bgr-yuv-conversion.png`                     | Visualization of color space conversion from BGR to YUV  |
| `udacity-simulator.png`                      | Udacity Self-Driving Car Simulator environment           |

---

# 🚗 Autonomous Driving System Architecture

The complete autonomous driving pipeline consists of data acquisition, preprocessing, deep learning inference, and vehicle control modules.

![Autonomous Driving System Architecture](autonomous-driving-system-architecture.png)

### Key Components

* Simulator Camera Feed
* Image Processing Pipeline
* Steering Angle Prediction Network
* Vehicle Control Module
* Autonomous Navigation System

This architecture enables real-time end-to-end steering prediction directly from camera images.

---

# 🧠 Behavioral Cloning

Behavioral Cloning is an imitation learning technique where a neural network learns driving behavior directly from human demonstrations.

![Behavioral Cloning](behavioral-cloning.png)

### Concept

Instead of manually designing driving rules, the model learns:

* Lane following behavior
* Steering corrections
* Road navigation patterns
* Recovery behavior

by observing recorded driving sessions.

---

# 🔬 CNN Model Architecture

The project utilizes NVIDIA's Behavioral Cloning Convolutional Neural Network (CNN) architecture.

![CNN Architecture](cnn-model-architecture.jpg)

### Architecture Overview

* Input Normalization Layer
* Convolutional Feature Extraction Layers
* ReLU Activation Functions
* Dropout Regularization
* Fully Connected Dense Layers
* Steering Angle Regression Output

The network directly predicts steering angle values from road images.

---

# 📸 Camera Configuration

Data collection utilizes multiple camera viewpoints provided by the simulator.

![Camera Angles](camera-angles.png)

### Camera Positions

* Center Camera
* Left Camera
* Right Camera

Using multiple viewpoints improves recovery behavior and helps the model learn corrective steering actions.

---

# 🔄 Data Preprocessing Pipeline

Before training, images undergo several preprocessing operations to improve model learning.

![Data Preprocessing Pipeline](data-preprocessing-pipeline.png)

### Processing Steps

1. Data Collection
2. Dataset Cleaning
3. Image Resizing
4. Color Space Conversion
5. Dataset Balancing
6. Data Augmentation
7. Training Dataset Generation

These steps improve training stability and model generalization.

---

# 🎨 BGR to YUV Conversion

Color space conversion is an important preprocessing step in the project.

![BGR to YUV Conversion](bgr-yuv-conversion.png)

### Why YUV?

* Separates luminance from chrominance information
* Improves robustness to lighting variations
* Reduces unnecessary color dependencies
* Commonly used in autonomous driving research

The converted images are supplied directly to the CNN model during training.

---

# 🕹️ Udacity Self-Driving Car Simulator

The project uses the Udacity Self-Driving Car Simulator as the virtual testing environment.

![Udacity Simulator](udacity-simulator.png)

### Simulator Features

* Realistic road environments
* Multiple driving tracks
* Real-time vehicle control
* Camera-based data collection
* Autonomous driving evaluation

The simulator serves as the platform for both dataset generation and model validation.

---

# 🎯 Purpose of This Directory

The diagrams and visualizations contained in this directory provide insight into:

* System Architecture
* Deep Learning Pipeline
* Data Collection Process
* Image Preprocessing Workflow
* Neural Network Design
* Autonomous Driving Methodology

Together, they illustrate the complete engineering workflow used to develop the end-to-end self-driving car system.

---

## ⭐ Highlights

* End-to-End Behavioral Cloning System
* NVIDIA CNN Architecture
* Multi-Camera Data Collection
* Data Augmentation Pipeline
* Real-Time Steering Prediction
* Autonomous Driving Deployment
* Computer Vision-Based Navigation
