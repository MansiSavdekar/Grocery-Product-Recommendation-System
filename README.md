# 🛒 Grocery Product Recommendation System

Personalized grocery suggestions with Market Basket Analysis (Apriori Algorithm) & Collaborative Filtering.

## Dataset

https://www.kaggle.com/datasets/heeraldedhia/groceries-dataset

This project uses the Groceries Dataset from Kaggle:
- Contains transactional data of grocery purchases.
- Each transaction represents items bought together by a customer.


## Recommendation Techniques
### 1. Market Basket Analysis (Apriori Algorithm)

Market Basket Analysis is a data mining technique used to find patterns of items that are frequently bought together. In this project, we use the Apriori algorithm to:
- Identify frequent itemsets from transaction data.
- Generate association rules to recommend products often purchased together.
- Help users discover related items they may not have thought to buy.
- Example: If a user buys milk, the system may recommend bread or butter because these items frequently appear together in transactions.

### 2. Collaborative Filtering

Collaborative Filtering is a personalized recommendation technique that suggests products based on the preferences and behaviors of similar users. It works by:
- Comparing users’ purchase histories to find similar users.
- Recommending items that those similar users have bought but the current user hasn’t.
- Improving personalization and helping users discover new items.
- Example: If user A and user B have bought mostly the same items, and user B also bought olive oil, the system may recommend olive oil to user A.

### 3. Hybrid Recommendation Engine

This project combines Market Basket Analysis and Collaborative Filtering to create a hybrid recommendation system:
- Market Basket Analysis ensures users see products frequently bought together.
- Collaborative Filtering adds a personalized touch, suggesting items based on similar users.
- Together, this improves accuracy, relevance, and user satisfaction.

## Project Structure

![Grocery Recommendation System Flow](Grocery_Recommender.png)

## Tech Stack

- Python 3.11
- Flask
- Bootstrap 5
- Pandas & NumPy
- Scikit-learn (Collaborative Filtering)
- Mlxtend (Apriori Algorithm) 


## Future Enhancements

- User login & purchase history tracking
- Real-time product stock updates
- Explainable recommendations (“Customers who bought this also bought…”)
- Interactive product cards with images
- Personalized dashboards & analytics


## Author

Mansi Savdekar

[GitHub Profile](https://github.com/mansisavdekar) | [Connect on LinkedIn](https://www.linkedin.com/in/mansi-savdekar-232577181/)

