# Import the dependencies.
from flask import Flask, jsonify
import datetime as dt
from sqlalchemy import func
from sqlalchemy.orm import Session



#################################################
# Database Setup
#################################################


# reflect an existing database into a new model
app = Flask(__name__)

@app.route("/")
def welcome():
    return (
        f"Welcome to the Climate App API!<br/><br/>"
        f"Available routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/&lt;start&gt;<br/>"
        f"/api/v1.0/&lt;start&gt;/&lt;end&gt;<br/>"
    )
# reflect the tables
@app.route("/api/v1.0/precipitation")
def precipitation():
    return jsonify(precipitation_data)

@app.route("/api/v1.0/stations")
def stations():
    return jsonify(station_data)

@app.route("/api/v1.0/tobs")
def tobs():
    return jsonify(tobs_data)

@app.route("/api/v1.0/<start>")
@app.route("/api/v1.0/<start>/<end>")
def temp_range(start, end=None):
    return jsonify(temp_stats)

if __name__ == "__main__":
    app.run(debug=True)

