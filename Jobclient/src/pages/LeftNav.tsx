import Sidebar from "../components/Sidebar";
import { useNavigate } from "react-router-dom";
import { Outlet } from "react-router-dom";

function LeftNav() {

    
    const navigate = useNavigate();
    const handleSidebar = async (sidebarData: string) => {navigate('/?get=' + sidebarData, { replace: true });};
    
  const sidebarOptions = ['/search/companies', '/search/professionals', '/search/company_offers', '/search/professional_offers',
  '/admin/companies', '/admin/professionals', '/admin/config', '/professionals/match_requests',
  '/search/professional_self_info', '/search/professional_self_offers', '/search/professional_company_offers',
  '/search/company_self_info', '/search/company_self_offers','/search/company_professional_offers',];

  return(
    <>
    <div>
    <Sidebar options={sidebarOptions} onSelect={handleSidebar} />
    <Outlet />
    </div>
    </>
  );
}

export default LeftNav;