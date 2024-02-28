# Comment-Toxicity-Prediction-App
deployed app link :https://comment-toxicity-prediction-app-hbzrx2phmufwb6j6f48qkm.streamlit.app/


DEMO video link: https://drive.google.com/file/d/1pTa2drGenWWnV8Zt05eltUEJS0I2D6p9/view?usp=sharing


# Comment Toxicity Prediction App

## Overview

This project, the "Comment-Toxicity-Prediction-App," utilizes a machine learning algorithm known as Naive Bayes for predicting the toxicity of comments. The model calculates the probability of a comment falling into categories such as toxic, severe toxic, obscene, insult, threat, identity hate, etc.

## Machine Learning Model

The toxicity prediction model is built using the Naive Bayes algorithm. This algorithm is commonly used for text classification tasks, making it suitable for analyzing and categorizing comments based on their toxicity levels. The model has been trained on a labeled dataset to make predictions on new comments.

## Prediction Categories

The model categorizes comments into the following toxicity levels:

- Toxic
- Severe Toxic
- Obscene
- Insult
- Threat
- Identity Hate

## Usage

To use the Comment Toxicity Prediction App, follow these steps:

1. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

2. Run the Streamlit app:

   ```bash
   streamlit run app.py
   ```

3. Open the provided URL in your web browser to access the app.

4. Enter a comment in the input field, and the app will provide the predicted probabilities for each toxicity category.

##Sample output:

###Good Comment
.
.
![good comment](https://github.com/adnanpatel878/Comment-Toxicity-Prediction-App/assets/105789120/9f2c5e63-189b-4d4c-a224-307e983dd877)


###Bad Comment
.
.
![bad comment](https://github.com/adnanpatel878/Comment-Toxicity-Prediction-App/assets/105789120/543e1d71-6cbc-48d9-8ddc-df36446201de)


   



