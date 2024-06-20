import React, { useState } from 'react';
import '../styles/Register.css';


const Register = () => {
  const [username, setUsername] = useState('');
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');

//USE FETCH TO POST NEW USER INFO

  return (
    <form className='register-form-container'>
      <h1 className='register-form-title'>Register</h1>
      <label className='register-form-label'>
        Username:
        <input className='register-form-input' type="text" value={username} onChange={(e) => setUsername(e.target.value)} />
      </label>
      <br />
      <label className='register-form-label'>
        Email:
        <input className='register-form-input' type="email" value={email} onChange={(e) => setEmail(e.target.value)} />
      </label>
      <br />
      <label className='register-form-label'>
        Password:
        <input className='register-form-input' type="password" value={password} onChange={(e) => setPassword(e.target.value)} />
      </label>
      <br />
      <button className='register-form-button' type="submit">Register</button>
    </form>
  );
};

export default Register;
