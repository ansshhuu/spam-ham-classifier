import streamlit as st
import pickle
import nltk
import string
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

nltk.download('punkt')
nltk.download('stopwords')

ps = PorterStemmer()
tfidf = pickle.load(open('vectorizer.pkl', 'rb'))
model = pickle.load(open('model.pkl', 'rb'))

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

st.set_page_config(page_title="Spam Classifier", page_icon="📩")

st.title("📩 Email / SMS Spam Classifier")
st.write("Easily check whether a message is **Spam** or **Not Spam**")

input_sms = st.text_area("Enter your message here:", height=120)

if st.button("Predict"):
    if input_sms.strip() == "":
        st.warning("⚠️ Please enter a message before predicting.")
    else:
        transformed_sms = transform_text(input_sms)
        vector_input = tfidf.transform([transformed_sms])
        result = model.predict(vector_input)[0]
        
        if result == 1:
            st.error("🚨 This message is classified as **SPAM**")
        else:
            st.success("✅ This message is classified as **NOT SPAM**")
