export const submitSupportRequest = async(authToken, content) => {
    const baseURL = import.meta.env.VITE_BE_URL || 'http://localhost:8000'

    try {
        const response = await fetch(baseURL + `/messages/chatbot`, {
            method: 'POST',
            headers: {
                'x-token': authToken
            },
            body: content,
        });
        
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }

        const data = await response.blob();
        return data;
        }
        catch (error) {
            console.error('Error fetching data:', error);
        }
}
