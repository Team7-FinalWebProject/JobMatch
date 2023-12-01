import React from 'react';


export default function ProfAvatar(photoData) {

    return (
      <>
        <div className="flex -space-x-2 overflow-hidden">
          {photoData && (
            <img
              className="inline-block h-8 w-8 rounded-full ring-2 ring-white"
              src={URL.createObjectURL(photoData)}
              alt="Image"
            />
          )}
        </div>
      </>
    );
  }
  