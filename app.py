"""Flask web application for the Anime Recommendation Expert System (Sistem Pakar)."""

import os
from flask import Flask, render_template, request, session, redirect, url_for
from inference_engine import run_inference, max_possible_score
from knowledge_base import QUESTIONS

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", os.urandom(24))


@app.route("/")
def index():
    """Home page — start the questionnaire."""
    session.clear()
    return render_template("index.html")


@app.route("/quiz", methods=["GET", "POST"])
def quiz():
    """Step-by-step questionnaire."""
    if "answers" not in session:
        session["answers"] = {}

    if request.method == "POST":
        q_id = request.form.get("question_id")
        answer = request.form.get("answer")
        if q_id and answer:
            answers = session["answers"]
            answers[q_id] = answer
            session["answers"] = answers

    # Determine which question to show next
    answers = session.get("answers", {})
    answered_ids = set(answers.keys())

    for i, question in enumerate(QUESTIONS):
        if question["id"] not in answered_ids:
            return render_template(
                "quiz.html",
                question=question,
                step=i + 1,
                total=len(QUESTIONS),
                progress=int((i / len(QUESTIONS)) * 100),
            )

    # All questions answered — run inference
    return redirect(url_for("results"))


@app.route("/results")
def results():
    """Display anime recommendations."""
    answers = session.get("answers", {})
    if not answers:
        return redirect(url_for("index"))

    recommendations = run_inference(answers)
    top_recommendations = recommendations[:8]

    # Build a human-readable summary of user preferences
    preference_labels = {}
    for q in QUESTIONS:
        val = answers.get(q["id"])
        if val:
            label = next((opt[1] for opt in q["options"] if opt[0] == val), val)
            preference_labels[q["text"]] = label

    return render_template(
        "results.html",
        recommendations=top_recommendations,
        preferences=preference_labels,
        max_score=max_possible_score(),
    )


@app.route("/restart")
def restart():
    """Clear session and restart the quiz."""
    session.clear()
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=os.environ.get("FLASK_DEBUG", "0") == "1")
