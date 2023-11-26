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


type Data = {
  [key: string]: string | number | Data | null;
};



function App() {
  const [userData, setUserData] = useState<Data | null>(null);
  const [authToken, setAuthToken] = useState<string | null>(null);
  const [dropdownData, setDropdownData] = useState<string | null>(null);
  const [data, setData] = useState<Data | null>(null);
  // handle state in APP ??
  // const [selectedDropdown, setSelectedDropdown] = useState<string | null>(null);
  // const [username, setUsername] = useState<string | null>(null);
  // const [password, setPassword] = useState<string | null>(null);


useEffect(() => {
  const handleLogin = async (userData: Data | null) => {
    if (!userData || !userData.username || !userData.password){
      return
    }
    try {
      const token = await loginUser(userData.username as string, userData.password as string);
      // console.log('Token:', token);
      setAuthToken(token);
    } catch (error) {
      console.error('Error fetching data:', error);
    }
  };
  
  // console.log('userData:', userData);
  handleLogin(userData);
}, [userData]);


  useEffect(() => {
    const fetchDataAndSetData = async () => {
      try {
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

    fetchDataAndSetData();
  }, [authToken, dropdownData]);

  // const baseURL = import.meta.env.VITE_BE_URL
  const baseURL = import.meta.env.VITE_BE_URL || "http://localhost:8000";

  const handleLoginSubmit = (username: string, password: string) => {
    setUserData({username, password});
    // console.log('Login submitted with:', JSON.stringify({userData }));
    // console.log('Login submitted with:', { username, password });
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
      <LoginForm onSubmit={handleLoginSubmit} />
      <Dropdown options={dropdownOptions} onSelect={handleDropdownSelect} />
      <DataDisplay data={data} />
    </>
  )
}

export default App


