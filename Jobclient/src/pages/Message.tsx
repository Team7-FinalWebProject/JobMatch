import Cookies from "universal-cookie";
import { submitMessage } from "../services/submitMessage";
import MessagesForm from "../components/MessageForm";
import { useState } from "react";


type Data = {
    [key: string]: string | number | Data| null;
};

function SendMessage() {
    const [data, setData] = useState<Data | null>(null);
    const cookies = new Cookies();
    const getAuthToken = () => {return cookies.get('authToken')};
    let authToken = getAuthToken();

    const handleMessageSubmit = async (username: string, content: string) => {
      if (!username || !content || !authToken) {
        return;
      }
      try {
        const result = await submitMessage(authToken, username, content);
        setData(result);
      } catch (error) {
        console.error('Error fetching data:', error);
      }
    };
  
    return (
      <MessagesForm onSubmit={handleMessageSubmit}/>
    );
}

export default SendMessage;