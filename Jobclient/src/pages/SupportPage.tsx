import Cookies from "universal-cookie";
import { submitSupportRequest } from "../services/submitSupportRequest";
import SupportForm from "../components/SupportForm";
import { useState } from "react";


function RequestSupport() {
    const [data, setData] = useState<File | null>(null);
    const cookies = new Cookies();
    const getAuthToken = () => {return cookies.get('authToken')};
    let authToken = getAuthToken();

    const handleSupportRequest = async (content: string) => {
      if (!content || !authToken) {
        return;
      }
      try {
        const result = await submitSupportRequest(authToken, content);
        setData(result);
      } catch (error) {
        console.error('Error fetching data:', error);
      }
    };
  
    return (
      <SupportForm onSubmit={handleSupportRequest}/>
    );
}

export default RequestSupport;