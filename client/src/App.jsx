import { useState, useEffect } from "react";
import ContactList from "./ContactList";
import ContactForm from "./ContactForm";
import "./App.css";
import "./index.css";

function App() {
  const [contact, setContact] = useState([]);
  const [isModalOpen, setIsModalOpened] = useState(false);
  const [currentContact, setCurrentContact] = useState({});

  useEffect(() => {
    fetchContacts();
  }, []);

  const fetchContacts = async () => {
    const response = await fetch("http://127.0.0.1:5000/contact");
    const data = await response.json();
    setContact(data.contacts);
  };

  const closeModal = () => {
    setIsModalOpened(false);
    setCurrentContact({});
  };

  const openCreateModal = () => {
    if (!isModalOpen) setIsModalOpened(true);
  };

  const openEditModal = (contact) => {
    if (isModalOpen) return;
    setCurrentContact(contact);
    setIsModalOpened(true);
  };

  const onUpdate = () => {
    closeModal();
    fetchContacts();
  };

  return (
    <div className="flex items-center justify-center min-h-screen bg-gray-100">
      <div className="flex flex-col border border-red-300 py-6 px-4 m-2 w-full max-w-3xl bg-white shadow-md">
        <ContactList
          contacts={contact}
          updateContact={openEditModal}
          updateCallback={onUpdate}
        />
        <button
          className="p-2 bg-blue-900 text-white rounded-md mt-4 w-36 mx-auto"
          onClick={openCreateModal}
        >
          New Contact
        </button>
        {isModalOpen && (
          <div className="fixed inset-0 flex items-center justify-center bg-black bg-opacity-50">
            <div className="bg-white p-6 rounded-md shadow-md relative">
              <span
                className="absolute top-2 right-2 cursor-pointer text-xl"
                onClick={closeModal}
              >
                &times;
              </span>
              <ContactForm
                existingContact={currentContact}
                updateCallback={onUpdate}
              />
            </div>
          </div>
        )}
      </div>
    </div>
  );
}

export default App;
