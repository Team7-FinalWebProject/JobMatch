import Cookies from 'universal-cookie';
import React from 'react'
import ReactDOM from 'react-dom/client'
import Login from './pages/Login.tsx'
import SendMessage from './pages/Message.tsx';
import Home from './pages/Home.tsx'
import './index.css'
import {
  createBrowserRouter,
  createRoutesFromElements,
  Route,
  RouterProvider,
} from "react-router-dom";
import { redirect } from "react-router-dom";
import { Switch } from '@headlessui/react';
import MessagesForm from './components/MessageForm.tsx';
import SignupCompany from './pages/SignupCompany';
import SignupProfessional from './pages/SingupProfessional.tsx';
import AccountProfessional from './pages/AccountProfessional.tsx';
import UserList from './pages/Professional.tsx';



const cookies = new Cookies();
const setAuthToken = (authToken: string) => {cookies.set('authToken', authToken, { path: '/' });};
const getAuthToken = () => {return cookies.get('authToken')};
const tokenLoader = () => {
  const authToken = getAuthToken();
  if (!authToken) {
    return redirect("/login");
  }
  return null;
};

const tokenUnloader = () => {
  setAuthToken(null);
  return redirect("/login");
};

const router = createBrowserRouter(
  createRoutesFromElements(
    <>
    <Route path="/" element={<Home/>} loader={tokenLoader}></Route>
    <Route path='/messages' element={<SendMessage/>}></Route>
    <Route path="/login" element={<Login />}></Route>
    <Route path="/signout" element={<Login />} loader={tokenUnloader}></Route>
    <Route path="/signup/company" element={<SignupCompany />}></Route>
    <Route path="/signup/professional" element={<SignupProfessional />}></Route>
    <Route path="/account/professional" element={<AccountProfessional />}></Route>
    <Route path="/professionals" element={<UserList />}></Route>
    {/* <Route path="/register" element={<App />}></Route> */}
      {/* <Route path="dashboard" element={<Dashboard />} /> */}
      {/* ... etc. */}
    </>
  )
);

ReactDOM.createRoot(document.getElementById("root")!).render(
  <React.StrictMode>
    <RouterProvider router={router} />
  </React.StrictMode>
);


// ReactDOM.createRoot(document.getElementById('root')!).render(
//   <React.StrictMode>
//     <App />
//   </React.StrictMode>,
// )
