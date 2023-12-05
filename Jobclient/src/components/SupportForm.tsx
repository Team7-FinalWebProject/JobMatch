import backgroundSVG from '../assets/subtle-prism.svg'
import { useState } from 'react';
import { submitSupportRequest } from '../services/submitSupportRequest';
import AudioPlayer from './AudioPlayer';

interface SupportForm_Props {
    onSubmit: (content: string) => void;
}


const SupportForm: React.FC<SupportForm_Props> = ({ onSubmit }) => {
  const [serverResponse, setServerResponse] = useState<{ text: string | null; audio: string | null }>({
    text: '',
    audio: '',
  });

  const handleSubmit = async (e:React.FormEvent) => {
    e.preventDefault();
    const target = e.target as typeof e.target & {
        submitContent: { value: string };
    };
    const submitContent = target.submitContent.value;
    
    try {
      const result = await submitSupportRequest(submitContent);
      setServerResponse(result);
    } catch (error) {
      console.error('Error fetching data:', error);
    }
  };

  return (
    <div className="min-h-screen isolate bg-white px-6 py-24 sm:py-32 lg:px-8" style={{ backgroundImage: `url(${backgroundSVG})` }}>
    {/* <div className="isolate bg-white px-6 py-24 sm:py-32 lg:px-8" style={{ backgroundImage: `url(${backgroundSVG})` }} > */}
      <div
        className="absolute inset-x-0 top-[-10rem] -z-10 transform-gpu overflow-hidden blur-3xl sm:top-[-20rem]"
        aria-hidden="true"
      >
        <div
          className="relative left-1/2 -z-10 aspect-[1155/678] w-[36.125rem] max-w-none -translate-x-1/2 rotate-[30deg] bg-gradient-to-tr from-[#ff80b5] to-[#9089fc] opacity-30 sm:left-[calc(50%-40rem)] sm:w-[72.1875rem]"
          style={{
            clipPath:
              'polygon(74.1% 44.1%, 100% 61.6%, 97.5% 26.9%, 85.5% 0.1%, 80.7% 2%, 72.5% 32.5%, 60.2% 62.4%, 52.4% 68.1%, 47.5% 58.3%, 45.2% 34.5%, 27.5% 76.7%, 0.1% 64.9%, 17.9% 100%, 27.6% 76.8%, 76.1% 97.7%, 74.1% 44.1%)',
          }}
        />
      </div>
      <div className="mx-auto max-w-2xl text-center">
        <h2 className="text-3xl font-bold tracking-tight text-black sm:text-4xl">Contact Tech Support</h2>
      </div>
      <form className="mx-auto mt-16 max-w-xl sm:mt-20" onSubmit={ handleSubmit }>
        <div className="grid grid-cols-1 gap-x-8 gap-y-6 sm:grid-cols-2">
          <div className="sm:col-span-2" style={{ border: "2px solid white", borderRadius: '8px', boxShadow: "0 6px 10px rgba(0, 0, 0, 0.1)"}}>
            <label htmlFor="message" className="block text-sm font-semibold leading-6 text-black flex justify-center items-center">
              What may we assist you with?
            </label>
            <div className="mt-2.5">
              <textarea
                name="submitContent"
                id="submitContent"
                rows={3}
                className="block w-full rounded-md border-0 px-3.5 py-2 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6"
                style={{
                  border: '2px solid white',
                  boxShadow: "0 6px 10px rgba(0, 0, 0, 0.1)"}}
                defaultValue={''}
              />
            </div>
          </div>
        </div>
        <div className="mt-10">
          <button
            type="submit"
            className="block w-full rounded-md bg-indigo-600 px-3.5 py-2.5 text-center text-sm font-semibold text-white shadow-sm hover:bg-indigo-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600"
            style={{
                border: '1px solid #ccc',
                boxShadow: "0 4px 8px rgba(0, 0, 0, 0.1)"
            }}
          >
            Let's talk
          </button>
        </div>
      </form>
      {serverResponse.text && (
        <div className="mt-6 text-center text-black">
          <p className="text-lg font-semibold">Answer:</p>
          <textarea readOnly rows={5}
            className='block w-full rounded-md border-0 px-3.5 py-2 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6'
            style={{
              border: '2px solid #ccc',
              boxShadow: "0 4px 8px rgba(0, 0, 0, 0.1)"
            }}
            value={serverResponse.text}
          />
        </div>
      )}
      {serverResponse.audio && (
        <div className="mt-6 text-center text-black">
        <p className="text-lg font-semibold">Audio Answer:</p>
        <AudioPlayer src={ serverResponse.audio }/>
      </div>
      )}
    </div>
  )
}

export default SupportForm;
