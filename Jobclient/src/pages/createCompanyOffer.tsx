import Cookies from "universal-cookie";
import backgroundSVG from '../assets/subtle-prism.svg'
import { useState } from "react";
import { createCompOffer } from "../services/createCompOffer";
import CompanyOfferCreate from "../components/companyOfferCreate";

type CompOfferData = {
  requirements: any;
  minSalary: number;
  maxSalary: number
}


function CompanyOfferPost() {
    const [offerData, setOfferData] = useState<CompOfferData | null>(null);
    const cookies = new Cookies();
    const getAuthToken = () => {return cookies.get('authToken')};
    let authToken = getAuthToken();

    const handleOfferSubmit = async (requirements: JSON, minSalary: number, maxSalary: number) => {
      if (!requirements || !minSalary || !maxSalary || !authToken) {
        return;
      }
      try {
        const result = await createCompOffer(requirements, minSalary, maxSalary, authToken);
        setOfferData(result);
     
      } catch (error) {
        console.error('Error fetching data:', error);
      }
    };
  
    return (
      <>
      <div style={{ backgroundImage: `url(${backgroundSVG})` }}>
        <CompanyOfferCreate onSubmit={handleOfferSubmit}/>
        {offerData && (
          <p className="bg-gray-200 p-4 rounded-md shadow-md flex justify-center items-center" style={{ backgroundImage: `url(${backgroundSVG})` }}>
            Requirements: {offerData.requirements} |||
            Min Salary: {offerData.minSalary} |||
            Max Salary: {offerData.maxSalary}
          </p>
        )}
      </div>
      </>
     
    );
}

export default CompanyOfferPost;