import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

df = pd.read_csv("Sleep_health_and_lifestyle_dataset.csv")
df['Sleep Disorder'] = df['Sleep Disorder'].fillna('None')

df = pd.get_dummies(
    df,
    columns=["Gender", "Occupation", "BMI Category"],
    drop_first=True,
    dtype=int
)
df[["Systolic BP", "Diastolic BP"]] = (
    df["Blood Pressure"]
    .str.split("/", expand=True)
    .astype(int)
)

X = df.drop(
    columns=["Person ID", "Sleep Disorder", "Blood Pressure"]
)

y = df["Sleep Disorder"]

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# Train Decision Tree
tree = DecisionTreeClassifier(
    max_depth=3,
    random_state=42
)

tree.fit(X_train, y_train)



st.title("Sleep Disorder Prediction")
st.write(
    "Enter the person's information below to predict "
    "their sleep disorder."
)

st.divider()


age = st.number_input(
    "Age",
    min_value=1,
    max_value=100,
    value=30
)

gender = st.selectbox(
    "Gender",
    ["Male", "Female"]
)

occupation = st.selectbox(
    "Occupation",
    [
        "Doctor",
        "Engineer",
        "Lawyer",
        "Manager",
        "Nurse",
        "Sales Representative",
        "Salesperson",
        "Scientist",
        "Software Engineer",
        "Teacher"
    ]
)

sleep_duration = st.number_input(
    "Sleep Duration (hours)",
    min_value=0.0,
    max_value=24.0,
    value=7.0,
    step=0.1
)

quality_of_sleep = st.slider(
    "Quality of Sleep",
    min_value=1,
    max_value=10,
    value=6
)

physical_activity = st.number_input(
    "Physical Activity Level",
    min_value=0,
    max_value=200,
    value=50
)

stress_level = st.slider(
    "Stress Level",
    min_value=1,
    max_value=10,
    value=5
)

bmi_category = st.selectbox(
    "BMI Category",
    [
        "Normal Weight",
        "Obese",
        "Overweight"
    ]
)

blood_pressure = st.text_input(
    "Blood Pressure",
    value="120/80"
)

heart_rate = st.number_input(
    "Heart Rate",
    min_value=30,
    max_value=200,
    value=70
)

daily_steps = st.number_input(
    "Daily Steps",
    min_value=0,
    max_value=50000,
    value=5000
)




if st.button("Predict Sleep Disorder"):

    try:

       
        systolic, diastolic = blood_pressure.split("/")

        systolic = int(systolic)
        diastolic = int(diastolic)

        new_data = pd.DataFrame({
            "Age": [age],
            "Sleep Duration": [sleep_duration],
            "Quality of Sleep": [quality_of_sleep],
            "Physical Activity Level": [physical_activity],
            "Stress Level": [stress_level],
            "Heart Rate": [heart_rate],
            "Daily Steps": [daily_steps],

            "Gender_Male": [
                1 if gender == "Male" else 0
            ],

            "Occupation_Doctor": [
                1 if occupation == "Doctor" else 0
            ],
            "Occupation_Engineer": [
                1 if occupation == "Engineer" else 0
            ],
            "Occupation_Lawyer": [
                1 if occupation == "Lawyer" else 0
            ],
            "Occupation_Manager": [
                1 if occupation == "Manager" else 0
            ],
            "Occupation_Nurse": [
                1 if occupation == "Nurse" else 0
            ],
            "Occupation_Sales Representative": [
                1 if occupation == "Sales Representative" else 0
            ],
            "Occupation_Salesperson": [
                1 if occupation == "Salesperson" else 0
            ],
            "Occupation_Scientist": [
                1 if occupation == "Scientist" else 0
            ],
            "Occupation_Software Engineer": [
                1 if occupation == "Software Engineer" else 0
            ],
            "Occupation_Teacher": [
                1 if occupation == "Teacher" else 0
            ],

            "BMI Category_Normal Weight": [
                1 if bmi_category == "Normal Weight" else 0
            ],
            "BMI Category_Obese": [
                1 if bmi_category == "Obese" else 0
            ],
            "BMI Category_Overweight": [
                1 if bmi_category == "Overweight" else 0
            ],

            "Systolic BP": [systolic],
            "Diastolic BP": [diastolic]
        })

       
        new_data = new_data[X.columns]

    
        prediction = tree.predict(new_data)[0]

        st.success(
            f"Predicted Sleep Disorder: {prediction}"
        )

    except ValueError:
        st.error(
            "Please enter blood pressure in the format "
            "120/80."
        )
