import os
from flask import Flask, render_template, request, redirect, url_for
from flask_socketio import SocketIO, send

app = Flask(__name__)
socketio = SocketIO(app)

@app.route("/chat")
def index():
    return(render_template("wsio_chat.html"))
    
@app.route("/chat") 
def chat():
    username=request.args.get("username")
    room = request.args.get("room")
    if room and username : 
        return render_template("wsio_chat.html", username=username, room= room)
    else:
       return render_template("wsio_chat.html",username=username, room= room)

@socketio.on('message')
def handle_message(msg):
    if msg:
        print("hello "+ msg)
        send("Hello amigos "+ msg, broadcast=True)
        
        
if (__name__ == '__main__'):
    socketio.run(app, host='127.0.0.1', port=5000, debug=True)
	
	
	
	