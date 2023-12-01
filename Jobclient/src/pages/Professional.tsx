import Cookies from "universal-cookie";
// UserList.js
import React, { useEffect, useState } from 'react';
import { getApprovedProfessionals } from  "../services/getAllProfessionals.js";

function UserList() {
  const [professionals, setProfessionals] = useState([]);
  const cookies = new Cookies();
  const getAuthToken = () => cookies.get('authToken');
  let authToken = getAuthToken();

  useEffect(() => {
    async function fetchProfessionals() {
      try {
        const data = await getApprovedProfessionals(authToken);
        setProfessionals(data);
      } catch (error) {
        console.error('Error fetching professionals', error);
      }
    }

    fetchProfessionals();
  }, []);

  return (
    <div style={{ padding: '20px' }}>
      <h2>Professional List</h2>
      <div style={{ display: 'flex', flexWrap: 'wrap' }}>
        {professionals.map((professional) => (
          <div
            key={professional.id}
            style={{
              border: '1px solid #ccc',
              padding: '10px',
              margin: '10px',
              width: '200px',
              textAlign: 'center',
            }}
          >
            <p>{professional.first_name} {professional.last_name}</p>
            <p>Status: {professional.status}</p>
          </div>
        ))}
      </div>
    </div>
  );
}

export default UserList;
