import Sidebar from "../components/Sidebar";
import { useNavigate } from "react-router-dom";
import Cookies from "universal-cookie";

function LeftNav() {
  const handleSaveLoad = () => {
    const cookies = new Cookies();
    const getAuthToken = () => {return cookies.get('authToken')};
    return getAuthToken();};
    
    const navigate = useNavigate();
    const handleSidebar = async (minSalary,maxSalary,salaryThreshold,allowMissing,skillID) => {
      const queryParamsArray = [
        { key: 'mins', value: minSalary },
        { key: 'maxs', value: maxSalary },
        { key: 'salt', value: salaryThreshold },
        { key: 'miss', value: allowMissing },
        { key: 'skillID', value: skillID },
      ];
      
      const queryParams = queryParamsArray
        .filter((param) => param.value !== undefined && param.value !== null)
        .map((param) => `${param.key}=${param.value}`)
        .join('&');
      
      const finalQueryString = queryParams.length > 0 ? `?${queryParams}` : '';
      
      navigate('.' + finalQueryString, { replace: true });};
    
  // const sidebarOptions = ['Minimum Salary', 'Maximum Salary', 'Salary Threshold', 'By Skills',
  // 'Allow Missing Skills',];

  return(
    <Sidebar onSelect={handleSidebar} handleSaveLoad={handleSaveLoad} />
  );
}

export default LeftNav;