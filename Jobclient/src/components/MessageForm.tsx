import backgroundSVG from '../assets/subtle-prism.svg'

interface MessagesForm_Props {
    onSubmit: (username: string, content: string) => void;
}


const MessagesForm: React.FC<MessagesForm_Props> = ({ onSubmit }) => {
  const handleSubmit = (e:React.FormEvent) => {
    e.preventDefault();
    const target = e.target as typeof e.target & {
        receiverUsername: { value: string };
        submitContent: { value: string };
    };
    const receiverUsername = target.receiverUsername.value;
    const submitContent = target.submitContent.value;
    
    onSubmit(receiverUsername, submitContent);
  };

  return (
    <div className="isolate bg-white px-6 py-24 sm:py-32 lg:px-8" style={{ backgroundImage: `url(${backgroundSVG})` }} >
      <div className="mx-auto max-w-2xl text-center">
        <h2 className="text-3xl font-bold tracking-tight text-black sm:text-4xl">Message</h2>
        <p className="mt-2 text-lg leading-8 text-black">
          Contact a company or professional.
        </p>
      </div>
      <form className="mx-auto mt-16 max-w-xl sm:mt-20" onSubmit={ handleSubmit }>
        <div className="grid grid-cols-1 gap-x-8 gap-y-6 sm:grid-cols-2">
          <div style={{border: '1px solid white', borderRadius: '8px', boxShadow: "0 4px 8px rgba(0, 0, 0, 0.1)", justifyContent: 'center', alignItems: 'center'}}>
            <label htmlFor="first-name" className="block text-sm font-semibold leading-6 text-black text-center"
              >
              Receiver Username
            </label>
            <div className="mt-2.5">
              <input
                type="receiverUsername"
                name="receiverUsername"
                id="receiverUsername"
                autoComplete="given-name"
                className="block w-full rounded-md border-0 px-3.5 py-2 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6 bg-opacity-50"
              />
            </div>
          </div>
         
          <div style={{border: '1px solid white', borderRadius: '8px', boxShadow: "0 4px 8px rgba(0, 0, 0, 0.1)", justifyContent: 'center', alignItems: 'center'}} 
               className="sm:col-span-2">
            <label htmlFor="message" className="block text-sm font-semibold leading-6 text-black text-center">
              Message
            </label>
            <div className="mt-2.5">
              <textarea
                name="submitContent"
                id="submitContent"
                rows={4}
                className="block w-full rounded-md border-0 px-3.5 py-2 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6"
                defaultValue={''}
              />
            </div>
          </div>
        </div>
        <div className="mt-10">
          <button
            type="submit"
            className="block w-full rounded-md bg-indigo-600 px-3.5 py-2.5 text-center text-sm font-semibold text-white shadow-sm hover:bg-indigo-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600"
            style={{border: '1px solid #ccc', boxShadow: "0 4px 8px rgba(0, 0, 0, 0.1)"}}
          >
            Send
          </button>
        </div>
      </form>
    </div>
  )
}

export default MessagesForm;
