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
import urllib.request


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

    # with open('templates/register.html') as x:
    #     data = x.read()
    # soup = BeautifulSoup(data, 'lxml')
    # try:
    #     soup.find(id='RNope').decopose()
    # except AttributeError:
    #     print("sus")
    # with open('templates/register.html', 'w') as file:
    #     file.write(soup.prettify())

    # eval_res, tempfile = js2py.run_file("static/js/register/RNope.js")
    # tempfile.RNope(1)

    # newUsrFile = open("users/" + conCurID + ".txt", "w+")
    # newUsrFile.write("Name: " + userName + "\n")
    # newUsrFile.write("Tag:" + userTag + "\n")
    # newUsrFile.write("Password" + userPswd + "\n")
    # newUsrFile.write("ID: "+ userID + "\n")
    # newUsr = User(str(userName), str(userTag), str(userPswd))

    # mycursor.execute("""SELECT * FROM `users` WHERE `name` = '%s' AND `tag` = '%s';""" % (userName, userTag))
    # rows = mycursor.fetchall()
    # rowcount = int(mycursor.rowcount)
    #
    # if rowcount == 0:
    #     with open('templates/register.html') as x:
    #         data = x.read()
    #     soup = BeautifulSoup(data, 'lxml')
    #     try:
    #         soup.find(id='RNope').decopose()
    #     except AttributeError:
    #         print("sus")
    #     with open('templates/register.html', 'w') as file:
    #         file.write(soup.prettify())

    #     mycursor.execute("""INSERT INTO `users`(`name`, `tag`, `passwd`) VALUES ('%s', '%s', '%s');""" % (userName, userTag, userPswd))
    #     g.db.commit()
    #
    #     mycursor.execute("""SELECT `id` from `users` WHERE `name` = '%s' AND `tag` = '%s' AND `passwd` = '%s';""" % (str(userName), str(userTag), str(userPswd)))
    #     rows = mycursor.fetchall()
    #     for row in rows:
    #         usrID = row[0]
    #
    #     mycursor.execute("INSERT INTO `userInv`(`id`) VALUES (%s);", (usrID))
    #     g.db.commit()
    #
    #     render_template("login.html")
    # elif rowcount > 0:
    #     with open('templates/register.html') as x:
    #         data = x.read()
    #     soup = BeautifulSoup(data, 'lxml')
    #     new_tag = soup.new_tag('h5', id="RNope", style="color: crimson;")
    #     new_tag.string = "Sorry that Username/Tag combination is already taken!"
    #     soup.html.body.append(new_tag)
    #     with open('templates/register.html', 'w') as file:
    #         file.write(soup.prettify())


class Login(FlaskForm):
    userNAME = StringField("Username:")
    userTAG = StringField("User tag (<name>#<tag>)")
    userPSWD = PasswordField("Password")
    submit0 = SubmitField("Login!")

    # with open('templates/login.html') as x:
    #     data = x.read()
    # soup = BeautifulSoup(data, 'lxml')
    # try:
    #     soup.find(id='LNope').decopose()
    # except AttributeError:
    #     print("sus")
    # with open('templates/login.html', 'w') as file:
    #     file.write(soup.prettify())
    #
    # mycursor.execute("""SELECT * FROM `users` WHERE `name` = '%s' AND `tag` = '%s' AND `passwd` = '%s';""" % (userNAME, userTAG, userPSWD))
    # rows = mycursor.fetchall()
    # rowcount = int(mycursor.rowcount)
    #
    # mycursor.execute("""SELECT `id` FROM `users` WHERE `name` = '%s' AND `tag` = '%s' AND `passwd` = '%s';""" % (userNAME, userTAG, userPSWD))
    # rows0 = mycursor.fetchall()
    #
    # if rowcount == 1:
    #     with open('templates/register.html') as x:
    #         data = x.read()
    #     soup = BeautifulSoup(data, 'lxml')
    #     soup.find(id='LNope').decopose()
    #     with open('templates/login.html', 'w') as file:
    #         file.write(soup.prettify())
    #     for row in rows0:
    #         usrID = row[0]
    #         render_template("home.html", id=usrID)
    # elif rowcount == 0:
    #     with open('templates/register.html') as x:
    #         data = x.read()
    #     soup = BeautifulSoup(data, 'lxml')
    #     new_tag = soup.new_tag('h5', id="LNope", style="color: crimson;")
    #     new_tag.string = "Incorrect Username/Tag/Password!"
    #     soup.html.body.append(new_tag)
    #     with open('templates/login.html', 'w') as file:
    #         file.write(soup.prettify())
