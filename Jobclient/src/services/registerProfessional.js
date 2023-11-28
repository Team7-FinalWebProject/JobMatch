export const registerProfessional = async (username, password, firstName, lastName, address, summary, photo) => {
    const baseURL = import.meta.env.VITE_BE_URL

    try {
        const base64Photo = photo instanceof File ? await convertFileToBase64(photo) : null;
        const response = await fetch(baseURL + '/register/professionals', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ 
                username, password, 
                firstName, lastName, 
                address, summary, photo: base64Photo }),
        });

        if (!response.ok) {
            throw new Error(('Network response was not ok'));
        }

        const data = await response.json();
        return data;
    }
    catch (error) {
        console.error('Error fetching data:', error);
    }
}   

const convertFileToBase64 = (file) => {
    return new Promise((resolve, reject) => {
        const reader = new FileReader();
        reader.onloadend = () => resolve(reader.result.split(',')[1]);
        reader.onerror = reject;
        reader.readAsDataURL(file);
    });
};