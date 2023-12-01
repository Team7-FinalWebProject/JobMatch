export const getApprovedProfessionals = async (authToken) => {
    const baseURL = import.meta.env.VITE_BE_URL || 'http://localhost:8000';

    try {
        const response = await fetch(baseURL + '/search/professionals', {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json',
                'x-token': authToken,
            },
        });

        if (!response.ok) {
            throw new Error('Network response was not ok');
        }

        const data = await response.json();
        return data;
    } catch (error) {
        console.error('Error fetching data:', error);
        throw error; // Re-throw the error to propagate it to the caller
    }
};
