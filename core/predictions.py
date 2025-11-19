from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import pandas as pd

def staff_computation(data, task_name, top=5):
    # Convert data to DataFrame
    df = pd.DataFrame(data)
    analyzer = SentimentIntensityAnalyzer()

    # Fill missing fields BEFORE grouping
    df['additional_comments'] = df['additional_comments'].fillna("This was okay.")
    df['positive_feedback'] = df['positive_feedback'].fillna("This was okay.")
    df['improvement_feedback'] = df['improvement_feedback'].fillna("This was okay.")

    # Compute sentiment for each row
    df['eval_add'] = df['additional_comments'].apply(lambda x: analyzer.polarity_scores(x)['compound'])
    df['eval_pos'] = df['positive_feedback'].apply(lambda x: analyzer.polarity_scores(x)['compound'])
    df['eval_imp'] = df['improvement_feedback'].apply(lambda x: analyzer.polarity_scores(x)['compound'])

    # Average sentiment per row (percentage)
    df['sentiment'] = ((df['eval_add'] + df['eval_pos'] + df['eval_imp']) / 3) * 100

    # Aggregate by service and staff
    df_task = df.groupby(['service', 'assigned_staff']).agg(
        avg_rating=('overall_rating', 'mean'),
        avg_sentiment=('sentiment', 'mean'),
        comments=('additional_comments', lambda x: list(x)),
        pos_feedback=('positive_feedback', lambda x: list(x)),
        imp_feedback=('improvement_feedback', lambda x: list(x))
    ).reset_index()

    # Filter for the selected service/task
    subset = df_task[df_task['service'] == task_name]

    # Sort by rating (descending)
    subset = subset.sort_values('avg_rating', ascending=False)

    print(subset.head(top).to_json(orient="records"))

    # Return top results as JSON
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