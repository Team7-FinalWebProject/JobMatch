import React, { useEffect, useState } from 'react';
import { getApprovedProfessionals } from '../services/getAllProfessionals.js';
import Cookies from 'universal-cookie';
import Layout from './Layout.js';
import backgroundSVG from '../assets/subtle-prism.svg'
import { getImage } from '../services/getImage.js';

interface Professional {
  id: number;
  first_name: string;
  last_name: string;
  status: string;
  image: string;
  username: string;
  summary: string;
}

function UserList() {
  const [professionals, setProfessionals] = useState<Professional[]>([]);
  const [imgs, setImgs] = useState({});
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

  
  const fetchImage = async (username) => {
    if (!authToken || !username) {
      return;
    }
  
    const imageBlob = await getImage(authToken,`/professionals/image/${username}`)
    const imageObjectURL = URL.createObjectURL(imageBlob);
    setImgs((prevImgs) => ({ ...prevImgs, [username]: imageObjectURL }));
  };

  useEffect(() => {
    // Load images for each username
    professionals.forEach((prof) => {
      fetchImage(prof.username);
    });
  }, [professionals]);

  // ADD MORE ELEMENTS TO SHOW MORE DATA FOR THE PROFESSIONAL && SHOULD FIX THE PHOTO 
  return (
    <Layout>
    <div style={styles.container}>
      <h2 style={styles.heading}>Professional List</h2>
      <div style={styles.professionalsContainer}>
        {professionals.map((professional) => (
          <div key={professional.id} style={styles.professionalCard}>
              <div style={styles.imageContainer}>
              <img key={professional.username} src={imgs[professional.username]} 
                  style={styles.image}
                />
                {/* alt={`Image for ${professional.username}`} */}
              </div>
              <div style={styles.contentContainer}>
                <p style={styles.name}>
                  {professional.first_name} {professional.last_name}
                </p>
                <p style={styles.status}>Status: {professional.status}</p>
                <p style={styles.username}>{professional.username}</p>
                <p style={styles.summary}>{professional.summary}</p>
              </div>
          </div>
        ))}
      </div>
    </div>
    </Layout>
  );
}

interface CSSProperties {
  [key: string]: string | number | CSSProperties;
}

const styles: { [key: string]: CSSProperties } = {
  container: {
    padding: '20px',
    backgroundImage: `url(${backgroundSVG})`, // Use backticks (`) for string interpolation
    backgroundSize: 'cover', // Adjust as needed
    backgroundPosition: 'center', // Adjust as needed
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
    display: 'flex',
    background: 'white',
    border: '2px solid #ccc',
    padding: '15px',
    margin: '15px',
    width: '100%', // Adjust the width as needed
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

  image: {
    width: '100px',
    height: '100px',
    borderRadius: '50%',
    objectFit: 'cover',
  },

  imageContainer: {
    marginRight: '15px', // Adjust the margin as needed
  },

  contentContainer: {
    flex: 1, // Takes the remaining space
  },

};

export default UserList;
