export const createCompOffer = async (requirements, minSalary, maxSalary, authToken) => {
    const baseURL = import.meta.env.VITE_BE_URL || 'http://localhost:8000'

    try {
        const response = await fetch(baseURL + '/companies/create_offer', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'x-token': authToken,
            },
            body: JSON.stringify({
                requirements,
                min_salary: minSalary,
                max_salary: maxSalary }),
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