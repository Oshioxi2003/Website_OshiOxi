import React from 'react';
import { PricingPlan } from '../../types/api';

interface PricingCardProps {
  plan: PricingPlan;
  className?: string;
}

const PricingCard = ({ plan, className = "" }: PricingCardProps) => {
  const formatPrice = (price: number) => {
    return price.toFixed(2);
  };

  const handleGetStarted = () => {
    if (plan.button_link) {
      window.open(plan.button_link, '_blank');
    } else {
      // Handle default action or contact form
      window.location.href = '/contact';
    }
  };

  return (
    <div className={`col-md-6 col-lg-4 ${className}`}>
      <div className={`process-card rounded-5 p-6 p-xl-8 text-center position-relative ${plan.is_popular ? 'border-primary border-2' : ''}`}>
        {plan.is_popular && (
          <div className="position-absolute top-0 start-50 translate-middle">
            <span className="badge bg-primary rounded-pill px-3 py-2">
              Most Popular
            </span>
          </div>
        )}
        
        <h4 className="text-light mt-3">{plan.name}</h4>
        <p className="text-light text-opacity-50 mb-0">{plan.description}</p>
        <hr className="my-8" />
        
        <h2 className="text-light">
          ${formatPrice(plan.price)}
          <span className="fs-16 fw-normal">/{plan.price_period}</span>
        </h2>
        
        <hr className="my-8" />
        
        <ul className="list gap-4">
          {plan.features.map((feature, index) => (
            <li 
              key={index}
              className={plan.highlighted_features.includes(feature) ? 'text-primary' : 'text-light text-opacity-75'}
            >
              <i className={`bi ${plan.highlighted_features.includes(feature) ? 'bi-check-circle-fill text-primary' : 'bi-check'} me-2`}></i>
              {feature}
            </li>
          ))}
        </ul>
        
        <div className="mt-8">
          <button
            onClick={handleGetStarted}
            className={`btn ${plan.is_popular ? 'btn-primary' : 'btn-outline-primary'} rounded-pill px-6`}
          >
            <span className="d-inline-block">{plan.button_text}</span>
            <span className="d-inline-block ms-2">
              <i className="bi bi-arrow-right"></i>
            </span>
          </button>
        </div>
      </div>
    </div>
  );
};

export default PricingCard;