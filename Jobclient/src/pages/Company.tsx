import React, { useEffect, useState } from 'react';
import { getApprovedCompanies } from '../services/getAllCompanies.js';
import Cookies from 'universal-cookie';

interface Professional {
  id: number;
  first_name: string;
  last_name: string;
  status: string;
}

function CompaniesList() {
  const [companies, setCompanies] = useState<Professional[]>([]);
  const cookies = new Cookies();
  const getAuthToken = () => cookies.get('authToken');
  let authToken = getAuthToken();

  useEffect(() => {
    async function fetchCompanies() {
      try {
        const data = await getApprovedCompanies(authToken);
        setCompanies(data);
      } catch (error) {
        console.error('Error fetching companies', error);
      }
    }

    fetchCompanies();
  }, []);

  // ADD MORE ELEMENTS TO SHOW MORE DATA FOR THE PROFESSIONAL && SHOULD FIX THE PHOTO 
  return (
    <div style={styles.container}>
      <h2 style={styles.heading}>Companies List</h2>
      <div style={styles.professionalsContainer}>
        {companies.map((company) => (
          <div key={company.id} style={styles.professionalCard}>
            <p style={styles.name}>
              {company.name}
            </p>
            {/* <p style={styles.status}>Status: {professional.status}</p> */}
            <p style={styles.description}>{company.description}</p>
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

export default CompaniesList;
