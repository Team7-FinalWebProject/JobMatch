import { Fragment, useState } from 'react'
import jobutopiaLogo from '../assets/jobutipiaLogo.svg'
// import backgroundSVG from '../assets/endless-constellation.svg'
import { Dialog, Disclosure, Popover, Transition } from '@headlessui/react'
import {
  Bars3Icon,
  ChartPieIcon,
  CursorArrowRaysIcon,
  CursorArrowRippleIcon,
  XMarkIcon,
} from '@heroicons/react/24/outline'
import { ChevronDownIcon, PhoneIcon, PlayCircleIcon } from '@heroicons/react/20/solid'
import { Link } from 'react-router-dom';


const products = [
  { name: 'Features', description: 'Something', href: '#', icon: ChartPieIcon },
  { name: 'Sign Out', href: '#', icon: CursorArrowRaysIcon },
  { name: 'About us', description: 'Info', href: '#', icon: CursorArrowRippleIcon },
]
const callsToAction = [
  { name: 'Watch demo', href: '#', icon: PlayCircleIcon },
  { name: 'Contact sales', href: '#', icon: PhoneIcon },
]

function classNames(...classes: string[]) {
  return classes.filter(Boolean).join(' ')
}

export default function Heading() {
  const [mobileMenuOpen, setMobileMenuOpen] = useState(false)

  return (
    <header className="bg-gray-200 border-b border-white" >
      {/* <header className="bg-gray-200 border-b border-white" style={{ backgroundImage: `url(${backgroundSVG})` }}> */}
      <nav className="mx-auto flex max-w-7xl items-center justify-between p-6 lg:px-8 mt-2" aria-label="Global">
        <Link to='/'>
          <div>
            <img
              className="mx-auto h-6 w-auto"
              src={jobutopiaLogo}
              alt="JobUtopia"
            />
          </div>
        </Link>
        <div className="flex lg:flex-1">
          <a href="#" className="-m-1.5 p-1.5">
            <span className="sr-only bg-white">JobUtopia</span>
          </a>
        </div>
        <div className="flex lg:hidden">
          <button
            type="button"
            className="-m-2.5 inline-flex items-center justify-center rounded-md p-2.5 text-gray-700"
            onClick={() => setMobileMenuOpen(true)}
          >
            <span className="sr-only">Open main menu</span>
            <Bars3Icon className="h-6 w-6" aria-hidden="true" />
          </button>
        </div>
        <Popover.Group className="hidden lg:flex lg:gap-x-12">
          <Link to="/admins" className="text-sm font-semibold leading-6 text-white">
            Admin
          </Link>
          <Link to="/companies" className="text-sm font-semibold leading-6 text-white">
            Companies
          </Link>
          <Link to="/professionals" className="text-sm font-semibold leading-6 text-white">
            Professionals
          </Link>
          {/* TODO: CHANGE LINK TO OFFERS MAIN PAGE. */}
          <Link to="/offers/professionals/create" className="text-sm font-semibold leading-6 text-white">
            Offers
          </Link>
          <Link to="/messages" className="text-sm font-semibold leading-6 text-white">
            Messages
          </Link>
          <Link to="/support"className="text-sm font-semibold leading-6 text-white">
            Support
          </Link>
        </Popover.Group>
        <div className="hidden lg:flex lg:flex-1 lg:justify-end">
          <Link to="/login" className="text-sm font-semibold leading-6 text-white">
            Log in <span aria-hidden="true">&rarr;</span>
          </Link>
        </div>
      </nav>
    </header>
  )
}
