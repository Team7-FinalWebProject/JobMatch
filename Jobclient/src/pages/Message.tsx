import Cookies from "universal-cookie";
import backgroundSVG from '../assets/subtle-prism.svg'
import { submitMessage } from "../services/submitMessage";
import MessagesForm from "../components/MessageForm";
import { useState } from "react";
import Layout from "./Layout";

type MessageData = {
  id: number | null;
  sender_username: string | null;
  receiver_username: string;
  content: string;
}


function SendMessage() {
    const [messageData, setMessageData] = useState<MessageData | null>(null);
    const cookies = new Cookies();
    const getAuthToken = () => {return cookies.get('authToken')};
    let authToken = getAuthToken();

    const handleMessageSubmit = async (username: string, content: string) => {
      if (!username || !content || !authToken) {
        return;
      }
      try {
        const result = await submitMessage(authToken, username, content);
        setMessageData(result);
      } catch (error) {
        console.error('Error fetching data:', error);
      }
    };
  
    return (
      <Layout>
        <div className="mt-4 flex-1">
          <MessagesForm onSubmit={handleMessageSubmit} />
          {messageData && (
            <p className="bg-gray-200 p-4 rounded-md shadow-md flex justify-center items-center" style={{ backgroundImage: `url(${backgroundSVG})` }}>
              Message ID: {messageData.id} ||| 
              Sender: {messageData.sender_username} ||| 
              Receiver: {messageData.receiver_username} ||| 
              Content: {messageData.content}
            </p>
          )}
        </div>
      </Layout>
    );
}

export default SendMessage;