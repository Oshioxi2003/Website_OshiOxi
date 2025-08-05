import React, { useState } from 'react';
import { useNewsletterSubscription } from '../../hooks';

const NewsletterForm = ({ className = "" }: { className?: string }) => {
  const { execute: subscribe, loading, error, data } = useNewsletterSubscription();
  const [email, setEmail] = useState('');
  const [name, setName] = useState('');
  const [subscribed, setSubscribed] = useState(false);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    
    if (!email) return;

    const result = await subscribe({ email, name });
    if (result) {
      setSubscribed(true);
      setEmail('');
      setName('');
      
      // Reset success message after 3 seconds
      setTimeout(() => {
        setSubscribed(false);
      }, 3000);
    }
  };

  return (
    <div className={className}>
      {subscribed && data ? (
        <div className="alert alert-success" role="alert">
          <i className="bi bi-check-circle me-2"></i>
          {data.message}
        </div>
      ) : (
        <form onSubmit={handleSubmit}>
          <div className="d-flex flex-column flex-md-row gap-3">
            <div className="flex-grow-1">
              <input
                type="text"
                className="form-control bg-dark text-light border-secondary"
                placeholder="Your name (optional)"
                value={name}
                onChange={(e) => setName(e.target.value)}
              />
            </div>
            <div className="flex-grow-1">
              <input
                type="email"
                className="form-control bg-dark text-light border-secondary"
                placeholder="Enter your email"
                value={email}
                onChange={(e) => setEmail(e.target.value)}
                required
              />
            </div>
            <button
              type="submit"
              className="btn btn-primary rounded-pill px-4"
              disabled={loading || !email}
            >
              {loading ? (
                <span className="spinner-border spinner-border-sm" role="status">
                  <span className="visually-hidden">Loading...</span>
                </span>
              ) : (
                'Subscribe'
              )}
            </button>
          </div>
          {error && (
            <div className="text-danger mt-2 fs-14">
              <i className="bi bi-exclamation-triangle me-1"></i>
              {error.message}
            </div>
          )}
        </form>
      )}
    </div>
  );
};

export default NewsletterForm;