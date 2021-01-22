"""
author:czy
creat_date: 2021/1/22 10:22
u_date: 2021/1/22 10:22
reversion:1.0
file_name: demo2
"""
from flask import Flask, render_template

demo2 = Flask(__name__)


@demo2.route("/")
def index():
    name = "十三"
    age = "17"
    return render_template("index.html", **locals())


if __name__ == '__main__':
    demo2.run(debug=True)
