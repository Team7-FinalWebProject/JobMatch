import React, { useEffect, useState } from 'react';
import { useSearchParams } from "react-router-dom";
import backgroundSVG from '../assets/subtle-prism.svg'
import Cookies from 'universal-cookie';
import Layout from './Layout.js';
// import { ProfOffers } from '../services/getProfOffers.js';
// import { CompOffers } from '../services/getCompanyOffers.js';
import { getData } from '../services/getData.js';


interface ProfessionalOffer {
    id: number;
    professional_id: number;
    chosen_company_offer_id: number;
    description: string;
    status: string;
    skills: any;
    min_salary: number;
    max_salary: number;
}

interface CompanyOffer {
    id: number;
    company_id: number;
    chosen_professional_offer_id: number;
    status: string;
    requrements: any;
    min_salary: number;
    max_salary: number;
}

function Offers() {
    const [searchParams, setSearchParams] = useSearchParams();
    const [prevSearchParams, setPrevSearchParams] = useState(null);
    const [profOffers, setProfOffers] = useState<ProfessionalOffer[]>([]);
    const [companyOffers, setCompOffers] = useState<CompanyOffer[]>([]);
    const cookies = new Cookies();
    const getAuthToken = () => cookies.get('authToken');
    let authToken = getAuthToken();

  const min_salary = searchParams.get("mins") || null
  const max_salary = searchParams.get("maxs") || null
  const salary_threshold_pct = searchParams.get("salt") || null
  const allowed_missing_skills = searchParams.get("miss") || null
  const saved_skill_filters_desc = searchParams.get("skillID") || null


  const handleQueryParam = async (min_salary, max_salary, salary_threshold_pct, allowed_missing_skills, saved_skill_filters_desc) => {
    try {
        if (!authToken) {
            return}
        const queryParams = "" +
        (min_salary ? `?min_salary=${min_salary}` : "") +
        (max_salary ? `&max_salary=${max_salary}` : "") +
        (salary_threshold_pct ? `&salary_threshold_pct=${salary_threshold_pct}` : "") +
        (allowed_missing_skills ? `&allowed_missing_skills=${allowed_missing_skills}` : "") +
        (saved_skill_filters_desc ? `&saved_skill_filters_desc=${saved_skill_filters_desc}` : "")
        console.log(queryParams)
        const professionalOffers = await getData(authToken, '/search/professional_offers' + queryParams );
        setProfOffers(professionalOffers);
        const companyOffers = await getData(authToken, '/search/company_offers' + queryParams );
        setCompOffers(companyOffers);
        console.log(companyOffers)
    } catch (error) {
        console.error('Error fetching offers', error);
    }
  };
  

    // useEffect(() => {
    //     async function fetchOffers() {
    //         try {
    //             if (!authToken) {
    //                 return}
    //             const queryParams = "" +
    //             (min_salary ? `?min_salary=${min_salary}` : "") +
    //             (max_salary ? `&max_salary=${max_salary}` : "") +
    //             (salary_threshold_pct ? `&salary_threshold_pct=${salary_threshold_pct}` : "") +
    //             (allowed_missing_skills ? `&allowed_missing_skills=${allowed_missing_skills}` : "") +
    //             (saved_skill_filters_desc ? `&saved_skill_filters_desc=${saved_skill_filters_desc}` : "")
    //             console.log(queryParams)
    //             const professionalOffers = await getData(authToken, '/search/professional_offers' + queryParams );
    //             setProfOffers(professionalOffers);
    //             const companyOffers = await getData(authToken, '/search/company_offers' + queryParams );
    //             setCompOffers(companyOffers);
    //             console.log(companyOffers)
    //         } catch (error) {
    //             console.error('Error fetching offers', error);
    //         }
            
    //     }
    //     fetchOffers();
    // }, []);

    if (JSON.stringify([min_salary, max_salary, salary_threshold_pct, allowed_missing_skills, saved_skill_filters_desc]) !== JSON.stringify(prevSearchParams)
        ){setPrevSearchParams([min_salary, max_salary, salary_threshold_pct, allowed_missing_skills, saved_skill_filters_desc]);
        handleQueryParam(min_salary, max_salary, salary_threshold_pct, allowed_missing_skills, saved_skill_filters_desc);
        }
    else if (!prevSearchParams){
        handleQueryParam(min_salary, max_salary, salary_threshold_pct, allowed_missing_skills, saved_skill_filters_desc);
    }


    return (
        <Layout>
        <div style={{backgroundImage: `url(${backgroundSVG})` }}>
        <h2 className='text-xl font-semibold mb-4 text-center'>Available Offers</h2>
        <div className='space-y-6'>
            <h3 className='text-xl font-semibold mb-6'>Professional Offers</h3>
            {profOffers && profOffers.length > 0 && profOffers.map((profOffer) => (
            <div key={profOffer.id} className='bg-white p-6 rounded-md shadow-md transition-transform hover:scale-105 border border-gray-300'>
                <p className='text-lg font-semibold mb-2'>
                {profOffer.description}
                </p>
                <p>Status: {profOffer.status}</p>
                <p>Skills: Skills: {renderSkills(profOffer.skills)}</p>
                <p>Salary Range: {profOffer.min_salary} - {profOffer.max_salary}</p>
            </div>
            ))}
            <h3 className='text-xl font-semibold mb-6'>Company Offers</h3>
            {companyOffers && companyOffers.length > 0 && companyOffers.map((compOffer) => (
            <div key={compOffer.id} className='bg-white p-6 rounded-md shadow-md transition-transform hover:scale-105 border border-gray-300'>
                <p className='text-lg font-semibold mb-2'>
                    Requirements: {renderSkills(compOffer.requrements)}
                </p>
                <p>Status: {compOffer.status}</p>
                <p>Salary Range: {compOffer.min_salary} - {compOffer.max_salary}</p>
            </div>
            ))}

        </div>
        </div>
        </Layout>
    );
}

export default Offers;

const renderSkills = (skills) => {
    if (!skills) {
        return null;
    }
    const skillsArray = Object.keys(skills);
    return skillsArray.map(skill => <span key={skill}>{skill}, </span>);
};