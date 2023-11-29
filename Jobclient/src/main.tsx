import React from 'react'
import ReactDOM from 'react-dom/client'
import App from './App.tsx'
import Layout from './pages/Layout.tsx'
import './index.css'

// import * as React from "react";
// import * as ReactDOM from "react-dom";
import {
  createBrowserRouter,
  createRoutesFromElements,
  Route,
  RouterProvider,
} from "react-router-dom";

const router = createBrowserRouter(
  createRoutesFromElements(
    
    <Route path="/" element={<App />}>
    <Route element={<Layout />}></Route>
    <Route path="/login" element={<App />}></Route>
    <Route path="/register" element={<App />}></Route>
      {/* <Route path="dashboard" element={<Dashboard />} /> */}
      {/* ... etc. */}
    </Route>
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
