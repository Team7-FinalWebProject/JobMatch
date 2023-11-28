import React, { useState } from 'react';
import '../index.css';

interface LoginFormProps {
  onSubmit: (username: string, password: string) => void;
}

const LoginForm: React.FC<LoginFormProps> = ({ onSubmit }) => {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    // validation here?
    onSubmit(username, password);
  };

  return (
    <form onSubmit={handleSubmit} className='custom-login-form'>
      <label className='mx-auto flex max-w-7xl items-center justify-between p-6 lg:px-8" aria-label="Global'>
        Username:
        <input type="text" value={username} onChange={(e) => setUsername(e.target.value)} className='custom-input'/>
      </label>
      <br />
      <label className='mx-auto flex max-w-7xl items-center justify-between p-6 lg:px-8" aria-label="Global'>
        Password:
        <input type="password" value={password} onChange={(e) => setPassword(e.target.value)} className='custom-input'/>
      </label>
      <br />
      <button type="submit" className='custom-button'>Submit</button>
    </form>
  );
};

export default LoginForm;
