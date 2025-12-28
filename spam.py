# Spam Message Detection using Machine Learning
# Dataset: Kaggle SMS Spam Collection

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score

# ==============================
# 1. Load dataset correctly
# ==============================
data = pd.read_csv("spam.csv", encoding="latin-1")

# Select ONLY required columns (VERY IMPORTANT)
data = data.iloc[:, 0:2]

# Rename columns
data.columns = ["label", "message"]

# ==============================
# 2. Convert labels to numbers
# ==============================
data["label"] = data["label"].map({"ham": 0, "spam": 1})

# ==============================
# 3. Split dataset
# ==============================
X_train, X_test, y_train, y_test = train_test_split(
    data["message"],
    data["label"],
    test_size=0.2,
    random_state=42
)

# ==============================
# 4. Text → Numbers
# ==============================
vectorizer = CountVectorizer()
X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)

# ==============================
# 5. Train model
# ==============================
model = MultinomialNB()
model.fit(X_train_vec, y_train)

# ==============================
# 6. Accuracy
# ==============================
y_pred = model.predict(X_test_vec)
print("Model Accuracy:", accuracy_score(y_test, y_pred))

# ==============================
# 7. Test custom message
# ==============================
msg = input("\nEnter a message: ")
msg_vec = vectorizer.transform([msg])
result = model.predict(msg_vec)

if result[0] == 1:
    print("Prediction: SPAM 🚫")
else:
    print("Prediction: HAM ✅")
