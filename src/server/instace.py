from flask import Flask
from db.database import db_init

class Server():
    def __init__(self):  
        self.app = Flask(__name__)
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
        self.app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        db_init(self.app)
 

    def run(self):    
        self.app.run(host="0.0.0.0", port=5000)
        
        
        



server = Server()

