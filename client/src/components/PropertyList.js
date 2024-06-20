import React, { useEffect, useState } from 'react';
import '../styles/PropertyList.css';
import Property from './Property';

function PropertyList() {
  const [properties, setProperties] = useState({
    title: 'Property 1',
    image: 'https://via.placeholder.com/150',
    description: 'This is the first property',
    price: 100000,
    location: 'San Francisco'
});




  return (
    <div className='propertylist-container'>
      <div className='propertylist-title-container'>
        <h1 className='propertylist-title'>{properties.title}</h1>
      </div>
      <div className='propertylist-image-container'>
        <img className='propertylist-image' src={properties.image} alt={properties.title} />
      </div>
      <ul className='propertylist-info-container'>
        <li className='propertylist-item'>{`$${properties.price}`}</li>
        <li className='propertylist-item'>{properties.location}</li>
        <li className='propertylist-item'>{properties.description}</li>
      </ul>
    </div>
  );
};

export default PropertyList;
