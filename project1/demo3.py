"""
author:czy
creat_date: 2021/1/22 11:39
u_date: 2021/1/22 11:39
reversion:1.0
file_name: demo3
"""
from flask import Flask, render_template

demo3 = Flask(__name__)

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


if __name__ == '__main__':
    demo3.run(debug=True)
