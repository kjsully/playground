from flask import Flask, render_template
app = Flask(__name__)



@app.route("/play/<int:num>")
def play(num):
    return render_template("index.html", num=num)





if __name__=="__main__":
    app.run(debug=True)

