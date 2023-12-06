import React, { useEffect, useState } from 'react';
import backgroundSVG from '../assets/subtle-prism.svg'
import Cookies from 'universal-cookie';
import Layout from './Layout.js';
import { ProfOffers } from '../services/getProfOffers.js';
import { CompOffers } from '../services/getCompanyOffers.js';


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
    const [profOffers, setProfOffers] = useState<ProfessionalOffer[]>([]);
    const [companyOffers, setCompOffers] = useState<CompanyOffer[]>([]);
    const cookies = new Cookies();
    const getAuthToken = () => cookies.get('authToken');
    let authToken = getAuthToken();

    useEffect(() => {
        async function fetchOffers() {
            try {
                const professionalOffers = await ProfOffers(authToken);
                setProfOffers(professionalOffers);
                const companyOffers = await CompOffers(authToken);
                setCompOffers(companyOffers);
            } catch (error) {
                console.error('Error fetching offers', error);
            }
            
        }
        fetchOffers();
    }, []);

    return (
        <Layout>
        <div style={{backgroundImage: `url(${backgroundSVG})` }}>
        <h2 className='text-xl font-semibold mb-4 text-center'>Available Offers</h2>
        <div className='space-y-6'>
            <h3 className='text-xl font-semibold mb-6'>Professional Offers</h3>
            {profOffers.map((profOffer) => (
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
            {companyOffers.map((compOffer) => (
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