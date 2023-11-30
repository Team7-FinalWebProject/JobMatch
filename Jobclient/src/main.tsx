import Cookies from 'universal-cookie';
import React from 'react'
import ReactDOM from 'react-dom/client'
import App from './App.tsx'
import Layout from './pages/Layout.tsx'
import Login from './pages/Login.tsx'
import SendMessage from './pages/Message.tsx';
import Home from './pages/Home.tsx'
import LeftNav from './pages/LeftNav.tsx';
import TopNav from './pages/TopNav.tsx';
import './index.css'

// import * as React from "react";
// import * as ReactDOM from "react-dom";
import {
  createBrowserRouter,
  createRoutesFromElements,
  Route,
  RouterProvider,
} from "react-router-dom";
import { redirect } from "react-router-dom";
import MessagesForm from './components/MessageForm.tsx';


const cookies = new Cookies();
// const setAuthToken = (authToken: string) => {cookies.set('authToken', authToken, { path: '/' });};
const getAuthToken = () => {return cookies.get('authToken')};
const tokenLoader = () => {
  const authToken = getAuthToken();
  if (!authToken) {
    return redirect("/login");
  }
  return null;
};

const children = {path: "/leftnav",element: <LeftNav />,}


const router = createBrowserRouter(
  createRoutesFromElements(
    <>
    <Route path="/" element={<Home/>} loader={tokenLoader} children={
      <Route path="/" element={<LeftNav />} children={<Route path="/" element={<TopNav />}></Route>}></Route>}></Route>
    {/* <Route element={<LeftNav />}></Route> */}
    <Route path='/messages' element={<SendMessage/>}></Route>
    <Route path="/login" element={<Login />}></Route>
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
