import React, { useEffect, useState } from 'react';
import { getApprovedProfessionals } from '../services/getAllProfessionals.js';
import Cookies from 'universal-cookie';

interface Professional {
  id: number;
  first_name: string;
  last_name: string;
  status: string;
}

function UserList() {
  const [professionals, setProfessionals] = useState<Professional[]>([]);
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

  // ADD MORE ELEMENTS TO SHOW MORE DATA FOR THE PROFESSIONAL && SHOULD FIX THE PHOTO 
  return (
    <div style={styles.container}>
      <h2 style={styles.heading}>Professional List</h2>
      <div style={styles.professionalsContainer}>
        {professionals.map((professional) => (
          <div key={professional.id} style={styles.professionalCard}>
            <p style={styles.name}>
              {professional.first_name} {professional.last_name}
            </p>
            <p style={styles.status}>Status: {professional.status}</p>
            <p style={styles.summary}>{professional.summary}</p>
            {/* <p style={styles.image}>{professional.image}</p> */}
          </div>
        ))}
      </div>
    </div>
  );
}

interface CSSProperties {
  [key: string]: string | number | CSSProperties;
}

const styles: { [key: string]: CSSProperties } = {
  container: {
    padding: '20px',
  },
  heading: {
    fontSize: '24px',
    marginBottom: '15px',
    color: '#333',
  },
  professionalsContainer: {
    display: 'flex',
    flexWrap: 'wrap' as 'wrap',
  },
  professionalCard: {
    border: '2px solid #ccc',
    padding: '15px',
    margin: '15px',
    width: '2000px',
    // textAlign: 'center',
    borderRadius: '8px',
    boxShadow: '0 4px 8px rgba(0, 0, 0, 0.1)',
    transition: 'transform 0.3s ease-in-out',
    '&:hover': {
      transform: 'scale(1.05)',
    },
  },
  name: {
    fontSize: '18px',
    fontWeight: 'bold',
    margin: '0',
    color: '#555',
  },
  status: {
    color: '#777',
    margin: '8px 0 0',
  },
};

export default UserList;
