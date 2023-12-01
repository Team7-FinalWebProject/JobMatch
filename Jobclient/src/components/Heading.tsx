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
          <Popover className="relative">
            <Popover.Button className="flex items-center gap-x-1 text-sm font-semibold leading-6 text-white">
              Product
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
                  {products.map((item) => (
                    <div
                      key={item.name}
                      className="group relative flex items-center gap-x-6 rounded-lg p-4 text-sm leading-6 hover:bg-gray-50"
                    >
                      <div className="flex h-11 w-11 flex-none items-center justify-center rounded-lg bg-gray-50 group-hover:bg-white">
                        <item.icon className="h-6 w-6 text-gray-600 group-hover:text-indigo-600" aria-hidden="true" />
                      </div>
                      <div className="flex-auto">
                        <a href={item.href} className="block font-semibold text-gray-900">
                          {item.name}
                          <span className="absolute inset-0" />
                        </a>
                        <p className="mt-1 text-gray-600">{item.description}</p>
                      </div>
                    </div>
                  ))}
                </div>
                <div className="grid grid-cols-2 divide-x divide-gray-900/5 bg-gray-50">
                  {callsToAction.map((item) => (
                    <a
                      key={item.name}
                      href={item.href}
                      className="flex items-center justify-center gap-x-2.5 p-3 text-sm font-semibold leading-6 text-gray-900 hover:bg-gray-100"
                    >
                      <item.icon className="h-5 w-5 flex-none text-gray-400" aria-hidden="true" />
                      {item.name}
                    </a>
                  ))}
                </div>
              </Popover.Panel>
            </Transition>
          </Popover>

          <Link to="/admins" className="text-sm font-semibold leading-6 text-white">
            Admin
          </Link>
          <Link to="/companies" className="text-sm font-semibold leading-6 text-white">
            Companies
          </Link>
          <Link to="/professionals" className="text-sm font-semibold leading-6 text-white">
            Professionals
          </Link>
          <Link to="/offers" className="text-sm font-semibold leading-6 text-white">
            Offers
          </Link>
          <Link to="/messages" className="text-sm font-semibold leading-6 text-white">
            Messages
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
