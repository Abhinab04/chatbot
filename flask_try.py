from flask import Flask, render_template, request, jsonify
import subprocess
app=Flask(__name__)
@app.route("/")
def index():
    return render_template("index.html")
@app.route("/get_response", methods=["POST"])
def get_response():
    user_input=request.form["user_input"]
    response=subprocess.run(["python", "cleopatra.py"], input=user_input.encode(), text=True, capture_output=True)
    return jsonify({"response": response.stdout})
if __name__=="__main__":
    app.run(debug=True)
