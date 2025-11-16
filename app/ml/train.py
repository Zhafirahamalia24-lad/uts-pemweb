import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import joblib

DATA_PATH = 'backend/data/sessions.csv'
MODEL_OUT = 'backend/app/ml/model.pkl'

if __name__ == '__main__':
    df = pd.read_csv(DATA_PATH)
    feature_cols = ['duration_minutes','breaks','focus_score','sleep_hours','mood']
    X = df[feature_cols]
    y = df['label']
    X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=42)
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train,y_train)
    print(classification_report(y_test, model.predict(X_test)))
    joblib.dump(model, MODEL_OUT)
    print('Model saved to', MODEL_OUT)
