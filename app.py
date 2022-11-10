from flask import Flask, render_template, json
from flask_mysqldb import MySQL
from flask import request
from dotenv import load_dotenv, find_dotenv
import os
import database.db_connector as db

# Configuration
app = Flask(__name__)

# Load our environment variables from the .env file in the root of our project.
load_dotenv(find_dotenv())

# database connection info
app.config["MYSQL_HOST"] = os.environ.get("340DBHOST")
app.config["MYSQL_USER"] = os.environ.get("340DBUSER")
app.config["MYSQL_PASSWORD"] = os.environ.get("340DBPW")
app.config["MYSQL_DB"] = os.environ.get("340DB")
app.config["MYSQL_CURSORCLASS"] = "DictCursor"

mysql = MySQL(app)

# Routes 

@app.route('/')
def root():
    return render_template("main.j2")

@app.route('/dinosaurs', methods=["POST", "GET"])
def dinosaurs():
    # Grab Dinosaurs data so we send it to our template to display
    if request.method == "GET":
        # mySQL query to grab all the people in bsg_people
        query = "SELECT Dinosaurs.id AS 'ID', Dinosaurs.name AS 'Name', Species.species_name AS 'Species', Locations.location_name AS 'Location', Dinosaurs.health_status AS 'Status' FROM Dinosaurs INNER JOIN Species ON Dinosaurs.species_id = Species.id INNER JOIN Locations ON Dinosaurs.location_id = Locations.id"
        cur = mysql.connection.cursor()
        cur.execute(query)
        data = cur.fetchall()

        # mySQL query to grab planet id/name data for our dropdown
        # query2 = "SELECT id, name FROM bsg_planets"
        # cur = mysql.connection.cursor()
        # cur.execute(query2)
        # homeworld_data = cur.fetchall()

        # render edit_people page passing our query data and homeworld data to the edit_people template
        return render_template("dinosaurs.j2", data=data)


@app.route('/species')
def species():
    # Write the query and save it to a variable
    query = "SELECT * FROM Species;"

    # The way the interface between MySQL and Flask works is by using an
    # object called a cursor. Think of it as the object that acts as the
    # person typing commands directly into the MySQL command line and
    # reading them back to you when it gets results
    cur = mysql.connection.cursor()
    cur.execute(query)
    # The cursor.fetchall() function tells the cursor object to return all
    # the results from the previously executed
    results = cur.fetchall()

    # Sends the results back to the web browser.
    # return results
    return render_template("species.j2", Species=results)


@app.route('/dinosaurAssignments')
def dinosaurAssignments():
    # Write the query and save it to a variable
    query = "SELECT * FROM Employees_To_Dinosaurs;"

    # The way the interface between MySQL and Flask works is by using an
    # object called a cursor. Think of it as the object that acts as the
    # person typing commands directly into the MySQL command line and
    # reading them back to you when it gets results
    cur = mysql.connection.cursor()
    cur.execute(query)
    # The cursor.fetchall() function tells the cursor object to return all
    # the results from the previously executed
    results = cur.fetchall()

    # Sends the results back to the web browser.
    # return results
    return render_template("dinosaurAssignments.j2", dinosaurAssignments=results)

@app.route('/employees')
def employees():
    # Write the query and save it to a variable
    query = "SELECT * FROM Employees;"

    # The way the interface between MySQL and Flask works is by using an
    # object called a cursor. Think of it as the object that acts as the
    # person typing commands directly into the MySQL command line and
    # reading them back to you when it gets results
    cur = mysql.connection.cursor()
    cur.execute(query)
    # The cursor.fetchall() function tells the cursor object to return all
    # the results from the previously executed
    results = cur.fetchall()

    # Sends the results back to the web browser.
    # return results
    return render_template("employees.j2", Species=results)


@app.route('/locations')
def locations():
    # Write the query and save it to a variable
    query = "SELECT * FROM Locations;"

    # The way the interface between MySQL and Flask works is by using an
    # object called a cursor. Think of it as the object that acts as the
    # person typing commands directly into the MySQL command line and
    # reading them back to you when it gets results
    cur = mysql.connection.cursor()
    cur.execute(query)
    # The cursor.fetchall() function tells the cursor object to return all
    # the results from the previously executed
    results = cur.fetchall()

    # Sends the results back to the web browser.
    # return results
    return render_template("locations.j2", Locations=results)


@app.route('/visitors')
def visitors():
    # Write the query and save it to a variable
    query = "SELECT * FROM Visitors;"

    # The way the interface between MySQL and Flask works is by using an
    # object called a cursor. Think of it as the object that acts as the
    # person typing commands directly into the MySQL command line and
    # reading them back to you when it gets results
    cur = mysql.connection.cursor()
    cur.execute(query)
    # The cursor.fetchall() function tells the cursor object to return all
    # the results from the previously executed
    results = cur.fetchall()

    # Sends the results back to the web browser.
    # return results
    return render_template("visitors.j2", Visitors=results)
# Listener

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 1857)) 
    #                                 ^^^^
    #              You can replace this number with any valid port
    
    app.run(port=port, debug=True) 