import Heading from "../components/Heading";
import { useNavigate } from "react-router-dom";
import { Outlet } from "react-router-dom";

function TopNav() {
    // const navigate = useNavigate();
    
    // const handleTopbar = async (topbarData: string) => {navigate('/?get=' + topbarData, { replace: true });};
    
//   const topbarOptions = ['/search/companies', '/search/professionals', '/search/company_offers', '/search/professional_offers',
//   '/admin/companies', '/admin/professionals', '/admin/config', '/professionals/match_requests',
//   '/search/professional_self_info', '/search/professional_self_offers', '/search/professional_company_offers',
//   '/search/company_self_info', '/search/company_self_offers','/search/company_professional_offers',];

  return(
    <>
    <Heading></Heading>
    <Outlet />
    </>
  );
}

export default TopNav;