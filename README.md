# 🏥Health & Fitness web application
Web application: 
![image](https://github.com/user-attachments/assets/5419b247-14d6-4ffd-bc7c-417b2e71f373)
PCOS prediction:
![image](https://github.com/user-attachments/assets/460300f8-e7c7-4ea6-bc88-038dc0a9f43d)
Diet recommendation:
![image](https://github.com/user-attachments/assets/822b0bc3-c817-454a-a1ca-8c5d102768a0)
Exercise Recommendation:
![image](https://github.com/user-attachments/assets/e5ba31f4-27c2-498b-952d-97d44bf5ee64)



This is an AI-powered Health and Fitness App that offers three main functionalities:
1. **👩‍⚕️PCOS Prediction**: Predicts the likelihood of PCOS (Polycystic Ovary Syndrome) based on user inputs.
2. **🥗Diet Recommendations**: Provides personalized meal recommendations based on user preferences, age, weight, height, activity level, and goals.
3. **🏋️Exercise Recommendations**: Suggests personalized exercise plans based on gender, age, weight, fitness level, and goals.

## Features

### 1. 🔬PCOS Prediction
- The app predicts if a user has PCOS based on the following inputs:
  - Cycle regularity
  - Weight gain
  - Hair growth
  - Skin darkening
  - Fast food consumption
  - Follicle counts in ovaries
  
- It uses an XGBoost model to predict the result, which will either indicate **PCOS Detected** or **No PCOS**.

### 2. 🥗Diet Recommendations
- The app suggests personalized meal plans based on:
  - Age
  - Sex
  - Weight and height
  - Activity level
  - Goal (weight loss, weight gain, or maintenance)
  - Diet preference (e.g., vegetarian, vegan)
  - Allergies
  
- After input, the app will provide meal suggestions tailored to the user's inputs.

### 3. 🏋️Exercise Plan Recommendations
- The app generates a personalized exercise plan based on:
  - Gender
  - Age
  - Weight and height
  - Fitness level
  - Fitness goal (weight loss or weight gain)
  - Fitness type (cardio or muscular fitness)
  
- The user gets a customized exercise plan to help them reach their fitness goal.

## Installation

To run this app locally, follow the steps below:

### 1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/health-fitness-app.git
   ```

### 2. **Navigate to the app folder**:
  ```bash
  cd health-fitness-app
```

### 3. **Create a virtual environment (Optional but recommended)**  
```bash
python -m venv venv
```

### 4. **Activate the virtual environment**  
- **On Windows:**  
  ```bash
  venv\Scripts\activate
  ```
- **On Mac/Linux:**  
  ```bash
  source venv/bin/activate
  ```

### 5. **Install the dependencies**  
```bash
pip install -r requirements.txt
```

### 6. **Run the Streamlit app**  
```bash
streamlit run app.py
```

---

## Files  

| File Name                                       | Description |
|------------------------------------------------|-------------|
| `app.py`                                      | Main Streamlit app file containing the logic for all pages. |
| `xgboost_model.joblib`                         | Pre-trained XGBoost model for PCOS prediction. |
| `recipes.csv`                                  | Dataset for meal recommendations. |
| `gym recommendation.csv`                       | Dataset for exercise recommendations. |
| `personalised-exercise-recommendation.ipynb`   | Python code for exercise recommendation. |
| `pcos_filtered.csv`                            | Dataset with selected features for PCOS prediction. |
| `pcos-prediction.ipynb`                        | Python code for PCOS prediction. |
| `diet-recommendation.ipynb`                    | Python code for diet recommendation. |
| `PCOS_infertility.csv`                         | Dataset with infertility data. |
| `PCOS_data_without_infertility.xlsx`           | Dataset for PCOS without infertility. |

---

## License  

This project is licensed under the **MIT License** – see the [LICENSE](LICENSE) file for details.

