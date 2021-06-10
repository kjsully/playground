from flask import Flask, render_template
app = Flask(__name__)



@app.route("/play/<int:num>/<colors>")
def play(num, colors):
    return render_template("index.html", num=num, colors=colors)





if __name__=="__main__":
    app.run(debug=True)

