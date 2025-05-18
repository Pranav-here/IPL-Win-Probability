# 🏏 IPL Win Probability Predictor

This project is a **logistic regression-based machine learning model** that predicts the **probability of a team winning an IPL match** during a second innings chase. It uses **real IPL data (2008–2023)** and includes a **Streamlit web interface** to allow real-time probability predictions.

🌐 **Live Demo**: [IPL Win Predictor](https://ipl-win-probability-pranav-kuchibhotla.streamlit.app/)

---

## 📂 Files

| File | Description |
|------|-------------|
| `app.py` | Streamlit web app for predicting win probabilities |
| `pipe.pkl` | Trained logistic regression pipeline |
| `Win probability.ipynb` | Full data preprocessing, modeling, and visualization notebook |
| `matches.csv` | IPL match-level data |
| `requirements.txt` | Required libraries to run the project |
| `README.md` | You're looking at it! |

---

## 📊 Model Features

- **Match Situation**: Required runs, balls left, current and required run rate
- **Team Stats**: Batting team, Bowling team, Venue
- **Match Result**: Binary outcome (win/lose)

Model trained using:
- One-hot encoding for categorical data (teams and venue)
- Logistic Regression (unskewed probabilities compared to Random Forest)
- Accuracy: ~80.6% on test set

---

## 🚀 Streamlit App

Inputs:
- Batting team, Bowling team, Venue
- Target score, Current score, Overs completed, Wickets lost

Outputs:
- Win % for the batting team and bowling team

---

## 🧠 How It Works

Data from `matches.csv` and `deliveries.csv` is cleaned and combined to compute:
- Target score
- Score progression
- Ball-by-ball metrics: CRR, RRR, wickets left

These are fed into a logistic regression model to predict win probability at any point in a match.

### 📈 Visualization

The notebook includes match progression visualizations:
- Over-by-over runs and wickets
- Win/Loss probability changes

---

## 📦 Installation

```bash
git clone https://github.com/Pranav-here/IPL-Win-Probability.git
cd IPL-Win-Probability
pip install -r requirements.txt
streamlit run app.py
```

---

## ✅ Dependencies

- pandas
- numpy
- scikit-learn
- matplotlib
- streamlit
- pickle

---

## 📌 Author

**Pranav Kuchibhotla**  
🔗 [GitHub](https://github.com/Pranav-here) 

---

© 2025 – Predict responsibly. Not for gambling use.