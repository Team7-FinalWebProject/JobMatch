import { Popover, Transition } from "@headlessui/react"
import { ChevronDownIcon, PhoneIcon, PlusCircleIcon } from "@heroicons/react/24/outline"
import { Fragment, useState } from "react"
import { CompRequestMatch } from "../services/SendMatchRequestComp"


const CompMatchRequestPopover = ({ offerId, authToken }) => {
    const [offerIdInput, setOfferIdInput] = useState(null);
    const [responseMessage, setResponseMessage] = useState(null);

    const handleButtonClick = async() => {
        try {
            if (authToken.user_type === "Company") {
                const result = await CompRequestMatch(offerIdInput, offerId, authToken);
                setResponseMessage(result.text);
            }
            else {
                setResponseMessage('You are not authorized')
            }
            
        } catch (error) {
            console.error('Error sending match request:', error);
            setResponseMessage('Error sending request');
       
        }
    };

    return (
        <div className='flex justify-end'>
            <Popover className="relative">
            <Popover.Button className="flex items-center gap-x-1 text-sm font-semibold leading-6 text-black">
                Send Match Request
                <ChevronDownIcon className="h-5 w-5 flex-none text-gray-400" aria-hidden="true" />
            </Popover.Button>
        
            <Transition
                as={Fragment}
                enter="transition ease-out duration-200"
                enterFrom="opacity-0 translate-y-1"
                enterTo="opacity-100 translate-y-0"
                leave="transition ease-in duration-150"
                leaveFrom="opacity-100 translate-y-0"
                leaveTo="opacity-0 translate-y-1"
            >
                <Popover.Panel className="absolute -left-8 top-full z-10 mt-3 w-screen max-w-md overflow-hidden rounded-3xl bg-white shadow-lg ring-1 ring-gray-900/5">
                <div className="p-4">
                    <div
                        key="Account Info"
                        className="group relative flex items-center gap-x-6 rounded-lg p-4 text-sm leading-6 hover:bg-gray-50"
                    >
                        <div className="flex h-11 w-11 flex-none items-center justify-center rounded-lg bg-gray-50 group-hover:bg-white">
                        <PlusCircleIcon className="h-6 w-6 text-gray-600 group-hover:text-indigo-600" aria-hidden="true" />
                        </div>
                        <div className="flex-auto">
                        <input 
                            style={{border: '2px solid #ccc', borderRadius: "8px"}} 
                            type="number"
                            value={offerIdInput}
                            onChange={(e) => setOfferIdInput(e.target.value)} />
                        <p className="mt-1 text-gray-600">{"Your offer ID"}</p>
                        </div>
                    </div>
    
                </div>
                <div className="bg-blue-200">
                    <button
                        className="flex items-center justify-center gap-x-2.5 p-3 text-sm font-semibold leading-6 text-gray-900 hover:bg-gray-100"
                        onClick={handleButtonClick}
                    >
                        <PhoneIcon className="h-5 w-5 flex-none text-gray-400" aria-hidden="true" />
                        Send
                    </button>
                </div>
                {responseMessage && (
                        <div className="p-4 text-center">
                            <p className="text-gray-800">{responseMessage}</p>
                        </div>
                    )}
                </Popover.Panel>
            </Transition>
            </Popover>
        </div>
    )
}

export default CompMatchRequestPopover;