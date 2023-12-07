import Cookies from "universal-cookie";
import backgroundSVG from '../assets/subtle-prism.svg'
import { createProfOffer } from "../services/createProfOffer";
import { useState } from "react";
import ProfessionalOfferCreate from "../components/ProfessionalOfferCreate";

type ProfOfferData = {
  description: string;
  offerStatus: string;
  skills: any;
  minSalary: number;
  maxSalary: number
}


function ProfessionalOfferPost() {
    const [offerData, setOfferData] = useState<ProfOfferData | null>(null);
    const cookies = new Cookies();
    const getAuthToken = () => {return cookies.get('authToken')};
    let authToken = getAuthToken();

    const handleOfferSubmit = async (description: string, offerStatus: string, skills: JSON, minSalary: number, maxSalary: number) => {
      if (!description || !offerStatus || !skills || !minSalary || !maxSalary || !authToken) {
        return;
      }
      try {
        const result = await createProfOffer(description, offerStatus, skills, minSalary, maxSalary, authToken);
        setOfferData(result);
      
      } catch (error) {
        console.error('Error fetching data:', error);
      }
    };
  
    return (
      <>
      <div style={{ backgroundImage: `url(${backgroundSVG})` }}>
        <ProfessionalOfferCreate onSubmit={handleOfferSubmit}/>
        {offerData && (
          <p className="bg-gray-200 p-4 rounded-md shadow-md flex justify-center items-center" style={{ backgroundImage: `url(${backgroundSVG})` }}>
            Description: {offerData.description} |||
            Status: {offerData.offerStatus} |||
            Skills: {JSON.stringify(offerData.skills)} |||
            Min Salary: {offerData.minSalary} |||
            Max Salary: {offerData.maxSalary}
          </p>
        )}
      </div>
      </>
     
    );
}

export default ProfessionalOfferPost;