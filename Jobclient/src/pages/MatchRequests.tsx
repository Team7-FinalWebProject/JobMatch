import React, { useEffect, useState } from 'react';
import backgroundSVG from '../assets/subtle-prism.svg'
import Cookies from 'universal-cookie';
import Layout from './Layout.js';
import { ProfRequests } from '../services/getProfRequests.js';
import { CompRequests } from '../services/getCompRequests.js';
import { Link } from 'react-router-dom';
import { MatchCompOffer } from '../services/MatchCompanyOffer.js';
import { MatchProfOffer } from '../services/MatchProfOffer.js';


interface ProfessionalRequest {
    id: number;
    prof_offer_id: number;
    comp_offer_id: number;
    request_from: string;
}

interface CompanyRequest {
    id: number;
    prof_offer_id: number;
    comp_offer_id: number;
    request_from: string;
}

function MatchRequests() {
    const [ProfessionalRequests, setProfRequests] = useState<ProfessionalRequest[]>([]);
    const [companyRequests, setCompRequests] = useState<CompanyRequest[]>([]);
    const [responseMessage, setResponseMessage] = useState(null);
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

    const handleCompanyOfferMatch = async(offerId, compOfferId, authToken) => {
        const response = await MatchCompOffer(offerId, compOfferId, authToken);
        console.log(response)
        if (response.text === true) {
            setResponseMessage('You have a match!')
        }
    };

    const handleProfessionalOfferMatch = async(offerId, profOfferId, authToken) => {
        const response = await MatchProfOffer(offerId, profOfferId, authToken);
        console.log(response)
        if (response.text === true) {
            setResponseMessage('You have a match!')
        }
    }

    if (isProfessional) {
        return (
            <Layout>
                <div style={{height: '100%', backgroundImage: `url(${backgroundSVG})`}}>
                    <div className="isolate bg-white px-6 py-12 sm:py-20 lg:px-8" style={{backgroundImage: `url(${backgroundSVG})`}}>
                        <div className='space-y-6'>
                            <div className='border-b border-gray-400'>
                            <h3 className='text-xl font-bold mb-6 text-left'>Receieved Offers</h3>
                            </div>
                            <div className='grid grid-cols-1 sm:grid-cols-2 gap-6 justify-center'>
                            {ProfessionalRequests.length === 0 ? (
                                <div className='text-center text-gray-500'>
                                    <p>You have not received any requests.</p>
                                </div>
                            ) : (
                                ProfessionalRequests.map((ProfRequests) => (
                                    <div key={ProfRequests.id} className='bg-white p-6 rounded-md shadow-md transition-transform hover:scale-105' style={{border: '2px solid #ccc', maxWidth: '500px'}}>
                                        <p className='font-semibold top-0 right-0'>Your Offer ID: {ProfRequests.prof_offer_id}</p>
                                        <p className='font-semibold top-0 right-0'>Company Offer ID: {ProfRequests.comp_offer_id}</p>
                                        <p className='font-semibold top-0 right-0'>Request From: {ProfRequests.request_from}</p>
                                        <div className='flex justify-end mt-3'>
                                            <button onClick={() => handleCompanyOfferMatch(ProfRequests.prof_offer_id, ProfRequests.comp_offer_id, authToken)} 
                                            className='px-4 py-2 bg-blue-500 text-white rounded hover:bg-blue-700 focus:outline-none focus:shadow-outline-blue active:bg-blue-800 z-10' style={{border: '1px solid #ccc', boxShadow: "0 4px 8px rgba(0, 0, 0, 0.1)"}}>
                                            Match
                                            </button>
                                        </div>
                                    </div>
                                ))
                            )}
                            </div>
                            {responseMessage && (
                                <div className="p-4 text-center">
                                    <p className="text-gray-800">{responseMessage}</p>
                                </div>
                            )}
                        </div>
                    </div>
                </div>
            </Layout>
        );
    }
    else if (isCompany) {
        return (
            <Layout>
                <div style={{height: '100%', backgroundImage: `url(${backgroundSVG})`}}>
                    <div className="isolate bg-white px-6 py-12 sm:py-20 lg:px-8" style={{backgroundImage: `url(${backgroundSVG})` }}>
                        <div className='space-y-6'>
                            <div className='border-b border-gray-400'>
                            <h3 className='text-xl font-bold mb-6 text-left'>Receieved Offers</h3>
                            </div>
                            <div className='grid grid-cols-1 sm:grid-cols-2 gap-6 justify-center'>
                            {companyRequests.length === 0 ? (
                                <div className='text-center text-gray-500'>
                                    <p>You have not received any requests.</p>
                                </div>
                            ) : (
                                companyRequests.map((compRequest) => (
                                    <div key={compRequest.id} className='bg-white p-6 rounded-md shadow-md transition-transform hover:scale-105' style={{border: '2px solid #ccc', maxWidth: '500px'}}>
                                        <p className='font-semibold top-0 right-0'>Your Offer ID: {compRequest.comp_offer_id}</p>
                                        <p className='font-semibold top-0 right-0'>
                                            Professional Offer ID: {compRequest.prof_offer_id}
                                            <Link to='/offers' className="ml-2 text-blue-500">View offers</Link>
                                        </p>
                                        <div className='flex justify-end mt-3'>
                                            <button onClick={() => {handleProfessionalOfferMatch(compRequest.comp_offer_id, compRequest.prof_offer_id, authToken)}} 
                                            className='px-4 py-2 bg-blue-500 text-white rounded hover:bg-blue-700 focus:outline-none focus:shadow-outline-blue active:bg-blue-800 z-10' style={{border: '1px solid #ccc', boxShadow: "0 4px 8px rgba(0, 0, 0, 0.1)"}}>
                                            Match
                                            </button>
                                        </div>
                                    </div>
                                ))
                            )}
                            </div>
    
                        </div>
                    </div>
                </div>
            </Layout>
        );
    }
    // return (
    //     <Layout>
    //         <div>
    //             <div className="isolate bg-white px-6 py-12 sm:py-20 lg:px-8" style={{backgroundImage: `url(${backgroundSVG})` }}>
    //                 <div className='mx-auto max-w-2xl text-center px-6 py-8 sm:py-20 lg:px-8'>
    //                     <h2 className='text-3xl font-bold tracking-tight text-black sm:text-4xl'>Available Offers</h2>
    //                 </div>
    //                 <div className='space-y-6'>
    //                     <div className='border-b border-gray-400'>
    //                     <h3 className='text-xl font-bold mb-6 text-left'>Receieved Offers</h3>
    //                     </div>
    //                     <div className='grid grid-cols-1 sm:grid-cols-2 gap-6 justify-center'>
    //                     {ProfessionalRequests.length === 0 ? (
    //                         <div className='text-center text-gray-500'>
    //                             <p>You have not received any requests.</p>
    //                         </div>
    //                     ) : (
    //                         ProfessionalRequests.map((ProfRequests) => (
    //                             <div key={ProfRequests.id} className='bg-white p-6 rounded-md shadow-md transition-transform hover:scale-105' style={{border: '2px solid #ccc', maxWidth: '500px'}}>
    //                                 <p className='font-semibold top-0 right-0'>Your Offer ID: {ProfRequests.professional_offer_id}</p>
    //                                 <p className='font-semibold top-0 right-0'>Company Offer ID: {ProfRequests.company_offer_id}</p>
    //                                 <p className='font-semibold top-0 right-0'>Request From: {ProfRequests.request_from}</p>
    //                             </div>
    //                         ))
    //                     )}
    //                     </div>
    //                 </div>
    //                 <div className='space-y-10' style={{ height: '100px' }}>
    //                 </div>
    //                 <div className='space-y-4'>
    //                     <div className='justify-center border-b border-gray-400'>
    //                         <h2 className='text-xl font-bold mb-6 text-left'>Company Offers</h2>
    //                     </div>
    //                     <div className='grid grid-cols-1 sm:grid-cols-2 gap-6 justify-center'>
    //                     {companyRequests.length === 0 ? (
    //                         <div className='text-center text-gray-500'>
    //                             <p>You have not received any company offers.</p>
    //                         </div>
    //                     ) : (
    //                         companyRequests.map((compRequest) => (
    //                             <div key={compRequest.id} className='bg-white p-6 rounded-md shadow-md transition-transform hover:scale-105' style={{border: '2px solid #ccc', maxWidth: '500px'}}>
    //                                 <p className='font-semibold top-0 right-0'>Your Offer ID: {compRequest.company_offer_id}</p>
    //                                 <p className='font-semibold top-0 right-0'>Professional Offer ID: {compRequest.professional_offer_id}</p>
    //                             </div>
    //                         ))
    //                     )}
    //                     </div>

    //                 </div>
    //             </div>
    //         </div>
    //         {/* </div> */}
    //     </Layout>
    // );
}

export default MatchRequests;