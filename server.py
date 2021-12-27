from flask import Flask, render_template, jsonify, url_for, request
from forms import Register, Login
import globalV as g

app = Flask(__name__)
application = app
app.config["SECRET_KEY"] = "1234-asdf-!@#$-ASDF"

mycursor = g.db.cursor()


# setID = open("currentID.txt", "w+")
# setID.truncate(0)
# setID.write("0")

# g.init()

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    form = Register()
    sub = False
    if form.is_submitted():
        result = request.form
        sub = True
        return render_template("registrationComplete.html", result=result)
    return render_template("register.html", form=form)

@app.route("/reg_check", methods=["GET", "POST"])
def reg_check():
    if request.method == 'POST':
        data = request.get_json()
        user_name = str(data[0]["name"])
        user_tag = str(data[1]["tag"])
        user_passwd = str(data[2]["passwd"])
        mycursor.execute("""SELECT * FROM `users` WHERE `name` = '%s' AND `tag` = '%s';""" % (user_name, user_tag))
        rows = mycursor.fetchall()
        rowcount = int(mycursor.rowcount)
        if rowcount > 0:
            return jsonify('', render_template("/data/data1", x=0))
        elif rowcount == 0:
            mycursor.execute("""INSERT INTO `users`(`name`, `tag`, `passwd`) VALUES ('%s', '%s', '%s');""" % (user_name, user_tag, user_passwd))
            g.db.commit()

            mycursor.execute("""SELECT `id` from `users` WHERE `name` = '%s' AND `tag` = '%s' AND `passwd` = '%s';""" % (user_name, user_tag, user_passwd))
            rows = mycursor.fetchall()
            for row in rows:
                usrID = row[0]

            mycursor.execute("INSERT INTO `userInv`(`id`) VALUES (%s);", (usrID))
            g.db.commit()
            return jsonify('', render_template("/data/data1", x=1))

@app.route("/log_check", methods=["GET", "POST"])
def log_check():
    if request.method == 'POST':
        data = request.get_json()
        user_name = str(data[0]["name"])
        user_tag = str(data[1]["tag"])
        user_passwd = str(data[2]["passwd"])

        mycursor.execute("""SELECT * FROM `users` WHERE `name` = '%s' AND `tag` = '%s' AND `passwd` = '%s';""" % (user_name, user_tag, user_passwd))
        rows = mycursor.fetchall()
        rowcount = int(mycursor.rowcount)

        mycursor.execute("""SELECT `id` FROM `users` WHERE `name` = '%s' AND `tag` = '%s' AND `passwd` = '%s';""" % (user_name, user_tag, user_passwd))
        rows0 = mycursor.fetchall()

        if rowcount == 1:
            for row in rows0:
                usrID = row
                render_template("home.html", id=usrID)
        elif rowcount == 0:
            return jsonify('', render_template("/data/data1", x=0))

@app.route("/login", methods=["GET", "POST"])
def login():
    form = Login()
    return render_template("login.html", form=form)


@app.route("/main")
def main():
    return render_template("home.html")


@app.route("/tree1", methods=['POST', 'GET'])
def tree1():
    g.treeSize = 0
    return jsonify('', render_template("/data/data1", x=0))


@app.route("/tree2", methods=['POST', 'GET'])
def tree2():
    g.treeSize = 1
    return jsonify('', render_template("/data/data1", x=1))


@app.route("/tree3", methods=['POST', 'GET'])
def tree3():
    g.treeSize = 2
    return jsonify('', render_template("/data/data1", x=2))


@app.route("/tree4", methods=['POST', 'GET'])
def tree4():
    axe = 0
    stat = 0
    if request.method == "POST":
        data = request.get_json()
        usrID = int(data[2]["userID"])
        mycursor.execute("SELECT `axe` FROM `userInv` WHERE `id` = %s", (usrID))
        rows = mycursor.fetchall()
        for row in rows:
            axe = row[0]
    mycursor.execute("SELECT `stat` FROM `items` WHERE `id` = %s", (axe))
    rows = mycursor.fetchall()
    for row in rows:
        stat = row[0]
    return jsonify('', render_template("/data/data1", x=stat))


@app.route("/render-forest", methods=['POST', 'GET'])
def renderForest():
    usrID = 0
    if request.method == "POST":
        data = request.get_json()
        usrID = int(data[0]["userID"])
    return render_template("mapSpots/forest.html", id=usrID)


if __name__ == "__main__":
    app.run()
