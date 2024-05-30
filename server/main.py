from flask import request, jsonify
from config import app, db
from models import Contact

# Decorator for contact using the get method.

@app.route("/contact", methods =["GET"])


def get_contacts():
    contacts = Contact.query.all() # Get all context  from Contact db.

# Convert each contact object in the 'contacts' list to a JSON-serializable dictionary
# using the 'to_json' method, and store the resulting list of dictionaries in 'json_contacts'.
    json_contacts = list(map(lambda x: x.to_json(), contacts))
    return (jsonify({"contacts": json_contacts })), 200 # data is returned in json format

# Decorator for contact using the post(create)method.

@app.route("/create_contact", methods=["POST"])
def create_contact():
    # from python(from db) to js(from frontend).
    first_name = request.json.get("firstName")
    last_name = request.json.get("lastName")
    email = request.json.get("email")

    if not first_name or not last_name or email:
        return(
            jsonify({"message": "Must include first name, last name and email"}), 400, # bad request
        )
 # add to db.
    new_contact = Contact(first_name=first_name, last_name=last_name, email=email)
    try:
        db.session.add(new_contact)# add to db.
        db.session.commit()# sent and save to db.

# used to show errors when wrong data is entered in the db.
    except Exception as e:
        return jsonify({"message":str(e)}), 400   # if not a str return error message, Status code bad request.

    # When user is created.

    return jsonify({"message": "User Created! ✅"}), 201

# To update Contact.

@app.route("/update_contact/<int:user_id>", methods=["PATCH"]) # update is by id. 

 # Defines a function to update a contact's details using the user ID.

def update_contact(user_id):

# Queries(retrieve) the database for a Contact object with the primary key 'user_id'.

    contact = Contact.query.get(user_id)

# If no such contact exists, 'contact' will be None
    if not contact:

        return({"message": "USer not found!"}), 404 # Not found

  # Retrieves the JSON data from the incoming request.
    data = request.json

 # This data contains the new values for the contact's fields.
# If the field is not provided in the request, it retains the existing value.

    contact.first_name = data.get("firstName", contact.first_name)
    contact.last_name = data.get("lastName", contact.last)
    contact.email = data.get("email", contact.email)    

    #make the changes to the db

    db.session.commit() 

    return jsonify ({"message": "User Updated Successfully✨"}), 200



# Handling Delete request

@app.route("/delete_contact/<int:user_id>", methods = ["DELETE"])

# A function to handle the delete request.
def delete_contact(user_id):

# Retrieve the database for a Contact object with the primary key 'user_id'.

    contact = Contact.query.get(user_id)

    if not contact:
        return ({"message": "Contact not found"}), 404

    db.session.delete(contact) 
    db.session.commit()

    return ({"message":"Contact Deleted 🗑"})   


              

    
# Run the application.
if __name__ == "__main__":
    # Check if the script is being run directly (not imported as a module).
    with app.app_context():
        # Create an application context which is necessary for database operations.
        db.create_all()
        # Create all tables defined in SQLAlchemy models if they don't exist already.
    app.run(debug=True)
    # Run the Flask application with debugging enabled for easier development.
