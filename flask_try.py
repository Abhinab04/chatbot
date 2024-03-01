from flask import Flask, render_template, request
import subprocess
app=Flask(__name__)
@app.route("/")
def index():
    return render_template("index.html")
@app.route("/process_audio", methods=["POST"])
def process_audio():
    subprocess.run(["python", "cleopatra.py"])
    return "success"
if __name__=="__main__":
    app.run(debug=True)
