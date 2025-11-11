from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/process", methods=["POST"])
def process():
    notes = request.form["notes"]

    # AI draft simulation
    draft = "Summary generated from notes: " + notes[:60] + "..."

    # Simple clinical rule check simulation
    warning = ""
    risky_words = ["interaction", "overdose", "contraindicated", "allergy"]

    for w in risky_words:
        if w in notes.lower():
            warning = "Possible risk detected (check medications and interactions)."
            break

    return render_template("results.html", draft=draft, warning=warning)
if __name__ == "__main__":
    app.run(debug=True)

