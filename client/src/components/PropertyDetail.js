import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';

const PropertyDetail = () => {
  const { id } = useParams();
  const [property, setProperty] = useState(null);

  useEffect(() => {
    fetch(`http://localhost:5555/properties/${id}`)
      .then((res) => res.json())
      .then((data) => {
      setProperty(data);
      });
  }, [id]);

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
      <p>Location: {property.address}</p>
      <img className='property-image' src={property.image} alt={property.title} />
    </div>
  );
};

export default PropertyDetail;