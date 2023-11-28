import React from 'react';
import '../index.css';

interface LoginFormProps {
  onSubmit: (username: string, password: string) => void;
}

const LoginForm: React.FC<LoginFormProps> = ({ onSubmit }) => {

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    const target = e.target as typeof e.target & {
      loginusername: { value: string };
      loginpassword: { value: string };
    };
    const loginusername = target.loginusername.value; // typechecks!
    const loginpassword= target.loginpassword.value; // typechecks!
    // validation here?
    onSubmit(loginusername, loginpassword);
  };

  return (
    <form onSubmit={handleSubmit} className='custom-login-form' id='loginform'>
      <label className='mx-auto flex max-w-7xl items-center justify-between p-6 lg:px-8" aria-label="Global'>
        Username:
        <input type="text" name='loginusername' className='custom-input'/>
      </label>
      <br />
      <label className='mx-auto flex max-w-7xl items-center justify-between p-6 lg:px-8" aria-label="Global'>
        Password:
        <input type="password" name='loginpassword' className='custom-input'/>
      </label>
      <br />
      <button type="submit" className='custom-button'>Submit</button>
    </form>
  );
};

export default LoginForm;
