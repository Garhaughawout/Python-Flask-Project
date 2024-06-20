import React, { useState } from 'react';
import '../styles/AddProperty.css';


const AddProperty = () => {
  const [title, setTitle] = useState('');
  const [description, setDescription] = useState('');
  const [price, setPrice] = useState('');
  const [location, setLocation] = useState('');

// ADD NEW LISTING AFTER USER INFO CHECKED

  return (
    <form className='property-form-container'>
        <h1 className='property-form-title'>Add Property</h1>
        <label className='property-form-label'>
            Title:
            <input className='property-form-input' type="text" value={title} onChange={(e) => setTitle(e.target.value)} />
        </label>
        <br />
        <label className='property-form-label'>
            Image:
            <input className='property-form-input' type="text" />
        </label>
            <br />
        <label className='property-form-label'>
            Price:
            <input className='property-form-input' type="number" value={price} onChange={(e) => setPrice(e.target.value)} />
        </label>
        <br />
        <label className='property-form-label'>
            Location:
            <input className='property-form-input' type="text" value={location} onChange={(e) => setLocation(e.target.value)} />
        </label>
        <label className='property-form-label'>
            Description:
            <textarea className='property-form-textarea' value={description} onChange={(e) => setDescription(e.target.value)} />
        </label>
        <br />
        <button className='property-form-button' type="submit">Add Property</button>
    </form>
  );
};

export default AddProperty;
