from flask import Flask, request, render_template
import sqlite3
app = Flask(__name__)

@app.route("/create", methods = ['GET', 'POST'])
def AddUser():
   #print(request.form['newUserName'])
   #print(request.form['newUserID'])
   #print(request.form['newUserPoints'])
   #print(type(request.form['newUserName']))
   con = sqlite3.connect("CRUDDatabase")
   cur = con.cursor()
   flag = True
   try: 
      (int)(request.form['newUserID'])
      (int)(request.form['newUserPoints'])
   except ValueError:
      flag = False
      print("User did not type an integer in the correct places")
   print(len(request.form['newUserName']))
   if(len(request.form['newUserName']) == 0 or
      len(request.form['newUserID']) == 0 or
      len(request.form['newUserPoints']) == 0 or not flag):
      print(isinstance(request.form['newUserID'], int))
      print(isinstance(request.form['newUserID'], int))
      print("This will not be added to the database")

   else:
      cur.execute("INSERT INTO PlayerData (Name, Id, Points) VALUES (?, ?, ?)",
            (request.form['newUserName'], request.form['newUserID'], request.form['newUserPoints']))
      #cur.execute("INSERT INTO PlayerData (Name, Id, Points) VALUES ('Steve Smith', 211, 80)")
      con.commit()
      #I'll remove all tables for testing
      #I'll output results in the actual website
      #cur.execute("CREATE TABLE IF NOT EXISTS movie(title, year, score)")
   
   cur.execute("SELECT * FROM PlayerData")
   rows = cur.fetchall()
   con.close()
   return render_template('CRUDWebsite.html', players=rows, foundPlayer = [])

@app.route("/read", methods = ['GET', 'POST'])
def FindUser():
   con = sqlite3.connect("CRUDDatabase")
   cur = con.cursor()
   cur.execute("SELECT * FROM PlayerData")
   rows = cur.fetchall()
   f_player = ["This player is not in the database"]
   for row in rows:
      if row[0] == request.form['findUser']:
         f_player = row
         break
   
   con.close()
   return render_template('CRUDWebsite.html', players=rows, foundPlayer = f_player)

@app.route("/update", methods = ['GET', 'POST'])
def EditUser():
   con = sqlite3.connect("CRUDDatabase")
   cur = con.cursor()

   flag = True
   try: 
      (int)(request.form['IDChange'])
      (int)(request.form['scoreChange'])
   except ValueError:
      flag = False
      print("User did not type an integer in the correct places")

   cur.execute("SELECT * FROM PlayerData")
   rows = cur.fetchall()

   inDB = False
   for row in rows:
      if (request.form['userToUpdate'] == row[0]):
         print("This user is in the database")
         inDB = True

   if(len(request.form['userToUpdate']) == 0 or
      len(request.form['IDChange']) == 0 or
      len(request.form['scoreChange']) == 0 or not flag or not inDB):

      print("No updates made to database")
   else:

      cur.execute("UPDATE PlayerData SET Name = ?, Id = ?, Points = ? WHERE Name = ?",
         (request.form['userToUpdate'], request.form['IDChange'], request.form['scoreChange'], request.form['userToUpdate']))
      #cur.execute("UPDATE PlayerData SET (Name, Id, Points) VALUES (?, ?, ?)",
      #      (request.form['newUserName'], request.form['newUserID'], request.form['newUserPoints']))
      
   cur.execute("SELECT * FROM PlayerData")
   rows = cur.fetchall()
   con.close()
   return render_template('CRUDWebsite.html', players=rows, foundPlayer = [])

@app.route("/delete", methods = ['GET', 'POST'])
def RemoveUser():
   con = sqlite3.connect("CRUDDatabase")
   cur = con.cursor()
   cur.execute("DELETE FROM PlayerData WHERE Name = ?", (request.form['removeUser'],))
   cur.execute("SELECT * FROM PlayerData")
   rows = cur.fetchall()
   con.close()
   return render_template('CRUDWebsite.html', players=rows, foundPlayer = [])

@app.route("/")
def hello():
   con = sqlite3.connect("CRUDDatabase")
   cur = con.cursor()

   #I'll remove all tables for testing
   #I'll output results in the actual website
   #cur.execute("CREATE TABLE IF NOT EXISTS movie(title, year, score)")
   cur.execute("DROP TABLE IF EXISTS PlayerData")
   cur.execute("CREATE TABLE IF NOT EXISTS PlayerData(Name TEXT, Id INTEGER, Points INTEGER)")
   cur.execute("INSERT INTO PlayerData (Name, Id, Points) VALUES ('Steve Smith', 211, 80)," + 
               "('Jian Wong', 122, 92), ('Chris Peterson', 213, 91), ('Sai Patel', 524, 94)," + 
               "('Andrew Whitehead', 425, 99), ('Lynn Roberts', 626, 90), ('Rovert Sanders', 287, 75)")
   con.commit()
   cur.execute("SELECT * FROM PlayerData")
   rows = cur.fetchall()

   print(type(rows))
   print("Test")
   #con.commit()
   con.close()
   return render_template('CRUDWebsite.html', players=rows, foundPlayer = [])

if __name__ == '__main__':
   app.run(debug=True)