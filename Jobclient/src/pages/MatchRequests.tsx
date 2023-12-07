import React, { useEffect, useState } from 'react';
import backgroundSVG from '../assets/subtle-prism.svg'
import Cookies from 'universal-cookie';
import Layout from './Layout.js';
import { ProfRequests } from '../services/getProfRequests.js';
import { CompRequests } from '../services/getCompRequests.js';
import { Link } from 'react-router-dom';


interface ProfessionalRequest {
    id: number;
    professional_offer_id: number;
    company_offer_id: number;
    request_from: string;
}

interface CompanyRequest {
    id: number;
    professional_offer_id: number;
    company_offer_id: number;
    request_from: string;
}

function MatchRequests() {
    const [ProfessionalRequests, setProfRequests] = useState<ProfessionalRequest[]>([]);
    const [companyRequests, setCompRequests] = useState<CompanyRequest[]>([]);
    const cookies = new Cookies();
    const getAuthToken = () => cookies.get('authToken');
    let authToken = getAuthToken();

    const jwtPayload = authToken ? JSON.parse(atob(authToken.split('.')[1])) : null;
    const isProfessional = jwtPayload && jwtPayload.summary;
    const isCompany = jwtPayload && jwtPayload.description;

    useEffect(() => {
        async function fetchOffers() {
            try {
                if (isProfessional) {
                    const professionalRequest = await ProfRequests(authToken);
                    console.log('Professional Requests', professionalRequest)
                    setProfRequests(professionalRequest);
                }
                if (isCompany) {
                    const companyRequest = await CompRequests(authToken);
                    console.log('Company Requests:', companyRequest)
                    setCompRequests(companyRequest);
                }
            } catch (error) {
                console.error('Error fetching offers', error);
            }
            
        }
        fetchOffers();
    }, []);


    return (
        <Layout>
            <div>
                <div className="isolate bg-white px-6 py-12 sm:py-20 lg:px-8" style={{backgroundImage: `url(${backgroundSVG})` }}>
                    <div className='mx-auto max-w-2xl text-center px-6 py-8 sm:py-20 lg:px-8'>
                        <h2 className='text-3xl font-bold tracking-tight text-black sm:text-4xl'>Available Offers</h2>
                    </div>
                    <div className='space-y-6'>
                        <div className='border-b border-gray-400'>
                        <h3 className='text-xl font-bold mb-6 text-left'>Receieved Offers</h3>
                        </div>
                        <div className='grid grid-cols-1 sm:grid-cols-2 gap-6 justify-center'>
                        {ProfessionalRequests.map((ProfRequests) => (
                        <div key={ProfRequests.id} className='bg-white p-6 rounded-md shadow-md transition-transform hover:scale-105' style={{border: '2px solid #ccc', maxWidth: '500px'}}>
                            <p className='font-semibold top-0 right-0'>Your Offer ID: {ProfRequests.professional_offer_id}</p>
                            <p className='font-semibold top-0 right-0'>Company Offer ID: {ProfRequests.company_offer_id}</p>
                        </div>
                        ))}
                        </div>
                    </div>
                    <div className='space-y-10' style={{ height: '100px' }}>
                    </div>
                    <div className='space-y-4'>
                        <div className='justify-center border-b border-gray-400'>
                            <h2 className='text-xl font-bold mb-6 text-left'>Company Offers</h2>
                        </div>
                        <div className='grid grid-cols-1 sm:grid-cols-2 gap-6 justify-center'>
                        {companyRequests.map((compOffer) => (
                        <div key={compOffer.id} className='bg-white p-6 rounded-md shadow-md transition-transform hover:scale-105' style={{border: '2px solid #ccc', maxWidth: '500px'}}>
                            <p className='font-semibold top-0 right-0'>Your Offer ID: {compOffer.company_offer_id}</p>
                            <p className='font-semibold top-0 right-0'>Professional Offer ID: {compOffer.professional_offer_id}</p>
                        </div>
                        ))}
                        </div>

                    </div>
                </div>
            </div>
            {/* </div> */}
        </Layout>
    );
}

export default MatchRequests;