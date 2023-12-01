import React, { useEffect, useState } from 'react';
import axios from 'axios';
import Cookies from 'universal-cookie';
import backgroundSVG from '../assets/endless-constellation.svg'


function UserList() {
  const [professionals, setProfessionals] = useState([]);
  const cookies = new Cookies();
  const getAuthToken = () => {return cookies.get('authToken')};
  let authToken = getAuthToken();

  useEffect(() => {
    async function fetchProfessionals() {
      try {
        const baseURL = import.meta.env.VITE_BE_URL || 'http://localhost:8000'
        const response = await axios.get(baseURL + '/search/professionals', {
          headers: {
              'x-token': authToken}
        });
        setProfessionals(response.data);
      } catch (error) {
        console.error('Error fetching professionals', error);
      }
    }

    fetchProfessionals();
  }, []);

  // ADD MORE ELEMENTS TO SHOW MORE DATA FOR THE PROFESSIONAL && SHOULD FIX THE PHOTO 
  return (
    <ul role="list" className="divide-y divide-white pl-4 pr-10" style={{ backgroundImage: `url(${backgroundSVG})` }}>
      {professionals.map((professional) => (
        <li key={professional.username} className="flex justify-between gap-x-6 py-5 pl-4">
          <div className="flex min-w-0 gap-x-4">
            <img className="h-12 w-12 flex-none rounded-full bg-gray-50" src={professional.imageUrl} alt="" />
            <div className="min-w-0 flex-auto">
              <p className="text-sm font-semibold leading-6 text-white">{professional.username}</p>
            </div>
          </div>
          <div className="hidden shrink-0 sm:flex sm:flex-col sm:items-end">
            <p className="text-sm leading-6 text-white">{professional.status}</p>
          </div>
        </li>
      ))}
    </ul>
  );
}

export default UserList;
