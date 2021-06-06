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
    counter = 1
    print("in 0", digit, counter)
    if request.method == "POST":
        shot_max = int(request.form["shot_hi"])
        shot_min = int(request.form["shot_lo"])
        counter = int(request.form["counter"])
        result = int(request.form["result"])
        if counter == 10:
            return render_template("failure.html")
        elif result == 0:
            return redirect(url_for("win"))
        elif result == 1:
            shot_max = int(request.form["digit"])
            digit = first_guess(shot_max, shot_min)
            counter += 1
        elif result == 2:
            shot_min = int(request.form["digit"])
            digit = first_guess(shot_max, shot_min)
            counter += 1
        elif counter == 10:
            return render_template("welcome.html")

    return render_template("guees.html", form=form, digit=digit, shot_hi=shot_max, shot_lo=shot_min, counter=counter)


@app.route("/win", methods=["GET", "POST"])
def win():
    if request.method == "POST":
        return render_template("welcome.html")
    return render_template("win.html", form=form)


@app.route("/failure", methods=["GET", "POST"])
def failure():
    if request.method == "POST":
        return render_template("welcome.html")
    return render_template("failure.html", form=form)


def first_guess(maxv=1000, minv=0):
    shot = ((maxv - minv) // 2) + minv
    return shot


if __name__ == "__main__":
    app.run(debug=True)
