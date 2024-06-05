import React from "react";

const ContactList = ({ contacts, updateContact, updateCallback }) => {
  const onDelete = async (id) => {
    try {
      const options = {
        method: "DELETE",
      };
      const response = await fetch(
        `http://127.0.0.1:5000/delete_contact/${id}`,
        options
      );
      if (response.status === 200) {
        updateCallback();
      } else {
        console.error("Failed to delete");
      }
    } catch (error) {
      console.error("Error deleting contact:", error);
      alert("Error deleting contact");
    }
  };

  return (
    <div className="p-4">
      <h1 className="text-3xl font-serif mb-6 text-center">Contacts</h1>
      <table className="min-w-full bg-white border border-gray-300">
        <thead className="bg-gray-50">
          <tr>
            <th className="py-2 px-4 border-b border-gray-200">First Name</th>
            <th className="py-2 px-4 border-b border-gray-200">Last Name</th>
            <th className="py-2 px-4 border-b border-gray-200">Email</th>
            <th className="py-2 px-4 border-b border-gray-200">Actions</th>
          </tr>
        </thead>
        <tbody>
          {contacts.map((contact) => (
            <tr key={contact.id} className="hover:bg-gray-100">
              <td className="py-2 px-4 border-b border-gray-200">{contact.firstName}</td>
              <td className="py-2 px-4 border-b border-gray-200">{contact.lastName}</td>
              <td className="py-2 px-4 border-b border-gray-200">{contact.email}</td>
              <td className="py-2 px-4 border-b border-gray-200 space-x-2">
                <button
                  onClick={() => updateContact(contact)}
                  className="px-3 py-1 bg-blue-400 text-white rounded hover:bg-blue-800"
                >
                  Edit
                </button>
                <button
                  onClick={() => onDelete(contact.id)}
                  className="px-3 py-1 bg-red-700 text-white rounded hover:bg-red-600"
                >
                  Delete
                </button>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default ContactList;
