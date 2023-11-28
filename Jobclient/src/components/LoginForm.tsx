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
      <label>
        Username:
        <input type="text" value={username} onChange={(e) => setUsername(e.target.value)} className='custom-input'/>
      </label>
      <br />
      <label>
        Password:
        <input type="password" value={password} onChange={(e) => setPassword(e.target.value)} className='custom-input'/>
      </label>
      <br />
      <button type="submit" className='custom-button'>Submit</button>
    </form>
  );
};

export default LoginForm;
