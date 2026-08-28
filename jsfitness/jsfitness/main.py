
from flask import Flask
from public import public
from admin import admin
from trainer import trainer
from user import user



app = Flask(__name__)
app.register_blueprint(public)
app.register_blueprint(admin)
app.register_blueprint(trainer)
app.register_blueprint(user)


app.secret_key='@#$nm'


app.run(debug=True,port=5004,host="0.0.0.0")