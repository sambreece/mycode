from flask import Flask
from flask import redirect
from flask import request
from flask import render_template


app= Flask(__name__)

question = "What is the country of origin of golden retrievers?"
answer = "Scotland"

@app.route("/")
def index():
	return render_template('postmaker.html')
@app.route('/guess', methods=["GET", "POST"])
def guess():
	if request.method == 'POST':
		if request.form.get("user_input") == "Scotland":
			return redirect('/correct')
		else:
			return redirect('/')
	else:
		return "Got it, but don't know what to do."

@app.route('/correct')
def correct():
	return "That was correct!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2224)
