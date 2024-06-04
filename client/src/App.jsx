import { useState, useEffect } from "react";
import ContactList from "./ContactList";
import ContactForm from "./ContactForm";
import "./App.css";
import "./index.css"

function App() {
  const [contact, setContact] = useState([]);
  const [isModalOpen, setIsModalOpened] = useState(false)
  const [currentContact, setCurrentContact] = useState({});

  useEffect(() => {
    fetchContacts();
  }, []);

  const fetchContacts = async () => {
    const response = await fetch("http://127.0.0.1:5000/contact"); // fetch contacts from server's url.
    const data = await response.json();
    setContact(data.contacts); // contacts from the get request from server.
  }
 
  const closeModal = () => {
    setIsModalOpened(false)
    setCurrentContact({})
  }

  const openCreateModal = () =>{

if (!isModalOpen) setIsModalOpened(true)
  }
  const openEditModal = (contact) =>{

    if (isModalOpen) return 
    setCurrentContact(contact)
    setIsModalOpened(true)
  }

  const onUpdate = () => {
    closeModal()
    fetchContacts()
  }

  return (
    <>
      <ContactList
        contacts={contact}
        updateContact={openEditModal}
        updateCallback={onUpdate}
      />
      <button onClick={openCreateModal}>New Contact</button>
      {isModalOpen && (
        <div className="modal">
          <div className="modal-con">
            <span className="close" onClick={closeModal}>
              &times;
            </span>
            <ContactForm
              existingContact={currentContact}
              updateCallback={onUpdate}
            />
          </div>
        </div>
      )}
    </>
  );
}

export default App;
