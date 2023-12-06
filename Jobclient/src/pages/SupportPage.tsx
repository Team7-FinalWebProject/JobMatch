import { submitSupportRequest } from "../services/submitSupportRequest";
import SupportForm from "../components/SupportForm";
import { useState } from "react";
import Layout from "./Layout";


function RequestSupport() {
    const [data, setData] = useState({ text: '', audio: null});

    const handleSupportRequest = async (content: string) => {
      if (!content) {
        return;
      }
      try {
        const result = await submitSupportRequest(content);
        setData(result);
      } catch (error) {
        console.error('Error fetching data:', error);
      }
    };
  
    return (
      <Layout>
        <SupportForm onSubmit={handleSupportRequest}/>
      </Layout>
    );
}

export default RequestSupport;