# Fake News Detection - MLOps Project

A machine learning application for detecting fake news using Natural Language Processing, deployed with Docker.

## 🚀 Features

- **Machine Learning Model**: Logistic Regression with TF-IDF vectorization
- **REST API**: FastAPI backend for predictions
- **Web Interface**: Streamlit frontend for user interaction
- **Database**: MongoDB for storing prediction history
- **Containerization**: Docker & Docker Compose for easy deployment

## 🛠️ Tech Stack

- **Frontend**: Streamlit
- **Backend**: FastAPI
- **Database**: MongoDB
- **ML Libraries**: scikit-learn, NLTK
- **Deployment**: Docker, Docker Compose

## 📦 Installation

### Prerequisites
- Docker Desktop installed
- Git

### Steps

1. Clone the repository:
```bash
git clone https://github.com/YOUR_USERNAME/fake-news-detection-mlops.git
cd fake-news-detection-mlops
```

2. Run with Docker Compose:
```bash
docker-compose up -d --build
```

3. Access the application:
- Frontend: http://localhost:8501
- Backend API: http://localhost:8000
- API Docs: http://localhost:8000/docs

## 🎯 Usage

1. Open http://localhost:8501 in your browser
2. Enter news text in the text area
3. Click "Predict"
4. View the prediction (REAL/FAKE) and confidence score

## 📊 Model Details

- **Algorithm**: Logistic Regression
- **Features**: TF-IDF (Term Frequency-Inverse Document Frequency)
- **Preprocessing**: Lowercase, URL removal, stopword removal, punctuation removal

## 🏗️ Project Structure
```
fake-news-app/
├── frontend/
│   ├── Dockerfile
│   ├── app.py
│   └── requirements.txt
├── backend/
│   ├── Dockerfile
│   ├── main.py
│   ├── requirements.txt
│   └── model/
│       ├── model.pkl
│       └── vectorizer.pkl
└── docker-compose.yml
```

## 🔧 API Endpoints

- `GET /` - Health check
- `POST /predict` - Predict fake/real news

## 🛑 Stopping the Application
```bash
docker-compose down
```

## 📝 License

MIT License

## 👤 Author

Your Name - [Your GitHub](https://github.com/YOUR_USERNAME)
