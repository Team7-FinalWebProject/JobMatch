// File: "../services/login"

// Import the original loginUser function
import { loginUser } from './login';

// Add a new function to fetch user information
export const getUserInfo = async (authToken) => {
    const baseURL = import.meta.env.VITE_BE_URL || 'http://localhost:8000';
    
    try {

        const response = await fetch(baseURL + '/user/user_info', {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json',
                'x-token': authToken,
            },
        });


        if (!response.ok) {
            // TODO: catch expired token and delete token + re-login
            console.error('Error fetching data');
        }
        // console.log('Headers:', JSON.stringify(headers));
        const data = await response.json();
        return data
    }
    catch (error) {
        console.error('Error fetching data:', error);
    }
}

// Export both functions
export { loginUser, getUserInfo };
