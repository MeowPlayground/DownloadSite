from flask import Flask, render_template, url_for
from common.fileMaster import getfile, getsize, toSrc_floder
from common.item import getImg

app = Flask(__name__)


@app.route("/")
def i():
    return render_template('index.html')


@app.route("/file/<path:name>")
def index(name):
    f = getfile(name)

    if f[1] == 200:

        fileList = f[0][0]
        folderList = f[0][1]
        data = []

        if len(fileList) > 0:
            for i in fileList:
                if i == '':
                    break
                imgDate = getImg(name, i)
                data.append({
                    "fileName": i,
                    "imgSrc": url_for('static', filename=imgDate[0]),
                    "size": getsize(name, i),
                    "suffix": imgDate[1],
                    "url": name + "/" + i
                })

        folderData = []
        if len(folderList) > 0:
            for i in folderList:
                if i == '':
                    break
                folderData.append({
                    "folderName": i,
                    "toSrc": "/file/" + name + "/" + i
                })

        return render_template('download.html', data=data, folderData=folderData, route="/"+name)
    else:
        return render_template('404.html')


if __name__ == '__main__':
    app.run(debug=True)