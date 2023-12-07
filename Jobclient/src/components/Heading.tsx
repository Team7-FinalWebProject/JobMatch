import { Fragment, useState } from 'react'
import jobutopiaLogo from '../assets/jobutopia-high-resolution-logo-black-transparent.svg'
import backgroundSVG from '../assets/subtle-prism.svg'
import { Dialog, Disclosure, Popover, Transition } from '@headlessui/react'
import {
  Bars3Icon,
  ChartPieIcon,
  CursorArrowRaysIcon,
  CursorArrowRippleIcon,
  XMarkIcon,
} from '@heroicons/react/24/outline'
import { ChevronDownIcon, PhoneIcon, PlayCircleIcon } from '@heroicons/react/20/solid'
import { NavLink, useLocation, useNavigate } from 'react-router-dom';


export default function Heading() {
  const navigate = useNavigate();
  const location = useLocation();

  const handleNavigation = (route) => {
    if (route.startsWith('/')) {
      navigate(route);
    } else {
      const currentPath = location.pathname.endsWith('/')
        ? location.pathname
        : `${location.pathname}/`;
      const relativePath = `${currentPath}${route}`;
      console.log('Relative Path:', relativePath);

      navigate(relativePath);
    }
  };

  return (
    <header className="bg-gray-200 border-b border-white" style={{border: '1px solid white', borderRadius: '8px', boxShadow: "0 4px 8px rgba(0, 0, 0, 0.1)", backgroundImage: `url(${backgroundSVG})` }} >
      <nav className="mx-auto flex max-w-7xl items-center justify-between p-6 lg:px-8 mt-2" aria-label="Global">
        <NavLink onClick={() => handleNavigation('/')} to='/'>
          <div>
            <img
              className="mx-auto h-6 w-auto"
              src={jobutopiaLogo}
              alt="JobUtopia"
            />
          </div>
        </NavLink>
        <Popover.Group className="hidden lg:flex lg:gap-x-12">
          <NavLink to="/requests" className="text-sm font-semibold leading-6 text-black">
            Requests
          </NavLink>
          <NavLink onClick={() => handleNavigation('companies')} to="/companies" className="text-sm font-semibold leading-6 text-black">
            Companies
          </NavLink>
          <NavLink onClick={() => handleNavigation('professionals')} to="/professionals" className="text-sm font-semibold leading-6 text-black">
            Professionals
          </NavLink>
          <NavLink onClick={() => handleNavigation('offers')} to="/offers" className="text-sm font-semibold leading-6 text-black">
            Offers
          </NavLink>
          <NavLink onClick={() => handleNavigation('messages')} to="/messages" className="text-sm font-semibold leading-6 text-black">
            Messages
          </NavLink>
          <NavLink onClick={() => handleNavigation('support')} to="/support"className="text-sm font-semibold leading-6 text-black">
            Support
          </NavLink>
        </Popover.Group>
      </nav>
    </header>
  )
}
