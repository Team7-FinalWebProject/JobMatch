import { useState, useEffect } from 'react';

export const ProfAvatar = async (authToken, professional) => {
  const baseURL = import.meta.env.VITE_BE_URL || 'http://localhost:8000';

  const [photoData, setPhotoData] = useState(null);

  useEffect(() => {
    const fetchPhoto = async () => {
      try {
        const response = await fetch(baseURL + `/professionals/image/${professional.picture_url}`, {
          method: 'GET',
          headers: { 'x-token': authToken },
        });
        if (!response.ok) {
          throw new Error('Failed to fetch photo');
        }

        const data = await response.blob();
        setPhotoData(data);
      } catch (error) {
        console.error('Error fetching photo:', error.message);
      }
    };

    fetchPhoto();
  }, [authToken, baseURL, professional.picture_url]);

  return photoData;
};
