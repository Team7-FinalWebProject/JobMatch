export const ProfOffers = async (authToken) => {
    const baseURL = import.meta.env.VITE_BE_URL || 'http://localhost:8000';

    try {
        const response = await fetch(baseURL + '/search/professional_offers', {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json',
                'x-token': authToken, 
            },
        });

        if (!response.ok) {
            throw new Error('Network response was not ok');
        }

        const offers = await response.json();
        return offers;
    } catch (error) {
        console.error('Error fetching data:', error);
        throw error;
    }
};