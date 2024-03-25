# Diabetes Prediction Model with Logistic Regression

---

### Overview:

This repository contains a machine learning model built using logistic regression to predict whether a person has diabetes or not based on input features. The model utilizes regularization, GridCV for hyperparameter tuning, k-fold cross-validation, and all available features from the diabetes dataset.

### Dataset:

The dataset used for training the model is the Diabetes dataset, which is publicly available and widely used for predictive modeling tasks. Exploratory Data Analysis (EDA) has been performed on the dataset to gain insights into its structure, distribution, and relationships between variables.

### Model Building:

The model is built using logistic regression, a commonly used algorithm for binary classification tasks. Regularization techniques (L1 and L2) are applied to prevent overfitting and improve generalization performance. GridCV is used for hyperparameter tuning to find the optimal values of regularization strength and other parameters.

### Web Application:

A Flask-based web application has been developed to provide a user-friendly interface for predicting diabetes based on user input. The deployed web app allows users to input relevant features (e.g., glucose level, BMI, blood pressure) and obtain predictions from the trained logistic regression model.

### Repository Structure:

- **/data:** Contains the dataset used for model training and testing.
- **/notebooks:** Includes Jupyter notebooks for Exploratory Data Analysis (EDA) and model development.
- **/models:** Stores the trained logistic regression model and any associated files.
- **/web_app:** Contains the Flask-based web application files for user interaction and prediction.
- **/requirements.txt:** Lists all dependencies required to run the web application.
- **README.md:** Provides an overview of the project, instructions for running the web application, and other relevant information.

### Usage:

To run the web application locally:

1. Clone this repository to your local machine.
2. Navigate to the `root` directory.
3. Install dependencies using `pip install -r requirements.txt`.
4. Run the Flask application using `python app.py`.
5. Access the web application in your browser at the specified URL.

### Deployment:

The web application has been deployed on Render for easy access and usage. Users can access the deployed application through the provided URL and interact with the model to predict diabetes based on their input.

### Contributors:

-[ Damodar Yadav ](https://github.com/daemonX10)


### License:

This project is licensed under the MIT License - see the `LICENSE` file for details and permissions granted to users and contributors of the project code and resources used in the repository for educational and research purposes only and not for commercial use or distribution without permission from the author or owner of the repository and its contents or resources used in the project development. 

### Acknowledgments:

Special thanks to Krish Naik and CourseX.

