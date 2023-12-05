import { useState } from 'react';
import SkillForm from './SkillsForm';

interface ProfOfferForm_Props {
  onSubmit: (
    description: string,
    status: string,
    skills: any,
    min_salary: number,
    max_salary: number
    ) => void;
}

const ProfessionalOfferCreate: React.FC<ProfOfferForm_Props> = ({ onSubmit }) => {
  const [skills, setSkills] = useState<any>(null);

  const handleAddSkill = (skillsDictionary: any) => {
    setSkills(skillsDictionary);
  };
  
  const handleSubmit = async (e:React.FormEvent) => {
    e.preventDefault();
    const target = e.target as typeof e.target & {
        offerDescription: { value: string };
        offerStatus: { value: string };
        offerSkills: { value: any };
        offerMinSalary: { value: number };
        offerMaxSalary: { value: number };
    };
    const offerDescription = target.offerDescription.value;
    const offerStatus = target.offerStatus.value;
    const offerSkills = target.offerSkills.value;
    const offerMinSalary = target.offerMinSalary.value;
    const offerMaxSalary = target.offerMaxSalary.value;

    onSubmit(
      offerDescription, 
      offerStatus, 
      offerSkills,
      offerMinSalary,
      offerMaxSalary);
  };

  return (
    <div className="mx-auto sm:max-w-5xl">
      <form onSubmit={ handleSubmit }>
        <div className="px-4 sm:px-0">
          <h3 className="text-center text-2xl font-semibold leading-7 text-black h-full flex items-center justify-center">Create Offer</h3>
        </div>
        <div className="mt-6 border-t border-gray-100">
          <dl className="divide-y divide-gray-100">
            <div className="px-4 py-6 sm:grid sm:grid-cols-3 sm:gap-4 sm:px-0">
              <dt className="text-sm font-medium leading-6 text-gray-900">Description</dt>
              <textarea
                  name="offerDescription"
                  id="offerDescription"
                  rows={3}
                  className="block w-full rounded-md border-0 px-3.5 py-2 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6"
                  style={{
                    border: '2px solid white',
                    boxShadow: "0 6px 10px rgba(0, 0, 0, 0.1)"}}
                  defaultValue={''}
                />
            </div>
            <div className="px-4 py-6 sm:grid sm:grid-cols-3 sm:gap-4 sm:px-0">
              <dt className="text-sm font-medium leading-6 text-gray-900">Status</dt>
              <textarea
                  name="offerStatus"
                  id="offerStatus"
                  rows={1}
                  className="block w-full rounded-md border-0 px-3.5 py-2 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6"
                  style={{
                    border: '2px solid white',
                    boxShadow: "0 6px 10px rgba(0, 0, 0, 0.1)"}}
                  defaultValue={''}
                />
            </div>
            <div className="px-4 py-6 sm:grid sm:grid-cols-3 sm:gap-4 sm:px-0">
              <dt className="text-sm font-medium leading-6 text-gray-900">Skills</dt>
              <SkillForm onAddSkill={handleAddSkill}/>
            </div>
            <div className="px-4 py-6 sm:grid sm:grid-cols-3 sm:gap-4 sm:px-0">
              <dt className="text-sm font-medium leading-6 text-gray-900">Minimum salary</dt>
              <textarea
                  name="offerMinSalary"
                  id="offerMinSalary"
                  rows={1}
                  className="block w-full rounded-md border-0 px-3.5 py-2 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6"
                  style={{
                    border: '2px solid white',
                    boxShadow: "0 6px 10px rgba(0, 0, 0, 0.1)"}}
                  defaultValue={''}
                />
            </div>
            <div className="px-4 py-6 sm:grid sm:grid-cols-3 sm:gap-4 sm:px-0">
              <dt className="text-sm font-medium leading-6 text-gray-900">Maximum salary</dt>
              <textarea
                  name="offerMaxSalary"
                  id="offerMaxSalary"
                  rows={1}
                  className="block w-full rounded-md border-0 px-3.5 py-2 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6"
                  style={{
                    border: '2px solid white',
                    boxShadow: "0 6px 10px rgba(0, 0, 0, 0.1)"}}
                  defaultValue={''}
                />
            </div>
          </dl>
        </div>
        <div className="mt-10">
            <button type="submit"
                    className="block w-full rounded-md bg-indigo-600 px-3.5 py-2.5 text-center text-sm font-semibold text-white shadow-sm hover:bg-indigo-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600"
                    style={{border: '1px solid #ccc', boxShadow: "0 4px 8px rgba(0, 0, 0, 0.1)"}}>
            Submit 
            </button>
          </div>
      </form>
    </div>
  )
}

export default ProfessionalOfferCreate;
