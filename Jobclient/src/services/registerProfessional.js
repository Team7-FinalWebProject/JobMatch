export const registerProfessional = async (username, password, firstName, lastName, address, summary) => {
    const baseURL = import.meta.env.VITE_BE_URL

    try {
        const response = await fetch(baseURL + '/register/professionals', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ 
                username, password, 
                firstName, lastName, 
                address, summary }),
        });

        if (!response.ok) {
            throw new Error(('Network response was not ok'));
        }

        const data = await response.json();
        return data;
    }
    catch (error) {
        console.error('Error fetching data:', error);
    }
}   