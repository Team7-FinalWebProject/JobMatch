import React, { useState, useEffect } from 'react';
import { Popover, Transition } from '@headlessui/react';
import { Fragment } from 'react';
import Cookies from 'universal-cookie';
import {
    Bars3Icon,
    ChartPieIcon,
    CursorArrowRaysIcon,
    CursorArrowRippleIcon,
    XMarkIcon,
  } from '@heroicons/react/24/outline'
  import { ChevronDownIcon, PhoneIcon, PlayCircleIcon } from '@heroicons/react/20/solid'
import { Link } from 'react-router-dom';
import { getUserInfo } from "../services/getUserInfo"


const Profile = () => {
//   let [isOpen, setIsOpen] = useState(true)
  const cookies = new Cookies();
  const [userType, setUserType] = useState(null);
//   const getAuthToken = () => cookies.get('authToken');
//   let authToken = getAuthToken();

  useEffect(() => {
    // Assuming you have a state to store the user's type
    const authToken = cookies.get('authToken');
    getUserInfo(authToken)
        .then(data => {
            console.log('User Info:', data);
            setUserType(data.type);
        })
        .catch(error => {
            console.error('Error fetching user info:', error);
        });
  }, []); // Ensure the effect runs only once on mount


  return (
    <Popover className="relative">
    <Popover.Button className="flex items-center gap-x-1 text-sm font-semibold leading-6 text-black">
        Profile
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
                <CursorArrowRaysIcon className="h-6 w-6 text-gray-600 group-hover:text-indigo-600" aria-hidden="true" />
                </div>
                <div className="flex-auto">
                <Link to={userType === 'professional' ? '/account/professional' : '/account/company'} className="block font-semibold text-gray-900">
                    Account Info
                    <span className="absolute inset-0" />
                </Link>
                <p className="mt-1 text-gray-600">{"View/Edit Account"}</p>
                </div>
            </div>
            <div
                key="Sign Out"
                className="group relative flex items-center gap-x-6 rounded-lg p-4 text-sm leading-6 hover:bg-gray-50"
            >
                <div className="flex h-11 w-11 flex-none items-center justify-center rounded-lg bg-gray-50 group-hover:bg-white">
                <CursorArrowRaysIcon className="h-6 w-6 text-gray-600 group-hover:text-indigo-600" aria-hidden="true" />
                </div>
                <div className="flex-auto">
                <Link to="/signout" className="block font-semibold text-gray-900">
                    Sign Out
                    <span className="absolute inset-0" />
                </Link>
                <p className="mt-1 text-gray-600">{"Logout"}</p>
                </div>
            </div>
        </div>
        <div className="grid grid-cols-2 divide-x divide-gray-900/5 bg-gray-50">
            <Link
                key="Sign Out"
                to="/signout"
                className="flex items-center justify-center gap-x-2.5 p-3 text-sm font-semibold leading-6 text-gray-900 hover:bg-gray-100"
            >
                <PlayCircleIcon className="h-5 w-5 flex-none text-gray-400" aria-hidden="true" />
                Sign Out
            </Link>
            <Link
                key="Login"
                to="/login"
                className="flex items-center justify-center gap-x-2.5 p-3 text-sm font-semibold leading-6 text-gray-900 hover:bg-gray-100"
            >
                <PhoneIcon className="h-5 w-5 flex-none text-gray-400" aria-hidden="true" />
                Login
            </Link>
        </div>
        </Popover.Panel>
    </Transition>
    </Popover>
    )
}

export default Profile;

