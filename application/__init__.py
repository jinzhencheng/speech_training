
from flask import Flask
from admin import admin
from web import web

app = Flask(__name__)
app.secret_key = "12(*&6R234@#(5867adb23.xyeE&!D"
app.register_blueprint(admin, web)

app.debug = True