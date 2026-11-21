from flask import Flask, render_template, request

app = Flask(__name__)

GRACE_DAYS = 3       # no fine for the first 3 days overdue
FINE_PER_DAY = 10    # Rs per day after the grace period
MAX_DAYS = 30        # input range: 0..30 days


def calculate_fine(raw):
    """Return (ok, message) for days overdue (integer 0-30)."""
    try:
        days = int(raw.strip())
    except (ValueError, AttributeError):
        return False, "Invalid input"
    if not 0 <= days <= MAX_DAYS:
        return False, "Invalid input"
    fine = max(0, days - GRACE_DAYS) * FINE_PER_DAY
    return True, f"Fine: Rs {fine}"


@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        ok, message = calculate_fine(request.form.get("days", ""))
        result = {"ok": ok, "message": message}
    return render_template("index.html", result=result)


if __name__ == "__main__":
    app.run(debug=True)
