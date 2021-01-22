"""
author:czy
creat_date: 2021/1/22 9:37
u_date: 2021/1/22 9:37
reversion:1.0
file_name: demo1
"""
from flask import Flask

demo1 = Flask(__name__)


@demo1.route("/")
def index():
    return "这里是Flask的主页"


@demo1.route("/<int:pk>")
def detail(pk):
    return f"这里是Flask {pk} 的详情页"


if __name__ == '__main__':
    demo1.run(host="192.168.11.15", port="1313", debug=True)
