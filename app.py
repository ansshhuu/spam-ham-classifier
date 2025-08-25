import streamlit as st
import pickle
import nltk
from nltk.corpus import stopwords
import string
from nltk.stem.porter import PorterStemmer

# Load model and vectorizer
ps = PorterStemmer()
tfidf = pickle.load(open('vectorizer.pkl', 'rb'))
model = pickle.load(open('model.pkl', 'rb'))

# Preprocessing
def transform_text(text):
    text = text.lower()
    text = nltk.word_tokenize(text)

    temp = []
    for i in text:
        if i.isalnum():
            temp.append(i)

    text = temp[:]
    temp.clear()

    for i in text:
        if i not in stopwords.words('english') and i not in string.punctuation:
            temp.append(i)

    text = temp[:]
    temp.clear()

    for i in text:
        temp.append(ps.stem(i))
    return " ".join(temp)


# ---------------- Streamlit UI ----------------
st.set_page_config(page_title="Spam Classifier", page_icon="📩")

st.title("📩 Email / SMS Spam Classifier")
st.write("Easily check whether a message is **Spam** or **Not Spam**")

# Input box
input_sms = st.text_area("Enter your message here:", height=120)

# Predict button
if st.button("Predict"):
    if input_sms.strip() == "":
        st.warning("⚠️ Please enter a message before predicting.")
    else:
        # Preprocess
        transformed_sms = transform_text(input_sms)

        # Vectorize
        vector_input = tfidf.transform([transformed_sms])

        # Predict
        result = model.predict(vector_input)[0]

        # Display Result (clean, card-like style)
        if result == 1:
            st.error("🚨 This message is classified as **SPAM**")
        else:
            st.success("✅ This message is classified as **NOT SPAM**")
