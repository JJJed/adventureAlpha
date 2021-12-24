from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from genUser import User
import globalV as g
import numpy as np
import js2py
from temp import *
from bs4 import BeautifulSoup
import lxml
from io import StringIO, BytesIO


mycursor = g.db.cursor()


class Register(FlaskForm):
    # curID = open("currentID.txt", "w+")
    # conCurID = curID.read()
    # userID = conCurID
    # newID = int(conCurID) + 1
    # curID.truncate(0)
    # curID.write(newID)
    userName = StringField("Username:")
    userTag = StringField("User tag (<name>#<tag>)")
    userPswd = PasswordField("Password")
    submit = SubmitField("Register!")

    soup = BeautifulSoup('/templates/register.html', 'lxml')
    soup.find(id='RNope').i.replace_with("")
    file = open('/templates/register.html', 'w')
    file.write(str(BeautifulSoup.prettify()))


    eval_res, tempfile = js2py.run_file("static/js/register/RNope.js")
    tempfile.RNope(1)

    # newUsrFile = open("users/" + conCurID + ".txt", "w+")
    # newUsrFile.write("Name: " + userName + "\n")
    # newUsrFile.write("Tag:" + userTag + "\n")
    # newUsrFile.write("Password" + userPswd + "\n")
    # newUsrFile.write("ID: "+ userID + "\n")
    newUsr = User(str(userName), str(userTag), str(userPswd))

    mycursor.execute("SELECT * FROM `users` WHERE `name` = " + str(userName) + " && `tag` = " + str(userTag))
    rows = mycursor.fetchall()
    rowcount = int(mycursor.rowcount)

    if rowcount == 0:
        soup = BeautifulSoup('/templates/register.html', 'lxml')
        soup.find(id='RNope').i.replace_with("")
        file = open('/templates/register.html', 'w')
        file.write(str(BeautifulSoup.prettify()))

        mycursor.execute("INSERT INTO `users`(`name`, `tag`, `passwd`) VALUES (%s, %s, %s)",
                         (str(userName), str(userTag), str(userPswd)))
        g.db.commit()

        mycursor.execute("SELECT `id` from `users` WHERE `name` = %s && `tag` = %s && `passwd` = %s", (str(userName), str(userTag), str(userPswd)))
        rows = mycursor.fetchall()
        for row in rows:
            usrID = row[0]

        mycursor.execute("INSERT INTO `userInv`(`id`) VALUES (%s)", (usrID))
        g.db.commit()

        render_template("login.html")
    elif rowcount > 0:
        soup = BeautifulSoup('/templates/register.html', 'lxml')
        soup.find(id='RNope').i.replace_with("Sorry that Username/Tag combination is already taken!")
        file = open('/templates/register.html', 'w')
        file.write(str(BeautifulSoup.prettify()))


class Login(FlaskForm):
    userNAME = StringField("Username:")
    userTAG = StringField("User tag (<name>#<tag>)")
    userPSWD = PasswordField("Password")
    submit0 = SubmitField("Login!")

    soup = BeautifulSoup('/templates/login.html', 'lxml')
    soup.find(id='LNope').i.replace_with("")
    file = open('/templates/login.html', 'w')
    file.write(str(BeautifulSoup.prettify()))

    mycursor.execute(
        "SELECT * FROM `users` WHERE `name` = " + userNAME + " && `tag` = " + userTAG + " && `passwd` = " + userPSWD)
    rows = mycursor.fetchall()
    rowcount = int(mycursor.rowcount)

    mycursor.execute()

    mycursor.execute(
        "SELECT `id` FROM `users` WHERE `name` = " + userNAME + " && `tag` = " + userTAG + " && `passwd` = " + userPSWD)
    rows0 = mycursor.fetchall()

    if rowcount == 1:
        soup = BeautifulSoup('/templates/login.html', 'lxml')
        soup.find(id='LNope').i.replace_with("")
        file = open('/templates/login.html', 'w')
        file.write(str(BeautifulSoup.prettify()))
        for row in rows0:
            usrID = row[0]
            render_template("home.html", id=usrID)
    elif rowcount == 0:
        soup = BeautifulSoup('/templates/login.html', 'lxml')
        soup.find(id='LNope').i.replace_with("Incorrect Username/Tag/Password!")
        file = open('/templates/login.html', 'w')
        file.write(str(BeautifulSoup.prettify()))
