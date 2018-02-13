# -*- coding:utf-8 -*-
# Created by Jin(jinzhencheng@outlook.com) at 2018/01/21.

from flask import render_template
from flask import request
from flask import session
from flask import jsonify
from flask import redirect
from flask import url_for
from application.admin import admin_blueprint
from application.model import admin_dal


@admin_blueprint.route("/index")
def index():
    return render_template("admin/layout.html")


@admin_blueprint.route("/login", methods=["POST", "GET"])
def login():
    if "username" in request.form and "password" in request.form:
        username = request.form["username"]
        password = request.form["password"]
        admin = admin_dal.login(username, password)
        if admin:
           session["admin"] = admin
           return redirect(url_for("admin.index"))
        else:
            return render_template("/admin/login.html", info=u"警告：用户名或密码有误")
    else:
        return render_template("/admin/login.html")


@admin_blueprint.route("/logout")
def logout():
   session.pop("admin", None)
   return redirect(url_for("admin.login"))