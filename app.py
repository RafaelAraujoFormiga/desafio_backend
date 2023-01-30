from dict import CNAB
from flask import Flask, render_template, request


app = Flask(__name__)

data = []


def open_file(file):

    for line in file:
        line = line.rstrip().decode("utf-8")
        dict = CNAB(
            line[0],
            line[1:9],
            line[9:19],
            line[19:30],
            line[30:42],
            line[42:48],
            line[48:62],
            line[62:81],
        )
        data.append(
            {
                dict.type,
                dict.date,
                dict.value,
                dict.store_name,
                dict.store_owner,
                dict.card,
                dict.cpf,
                dict.hour,
            }
        )


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/upload", methods=["POST", "GET"])
def upload():
    file = request.files["file-sent"]

    open_file(file)
    return render_template("list.html", data)


if __name__ == "__main__":
    app.run(debug=True)
