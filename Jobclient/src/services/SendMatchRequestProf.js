export const ProfRequestMatch = async(compOfferId, profOfferId, authToken) => {
    const baseURL = import.meta.env.VITE_BE_URL || 'http://localhost:8000'

    try {
        const response = await fetch(baseURL + `/professionals/${compOfferId}/${profOfferId}/requests`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'x-token': authToken 
            },            
        });
        
        if (!response.ok) {
            throw new Error(response.statusText);
        }
        else {
            return true;
        }
    } catch (error) {
        console.error('Error fetching data:', error)
    }
    
}