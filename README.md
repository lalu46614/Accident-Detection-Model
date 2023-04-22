# Accident-Detection-Model
Accident Detection Model is made using YOLOv8, Google Collab, Python, Roboflow, Deep Learning, OpenCV, Machine Learning, Artificial Intelligence. This model can detect an accident on any image or video provided. This model is trained on a dataset of 1200+ images, These images were annotated on roboflow.

## Problem Statement
- Road accidents are a major problem in India, with thousands of people losing their lives and many more suffering serious injuries every year. 
- According to the Ministry of Road Transport and Highways, India witnessed around 4.5 lakh road accidents in 2019, which resulted in the deaths of more than 1.5 lakh people. 
- The age range that is most severely hit by road accidents is 18 to 45 years old, which accounts for almost 67 percent of all accidental deaths.

## Accidents survey 
![image](https://user-images.githubusercontent.com/78155393/233774342-287492bb-26c1-4acf-bc2c-9462e97a03ca.png)

## Literature Survey
- Sreyan Ghosh in Mar-2019, The goal is to develop a system using deep learning convolutional neural network that has been trained to identify video frames as accident or non-accident.
- Deeksha Gour Sep-2019, uses computer vision technology, neural networks, deep learning, and various approaches and algorithms to detect objects.

## Research Gap
- Lack of real-world data - We trained model for more then 1200 images.
- Large interpretability time and space needed - Using google collab to reduce interpretability time and space required.
- Outdated Versions of previous works - We aer using Latest version of Yolo v8.

## Proposed methodology
- We are using Yolov8 to train our custom dataset which has been 1200+ images, collected from different platforms.
- This model after training with 25 iterations and is ready to detect an accident with a significant probability.

## Model Set-up
- Preparing Custom dataset - We have collected over 1200 images. We have annotated all of them individually on roboflow and then downloaded in yolov8 format.
- Using Google Collab - Further We have used Google collab to code and train the model for time and space optimization.
- Coding - We installed Yolov8 , connected our google drive account, created the data.yaml file containing classes and path for train, val, test images path.
- Finally we used the Yolo commands to train our model on the data set of train folder.

## Results
- Accident detection demo.mp4 is Live accident detection on a video by this model 
![image](https://user-images.githubusercontent.com/78155393/233783477-bf31573d-2bd7-4e3c-bb06-dc1c151fb072.png)

## Way Forward
- This Model can be implemented in the cameras placed on highway Pol with the help of an iot device in camera it can be used to report to the nearest control room.
- This model can also be transformed into an open source web application using Frameworks like Flask which can be used by anyone to cross check any image to know about if any accident occured in it.
