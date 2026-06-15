# 💻 Source Code

This directory contains the implementation files used for training, validating, and deploying the autonomous driving model developed for the project **"AI-Based Self-Driving Car Simulator for Steering Angle Prediction Using Computer Vision and Deep Learning."**

The source code covers the complete workflow from dataset preparation and model training to real-time autonomous vehicle control inside the Udacity Self-Driving Car Simulator.

---

# 📁 Directory Contents

| File        | Description                                                                          |
| ----------- | ------------------------------------------------------------------------------------ |
| `train.py`  | Training pipeline for the NVIDIA CNN steering angle prediction model                 |
| `drive.py`  | Real-time autonomous driving server used to control the vehicle inside the simulator |
| `README.md` | Documentation for the source code directory                                          |

---

# 🧠 train.py

The `train.py` script is responsible for training the steering angle prediction model using Behavioral Cloning techniques.

### Key Responsibilities

* Load driving datasets from multiple simulator tracks
* Combine and balance datasets
* Perform train-validation splitting
* Apply image preprocessing
* Perform data augmentation
* Build the NVIDIA CNN architecture
* Train the model using TensorFlow/Keras
* Generate loss visualizations
* Save the trained model

---

## Data Preprocessing

The following preprocessing operations are performed:

* Image resizing to **66 × 200**
* BGR to YUV color space conversion
* Pixel normalization
* Dataset balancing
* Horizontal image flipping

These techniques improve model robustness and generalization capability.

---

## Data Augmentation

To reduce overfitting and improve recovery behavior, the training pipeline includes:

* Horizontal image flipping
* Steering angle inversion after flipping
* Dataset balancing for turning scenarios

---

## Model Architecture

The project uses NVIDIA's Behavioral Cloning CNN architecture.

### Architecture Overview

* Input Normalization Layer
* 5 Convolution Layers
* ReLU Activations
* Dropout Layer
* Fully Connected Dense Layers
* Single Steering Angle Output

The network performs regression and predicts a continuous steering angle value.

---

## Training Configuration

| Parameter     | Value                    |
| ------------- | ------------------------ |
| Optimizer     | Adam                     |
| Learning Rate | 0.0001                   |
| Loss Function | Mean Squared Error (MSE) |
| Batch Size    | 32                       |
| Epochs        | 25                       |

---

# 🚗 drive.py

The `drive.py` script is responsible for deploying the trained model and performing real-time autonomous driving inside the Udacity simulator.

The script establishes communication between the simulator and the trained deep learning model using Flask and Socket.IO.

---

## Key Responsibilities

* Load the trained CNN model
* Receive camera images from the simulator
* Preprocess incoming frames
* Predict steering angles
* Apply steering smoothing
* Generate throttle commands
* Send control signals back to the simulator

---

## Real-Time Inference Pipeline

```text
Simulator Camera Feed
          │
          ▼
Image Preprocessing
          │
          ▼
CNN Model Prediction
          │
          ▼
Steering Angle Output
          │
          ▼
Steering Smoothing
          │
          ▼
Throttle Control
          │
          ▼
Vehicle Movement
```

---

## Steering Smoothing

To improve driving stability, the predicted steering angle is smoothed using previous predictions.

Benefits include:

* Reduced steering oscillations
* Smoother lane following
* Improved vehicle stability
* Better autonomous driving performance

---

## Dynamic Throttle Control

The deployment pipeline includes adaptive throttle control based on vehicle speed.

### Behavior

* Higher throttle at low speeds
* Moderate throttle during normal driving
* Reduced throttle at higher speeds

This helps maintain stable vehicle movement within the simulator.

---

# ⚙️ Technologies Used

### Deep Learning

* TensorFlow
* Keras

### Computer Vision

* OpenCV
* NumPy

### Backend & Deployment

* Flask
* Socket.IO
* Eventlet

### Data Processing

* Pandas
* Scikit-Learn

### Visualization

* Matplotlib

---

# 🔄 End-to-End Workflow

```text
Driving Dataset
        │
        ▼
Preprocessing & Augmentation
        │
        ▼
CNN Training
        │
        ▼
Model Validation
        │
        ▼
Model Export
        │
        ▼
Real-Time Deployment
        │
        ▼
Autonomous Driving
```

---

# 🎯 Purpose

The source code demonstrates the implementation of an end-to-end autonomous driving system capable of learning steering behavior directly from camera images using deep learning.

The project showcases practical applications of:

* Computer Vision
* Deep Learning
* Behavioral Cloning
* Autonomous Driving
* Real-Time AI Systems

within a simulated self-driving vehicle environment.
