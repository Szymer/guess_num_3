import flask as flask

from flask import Flask, render_template, request, redirect, url_for
from flask_wtf import FlaskForm, form

app = Flask(__name__)
app.config['SECRET_KEY'] = 'pi'


@app.route("/game", methods=['GET', 'POST'])
def guess_game():
    if request.method == "POST":
        start = request.form["go"]
        if start == "start":
            return redirect(url_for("guess"))
    return render_template("welcome.html", form=form)


@app.route("/game/guess", methods=['GET', 'POST'])
def guess():
    digit = first_guess()
    shot_min = 0
    shot_max = 1000
    if request.method == "POST":

        result = int(request.form["result"])
        if result == 0:
            return render_template("welcome.html")
        elif result == 1:
            digit = first_guess(maxv=int(request.form["shot_hi"]), minv=int(request.form["shot_lo"]))
            shot_max = int(request.form["digit"])
            print("shotmax", shot_max)
        elif result == 2:
            digit = first_guess(maxv=int(request.form["shot_hi"]), minv=int(request.form["shot_lo"]))
            shot_min = int(request.form["digit"])
            print("shotmmin", shot_min)

    return render_template("guees.html", form=form, digit=digit, a=shot_max,  b=shot_min)


def first_guess(maxv=1000, minv=0):
    shot = ((maxv - minv) // 2) + minv
    return shot


if __name__ == "__main__":
    app.run(debug=True)
