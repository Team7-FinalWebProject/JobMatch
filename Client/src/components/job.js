import React, { useState, useEffect } from "react";

import { SectionHeading, Subheading } from "components/misc/Headings.js";

// const App = () => {
//   const [posts, setPosts] = useState([]);
//   useEffect(() => {
//      fetch('http://localhost:8000')
//         .then((response) => response.json())
//         .then((data) => {
//            console.log(data);
//            setPosts(data);
//         })
//         .catch((err) => {
//            console.log(err.message);
//         });
//   }, []);

// return (
//     subheading = "Our Portfolio",
//   <div className="posts-container">
//      {posts.map((post) => {
//         return (
//           //  <div className="post-card" key={}>
//               <div className="post-card">
//               <h2 className="post-title">{JSON.stringify(post.text)}</h2>
//               <p className="post-body">{"adsadaad"}</p>
//               <div className="button">
//               <div className="delete-btn">Delete</div>
//               </div>
//            </div>
//         );
//      })}
//   </div>
//   );
// };

// export default App;


const MyComponent = () => {
  const [data, setData] = useState(null);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await fetch('http://localhost:8000');
        if (!response.ok) {
          throw new Error('Network response was not ok');
        }

        const responseData = await response.text();
        setData(responseData);
      } catch (error) {
        console.error('Error fetching data:', error);
      }
    };

    fetchData();
  }, []); // The empty dependency array means this effect runs once when the component mounts

  return (
    <div>
      <h1>Data from API:</h1>
      {data ? (
        <p>{data}</p>
      ) : (
        <p>Loading...</p>
      )}
    </div>
  );
};

export default MyComponent;
