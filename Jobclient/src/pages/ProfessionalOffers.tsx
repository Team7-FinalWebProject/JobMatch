import React, { useEffect, useState } from 'react';
import { useSearchParams } from "react-router-dom";
import backgroundSVG from '../assets/subtle-prism.svg'
import Cookies from 'universal-cookie';
import Layout from './Layout.js';
import { getData } from '../services/getData.js';
import ProfessionalOfferPost from './createProfessionalOffer.js';
import { Link } from 'react-router-dom';
import ProfMatchRequestPopover from '../components/ProfSendMatch.js';
import CompMatchRequestPopover from '../components/CompSendMatch.js';


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

function ProfessionalOffers() {
    const [searchParams, setSearchParams] = useSearchParams();
    const [prevSearchParams, setPrevSearchParams] = useState(null);
    const [profOffers, setProfOffers] = useState<ProfessionalOffer[]>([]);
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
    } catch (error) {
        console.error('Error fetching offers', error);
    }
  };

    if (JSON.stringify([min_salary, max_salary, salary_threshold_pct, allowed_missing_skills, saved_skill_filters_desc]) !== JSON.stringify(prevSearchParams)
        ){setPrevSearchParams([min_salary, max_salary, salary_threshold_pct, allowed_missing_skills, saved_skill_filters_desc]);
        handleQueryParam(min_salary, max_salary, salary_threshold_pct, allowed_missing_skills, saved_skill_filters_desc);
        }
    else if (!prevSearchParams){
        handleQueryParam(min_salary, max_salary, salary_threshold_pct, allowed_missing_skills, saved_skill_filters_desc);
    }
        return (
            <Layout>
                <div>
                    <div className="isolate bg-white px-6 py-12 sm:py-20 lg:px-8" style={{backgroundImage: `url(${backgroundSVG})` }}>
                        <div className='mx-auto max-w-2xl text-center px-6 py-8 sm:py-20 lg:px-8'>
                            <h2 className='text-3xl font-bold tracking-tight text-black sm:text-4xl'>Available Offers</h2>
                        </div>
                        <div className='space-y-6'>
                         
                            <Link to="/offers/companies/create">
                                <button className='top-0 left-0 px-4 py-2 bg-blue-500 text-white rounded hover:bg-blue-700 focus:outline-none focus:shadow-outline-blue active:bg-blue-800 z-10' style={{border: '1px solid #ccc', boxShadow: "0 4px 8px rgba(0, 0, 0, 0.1)"}}>
                                Create Offer
                                </button>
                            </Link>
                            
                            <div className='border-b border-gray-400'>
                            <h3 className='text-xl font-bold mb-6 text-left'>Professional Offers</h3>
                            </div>
                            <div className='grid grid-cols-1 sm:grid-cols-2 gap-6 justify-center'>
                            {profOffers && profOffers.length > 0 && profOffers.map((profOffer) => (
                            <div key={profOffer.id} className='bg-white p-6 rounded-md shadow-md transition-transform hover:scale-105' style={{border: '2px solid #ccc', maxWidth: '500px'}}>
                                <p className='font-semibold top-0 right-0'>Professional ID: {profOffer.professional_id}</p>
                                <p className='text-lg font-semibold mb-2'>
                                {profOffer.description}
                                </p>
                                <p>Status: {profOffer.status}</p>
                                <p>Skills: {renderProfSkills(profOffer.skills)}</p>
                                <p>Salary Range: {profOffer.min_salary} - {profOffer.max_salary}</p>
                                <p>Offer ID: {profOffer.id}</p>
                                <CompMatchRequestPopover offerId={profOffer.id} authToken={authToken}/>
                            </div>
                            ))}
                            </div>
                        </div>
                    </div>
                </div>
            </Layout>
        );
}
export default ProfessionalOffers;

const renderProfSkills = (skills) => {
    if (!skills) {
        return null;
    }
    const skillsArray = Object.keys(skills);
    return skillsArray.map(skill => <span key={skill}>{skill}, </span>);
};