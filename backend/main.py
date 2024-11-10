from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import os

# Initialize Flask app and the database
app = Flask(__name__)

# Configure the database URI (using SQLite for local testing)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI', 'sqlite:///messages.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

CORS(app)

# Define the Message model
class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # Column for the message ID (primary key)
    message = db.Column(db.String(255), nullable=False)  # Column for storing the message content

    def __repr__(self):
        return f"<Message {self.id}>"

# Create the database tables if not exist
with app.app_context():
    db.create_all()  # TODO: Create tables based on the model

@app.route('/')
def is_alive():
    return jsonify('live')

@app.route('/api/msg/<string:msg>', methods=['POST'])
def msg_post_api(msg):
    # TODO: store msg in DB and return identifier
    new_msg = Message(message=msg)  # Create a new Message object with the provided message
    db.session.add(new_msg)  # Add the new message to the session
    db.session.commit()  # Commit to the database
    
    # TODO: Return the message ID as a JSON response
    return jsonify({'msg_id': new_msg.id})  # Return the ID of the newly stored message

@app.route('/api/msg/<int:msg_id>', methods=['GET'])
def msg_get_api(msg_id):
    print(f"msg_get_api > msg_id = {msg_id}")
    # TODO: get msg from DB and return it
    msg = Message.query.get(msg_id)  # Retrieve the message by ID from the database
    
    if msg:  # If the message is found
        return jsonify({'msg': msg.message})  # Return the message content
    else:  # If the message is not found
        return jsonify({'error': 'Message not found'}), 404  # Return an error message

if __name__ == "__main__":
    # Run the app locally on localhost:8080
    app.run(debug=True, host="127.0.0.1", port=8080)


