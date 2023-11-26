import React from 'react';

type Data = {
  [key: string]: string | Data;
};

const DataDisplay: React.FC<{ data: Data | null }> = ({ data }) => {
  if (!data) {
    return <div>No data available</div>;
  }

  const keys = Object.keys(data);

  return (
    <div>
      <h2>Data Display</h2>
      <ul>
        {keys.map((key) => (
          <li key={key}>
            <strong>{key}:</strong> {renderValue(data[key])}
          </li>
        ))}
      </ul>
    </div>
  );
};

const renderValue = (value: string | Data): React.ReactNode => {
  if (typeof value === 'string') {
    return value;
  } else if (typeof value === 'object' && value !== null) {
    return <DataDisplay data={value} />;
  } else {
    return null;
  }
};

export default DataDisplay;
