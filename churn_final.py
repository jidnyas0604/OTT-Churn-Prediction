import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder, StandardScaler# type: ignore
from sklearn.model_selection import train_test_split, GridSearchCV# type: ignore
from sklearn.ensemble import VotingClassifier, RandomForestClassifier# type: ignore
from sklearn.svm import SVC# type: ignore
from sklearn.neighbors import KNeighborsClassifier# type: ignore
from sklearn.metrics import classification_report, roc_auc_score# type: ignore
from imblearn.over_sampling import SMOTE # type: ignore
import joblib # type: ignore

# Load dataset
file_path = "/Users/jidnyasbbhonge/Documents/JBB/Mini_Project/ott_churn.csv"
df = pd.read_csv(file_path)

# Handling missing values
df['gender'].fillna(df['gender'].mode()[0], inplace=True)
df['maximum_days_inactive'].fillna(df['maximum_days_inactive'].median(), inplace=True)
df.dropna(subset=['churn'], inplace=True)

# Dropping irrelevant columns
df.drop(['customer_id', 'phone_no', 'mail_subscribed'], axis=1, inplace=True)

# Encoding
le = LabelEncoder()
df['gender'] = le.fit_transform(df['gender'])  # Male = 1, Female = 0
df = pd.get_dummies(df, columns=['multi_screen'], drop_first=True)

# Split features and target
X = df.drop('churn', axis=1)
y = df['churn']

# Handle class imbalance using SMOTE
X_resampled, y_resampled = SMOTE().fit_resample(X, y)

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X_resampled, y_resampled, test_size=0.2, random_state=42)

# Scaling
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Define models
knn = KNeighborsClassifier(n_neighbors=5)
svc = SVC(C=1, kernel='rbf', probability=True)
rf = RandomForestClassifier(n_estimators=100, random_state=42)

# Voting Classifier
voting_model = VotingClassifier(
    estimators=[('knn', knn), ('svc', svc), ('rf', rf)],
    voting='soft'
)

# Fit model
voting_model.fit(X_train_scaled, y_train)

# Predictions
y_pred = voting_model.predict(X_test_scaled)

# Evaluation
print(classification_report(y_test, y_pred))
print("AUC-ROC Score:", roc_auc_score(y_test, voting_model.predict_proba(X_test_scaled)[:, 1]))

# Save model and scaler
joblib.dump(voting_model, "ott_churn_final.pkl")
joblib.dump(scaler, "scaler.save")
