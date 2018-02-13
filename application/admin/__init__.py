# -*- coding:utf-8 -*-
# Created by Jin(jinzhencheng@outlook.com) at 2018/01/18.

from flask import Blueprint

admin_blueprint = Blueprint("admin", __name__, template_folder="templates")

import login



