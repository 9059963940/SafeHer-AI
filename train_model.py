import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
import joblib

data = {
    "text": [
        "help me",
        "someone is following me",
        "i am scared",
        "emergency",
        "save me",
        "hello",
        "good morning",
        "how are you",
        "thank you",
        "nice day"
    ],
    "label": [
        1,
        1,
        1,
        1,
        1,
        0,
        0,
        0,
        0,
        0
    ]
}

df = pd.DataFrame(data)

model = Pipeline([
    ('vectorizer', CountVectorizer()),
    ('classifier', MultinomialNB())
])

model.fit(df['text'], df['label'])

joblib.dump(model, 'models/distress_model.pkl')

print("Model Saved Successfully")