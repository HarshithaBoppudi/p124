from flask import Flask,jsonify,request

app=Flask(__name__)

contacts=[
    {
    "id":1,
    "contact":9494153948,
    "name":"harshitha",
    "done":False

    },
    {
    "id":2,
    "contact":9494262738,
    "name":"vimal",
    "done":False

    }

]

@app.route("/add-data",methods=["POST"])
def add_data():
    if not request.json:
        return jsonify({
            "status":"Error",
            "message":"provide correct data"
        }),400
    contact= {
    "id":contacts[-1]['id']+1,
    "contact":request.json["contact"],
    "name":request.json["name"],
    "done":False

    }
    contacts.append(contact) 
    return jsonify({
        "status":"success",
        "message":"data added successfully"
    })

@app.route("/get-data")
def get_data():
    return jsonify({
        "data":contacts,
        
    })    
if __name__=="__main__":
    app.run(debug=True)     

