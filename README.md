# ChurnXplorer - Real-time Customer Churn Prediction Web Application 📈📊

ChurnXplorer is a powerful web application built on top of three machine learning models;CatBoost Classifier, Stochastic Gradient Boosting Classsifier and Logistic Regression Classifier model, designed to predict customer churn. It provides businesses with real-time insights into customer retention and helps optimize customer management strategies 💼💰🤖

## Table of Contents 📚

- [Introduction](#introduction) 📝
- [Features](#features) ✨
- [Demo](#demo) 🚀
- [Getting Started](#getting-started) 🏁
  - [Installation](#installation) 🛠️
  - [Running the App](#running-the-app) 🏃
- [App Structure](#app-structure) 🧱
- [Usage](#usage) 📊
  - [Making Predictions](#making-predictions) 📈
- [Technologies Used](#technologies-used) 💻🔬
- [Contributing](#contributing) 🤝🙌
- [License](#license) 📜

## Introduction 🚀

ChurnXplorer uses a state-of-the-art models(CatBoost,Logistic Regression and SGB models) to predict customer churn. It offers a user-friendly interface for inputting customer data and receiving instant churn predictions.

## Features ✨

- View Data - Allows you to view data 
- Predict - Feature that allows to make single prediction or predict your csv data in bulk
- View History - Allows you to view the history of your predictions
- Dashboard - View data visualizations

## Demo 🚀

- ### Pictures 📸
  | ![app header](utils\app-screenshots\Screenshot 2024-06-24 221230.png)| ![more cus info](https://p4-churn-detector-embedding-ml-models-in.onrender.com)|
  | --------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  |![submit and pred](utils\app-screenshots\Screenshot 2024-06-24 221524.png)| ![pred](https://p4-churn-detector-embedding-ml-models-in.onrender.com/Predict)|

- ### Article Link 🌐
  [Read Article](https://medium.com/@adubrightkwarrteng11/churnxplorer-e5af00c55cb6)

## Getting Started 🏁

Follow these instructions to get the app up and running on your local machine.

### Installation 🛠️

1. Clone the repository:

   ```bash
   git clone https://github.com/adubrightkwartengsnr/P4-Churn-Detector-Embedding-ML-models-in-Web-framework-Streamlit
   cd P4-Churn-Detector-Embedding-ML-models-in-Web-framework-Streamlit
   ```

2. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

### Running the App 🏃

Run the Streamlit app using the following command:

```bash
python src/app/app.py
```

Access the app through your web browser at `http://localhost:8501/`.

## App Structure 🧱

- `Home.py`: file is the entry point to the application/main scripts `Home.py`.
- `pages/`: Directory pages directory contains all the pages files.
- `data/`: Directory stores the data used for the application.
- `models/`: Directory for storing the pre-trained models and the encoder.
- `utils/`: Directory containing all other utility files.

## Usage 📊

### Making Predictions 📈

1. Fill in the customer data in the required fields.
2. Click the "Make Predictions" button to receive a real-time churn prediction.

## Technologies Used 💻🔬

- Streamlit: Python framework for building interactive interfaces for data science applications.
- Pandas: Data manipulation and analysis library.
- Scikit-Learn: Machine learning library.
- Plotly: an open-source module of Python that is used for data visualization and supports various graphs like line charts, scatter plots, bar charts, histograms, area plots, etc. Plotly produces interactive graphs, can be embedded on websites, and provides a wide variety of complex plotting options.

## Contributing 🤝🙌

Contributions to the ChurnXplorer project are welcome. Please follow these guidelines for contributing:

1. Fork the repository.
2. Create a new branch for your feature or bug fix: `git checkout -b feature-name`
3. Make your changes and commit them with clear, concise commit messages.
4. Push your changes to your fork.
5. Create a pull request against the main repository.

## License📜

This project is licensed under the [MIT License](LICENSE).

## Author✍️

Bright Kwarteng Senior Adu

Connect with me on LinkedIn: [LinkedIn Profile](https://www.linkedin.com/in/bright-adu-kwarteng-snr)

---

Feel free to star ⭐ this repository if you find it helpful!
