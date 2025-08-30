# 📩 SMS / Email Spam Classifier

A simple **Spam Classifier Web App** built with **Streamlit** and **Machine Learning**.  
This app can classify any SMS or Email message as **Spam** or **Not Spam**.

---

## 🚀 Features
- 📝 Input any SMS/Email message  
- ⚡ Instant prediction (Spam / Not Spam)  
- 🎨 Clean and interactive UI with Streamlit  
- 📦 Pre-trained model with TF-IDF + Multinomial Naive Bayes  

---

## 📂 File Structure

app.py - Main Streamlit app file with UI and logic for prediction.  
model.pkl - Trained ML model for SMS spam classification.  
vectorizer.pkl - TF-IDF vectorizer used for transforming input text.  
requirements.txt - List of dependencies for the app (e.g., Streamlit, scikit-learn, nltk).  
README.md - This file 😊.  

## 🛠 Installation (Run Locally)

1. Clone the repository
   ```bash
   git clone https://github.com/<your-username>/sms-spam-classifier.git
2. Install dependencies
   ```bash
   pip install -r requirements.txt
3. Run the app
   ```bash
   streamlit run app.py

## 📈 How It Works

The app processes the entered text message by performing the following steps:

1. **Text Preprocessing**  
   - Converts the text to lowercase.  
   - Removes punctuation, stopwords, and non-alphanumeric characters.  
   - Applies stemming to reduce words to their root form.  

2. **Vectorization**  
   - Uses the pre-trained TF-IDF vectorizer (`vectorizer.pkl`) to convert the cleaned text into numerical features.  

3. **Prediction**  
   - The trained ML model (`model.pkl`) predicts whether the message is **Spam** or **Not Spam**.  

4. **Result Display**  
   - The app shows the prediction result directly in the Streamlit UI.  

## 🛠️ Technologies Used

- **Streamlit** – For building the interactive web interface.  
- **Scikit-learn** – For training and saving the machine learning model.  
- **NLTK** – For text preprocessing (stopwords, tokenization, stemming).  
- **Pickle** – For saving and loading the trained model and vectorizer.

  # 📊 Model Performance

- The model is trained on a **SMS Spam Collection dataset**.  
- Achieves around **96–98% accuracy** depending on preprocessing and split.  
- Can effectively distinguish between **spam** (ads, fraud, promotional texts) and **ham** (normal messages).

  ## 📝 Troubleshooting

- If you encounter **`LookupError: Resource 'stopwords' not found`**, add the following in your `app.py`:
     ```python
     import nltk
     nltk.download('stopwords')
     nltk.download('punkt')
Ensure that both model.pkl and vectorizer.pkl are correctly placed in the project directory.
If deployment on Streamlit Cloud is stuck:
Double-check requirements.txt.
Restart the deployment after clearing cache.
  

🌐 Deployment

This project is deployed on Streamlit Cloud.
👉 

🧠 Model Details

Algorithm: Multinomial Naive Bayes
Vectorization: TF-IDF (Term Frequency – Inverse Document Frequency)
Dataset: SMS Spam Collection dataset (Kaggle / UCI)



🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you’d like to change.

📜 License

This project is licensed under the MIT License.see the [LICENSE](LICENSE) file for details.


