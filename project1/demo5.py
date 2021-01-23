"""
author:czy
creat_date: 2021/1/22 11:39
u_date: 2021/1/22 11:39
reversion:1.0
file_name: demo3
"""
from flask import Flask, render_template, request, redirect, url_for
import os
from views.user import userbp
from views.main_test import mainbp

demo3 = Flask(__name__)
demo3.register_blueprint(userbp)
demo3.register_blueprint(mainbp)

demo3.secret_key = os.urandom(24)

if __name__ == '__main__':
    demo3.run(debug=True)
