// File: "../services/login"

// Import the original loginUser function
import { loginUser } from './login';

// Add a new function to fetch user information
export const getUserInfo = async (token) => {
    const baseURL = import.meta.env.VITE_BE_URL || 'http://localhost:8000';

    try {
        const response = await fetch(baseURL + '/user/user_info', {
            method: 'GET',
            headers: {
                'Authorization': `Bearer ${token}`,
            },
        });

        if (!response.ok) {
            throw new Error('Network response was not ok');
        }

        const data = await response.json();
        return data;
    } catch (error) {
        console.error('Error fetching user info:', error);
    }
}

// Export both functions
export { loginUser, getUserInfo };
