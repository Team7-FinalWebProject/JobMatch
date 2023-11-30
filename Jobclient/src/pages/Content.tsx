import { useState } from "react";
import { useSearchParams } from "react-router-dom";
import Cookies from 'universal-cookie';
import { getData } from "../services/getData"
import DataDisplay from "../services/displayData";

type Data = {
    [key: string]: string | number | Data | null;
  };

function Content() {
const [data, setData] = useState<Data | null>(null);
const [searchParams, setSearchParams] = useSearchParams();
const [prevSearchParams, setPrevSearchParams] = useState<string>(null);

const cookies = new Cookies();
// const navigate = useNavigate();
const getAuthToken = () => {return cookies.get('authToken')};
const authToken = getAuthToken();

const handleQueryParam = async (sidebarData: string) => {
    try {
      const baseURL = import.meta.env.VITE_BE_URL || "http://localhost:8000";
      // const authToken = await handleLogin(userData);
      if (!authToken || !sidebarData) {
        // console.warn('Auth token is not available. Skipping data fetch.');
        return;
      }
      const responseData = await getData(authToken,baseURL+sidebarData);
      setData(responseData);
    } catch (error) {
      console.error('Error in handleSidebar', error);
    }
  };

  const sidebarParam = searchParams.get("get")

  if (sidebarParam && sidebarParam !== prevSearchParams
    ){setPrevSearchParams(sidebarParam);handleQueryParam(sidebarParam);}

  return(
    <div className="text-white">
    <DataDisplay data={data} />
    </div>
  );
}

export default Content