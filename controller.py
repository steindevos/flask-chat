from flask import Flask, request, render_template, redirect

app = Flask(__name__)

messages = [
    "Stein: whasdfs", 
    "Piet: sdflkjsdf",
    "Henk: nooo!"
    ]

@app.route("/")
def show_join():
    return render_template("join.html")

@app.route("/join")
def do_join():
    username = request.args["username"]
    return redirect("/chat/" + username)

def can_view(message, username): 
    addressed_to_me = "@" + username in message
    addressed_to_nobody = "@" not in message
    i_wrote_it = message.startswith(username + ":")
    
    return addressed_to_me or addressed_to_nobody or i_wrote_it

@app.route("/chat/<username>")
def show_chat(username):
    specific_messages = []
    for i in messages:
        if can_view(i, username):
            specific_messages.append(i)
      
    return render_template("chat.html", messages = specific_messages, username=username)
    

    
@app.route("/new", methods = ["POST"])
def show_add():
    message = request.form["message"]
    username = request.form["username"]
    messages.append(username + ": " + message)
    return redirect("/chat/" + username)
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)