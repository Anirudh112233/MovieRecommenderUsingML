
# 🎬 Movie Recommendation System using ML 📽️

Welcome to the **Movie Recommendation System**! This system leverages machine learning to suggest movies based on user preferences. The recommendation engine is built using various ML techniques and is designed to be intuitive and easy to use.

---

## 🚀 Project Overview

This project aims to create a movie recommendation system using machine learning. It recommends movies based on a user's historical interactions or by finding similar movies to what they like.

---

## 🛠️ How It's Made

The system is powered by a **content-based recommendation system** that uses a combination of movie metadata and machine learning models.

### 1. **Data Collection** 📊
The project uses the **TMDB Movie Metadata** dataset from Kaggle, which contains detailed information about thousands of movies, including:
- Movie titles 🎥
- Descriptions 📝
- Genres 🎬
- Cast 🧑‍🤝‍🧑
- and more...

[Download the dataset here](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata?resource=download)

### 2. **Preprocessing** 🔄
The data is preprocessed to ensure it's clean and ready for machine learning. Key steps include:
- Handling missing data 💀
- Converting categorical features to numerical ones 🧮
- Vectorizing movie descriptions 🖋️

### 3. **Model Training** 🤖
A **content-based filtering** algorithm is used, where the similarity between movies is calculated based on their metadata (e.g., genres, actors, and descriptions). The **Cosine Similarity** algorithm is employed to measure how similar the movies are to one another.

### 4. **Building the Recommendation System** 🎯
Once the model is trained, it recommends movies based on the similarity between movies in the dataset. The recommendation engine suggests the most similar movies to the ones the user has interacted with.

### 5. **Frontend Interface** 💻
The system uses **Streamlit** to create an interactive web-based interface for users to input movie preferences and receive recommendations.

### 6. **Deployment** 🚢
The project is deployed on **Streamlit Cloud**, allowing users to easily interact with the recommendation system without needing to run it locally.

---

## 🖼️ Screenshots

Here are some screenshots of the Movie Recommendation System in action:

### 1. **Homepage** 🏠

![Homepage]("ResultsImages/HomePage.png")

### 2. **Movie Recommendation Results** 🎬

![Recommendation Results 1]("ResultsImages/Resuts1.png")

![Recommendation Results 2]("ResultsImages/Results2.png")

---

## ⚙️ Setup & Installation

To get the Movie Recommendation System up and running on your local machine, follow the steps below.

### 1. **Clone the Repository** 🔁

```bash
git clone https://github.com/YourUsername/MovieRecommenderUsingML.git
```

### 2. **Install Dependencies** 📦

Navigate to the project directory and install the required dependencies using:

```bash
pip install -r requirements.txt
```

### 3. **Run the Application** 🏃‍♂️

To launch the Movie Recommendation System, use the following command:

```bash
streamlit run app.py
```

---

## 📑 File Structure

```plaintext
MovieRecommenderUsingML/
│
├── app.py                 # Main application file (Streamlit)
├── movie_dict.pkl         # Serialized dictionary with movie data
├── similarity.pkl         # Pre-trained similarity model
├── requirements.txt       # List of project dependencies
├── README.md              # Project documentation
└── other_files/           # Additional files (if any)
```

---

## 📍 Contribution Guidelines

Feel free to contribute to this project! Here’s how you can help:
- **Report Bugs** 🐞
- **Suggest Features** 🚀
- **Submit Pull Requests** 🛠️

---

## 🧑‍🤝‍🧑 Author

- **Anirudh Mishra** : *anirudhmishra112233@gmail.com*

---


