// UserList.js

import Cookies from "universal-cookie";
import { submitMessage } from "../services/submitMessage";
import MessagesForm from "../components/MessageForm";

// UserList.js
import React, { useEffect, useState } from 'react';
import axios from 'axios';

function UserList() {
  const [professionals, setProfessionals] = useState([]);

  useEffect(() => {
    async function fetchProfessionals() {
      try {
        const response = await axios.get('http://localhost:8000/search/professionals');
        setProfessionals(response.data);
      } catch (error) {
        console.error('Error fetching professionals', error);
      }
    }

    fetchProfessionals();
  }, []);

  return (
    <div>
      <h2>Professional List</h2>
      <ul>
        {professionals.map((professional) => (
          <li key={professional.id}>{professional.name}</li>
        ))}
      </ul>
    </div>
  );
}

export default UserList;
