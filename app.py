#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
from config import *

from flask import Flask, request, render_template, make_response, Response
from flask_login import LoginManager
from flask_wtf.csrf import CSRFProtect
from flask_bootstrap import Bootstrap
from flask_caching import Cache


#初期ページ
@flask_app.route('/', methods=['GET'])
@flask_app.route('/index', methods=['GET'])
def index():
    return render_template(
        'index.html',
        title = company_name + ' トップページ',
        dash_id = "today_rec_count",
        dash_src_url = "/dash/toppage_dashboard/")


if __name__ == '__main__':
    app_run()
