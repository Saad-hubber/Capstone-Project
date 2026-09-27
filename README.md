# Capstone-Project
This is a code that predicts the possible sleep disorder of an individual by using decision trees
# Sleep Disorder Prediction App

This is a machine learning web application that predicts the likelihood of a sleep disorder based on demographic, lifestyle, and health-related information!!!

## Overview

This project uses a **Decision Tree Classifier** to classify individuals into one of three categories:

* No Sleep Disorder
* Insomnia
* Sleep Apnea

The model was trained on sleep and health-related features including sleep duration, sleep quality, stress level, physical activity, heart rate, daily steps, BMI category, occupation, and blood pressure.

## Machine Learning Model

The project uses a **Decision Tree Classifier** with the following configuration:

* `max_depth = 3`
* `random_state = 42`
* Train/Test Split: 80/20

### Model Performance

| Metric             |  Score |
| ------------------ | -----: |
| Accuracy           | 93.33% |
| Weighted Precision | 93.54% |
| Weighted Recall    | 93.33% |
| Weighted F1-score  | 93.34% |


## Features

The model uses:

* Age
* Sleep Duration
* Quality of Sleep
* Physical Activity Level
* Stress Level
* Heart Rate
* Daily Steps
* Gender
* Occupation
* BMI Category
* Systolic Blood Pressure
* Diastolic Blood Pressure

Categorical variables were converted into numerical features using one-hot encoding.

## Tech Stack
**The libraries used in this project were:**

* Python
* Pandas
* NumPy
* Scikit-learn
* Matplotlib
* Seaborn
* Joblib
* HTML
* CSS
* JavaScript
* Vercel


## Working

1. The user enters their health, lifestyle, and demographic information.
2. The application preprocesses the inputs in the same way as the training data.
3. The trained Decision Tree model processes the inputs.
4. The model returns one of the three sleep-disorder classifications.
5. The prediction is displayed through the web interface.


