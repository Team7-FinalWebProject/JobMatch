import { Fragment, useState } from 'react'
import jobutopiaLogo from '../assets/jobutopia-high-resolution-logo-black-transparent.svg'
import backgroundSVG from '../assets/subtle-prism.svg'
import { Popover } from '@headlessui/react'
import { NavLink } from 'react-router-dom';


export default function Heading() {

  return (
    <header className="bg-gray-200 border-b border-white shadow-md" style={{border: '1px solid white', borderRadius: '8px', backgroundImage: `url(${backgroundSVG})` }} >
      <nav className="mx-auto flex max-w-7xl items-center justify-between p-6 lg:px-8 mt-2" aria-label="Global">
        <NavLink to='/'>
          <div>
            <img
              className="mx-auto h-6 w-auto"
              src={jobutopiaLogo}
              alt="JobUtopia"
            />
          </div>
        </NavLink>
        <Popover.Group className="hidden lg:flex lg:gap-x-12">
          {/* <NavLink to="/requests" className="text-sm font-semibold leading-6 text-black">
            Requests
          </NavLink> */}
          <NavLink to="/companies" className="text-sm font-semibold leading-6 text-black">
            Companies
          </NavLink>
          <NavLink to="/professionals" className="text-sm font-semibold leading-6 text-black">
            Professionals
          </NavLink>
          {/* <NavLink to="/offers" className="text-sm font-semibold leading-6 text-black">
            Offers
          </NavLink> */}
          <NavLink to="/jobs" className="text-sm font-semibold leading-6 text-black">
            Jobs
          </NavLink>
          <NavLink to="/candidates" className="text-sm font-semibold leading-6 text-black">
            Candidates
          </NavLink>
          <NavLink to="/messages" className="text-sm font-semibold leading-6 text-black">
            Messages
          </NavLink>
          <NavLink to="/support"className="text-sm font-semibold leading-6 text-black">
            Support
          </NavLink>
          <NavLink to="/generate" className="text-sm font-semibold leading-6 text-black">
            Generate
          </NavLink>
        </Popover.Group>
      </nav>
    </header>
  )
}
