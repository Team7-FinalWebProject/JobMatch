import Cookies from "universal-cookie";
import { registerProfessional } from "../services/registerProfessional";
import SignupProfessionalForm from "../components/SignupProfessionalForm";
import { useNavigate } from "react-router-dom";
import { useState } from "react";


type Data = {
    [key: string]: string | number | Data| null;
};

function RegisterProfessional() {
    const [data, setData] = useState<Data | null>(null);

    const handleProfessionalSignup = async (
        username: string, password: string, 
        firstName: string, lastName: string,
        address: string, summary: string) => {
        if (!username || !password || !firstName || !lastName || !address || !summary){
            return
        }
        try {
            const result = await registerProfessional(username, password, firstName, lastName, address, summary);
            setData(result);  
        } 
        catch (error) {
            console.error('Error fetching data:', error);
        }
    };
    return (
        <SignupProfessionalForm onSubmit={handleProfessionalSignup}/>
    );
};

export default RegisterProfessional;