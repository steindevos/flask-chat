from flask import Flask, request, render_template, redirect

app = Flask(__name__)

messages = [
    "Stein: whasdfs", 
    "Piet: sdflkjsdf",
    "Henk: nooo!"
    ]
    
@app.route("/")
def show_index():
    return render_template("index.html", messages = messages)
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)