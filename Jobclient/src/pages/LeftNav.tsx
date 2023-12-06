import Sidebar from "../components/Sidebar";
import { useNavigate } from "react-router-dom";

function LeftNav() {

    
    const navigate = useNavigate();
    const handleSidebar = async (sidebarData: string) => {navigate('/?get=' + sidebarData, { replace: true });};
    
  const sidebarOptions = ['Minimum Salary', 'Maximum Salary', 'Salary Threshold', 'By Skills',
  'Allow Missing Skills',];

  return(
    <Sidebar options={sidebarOptions} onSelect={handleSidebar} />
  );
}

export default LeftNav;