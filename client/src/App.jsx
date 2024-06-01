import { useState, useEffect } from "react";
import ContactList from "./ContactList";
import ContactForm from "./ContactForm";

import "./App.css";

function App() {
  const [contact, setContact] = useState([]);
  const [isModalOpen, setIsModalOpened] = useState(false)

  useEffect(() => {
    fetchContacts();
  }, []);

  const fetchContacts = async () => {
    const response = await fetch("http://127.0.0.1:5000/contact"); // fetch contacts from server's url.
    const data = await response.json();
    setContact(data.contacts); // contacts from the get request from server.
    console.log(data.contacts);
  }
 
  const closeModal = () => {
    setIsModalOpened(false)
  }

  const openCreateModal = () =>{

if (!isModalOpen) setIsModalOpened(true)
  }

  return (
    <>
      <ContactList contacts={contact} />
      <button onClick={openCreateModal}>New Contact</button>
      {isModalOpen && (
        <div className="modal">
          <div className="modal-con">
            <span className="close" onClick={closeModal}>&times;</span>   
            <ContactForm />
          </div>
        </div>
      )}
    </>
  );
}

export default App;
