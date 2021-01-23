"""
author:czy
creat_date: 2021/1/22 11:39
u_date: 2021/1/22 11:39
reversion:1.0
file_name: demo4
"""
from flask import Flask, render_template, request, redirect, url_for, flash, session
import os
demo3 = Flask(__name__)
demo3.secret_key=os.urandom(24)

story = {
    "name": "我被困在同一天一千年",
    "author": "丧择",
    "article": [
        {
            "id": 1,
            "title": "第1章 我被困在同一天一千年",
            "content": "“你说你睡过我一千次？”夜色即将落幕。"
        },
        {
            "id": 2,
            "title": "第2章 替你活出精彩",
            "content": "阳光透过窗户，洒在床上，照在卫仙儿的脸上，恬静而美丽。早上七点，卫仙儿缓缓睁开眼睛"
        },
        {
            "id": 3,
            "title": "第3章 狠人，什么都知道的王成！",
            "content": "这一刻，房间内，卫千琴威势十足，一双审视的目光打量王成。"
        },
    ]
}

users = [
    {
        "email": "111@qq.com",
        "password": "1"
    },
]


@demo3.route("/")
def index():
    articles = story["article"]
    return render_template("index_demo3.html", **locals())


@demo3.route("/<int:pk>")
def detail(pk):
    for a in story["article"]:
        if a["id"] == pk:
            article = a
    return render_template("detail.html", **locals())


@demo3.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html", **locals())
    elif request.method == "POST":
        user = None
        email = request.form.get("email")
        password = request.form.get("password")
        for u in users:
            if u["email"] == email and u["password"] == password:
                session["user"] = email
                return redirect(url_for('index'))
        flash("用户名或密码错误")
        return redirect(url_for('login'))


@demo3.route("/regist", methods=["GET", "POST"])
def regist():
    if request.method == "GET":
        return render_template("regist.html", **locals())
    elif request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
        password2 = request.form.get("password2")
        for u in users:
            if u["email"] == email:
                flash("邮箱已被注册")
                return redirect(url_for("regist"))
        if password != password2:
            flash("两次密码不一致")
            return redirect(url_for("regist"))
        users.append(
            {
                "email": email,
                "password": password
            }
        )
        return redirect(url_for("login"))


@demo3.route("/logout")
def logout():
    session.pop("user")
    return redirect(url_for("index"))


if __name__ == '__main__':
    demo3.run(debug=True)
