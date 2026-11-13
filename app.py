
from flask import Flask, render_template, request
from datetime import date

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():

    result = None
    error = None

    if request.method == "POST":

        fname = request.form.get("fname", "").strip()
        dob = request.form.get("dob", "").strip()
        weight = request.form.get("weight", "").strip()

        try:
            birth_year = int(dob)
            int_w = float(weight)

            current_year = date.today().year
            age = current_year - birth_year

            if not fname:
                raise ValueError("Please enter your name.")

            if birth_year < 1900 or birth_year > current_year:
                raise ValueError("Please enter a valid birth year.")

            if int_w <= 0:
                raise ValueError("Please enter a valid weight.")

            # General fitness guidance
            plan = [
                "Start with gentle warm-up activities.",
                "Enjoy regular physical activities you can manage.",
                "Include suitable strength and flexibility exercises.",
                "Allow your body enough time to rest.",
                "Drink water regularly throughout the day."
            ]

            result = {
                "name": fname,
                "age": age,
                "weight": int_w,
                "plan": plan
            }

        except ValueError as e:
            error = str(e) if str(e) else "Please enter valid information."

    return render_template(
        "index.html",
        result=result,
        error=error
    )


if __name__ == "__main__":
    app.run(debug=True)
