export const getImage = async (authToken, apiUrl) => {
    const baseURL = import.meta.env.VITE_BE_URL || 'http://localhost:8000'
    try {

        const headers = {
            'Content-Type': 'application/json',
            'x-token': authToken,
          };
        const response = await fetch(baseURL + apiUrl, {
            headers: headers,
        });

        if (!response.ok) {
            // TODO: catch expired token and delete token + re-login
            console.error('Error fetching data');
        }
        // console.log('Headers:', JSON.stringify(headers));
        const data = await response.blob()
        return data
    }
    catch (error) {
        console.error('Error fetching data:', error);
    }
}



