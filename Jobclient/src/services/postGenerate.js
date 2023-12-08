export const postGenerate = async (authToken, apiUrl, count, content, id) => {
    const baseURL = import.meta.env.VITE_BE_URL || 'http://localhost:8000'
    try {

        const response = await fetch(baseURL + apiUrl, {
            method: 'POST',
            headers: {            'Content-Type': 'application/json',
            'x-token': authToken,
            'count': count,
            'id' : id},
            body: JSON.stringify(content),
        });

        if (!response.ok) {
            // TODO: catch expired token and delete token + re-login
            console.error('Error fetching data');
        }
        // console.log('Headers:', JSON.stringify(headers));
        const resp = await response.json()
        return resp
    }
    catch (error) {
        console.error('Error fetching data:', error);
    }
}

