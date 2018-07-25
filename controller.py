from flask import Flask, request, render_template, redirect
from collections import Counter
import collections
import re

app = Flask(__name__)

messages = []
tags = []




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
    top_tags = Counter(tags)
    top_ten = top_tags.most_common(10)
    specific_messages = []
    for i in messages:
        if can_view(i, username):
            specific_messages.append(i)
      
    return render_template("chat.html", messages = specific_messages, username=username, tags=tags, top_tags=top_ten)
    
@app.route("/chat/<username>/tags/<hashtag>")
def show_topic(hashtag, username):
    hash_list = []
    for i in messages: 
        if "#" + hashtag in i:
            hash_list.append(i)
    return render_template("chat.html", messages = hash_list, username=username)
    

@app.route("/new", methods = ["POST"])
def show_add():
    message = request.form["message"]
    username = request.form["username"]
    messages.append(username + ": " + message)
    
    hash_message = message.split(" ")
    for word in hash_message:
        for character in word: 
            if character == "#":
                tags.append(word[1:])
            
    return redirect("/chat/" + username)
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)