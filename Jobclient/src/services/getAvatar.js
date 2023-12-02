export const getAvatar = async (authToken, apiUrl) => {

    try {
        const response = await fetch(apiUrl, {
        method: 'GET',
        headers: { 'x-token': authToken },
        });

        if (!response.ok) {
        throw new Error('Failed to fetch photo');
        }

        const data = await response.blob();
        return data;
    } catch (error) {
        console.error('Error fetching photo:', error.message);
        return null;
    }
}