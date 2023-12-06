import '../index.css'
// import jobutopia_logo from '../assets/images/jobutopia-logo-black.png'
import backgroundSVG from '../assets/subtle-prism.svg'
import jobutopiaLogo from '../assets/jobutipiaLogo.svg'


interface SignupFormProps {
    onSubmit: (
        username: string,
        password: string,
        firstName: string,
        lastName: string,
        address: string,
        summary: string
    ) => void;
}

const SignupProfessionalForm: React.FC<SignupFormProps> = ({onSubmit}) => {
    const handleSubmit = (e: React.FormEvent) => {
        e.preventDefault();
        const target = e.target as typeof e.target & {
            registerusername: { value: string };
            registerpassword: { value: string };
            registerfirstname: { value: string };
            registerlastname: { value: string };
            registeraddress: { value: string };
            registersummary: { value: string };
        };
        const registerusername = target.registerusername.value;
        const registerpassword = target.registerpassword.value;
        const registerfirstname = target.registerfirstname.value;
        const registerlastname = target.registerlastname.value;
        const registeraddress = target.registeraddress.value;
        const registersummary = target.registersummary.value;

        onSubmit(
            registerusername, 
            registerpassword, 
            registerfirstname,
            registerlastname,
            registeraddress,
            registersummary);
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
        <div className="flex min-h-full flex-1 flex-col justify-center px-6 py-12 lg:px-8"style={{ backgroundImage: `url(${backgroundSVG})` }}>
          <div className="sm:mx-auto sm:w-full sm:max-w-sm">
            <img
              className="mx-auto h-15 w-auto"
              src={ jobutopiaLogo }
              alt="JobUtopia"
            />
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
                    className="block w-full rounded-md border-0 py-1.5 pl-2 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6"
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
                    id="registerpassword"
                    name="registerpassword"
                    type="password"
                    autoComplete="current-password"
                    required
                    className="block w-full rounded-md border-0 py-1.5 pl-2 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6"
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
                    id="registerfirstname"
                    name="registerfirstname"
                    type="firstname"
                    required
                    className="block w-full rounded-md border-0 py-1.5 pl-2 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6"
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
                    id="registerlastname"
                    name="registerlastname"
                    type="lastname"
                    required
                    className="block w-full rounded-md border-0 py-1.5 pl-2 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6"
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
                    id="registeraddress"
                    name="registeraddress"
                    type="address"
                    required
                    className="block w-full rounded-md border-0 py-1.5 pl-2 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6"
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
                    id="registersummary"
                    name="registersummary"
                    type="summary"
                    required
                    className="block w-full rounded-md border-0 py-1.5 pl-2 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6"
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

export default SignupProfessionalForm;
  