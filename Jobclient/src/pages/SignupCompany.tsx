import Cookies from "universal-cookie";
import { registerCompany } from "../services/registerCompany";
import SignupCompanyForm from "../components/SignupCompanyForm";
import { useNavigate } from "react-router-dom";
import { useState } from "react";


type Data = {
    [key: string]: string | number | Data | null;
};

function SignupCompany() {
    const [data, setData] = useState<Data | null>(null);

    const handleCompanySignup = async (
        username: string, password: string,
        companyName: string, description: string, address: string) => {
        if (!username || !password || !companyName || !description || !address){
        return
        }
        try {
        const result = await registerCompany(username, password, companyName, description, address);
        setData(result);
        }
        catch (error) {
        console.error('Error fetching data:', error);
        }
    };
    return (
        <SignupCompanyForm onSubmit={handleCompanySignup}/>
    );
};

export default SignupCompany;