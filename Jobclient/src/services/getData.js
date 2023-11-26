export const getData = async (authToken, apiUrl) => {
    try {

        const headers = {
            'Content-Type': 'application/json',
            'x-token': authToken,
          };

        const response = await fetch(apiUrl, {
            headers: headers,
        });

        if (!response.ok) {
            // TODO: catch expired token and delete token + re-login
            console.error('Error fetching data');
        }
        // console.log('Headers:', JSON.stringify(headers));
        const data = await response.json();
        return data
    }
    catch (error) {
        console.error('Error fetching data:', error);
    }
}

