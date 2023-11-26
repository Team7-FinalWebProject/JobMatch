import React, { useState, useEffect } from "react";

const MyComponent: React.FC = () => {
  const [data, setData] = useState<string | null>(null);

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
  }, []);

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
