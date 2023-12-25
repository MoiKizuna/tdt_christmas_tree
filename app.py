from flask import Flask, render_template

app = Flask(__name__,
            static_folder='dist',   # 指定静态文件夹为 dist
            template_folder='dist')  # 指定模板文件夹为 dist


@app.route('/')
def home():
    return render_template('index.html')  # 从 dist 文件夹加载 index.html


if __name__ == '__main__':
    app.run(debug=True)
