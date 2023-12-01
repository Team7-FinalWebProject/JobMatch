import React, { useState, useEffect } from 'react';
import { getAvatar } from '../services/getAvatar.d';

interface ProfAvatarProps {
  authToken: string | null;
  photoPath: string;
}

const ProfAvatar: React.FC<ProfAvatarProps> = ({ authToken, photoPath }) => {
  const [photoData, setPhotoData] = useState<Blob | null>(null);
  const baseURL = import.meta.env.VITE_BE_URL || 'http://localhost:8000'

  useEffect(() => {
    const fetchPhoto = async () => {
      try {
        const data = await getAvatar(authToken, baseURL + photoPath);
        setPhotoData(data);
      } catch (error) {
        console.error('Error fetching photo:', error.message);
      }
    };

    fetchPhoto();
  }, [authToken, photoPath]);

  return (
    <>
      <div className="flex -space-x-2 overflow-hidden">
        {photoData && (
          <img
            className="inline-block h-8 w-8 rounded-full ring-2 ring-white"
            src={URL.createObjectURL(photoData)}
            alt="Image"
          />
        )}
      </div>
    </>
  );
};

export default ProfAvatar;
