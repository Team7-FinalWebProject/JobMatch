export const registerCompany = async (username, password, companyName, description, address) => {
    const baseURL = import.meta.env.VITE_BE_URL

    try {
        const response = await fetch('http://localhost:8000' + '/register/companies', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                username,
                password,
                company_name: companyName,
                description,
                address }),
        });

        if (!response.ok) {
            throw new Error(('Network response was not ok'));
        }
        console.error('Status code:', response.status);
        console.error('Error text:', response.text);
        const data = await response.json();
        return data;
    }
    catch (error) {
        console.error('Error fetching data:', error);
    }
}