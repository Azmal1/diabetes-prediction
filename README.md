🩺 Diabetes Prediction Project Documentation
🧾 Overview
This project predicts the likelihood of diabetes in a patient using a machine learning model based on health parameters. It uses the Logistic Regression algorithm and is built with Python and Streamlit for an interactive web interface.

🛠️ Tools & Libraries Used
Python

Pandas, NumPy, Scikit-learn (for data handling and machine learning)

Streamlit (for frontend UI)

VS Code (as the IDE)

Git & GitHub (for version control)

📂 Dataset Description (diabetes.csv)
The dataset contains health-related metrics:

Feature	Description
Pregnancies	Number of pregnancies
Glucose	Plasma glucose concentration
Blood Pressure	Diastolic blood pressure (mm Hg)
Skin Thickness	Triceps skin fold thickness (mm)
Insulin	2-Hour serum insulin (mu U/ml)
BMI	Body Mass Index
Diabetes Pedigree Function	Likelihood based on family history
Age	Age of the patient
Outcome	0 = Non-Diabetic, 1 = Diabetic

🔬 How to Train the Model (Run Once)
🔻 Step-by-Step Commands:

# Step 1: Navigate to your project directory
cd path/to/diabetes_prediction_project

# Step 2: Run the training script
python train_model.py

🌐 How to Run the Web Application
🔻 Step-by-Step Commands:

# Step 1: (One-time) Install required Python libraries
pip install pandas numpy scikit-learn streamlit

# Step 2: Run the Streamlit web app
streamlit run app.py
🔢 Prediction Algorithm Used
Logistic Regression – A binary classification method used to predict whether a person is diabetic (1) or not diabetic (0) based on their input values.

🧪 Sample Input Data
To test the app, you can enter the following in the UI:

Pregnancies: 2

Glucose: 120

Blood Pressure: 70

Skin Thickness: 20

Insulin: 85

BMI: 25.0

Diabetes Pedigree Function: 0.5

Age: 30


