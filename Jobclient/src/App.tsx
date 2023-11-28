import { useState, useEffect, } from "react";

// import RootTestGet from './services/old/getreqtest'
// import Vitetemplate from './pages/template'
// import Post from './services/old/login'
// import Get from './services/old/getreq'

import { loginUser } from "./services/login";
import { getData } from "./services/getData"
import DataDisplay from "./pages/displayData";
import LoginForm from "./components/LoginForm";
import Dropdown from "./components/Dropdown";
import Heading from "./components/Heading";
import LoginTW from "./components/LoginForm_TW";

type Data = {
  [key: string]: string | number | Data | null;
};



function App() {
  const [userData, setUserData] = useState<Data | null>(null);
  const [authToken, setAuthToken] = useState<string | null>(null);
  const [dropdownData, setDropdownData] = useState<string | null>(null);
  const [data, setData] = useState<Data | null>(null);
  const links = [
    {text: "Home", url: "/"},
    {text: "Message", url: "/messages"},
    {text: "Login", url: "/login"},
    {text: "Sign Up", url: "/register"}
  ]
  // handle state in APP ??
  // const [selectedDropdown, setSelectedDropdown] = useState<string | null>(null);
  // const [username, setUsername] = useState<string | null>(null);
  // const [password, setPassword] = useState<string | null>(null);


  useEffect(() => {
    fetchDataAndSetData();
  }, [authToken, dropdownData]);

  const handleLogin = async (username: string, password: string) => {
    if (!username || !password){
      return
    }
    try {
      const token = await loginUser(username as string, password as string);
      // console.log('Token:', token);
      setAuthToken(token);
    } catch (error) {
      console.error('Error fetching data:', error);
    }
  };

  const fetchDataAndSetData = async () => {
    try {
      // const baseURL = import.meta.env.VITE_BE_URL
      const baseURL = import.meta.env.VITE_BE_URL || "http://localhost:8000";
      // const authToken = await handleLogin(userData);
      if (!authToken || !dropdownData) {
        // console.warn('Auth token is not available. Skipping data fetch.');
        return;
      }
      const responseData = await getData(authToken,baseURL+dropdownData);
      setData(responseData);
    } catch (error) {
      console.error('Error in fetchDataAndSetData', error);
    }
  };


  const handleDropdownSelect = (selectedOption: string) => {
    setDropdownData(selectedOption);
    // console.log('Dropdown option selected:', selectedOption);
  };

  const dropdownOptions = ['/search/companies', '/search/professionals', '/search/company_offers', '/search/professional_offers',
  '/admin/companies', '/admin/professionals', '/admin/config', '/professionals/match_requests',
  '/search/professional_self_info', '/search/professional_self_offers', '/search/professional_company_offers',
  '/search/company_self_info', '/search/company_self_offers','/search/company_professional_offers',];


  return (
    <>
      {/* <Vitetemplate/> */}
      {/* <RootTestGet/> */}
      {/* <Post apiUrl='http://localhost:8000/login/admins"  />'/> */}
      <Heading title={"JobUtopia"} />
      <LoginTW/>
      <LoginForm onSubmit={handleLogin} />
      <Dropdown options={dropdownOptions} onSelect={handleDropdownSelect} />
      <DataDisplay data={data} />
    </>
  )
}

export default App


