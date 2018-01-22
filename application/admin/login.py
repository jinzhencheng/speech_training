# -*- coding:utf-8 -*-
# Created by Jin(jinzhencheng@outlook.com) at 2018/01/21.

from flask import render_template
from application import admin


@admin.route("/login")
def login():
    return render_template("login.html")
