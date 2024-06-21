import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import '../styles/PropertyDetail.css';
import { Link } from 'react-router-dom/cjs/react-router-dom.min';


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
      <div className='property-title'>
        <h1>{property.title}</h1>
      </div>
      <img className='property-image' src={property.image} alt={property.title} />
      <p className='property-description'>{property.description}</p>
      <p className='property-price'>Price: ${property.price.toLocaleString()}</p>
      <p className='property-location'>Location: {property.address}</p>
        <div>
        <Link className="home-link" to={"/"}>Back to Home</Link>
        <Link className="properties-link" to={`/properties/`}>View More Properties</Link>
        </div>
    </div>
  );
};

export default PropertyDetail;