from flask import Flask, render_template, flash, redirect, url_for, session, logging, request

app = Flask(__name__,template_folder='frontend')
app.secret_key = 'hello'

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        uname = request.form["uname"]
        return render_template("loginpage.html", uname=uname)
    else:
        return render_template("loginpage.html")


if __name__ == "__main__":
    app.run(debug=True,port=80,host='0.0.0.0')
