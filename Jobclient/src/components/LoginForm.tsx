import '../index.css';
import jobutopia_logo from '../assets/images/jobutopia-logo-black.png'
// import backgroundSVG from '../assets/endless-constellation.svg'
import jobutopiaLogo from '../assets/jobutipiaLogo.svg'
import { Link } from 'react-router-dom';

interface LoginForm_Props {
  onSubmit: (username: string, password: string) => void;
}
const LoginForm: React.FC<LoginForm_Props> = ({ onSubmit }) => {
    const handleSubmit = (e: React.FormEvent) => {
        e.preventDefault();
        const target = e.target as typeof e.target & {
          loginusername: { value: string };
          loginpassword: { value: string };
        };
        const loginusername = target.loginusername.value; // typechecks!
        const loginpassword= target.loginpassword.value; // typechecks!
        // validation here?
        onSubmit(loginusername, loginpassword);
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
        <div className="flex min-h-screen flex-1 flex-col justify-center px-6 py-12 lg:px-8" >
        {/* <div className="flex min-h-screen flex-1 flex-col justify-center px-6 py-12 lg:px-8" style={{ backgroundImage: `url(${backgroundSVG})` }}> */}
          <div className="sm:mx-auto sm:w-full sm:max-w-sm">
            <img
              className="mx-auto h-15 w-auto"
              src={ jobutopiaLogo }
              alt="JobUtopia"
            />
          </div>
          <div>
            <h2 className="mt-10 text-center text-2xl font-bold leading-9 tracking-tight text-black">
              Sign in to your account
            </h2>
          </div>
  
          <div className="mt-10 sm:mx-auto sm:w-full sm:max-w-sm">
            <form className="space-y-6" onSubmit={handleSubmit}>
              <div>
                <label htmlFor="email" className="block text-sm font-medium leading-6 text-white">
                  Username
                </label>
                <div className="mt-2">
                  <input
                    id="loginusername"
                    name="loginusername"
                    type="username"
                    autoComplete="username"
                    required
                    className="block w-full rounded-md border-0 py-1.5 pl-2 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6"
                  />
                </div>
              </div>
  
              <div>
                <div className="flex items-center justify-between">
                  <label htmlFor="password" className="block text-sm font-medium leading-6 text-white">
                    Password
                  </label>
                  <div className="text-white">
                    Register as: <Link to="/signup/company" className="font-semibold text-indigo-600 hover:text-indigo-500">Company</Link> or <Link to="/signup/professional" className="font-semibold text-indigo-600 hover:text-indigo-500">Professional</Link>
                  </div>
                </div>
                <div className="mt-2">
                  <input
                    id="loginpassword"
                    name="loginpassword"
                    type="password"
                    autoComplete="password"
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
                  Sign in
                </button>
              </div>
            </form>
  
            {/* <p className="mt-10 text-center text-sm text-gray-500">
              Not a member?{' '}
              <a href="#" className="font-semibold leading-6 text-indigo-600 hover:text-indigo-500">
                Start a 14 day free trial
              </a>
            </p> */}
          </div>
        </div>
      </>
    )
  }

  export default LoginForm;