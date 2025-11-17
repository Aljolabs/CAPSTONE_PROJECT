from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pandas as pd

def staff_computation(data, task_name, top=5):
    # Data to DataFrame
    df = pd.DataFrame(data)
    print(df)
    
    # Creating aggregation
    df_task = df.groupby(['service', "assigned_staff"])["overall_rating"].mean().reset_index()
    df_task.rename(columns={
        "overall_rating": "avg_rating"
    }, inplace=True)

    # Suggestiom of employee based on dataset
    subset = df_task[df_task['service'] == task_name]

    # Sorting by average
    subset = subset.sort_values("avg_rating", ascending=False)
    return subset.head(top).to_json(orient="records")
    
def employeeSuggestion(df, features, target, new_employee):
    """This function creates a employee suggestion based
    on the given data. This function tries to suggests
    who is the fit for the job . 
    """
    
    X = df[features]
    y = df[target]

    model = RandomForestClassifier()
    model.fit(X, y)

    probabilty = model.predict_proba([new_employee])[0][1]
    predict = model.predict([new_employee])[0]
    return predict, probabilty