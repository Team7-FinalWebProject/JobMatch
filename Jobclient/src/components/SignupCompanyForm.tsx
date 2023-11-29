import '../index.css'


interface SignupFormProps {
    onSubmit: (
        username: string,
        password: string,
        companyName: string,
        description: string,
        address: string,
    ) => void;
}

const SignupCompanyForm: React.FC<SignupFormProps> = ({onSubmit}) => {
    const handleSubmit = (e: React.FormEvent) => {
        e.preventDefault();
        const target = e.target as typeof e.target & {
            registerUsername: { value: string };
            registerPassword: { value: string };
            registerCompanyName: { value: string };
            registerDescription: { value: string };
            registerAddress: { value: string };
        };
        const registerUsername = target.registerUsername.value;
        const registerPassword = target.registerPassword.value;
        const registerCompanyName = target.registerCompanyName.value;
        const registerDescription = target.registerDescription.value;
        const registerAddress = target.registerAddress.value;

        onSubmit(
            registerUsername, 
            registerPassword, 
            registerCompanyName,
            registerDescription,
            registerAddress
            );
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
              Sign Up As Company
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
                    id="registerUsername"
                    name="registerUsername"
                    type="username"
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
                    id="registerPassword"
                    name="registerPassword"
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
                    Company Name
                  </label>
                </div>
                <div className="mt-2">
                  <input
                    id="registerCompanyName"
                    name="registerCompanyName"
                    type="companyname"
                    required
                    className="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6"
                  />
                </div>
              </div>

              <div>
                <div className="flex items-center justify-between">
                  <label htmlFor="lastname" className="block text-sm font-medium leading-6 text-gray-900">
                    Description
                  </label>
                </div>
                <div className="mt-2">
                  <input
                    id="registerDescription"
                    name="registerDescription"
                    type="description"
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
                    id="registerAddress"
                    name="registerAddress"
                    type="address"
                    required
                    className="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6"
                  />
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

export default SignupCompanyForm;
  