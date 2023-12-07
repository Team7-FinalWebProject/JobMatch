export const MatchProfOffer = async(offerId, profOfferId, authToken) => {
    const baseURL = import.meta.env.VITE_BE_URL || 'http://localhost:8000'

    try {
        const queryParams = new URLSearchParams({
            offer_id: offerId,
            prof_offer_id: profOfferId,
        });

        const response = await fetch(baseURL + `/companies/match?${queryParams.toString()}`, {
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