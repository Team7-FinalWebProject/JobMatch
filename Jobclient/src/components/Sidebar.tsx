import { useState } from "react";
// import { ChevronDownIcon, FunnelIcon, MinusIcon, PlusIcon, Squares2X2Icon } from '@heroicons/react/20/solid'
import { BookOpenIcon } from "@heroicons/react/24/outline";
import { ChevronDoubleLeftIcon } from "@heroicons/react/20/solid";
// import { ArrowLeftIcon } from "@heroicons/react/24/outline";
import { DocumentIcon } from "@heroicons/react/24/solid";

const Sidebar = ({ options, onSelect }) => {
  const [open, setOpen] = useState(true);
//   const Menus = [
//     { title: "Dashboard", src: "Chart_fill" },
//     { title: "Inbox", src: "Chat" },
//     { title: "Accounts", src: "User", gap: true },
//     { title: "Schedule ", src: "Calendar" },
//     { title: "Search", src: "Search" },
//     { title: "Analytics", src: "Chart" },
//     { title: "Files ", src: "Folder", gap: true },
//     { title: "Setting", src: "Setting" },
//   ];

  const handleSelect = (e: React.MouseEvent<HTMLButtonElement>) => {
    e.preventDefault();
    const selectedValue = e.currentTarget.value;
    onSelect(selectedValue);
  };

  return (
    <div className="flex border-r border-black">
      <div
        className={` ${
          open ? "w-72" : "w-20 "
        } bg-dark-purple h-screen p-5  pt-8 relative duration-300`}
      >
        <ChevronDoubleLeftIcon className={`absolute cursor-pointer -right-3 top-9 w-7 border-dark-purple
           border-2 rounded-full  ${!open && "rotate-180"}`} aria-hidden="true" onClick={() => setOpen(!open)} />
        <div className="flex gap-x-4 items-center">
            <BookOpenIcon className={`h-5 w-5 cursor-pointer duration-500 ${
              open && "rotate-[360deg]"
            }`} aria-hidden="true" />
          <h1
            className={`text-black origin-left font-medium text-xl duration-200 ${
              !open && "scale-0"
            }`}
          >
            List
          </h1>
        </div>
        <ul className="pt-6">
          {options.map((option, index) => (
            <li
              key={index}
              className={`flex  rounded-md p-2 cursor-pointer hover:bg-light-white text-gray-300 text-sm items-center gap-x-4 
              ${option.gap ? "mt-9" : "mt-2"} ${
                index === 0 && "bg-light-white"
              } `}
            >
              <DocumentIcon className="-mr-1 ml-1 h-5 w-5 flex-shrink-0 text-gray-900 group-hover:text-black"
                      aria-hidden="true"/>
                      {/* <h1 className="text-2xl font-semibold ">${Menu.src}</h1> */}
              <button onClick={handleSelect} className={`${!open && "hidden"} origin-left duration-200 text-black`} value={option}>
                {option}
              </button>
            </li>
          ))}
        </ul>
      </div>
      {/* <div className="h-screen flex-1 p-7">
        <h1 className="text-2xl font-semibold ">"-"</h1>
      </div> */}
    </div>
  );
};
export default Sidebar;