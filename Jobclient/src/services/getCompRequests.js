export const CompRequests = async (authToken) => {
    const baseURL = import.meta.env.VITE_BE_URL || 'http://localhost:8000';

    try {
        const response = await fetch(baseURL + '/companies/match_requests', {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json',
                'x-token': authToken, 
            },
        });

        if (!response.ok) {
            throw new Error('Network response was not ok');
        }

        const requests = await response.json();
        return requests;
    } catch (error) {
        console.error('Error fetching data:', error);
        throw error;
    }
};