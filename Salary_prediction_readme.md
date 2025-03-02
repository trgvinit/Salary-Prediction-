🪙Salary Prediction

Code Explanation
• Data Loading & Cleaning:
The dataset is loaded using pd.read_csv(). Missing values are checked with isnull().sum() and removed with dropna(inplace=True).
• Encoding Categorical Features:
Categorical columns are identified with select_dtypes(include=['object']) and then encoded into numerical values using LabelEncoder.
• Feature & Target Selection:
The features (X) are defined by dropping the 'Salary' column, while the target variable (y) is set as 'Salary'.
• Train-Test Split:
The data is split into training (80%) and testing (20%) sets using train_test_split with a fixed random state for reproducibility.
• Standardization:
Features are standardized using StandardScaler to normalize the data before model training.
• Model Training & Prediction:
A LinearRegression model is trained on the standardized training data. Predictions are made on the test set using the trained model.
• Evaluation:
The model's performance is measured using the R² score (converted to a percentage) and the Mean Absolute Percentage Error (MAPE), which quantifies the average prediction error as a percentage.
Evaluation Metrics
• R² Score:
Indicates the proportion of variance in the salary data that is predictable from the independent variables. Reported as a percentage.
• Mean Absolute Percentage Error (MAPE):
Provides the average percentage difference between the actual and predicted salary values.
Contributing
Contributions, improvements, and bug fixes are welcome. Please open an issue or submit a pull request for any changes.
License
This project is licensed under the MIT License.
Copy code