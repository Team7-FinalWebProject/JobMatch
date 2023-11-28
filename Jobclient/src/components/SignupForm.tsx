import '../index.css'

interface SignupFormProps {
    onSubmit: (
        username: string,
        password: string,
        firstName: string,
        lastName: string,
        address: string,
        summary: string,
        photo: File
    ) => void;
}

const SignupForm: React.FC<SignupFormProps> = ({onSubmit}) => {
    const handleSubmit = (e: React.FormEvent) => {
        e.preventDefault();
        const target = e.target as typeof e.target & {
            registerusername: { value: string };
            registerpassword: { value: string };
            registerfirstname: { value: string };
            registerlastname: { value: string };
            registeraddress: { value: string };
            registersummary: { value: string };
            registerphoto: { value: File};
        };
        const registerusername = target.registerusername.value;
        const registerpassword = target.registerpassword.value;
        const registerfirstname = target.registerfirstname.value;
        const registerlastname = target.registerlastname.value;
        const registeraddress = target.registeraddress.value;
        const registersummary = target.registersummary.value;
        const registerphoto = target.registerphoto.value;

        onSubmit(
            registerusername, 
            registerpassword, 
            registerfirstname,
            registerlastname,
            registeraddress,
            registersummary,
            registerphoto);
        };
        
    return (
      <>
        {/*
          This example requires updating your template:
  
          ```
          <html class="h-full bg-white">
          <body class="h-full">
          ```
        */}
        <div className="flex min-h-full flex-1 flex-col justify-center px-6 py-12 lg:px-8">
          <div className="sm:mx-auto sm:w-full sm:max-w-sm">
            {/* <img
              className="mx-auto h-10 w-auto"
              src="https://tailwindui.com/img/logos/mark.svg?color=indigo&shade=600"
              alt="Your Company"
            /> */}
            <h2 className="mt-10 text-center text-2xl font-bold leading-9 tracking-tight text-gray-900">
              Sign Up As Professional
            </h2>
          </div>
  
          <div className="mt-10 sm:mx-auto sm:w-full sm:max-w-sm">
            <form className="space-y-6" onSubmit={handleSubmit}>
              <div>
                <label htmlFor="username" className="block text-sm font-medium leading-6 text-gray-900">
                  Username
                </label>
                <div className="mt-2">
                  <input
                    id="registerusername"
                    name="registerusername"
                    type="registerusername"
                    required
                    className="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6"
                  />
                </div>
              </div>
  
              <div>
                <div className="flex items-center justify-between">
                  <label htmlFor="password" className="block text-sm font-medium leading-6 text-gray-900">
                    Password
                  </label>
                </div>
                <div className="mt-2">
                  <input
                    id="password"
                    name="password"
                    type="password"
                    autoComplete="current-password"
                    required
                    className="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6"
                  />
                </div>
              </div>

              <div>
                <div className="flex items-center justify-between">
                  <label htmlFor="firstname" className="block text-sm font-medium leading-6 text-gray-900">
                    First Name
                  </label>
                </div>
                <div className="mt-2">
                  <input
                    id="firstname"
                    name="firstname"
                    type="firstname"
                    required
                    className="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6"
                  />
                </div>
              </div>

              <div>
                <div className="flex items-center justify-between">
                  <label htmlFor="lastname" className="block text-sm font-medium leading-6 text-gray-900">
                    Last Name
                  </label>
                </div>
                <div className="mt-2">
                  <input
                    id="lastname"
                    name="lastname"
                    type="lastname"
                    required
                    className="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6"
                  />
                </div>
              </div>

              <div>
                <div className="flex items-center justify-between">
                  <label htmlFor="address" className="block text-sm font-medium leading-6 text-gray-900">
                    Address
                  </label>
                </div>
                <div className="mt-2">
                  <input
                    id="address"
                    name="address"
                    type="address"
                    required
                    className="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6"
                  />
                </div>
              </div>

              <div>
                <div className="flex items-center justify-between">
                  <label htmlFor="summary" className="block text-sm font-medium leading-6 text-gray-900">
                    Summary
                  </label>
                </div>
                <div className="mt-2">
                  <input
                    id="summary"
                    name="summary"
                    type="summary"
                    required
                    className="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6"
                  />
                </div>
              </div>

              <div className="sm:mx-auto sm:w-full sm:max-w-sm">
                <label className="block text-sm font-medium text-gray-700">
                    Upload Photo
                </label>
                <div className="mt-1 flex items-center">
                    <input
                    type="file"
                    accept="image/*"
                    onChange={handleSubmit}
                    className="hidden"
                    />
                    <label
                    htmlFor="upload-photo"
                    className="cursor-pointer text-sm text-blue-600 hover:underline ml-2 justify-right"
                    >
                    Choose a file
                    </label>
                </div>
                </div>
            

  
              <div>
                <button
                  type="submit"
                  className="flex w-full justify-center rounded-md bg-indigo-600 px-3 py-1.5 text-sm font-semibold leading-6 text-white shadow-sm hover:bg-indigo-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600"
                >
                  Create account
                </button>
              </div>
            </form>
  
          </div>
        </div>
      </>
    )
}

export default SignupForm;
  