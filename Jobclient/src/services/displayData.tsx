import React from 'react';
import { Disclosure } from '@headlessui/react'
import { ChevronUpIcon } from '@heroicons/react/20/solid'

type Data = {
  [key: string]: string | number | Data | null;
};

const DataDisplay: React.FC<{ data: Data | null}> = ({ data }) => {
  if (!data) {
    return <div>No data available</div>;
  }

  const keys = Object.keys(data);

  return (
    <div className="shadow-zinc-200 shadow-sm mr-5 rounded-lg text-sm font-medium leading-5 'ring-white/60 ring-offset-2 ring-offset-blue-400 focus:outline-none focus:ring-2">
      <ul className="ring-white/60 ring-offset-2 ring-offset-blue-400 focus:outline-none focus:ring-2 justify-between rounded-lg px-4 text-left text-sm font-medium text-purple-90 focus-visible:ring focus-visible:ring-purple-500/75">
        {keys.map((key) => ((key !== 'chosen_professional_offer_id' &&  key !== "status" &&  key !== "status" ) &&
          <li key={key} className="px-4 text-sm text-black">
            <strong className="px-4text-sm text-black">{key}:</strong> {renderValue(data[key])}
          </li>
        ))}
      </ul>
    </div>
  );
};

const renderValue = (value: string | Data | null | number): React.ReactNode => {
  if (typeof value === 'string' || typeof value == 'number') {
    return value;
  } else if (typeof value === 'object' && value !== null) {
    return <DataDisplay data={value} />;
  // } else if (typeof value === 'object' && !value) {
  //   return <><DataDisplay data={value} /><li>{'>empty<'}</li></>;
  } else if (value === null) {
    return ">null<"
  } else {
    return null;
  }
};

export default DataDisplay;
