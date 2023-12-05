import React from 'react';

interface AudioPlayerProps {
  src: string;
}

const AudioPlayer: React.FC<AudioPlayerProps> = ({ src }) => {
  return (
    <audio style={{border: '1px solid #ccc',
                    boxShadow: "0 4px 8px rgba(0, 0, 0, 0.1)",
                    borderRadius: '8px',
                    alignItems: 'center'}} controls>
      <source src={src} type="audio/mpeg" />
      Your browser does not support the audio element.
    </audio>
  );
};

export default AudioPlayer;