export const submitMessage = async(username, content) => {
    const baseURL = import.meta.env.VITE_BE_URL || 'http://localhost:8000'

    try {
        const response = await fetch(baseURL + `/${username}/messages`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ username, content }),
        });
        
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }

        const data = await response.json();
        return data.token;
        }
        catch (error) {
            console.error('Error fetching data:', error);
        }
}
