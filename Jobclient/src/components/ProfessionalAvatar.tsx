import React, { useState, useEffect } from 'react';
import { getAvatar } from '../services/getAvatar.d';

interface ProfAvatarProps {
  authToken: string | null;
}

const ProfAvatar: React.FC<ProfAvatarProps> = ({ authToken }) => {
  const [photoData, setPhotoData] = useState<Blob | null>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);
  const baseURL = import.meta.env.VITE_BE_URL || 'http://localhost:8000';

  useEffect(() => {
    const fetchPhoto = async () => {
      try {
        const data = await getAvatar(authToken, baseURL + '/professionals/image');
        setPhotoData(data);
      } catch (error) {
        setError('Error fetching photo');
      } finally {
        setLoading(false);
      }
    };

    fetchPhoto();
  }, [authToken]);

  if (loading) {
    return <div>Loading...</div>;
  }

  if (error) {
    return <div>Error: {error}</div>;
  }

  return (
    <div className="flex -space-x-2 overflow-hidden">
      {photoData && (
        <img
          className="inline-block h-8 w-8 rounded-full ring-2 ring-white"
          src={URL.createObjectURL(photoData)}
          alt="Image"
        />
      )}
    </div>
  );
};

export default ProfAvatar;
