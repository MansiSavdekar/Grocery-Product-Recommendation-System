from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

# ===============================
# Load trained models
# ===============================
with open("models/apriori_rules.pkl", "rb") as f:
    rules = pickle.load(f)

with open("models/item_similarity.pkl", "rb") as f:
    similarity_df = pickle.load(f)

products = sorted(similarity_df.columns.tolist())


# ===============================
# Hybrid Recommendation Logic
# ===============================
def recommend_hybrid(product, top_n=8):
    recs = {}

    # Collaborative Filtering (60%)
    if product in similarity_df.columns:
        cf_scores = similarity_df[product].sort_values(ascending=False)[1:top_n+3]
        for item, score in cf_scores.items():
            recs[item] = recs.get(item, 0) + score * 0.6

    # Market Basket Analysis (40%)
    basket_rules = rules[rules["antecedents"].apply(lambda x: product in x)]
    for _, row in basket_rules.iterrows():
        for item in row["consequents"]:
            recs[item] = recs.get(item, 0) + row["confidence"] * 0.4

    # Rank & Label
    final = []
    for item, score in sorted(recs.items(), key=lambda x: x[1], reverse=True)[:top_n]:
        if score >= 0.8:
            label = "🔥 Best Match"
            badge = "success"
        elif score >= 0.5:
            label = "👍 Good Match"
            badge = "warning"
        else:
            label = "Other Relevant"
            badge = "info"

        final.append({
            "product": item,
            "score": round(score, 3),
            "label": label,
            "badge": badge
        })

    return final


# ===============================
# Routes
# ===============================
@app.route("/", methods=["GET", "POST"])
def index():
    recommendations = []
    selected_product = None

    if request.method == "POST":
        selected_product = request.form.get("product")
        recommendations = recommend_hybrid(selected_product)

    return render_template(
        "index.html",
        products=products,
        recommendations=recommendations,
        selected_product=selected_product
    )


# ===============================
# Run App
# ===============================
if __name__ == "__main__":
    app.run(debug=True)
