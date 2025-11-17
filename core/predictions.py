from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pandas as pd

def staff_cmputation(df, employee_id):
    employee = df[df['employee_id'] == employee_id]

    score = 0.4 * employee['quality'].values[0] * 0.3 * employee['punctuality'].values[0] * 0.2 * employee['behavior'].values[0] * 0.1 * employee['overall'].values[0]
    return score

def employeeSuggestion(df, features, target, new_employee):
    """This function creates a employee suggestion based
    on the given data. This function tries to suggests
    who is the fit for the job.
    """
    
    X = df[features]
    y = df[target]

    model = RandomForestClassifier()
    model.fit(X, y)

    probabilty = model.predict_proba([new_employee])[0][1]
    predict = model.predict([new_employee])[0]
    return predict, probabilty