
from flask import Flask
from application.admin import admin_blueprint
from application.web import web_blueprint


app = Flask(__name__)

app.secret_key = "12(*&6R234@#(5867adb23.xyeE&!D"
app.register_blueprint(admin_blueprint, url_prefix="/admin")
app.register_blueprint(web_blueprint, url_prefix="/web")
