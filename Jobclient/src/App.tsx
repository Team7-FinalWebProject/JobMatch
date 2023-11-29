import { useState } from "react";

// import RootTestGet from './services/old/getreqtest'
// import Vitetemplate from './pages/template'
// import Post from './services/old/login'
// import Get from './services/old/getreq'

import { loginUser } from "./services/login";
import { registerProfessional } from "./services/registerProfessional";
import { registerCompany } from "./services/registerCompany";
import { getData } from "./services/getData"
import DataDisplay from "./services/displayData";
// import Dropdown from "./components/old/Dropdown";
import Heading from "./components/Heading";
import LoginForm from "./components/LoginForm";
import Sidebar from "./components/Sidebar";
import SignupProfessionalForm from "./components/SignupProfessionalForm";
import SignupCompanyForm from "./components/SignupCompanyForm";

type Data = {
  [key: string]: string | number | Data | null;
};

function App() {
  const [authToken, setAuthToken] = useState<string | null>(null);
  const [data, setData] = useState<Data | null>(null);

  const handleLogin = async (username: string, password: string) => {
    if (!username || !password){
      return
    }
    try {
      const token = await loginUser(username, password);
      // console.log('Token:', token);
      setAuthToken(token);
    } catch (error) {
      console.error('Error fetching data:', error);
    }
  };

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

  const handleSidebar = async (sidebarData: string) => {
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

  const sidebarOptions = ['/search/companies', '/search/professionals', '/search/company_offers', '/search/professional_offers',
  '/admin/companies', '/admin/professionals', '/admin/config', '/professionals/match_requests',
  '/search/professional_self_info', '/search/professional_self_offers', '/search/professional_company_offers',
  '/search/company_self_info', '/search/company_self_offers','/search/company_professional_offers',];


  return (
    <div className="flex">
      <Sidebar options={sidebarOptions} onSelect={handleSidebar} />
      <div className="flex-1 p-4">
        <Heading />
        <LoginForm onSubmit={handleLogin} />
        <SignupProfessionalForm onSubmit={handleProfessionalSignup} />
        <SignupCompanyForm onSubmit={handleCompanySignup} />
        <div className="mt-4">
          <DataDisplay data={data} />
        </div>
      </div>
    </div>

  );
}
//   return (
//     <>
//     <table><tr>
//       <Heading/>
//       <LoginForm onSubmit={handleLogin}/>
//       <SignupProfessionalForm onSubmit={handleProfessionalSignup} />
//       <SignupCompanyForm onSubmit={handleCompanySignup} />
//       {/* <Dropdown options={dropdownOptions} onSelect={handleDropdown} /> */}
//       </tr><tr>
//       <th>
//       <Sidebar options={sidebarOptions} onSelect={handleSidebar}/>
//       </th>
//       <th>
//       <DataDisplay data={data} />
//       </th>
//       </tr></table>
//     </>
//   )
// }

export default App


