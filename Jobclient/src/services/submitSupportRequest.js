import Cookies from "universal-cookie";


export const submitSupportRequest = async(content) => {
    const baseURL = import.meta.env.VITE_BE_URL || 'http://localhost:8000'
    const cookies = new Cookies();
    const getAuthToken = () => {return cookies.get('authToken')};
    let authToken = getAuthToken();

    if (!authToken) {
        throw new Error('Missing authentication token!')
    }

    try {
        const response = await fetch(baseURL + `/messages/chatbot`, {
            method: 'POST',
            headers: {
                'Content-Type': 'text/plain',
                'x-token': authToken
            },
            body: content,
        });
        
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        const data = await response.json();
        return data;
        }
        catch (error) {
            console.error('Error fetching data:', error);
        }
}
