from flask import Flask, render_template, request
app = Flask(__name__)
app.debug=True

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/one")
def one():
    return "<html><head><title>i am a a title</title></head><body>body blows</body></html>"

@app.route("/gashi", methods=['POST','GET']) #directory (default:5000) url building
def gashi():
	if request.method == 'GET':
		return render_template("gashi.html")
	else:
		ID = request.form.get("id")
		PW = request.form.get("password")
		return ID+','+PW

@app.route("/jumbo")
def jumbo():
	return render_template("boot.html")

@app.route("/new")
def new():
	return render_template("new.html")

if __name__ == "__main__":
    app.run()