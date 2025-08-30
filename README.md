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

## 📂 Project Structure
sms-spam-classifier/
│── app.py # Streamlit app
│── model.pkl # Trained ML model
│── vectorizer.pkl # TF-IDF vectorizer
│── requirements.txt # Dependencies
│── README.md # Project description

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

This project is licensed under the MIT License.


