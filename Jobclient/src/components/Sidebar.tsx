import { useState } from "react";
// import backgroundSVG from '../assets/endless-constellation.svg';
// import { ChevronDownIcon, FunnelIcon, MinusIcon, PlusIcon, Squares2X2Icon } from '@heroicons/react/20/solid'
import { BookOpenIcon } from "@heroicons/react/24/outline";
import { ChevronDoubleLeftIcon } from "@heroicons/react/20/solid";
// import { ArrowLeftIcon } from "@heroicons/react/24/outline";
import { DocumentIcon } from "@heroicons/react/24/solid";
import Profile_popover from "./Profile_popover";
import Slider from "rc-slider";
import "rc-slider/assets/index.css";
import SkillFilterForm from "./SkillFilterForm";


const Sidebar = ({ onSelect, handleSaveLoad }) => {
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
  const [minSalary, setMinSalary] = useState([0]);
  const [maxSalary, setMaxSalary] = useState([20000]);
  const [salaryThreshold, setSalaryThreshold] = useState([0]);
  const [allowMissing, setAllowMissing] = useState([0]);
  const [skillID, setSkillID] = useState([null]);

  // const handleSelect = (e: React.MouseEvent<HTMLButtonElement>) => {
  //   e.preventDefault();
  //   const selectedValue = e.currentTarget.value;
  //   onSelect(selectedValue);
  // };

  const handleSubmit = () => {
    onSelect(minSalary,maxSalary,salaryThreshold,allowMissing,skillID);
  };
  const handleMinSInputChange = (e) => {
    setMinSalary(e.target.value)
  };
  const handleMinSSliderChange = (value) => {
    setMinSalary(value)
  };
  const handleMaxSInputChange = (e) => {
    setMaxSalary(e.target.value)
  };
  const handleMaxSSliderChange = (value) => {
    setMaxSalary(value)
  };
  const handleThreshInputChange = (e) => {
    setSalaryThreshold(e.target.value)
  };
  const handleThreshSliderChange = (value) => {
    setSalaryThreshold(value)
  };
  const handleMissingInputChange = (e) => {
    setAllowMissing(e.target.value)
  };
  const handleMissingSliderChange = (value) => {
    setAllowMissing(value)
  };
  const handleSkillID = (value) => {
    setSkillID(value)
  };



  return (
    <div className="flex border-r border-y-neutral-600">
    {/* <div className="flex border-r border-white" style={{ backgroundImage: `url(${backgroundSVG})` }}> */}
      <div
        className={` ${
          open ? "w-72" : "w-20 "
        } bg-dark-purple h-screen p-5  pt-8 relative duration-300`}
      >
        <ChevronDoubleLeftIcon className={`absolute cursor-pointer -right-6 top-20 w-6 border-dark-purple
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
            <Profile_popover />
          </h1>
        </div>
        <ul className="pt-6">
            
            <li
              key="apply"
              className={`flex ${!open && "hidden"} origin-left duration-200 rounded-md p-2 cursor-pointer hover:bg-light-white text-black text-sm items-center gap-x-4 gap-y-4 "mt-9" : "mt-2"} ${
                1 && "bg-light-white"
              } `}
            >
              <button
              onClick={handleSubmit}
              className="bg-blue-500 text-white w-10/12 px-2 py-2 rounded-md hover:bg-blue-600 mr-2">
              Apply
              </button>
            </li>



            <li
              key="minSalary"
              className={`flex ${!open && "hidden"} origin-left duration-200 rounded-md p-2 cursor-pointer hover:bg-light-white text-black text-sm items-center gap-x-4 gap-y-4 "mt-9" : "mt-2"} ${
                1 && "bg-light-white"
              } `}
            >
              <div>
                <label htmlFor="minSalary" className="block text-sm font-medium leading-6 text-gray-900">
                {/* <DocumentIcon className="-mr-1 ml-1 h-5 w-5 flex-shrink-0 text-black group-hover:text-black"
                      aria-hidden="true"/> */}
                      {/* <h1 className="text-2xl font-semibold ">${Menu.src}</h1> */}
                {"Min Salary"}
                <input
                      value={minSalary}
                      onChange={handleMinSInputChange}
                      type="receiverUsername"
                      name="receiverUsername"
                      id="receiverUsername"
                      autoComplete="given-name"
                      className="block w-30 rounded-md border-0 px-0 py-1 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-3 bg-opacity-50"
                    />
                </label>
                <div className="mt-2">
                  <Slider onChange={handleMinSSliderChange} value={minSalary} max={20000}/>
                </div>
              </div>
            </li>


            <li
              key="maxSalary"
              className={`flex ${!open && "hidden"} origin-left duration-200 rounded-md p-2 cursor-pointer hover:bg-light-white text-black text-sm items-center gap-x-4 gap-y-4 "mt-9" : "mt-2"} ${
                0 && "bg-light-white"
              } `}
            >
              <div>
                <label htmlFor="maxSalary" className="block text-sm font-medium leading-6 text-gray-900">
                {/* <DocumentIcon className="-mr-1 ml-1 h-5 w-5 flex-shrink-0 text-black group-hover:text-black"
                      aria-hidden="true"/> */}
                      {"Max Salary"}
                      <input
                      value={maxSalary}
                      onChange={handleMaxSInputChange}
                      type="receiverUsername"
                      name="receiverUsername"
                      id="receiverUsername"
                      autoComplete="given-name"
                      className="block w-30 rounded-md border-0 px-0 py-1 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-3 bg-opacity-50"
                    />
                      {/* <h1 className="text-2xl font-semibold ">${Menu.src}</h1> */}
                </label>
                <div className="mt-2">
                  <Slider onChange={handleMaxSSliderChange} value={maxSalary} max={20000}/>
                </div>
              </div>
            </li>


            <li
              key="salaryThreshold"
              className={`flex ${!open && "hidden"} origin-left duration-200 rounded-md p-2 cursor-pointer hover:bg-light-white text-black text-sm items-center gap-x-4 gap-y-4 "mt-9" : "mt-2"} ${
                0 && "bg-light-white"
              } `}
            >
              <div>
                <label htmlFor="salaryThreshold" className="block text-sm font-medium leading-6 text-gray-900">
                {/* <DocumentIcon className="-mr-1 ml-1 h-5 w-5 flex-shrink-0 text-black group-hover:text-black"
                      aria-hidden="true"/> */}
                      {"Salary Strictness (0=Exact)"}
                      <input
                      value={salaryThreshold}
                      onChange={handleThreshInputChange}
                      type="receiverUsername"
                      name="receiverUsername"
                      id="receiverUsername"
                      autoComplete="given-name"
                      className="block w-30 rounded-md border-0 px-0 py-1 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-3 bg-opacity-50"
                    />
                      {/* <h1 className="text-2xl font-semibold ">${Menu.src}</h1> */}
                </label>
                <div className="mt-2">
                  <Slider onChange={handleThreshSliderChange} value={salaryThreshold} min={-100} max={1000}/>
                </div>
              </div>
            </li>


            <li
              key="allowMissing"
              className={`flex ${!open && "hidden"} origin-left duration-200 rounded-md p-2 cursor-pointer hover:bg-light-white text-black text-sm items-center gap-x-4 gap-y-4 "mt-9" : "mt-2"} ${
                0 && "bg-light-white"
              } `}
            >
              <div>
                <label htmlFor="allowMissing" className="block text-sm font-medium leading-6 text-gray-900">
                {/* <DocumentIcon className="-mr-1 ml-1 h-5 w-5 flex-shrink-0 text-black group-hover:text-black"
                      aria-hidden="true"/> */}
                      {"Allow Missing Skills (0=No)"}
                      <input
                      value={allowMissing}
                      onChange={handleMissingInputChange}
                      type="receiverUsername"
                      name="receiverUsername"
                      id="receiverUsername"
                      autoComplete="given-name"
                      className="block w-30 rounded-md border-0 px-0 py-1 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-3 bg-opacity-50"
                    />
                      {/* <h1 className="text-2xl font-semibold ">${Menu.src}</h1> */}
                </label>
                <div className="mt-2">
                  <Slider onChange={handleMissingSliderChange} value={allowMissing} max={20}/>
                </div>
              </div>
            </li>

            <li key="skillFilters" className={`${!open && "hidden"} origin-left duration-200 rounded-md p-2 cursor-pointer hover:bg-light-white text-black text-sm items-center gap-x-4 gap-y-4 "mt-9" : "mt-2"} ${
                0 && "bg-light-white"
              } `}>
              <label htmlFor="skillFilters" className="block text-sm font-medium leading-6 text-gray-900">
              {"Skill Filters"}</label>
              <SkillFilterForm onSaveLoad={handleSaveLoad} onSkillID={handleSkillID}/>
            </li>





  
        </ul>
      </div>
      {/* <div className="h-screen flex-1 p-7">
        <h1 className="text-2xl font-semibold ">"-"</h1>
      </div> */}
    </div>
  );
};
export default Sidebar;