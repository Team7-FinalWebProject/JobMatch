export const postData = async (authToken, apiUrl, content) => {
    const baseURL = import.meta.env.VITE_BE_URL || 'http://localhost:8000'
    try {

        const headers = {
            'Content-Type': 'application/json',
            'x-token': authToken,
          };

        const response = await fetch(baseURL + apiUrl, {
            method: 'POST',
            headers: headers,
            body: JSON.stringify(content),
        });

        if (!response.ok) {
            // TODO: catch expired token and delete token + re-login
            console.error('Error fetching data');
        }
        // console.log('Headers:', JSON.stringify(headers));
        await response
        return null
    }
    catch (error) {
        console.error('Error fetching data:', error);
    }
}

