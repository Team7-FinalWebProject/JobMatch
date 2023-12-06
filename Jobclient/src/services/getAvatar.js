export const getAvatar = async (authToken, apiUrl) => {

    try {
        const response = await axios.get(apiUrl, {
            method: 'GET',
            headers: { 'x-token': authToken },
            responseType: 'blob',
        });

        if (!response.ok) {
        throw new Error('Failed to fetch photo');
        }

        return response.data;
    } catch (error) {
        console.error('Error fetching photo:', error.message);
        return null;
    }
}