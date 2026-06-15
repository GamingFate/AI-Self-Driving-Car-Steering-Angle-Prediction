# 📊 Results & Performance Analysis

This directory contains the experimental results, training visualizations, performance analysis, and autonomous driving outputs generated during the development of the **AI-Based Self-Driving Car Simulator for Steering Angle Prediction Using Computer Vision and Deep Learning**.

The objective of these experiments was to evaluate the model's ability to learn steering behavior from human driving demonstrations and perform autonomous navigation within the Udacity Self-Driving Car Simulator.

---

# 📁 Directory Contents

| File                                               | Description                                                             |
| -------------------------------------------------- | ----------------------------------------------------------------------- |
| `MSE vs EPOCH curve.png`                           | Training and validation loss curves during model training               |
| `MSE vs Epoch curve demonstrating overfitting.png` | Visualization of overfitting behavior and model generalization analysis |
| `Implementation Pipeline.png`                      | Complete training and deployment workflow                               |
| `Autonomous Driving.png`                           | Autonomous driving results inside the simulator                         |

---

# 📈 Training Loss Analysis

The model was trained using the Mean Squared Error (MSE) loss function, which measures the difference between predicted steering angles and ground truth steering angles.

![Training Loss Curve](MSE%20vs%20EPOCH%20curve.png)

### Observations

* Training loss decreases consistently throughout training.
* Validation loss follows a similar trend, indicating effective learning.
* The model successfully learns meaningful driving behavior from the dataset.
* Stable convergence suggests successful optimization using the Adam optimizer.

---

# 📉 Overfitting Analysis

Deep learning models can suffer from overfitting when they memorize training data rather than learning generalized driving behavior.

The following figure demonstrates model performance under overfitting conditions.

![Overfitting Analysis](MSE%20vs%20Epoch%20curve%20demonstrating%20overfitting.png)

### Mitigation Techniques Used

* Dataset balancing
* Data augmentation
* Horizontal image flipping
* Dropout regularization
* Multi-track training data

These techniques improved model generalization and reduced prediction bias.

---

# 🔄 Implementation Pipeline

The complete workflow used during project development is shown below.

![Implementation Pipeline](Implementation%20Pipeline.png)

### Pipeline Stages

1. Driving Data Collection
2. Dataset Balancing
3. Data Augmentation
4. Image Preprocessing
5. CNN Training
6. Model Validation
7. Real-Time Inference
8. Autonomous Driving

This pipeline forms the foundation of the end-to-end behavioral cloning system.

---

# 🚗 Autonomous Driving Performance

The trained model was deployed inside the Udacity Self-Driving Car Simulator for real-time autonomous navigation.

![Autonomous Driving](Autonomous%20Driving.png)

### Performance Highlights

* Successful lane following behavior
* Real-time steering angle prediction
* Stable vehicle control
* Smooth steering transitions
* Effective navigation across simulator tracks

The model demonstrates that end-to-end deep learning approaches can learn driving behavior directly from camera images without manually engineered lane detection algorithms.

---

# 💡 Key Findings

* The NVIDIA CNN architecture effectively learns steering behavior from visual inputs.
* Dataset balancing significantly improves turning performance.
* Data augmentation enhances robustness and generalization.
* Steering smoothing improves driving stability during deployment.
* Behavioral cloning provides a practical approach for autonomous navigation in simulated environments.

---

# 🏁 Conclusion

The experimental results demonstrate the effectiveness of deep learning-based behavioral cloning for steering angle prediction. The trained model successfully learned driving behavior from human demonstrations and was capable of autonomously navigating the simulator environment in real time.

These findings highlight the potential of end-to-end computer vision systems for autonomous driving research and intelligent transportation applications.

---

## ⭐ Key Achievements

* End-to-End Autonomous Driving System
* NVIDIA Behavioral Cloning CNN
* Real-Time Steering Prediction
* Autonomous Simulator Navigation
* Dataset Balancing & Augmentation
* TensorFlow & Keras Implementation
* Stable Training Convergence
* Successful Deployment in Udacity Simulator
