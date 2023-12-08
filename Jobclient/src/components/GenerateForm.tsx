import backgroundSVG from '../assets/subtle-prism.svg'
import { Tab } from '@headlessui/react';
import DataDisplay from '../services/displayData';
import { useState } from 'react';
import { postGenerate } from '../services/postGenerate';
import Cookies from "universal-cookie";

type Generate = {
    [key: string]: any;
  };


function classNames(...classes) {
    return classes.filter(Boolean).join(' ')
  }

const GenerateForm: React.FC = () => {
    const [generateData, setGenerateData] = useState<Generate | null>(null);
    const [generateType, setGenerateType] = useState<string>("company");

    const cookies = new Cookies();
    const getAuthToken = () => {return cookies.get('authToken')};
    let authToken = getAuthToken();


    const handleGenerateSubmit = async (count: number, content: string, ID: number) => {
        if (!authToken) {
          return;
        }
        try {
          const result = await postGenerate(authToken, '/generate/' + generateType, count, content, ID);
          setGenerateData(result);
        } catch (error) {
          console.error('Error fetching data:', error);
        }
      };

    const handleCompany = () => {setGenerateType("company")};
    const handleProfessional = () => {setGenerateType("professional")};
    const handleCompanyOffer = () => {setGenerateType("company_offer")};
    const handleProfessionalOffer = () => {setGenerateType("professional_offer")};


  const handleSubmit = (e:React.FormEvent) => {
    e.preventDefault();
    const target = e.target as typeof e.target & {
        count: { value: number };
        submitContent: { value: string };
        ID: { value: number | null };
    };
    const count = Number(target.count.value);
    const submitContent = target.submitContent.value;
    const ID = Number(target.ID.value)
    
    handleGenerateSubmit(count, submitContent, ID);
  };

  return (
    <div className="isolate bg-white px-6 py-24 sm:py-32 lg:px-8" style={{ backgroundImage: `url(${backgroundSVG})` }} >
           <Tab.Group>
      <Tab.List>
        <Tab onClick={handleCompany} className={({ selected }) =>
                classNames(
                  ' mr-5 rounded-lg py-2.5 text-sm font-medium leading-5',
                  'ring-white/60 ring-offset-2 ring-offset-blue-400 focus:outline-none focus:ring-2',
                  selected
                    ? 'bg-white text-blue-700 shadow'
                    : 'text-black hover:bg-white/[0.12] hover:text-white'
                )}>Company</Tab>
        <Tab onClick={handleProfessional} className={({ selected }) =>
                classNames(
                  'mr-5 rounded-lg py-2.5 text-sm font-medium leading-5',
                  'ring-white/60 ring-offset-2 ring-offset-blue-400 focus:outline-none focus:ring-2',
                  selected
                    ? 'bg-white text-blue-700 shadow'
                    : 'text-black hover:bg-white/[0.12] hover:text-white'
                )}>Professional</Tab>
        <Tab onClick={handleCompanyOffer} className={({ selected }) =>
                classNames(
                  'mr-5 rounded-lg py-2.5 text-sm font-medium leading-5',
                  'ring-white/60 ring-offset-2 ring-offset-blue-400 focus:outline-none focus:ring-2',
                  selected
                    ? 'bg-white text-blue-700 shadow'
                    : 'text-black hover:bg-white/[0.12] hover:text-white'
                )}>Company Offer</Tab>
        <Tab onClick={handleProfessionalOffer} className={({ selected }) =>
                classNames(
                  'rounded-lg py-2.5 text-sm font-medium leading-5',
                  'ring-white/60 ring-offset-2 ring-offset-blue-400 focus:outline-none focus:ring-2',
                  selected
                    ? 'bg-white text-blue-700 shadow'
                    : 'text-black hover:bg-white/[0.12] hover:text-white'
                )}>Professional Offer</Tab>
        </Tab.List>
        </Tab.Group>
      <div className="mx-auto max-w-2xl text-center">
        <h2 className="text-3xl font-bold tracking-tight text-black sm:text-4xl">Generate</h2>
        <p className="mt-2 text-lg leading-8 text-black">
          Generate {generateType}.
        </p>
      </div>
      <form className="mx-auto mt-16 max-w-xl sm:mt-20" onSubmit={ handleSubmit }>
        <div className="grid grid-cols-1 gap-x-8 gap-y-6 sm:grid-cols-2">
          <div style={{border: '1px solid white', borderRadius: '8px', boxShadow: "0 4px 8px rgba(0, 0, 0, 0.1)", justifyContent: 'center', alignItems: 'center'}}>
            <label htmlFor="first-name" className="block text-sm font-semibold leading-6 text-black text-center"
              >
              Count
            </label>
            <div className="mt-2.5">
              <input
                type="number"
                name="count"
                id="count"
                autoComplete="given-name"
                className="block w-full rounded-md border-0 px-3.5 py-2 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6 bg-opacity-50"
              />
            </div>
          </div>


          <div style={{border: '1px solid white', borderRadius: '8px', boxShadow: "0 4px 8px rgba(0, 0, 0, 0.1)", justifyContent: 'center', alignItems: 'center'}}>
            <label htmlFor="first-name" className="block text-sm font-semibold leading-6 text-black text-center" 
              >
              ID
            </label>
            <div className="mt-2.5">
              <input
                type="number"
                name="ID"
                id="ID"
                autoComplete="given-name"
                className={"block w-full rounded-md border-0 px-3.5 py-2 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6 bg-opacity-50" + (!(generateType === "company_offer" || generateType === "professional_offer") && "invisible hidden")}
              />
            </div>
          </div>
         
          <div style={{border: '1px solid white', borderRadius: '8px', boxShadow: "0 4px 8px rgba(0, 0, 0, 0.1)", justifyContent: 'center', alignItems: 'center'}} 
               className="sm:col-span-2">
            <label htmlFor="message" className="block text-sm font-semibold leading-6 text-black text-center">
              Prompt
            </label>
            <div className="mt-2.5">
              <textarea
                name="submitContent"
                id="submitContent"
                placeholder={"Please suggest a json for a " + generateType + "!"}
                rows={4}
                className="block w-full rounded-md border-0 px-3.5 py-2 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6"
                defaultValue={''}
              />
            </div>
          </div>
        </div>
        <div className="mt-10">
          <button
            type="submit"
            className="block w-full rounded-md bg-indigo-600 px-3.5 py-2.5 text-center text-sm font-semibold text-white shadow-sm hover:bg-indigo-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600"
            style={{border: '1px solid #ccc', boxShadow: "0 4px 8px rgba(0, 0, 0, 0.1)"}}
          >
            Send
          </button>
        </div>
      </form>
      {generateData && (
            <p className="bg-gray-200 p-4 rounded-md shadow-md flex justify-center items-center" style={{ backgroundImage: `url(${backgroundSVG})` }}>
                <DataDisplay data={generateData} />
                {/* Sender: {messageData.sender_username} ||| 
                Receiver: {messageData.receiver_username} ||| 
                Content: {messageData.content} */}
            </p>
            )}
    </div>
  )
}

export default GenerateForm;
