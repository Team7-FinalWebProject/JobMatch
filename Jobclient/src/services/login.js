export const loginUser = async (username, password) => {
    // Perform login API call and get the token
    try {
        const response = await fetch('http://localhost:8000/login/admins', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ username, password }),
        });

        // console.log(JSON.stringify({ username, password })); 
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }

        const data = await response.json();
        return data.token;
        }
        catch (error) {
            console.error('Error fetching data:', error);
        }
  }

