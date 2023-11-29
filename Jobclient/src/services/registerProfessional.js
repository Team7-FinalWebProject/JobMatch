export const registerProfessional = async (username, password, firstName, lastName, address, summary) => {
    const baseURL = import.meta.env.VITE_BE_URL

    try {
        const response = await fetch('http://localhost:8000' + '/register/professionals', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ 
                username, 
                password, 
                first_name: firstName, 
                last_name: lastName, 
                address, 
                summary }),
        });

        if (!response.ok) {
            throw new Error(('Network response was not ok'));
        }
        console.error('Status code:', response.status);
        console.error('Error Text', response.text);
        const data = await response.json();
        return data;
    }
    catch (error) {
        console.error('Error fetching data:', error);
    }
}   