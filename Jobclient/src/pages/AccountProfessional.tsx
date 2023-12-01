import { useState } from "react";
import Cookies from 'universal-cookie';
import { getData } from "../services/getData"
import PAccount from "../components/Professional_account";
import LeftNav from "./LeftNav";
import TopNav from "./TopNav";

type Data = {
    [key: string]: string | number | Data | null;
  };

function Content() {
const [data, setData] = useState<Data | null>(null);

const cookies = new Cookies();
// const navigate = useNavigate();
const getAuthToken = () => {return cookies.get('authToken')};
const authToken = getAuthToken();

const handleQueryParam = async () => {
    try {
      const baseURL = import.meta.env.VITE_BE_URL || "http://localhost:8000";
      // const authToken = await handleLogin(userData);
      if (!authToken) {
        // console.warn('Auth token is not available. Skipping data fetch.');
        return;
      }
      const responseData = await getData(authToken,baseURL+"/search/professional_self_info");
      setData(responseData);
    } catch (error) {
      console.error('Error in handleSidebar', error);
    }
  };


  handleQueryParam();

  return(
    <div className="flex">
    <LeftNav />
    <div className="flex-1">
      <TopNav />
      <div className="mt-4">
        <PAccount data={data} />
      </div>
    </div>
  </div>
  );
}

export default Content