import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';

const PropertyDetail = () => {
  const { id } = useParams();
  const [property, setProperty] = useState(null);

  if (!property) {
    return <div>Loading...</div>;
  }

  return (
    <div className='property-container'>
      <div>
        <h1>{property.title}</h1>
      </div>
      <p>{property.description}</p>
      <p>Price: ${property.price}</p>
      <p>Location: {property.location}</p>
    </div>
  );
};

export default PropertyDetail;
