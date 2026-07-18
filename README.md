# Beyond Star Ratings
### How Brand Loyalty and Price Shape Smartphone Customer Sentiment

## Live Links
- Streamlit App: https://smartphones-review-analyzer-846mxfpa56jczumdxrxd9t.streamlit.app/
- Tableau Dashboard: https://public.tableau.com/app/profile/vinh.lam3565/viz/Book1_17838755321340/SmartphoneSentimentDashboard
- GitHub: https://github.com/vinhlam123/smartphones-review-analyzer

## Research Question
How do brand loyalty and price influence customer sentiment toward smartphone features, and how is this affected by AI features like voice assistants and biometric authentication?

## Key Findings
- OnePlus and Huawei have the highest customer sentiment despite lower brand recognition
- Apple has the lowest VADER score (0.336) despite premium pricing
- AI camera mentions produce the largest sentiment boost (+0.41)
- Google Assistant scores highest among voice assistants (0.709) vs Bixby (0.347)
- Premium phones score 20% higher sentiment than budget phones
- Problems and Returns is the only net-negative topic across all 15 LDA topics

## Dataset
- Amazon Unlocked Mobile: 413,840 reviews
- Scraped Amazon Reviews 2019: 67,986 reviews
- Combined after cleaning: 124,108 reviews across 9 brands

## Tech Stack
- Python 3.11, Pandas, NLTK
- VADER Sentiment Analysis
- Gensim LDA Topic Modeling
- SQLite database
- Tableau Public dashboard
- Streamlit + Plotly web app
- Git / GitHub version control

## Author
Vinh Lam — Built as a summer portfolio project.
