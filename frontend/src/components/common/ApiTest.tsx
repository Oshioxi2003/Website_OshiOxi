import React, { useState } from 'react';
import { 
  useBlogPosts, 
  usePricingPlans, 
  useFeaturedServices,
  useContactSubmission,
  useNewsletterSubscription 
} from '../../hooks';

const ApiTest = () => {
  const [showTests, setShowTests] = useState(false);
  
  // Test hooks
  const { data: blogPosts, loading: blogLoading, error: blogError } = useBlogPosts();
  const { data: pricingPlans, loading: pricingLoading, error: pricingError } = usePricingPlans();
  const { data: services, loading: servicesLoading, error: servicesError } = useFeaturedServices();
  
  // Form test hooks
  const { execute: submitContact, loading: contactLoading, data: contactResult } = useContactSubmission();
  const { execute: subscribeNewsletter, loading: newsletterLoading, data: newsletterResult } = useNewsletterSubscription();

  const testContact = async () => {
    await submitContact({
      name: 'Test User',
      email: 'test@example.com',
      subject: 'general',
      message: 'This is a test message from API integration test.'
    });
  };

  const testNewsletter = async () => {
    await subscribeNewsletter({
      email: 'newsletter-test@example.com',
      name: 'Test Subscriber'
    });
  };

  if (!showTests) {
    return (
      <div className="fixed-bottom p-3">
        <button 
          className="btn btn-sm btn-outline-info"
          onClick={() => setShowTests(true)}
        >
          🔧 API Test Panel
        </button>
      </div>
    );
  }

  return (
    <div className="fixed-bottom bg-dark border-top border-secondary p-3" style={{ height: '40vh', overflowY: 'auto' }}>
      <div className="d-flex justify-content-between align-items-center mb-3">
        <h6 className="text-light mb-0">🔧 API Integration Test Panel</h6>
        <button 
          className="btn btn-sm btn-outline-secondary"
          onClick={() => setShowTests(false)}
        >
          ✕
        </button>
      </div>
      
      <div className="row g-3">
        {/* Blog Posts Test */}
        <div className="col-md-3">
          <div className="bg-dark-light p-2 rounded">
            <h6 className="text-info fs-14">Blog Posts</h6>
            {blogLoading && <span className="text-warning fs-12">Loading...</span>}
            {blogError && <span className="text-danger fs-12">Error: {blogError.message}</span>}
            {blogPosts?.results && (
              <span className="text-success fs-12">✅ {blogPosts.results.length} posts loaded</span>
            )}
          </div>
        </div>

        {/* Pricing Plans Test */}
        <div className="col-md-3">
          <div className="bg-dark-light p-2 rounded">
            <h6 className="text-info fs-14">Pricing Plans</h6>
            {pricingLoading && <span className="text-warning fs-12">Loading...</span>}
            {pricingError && <span className="text-danger fs-12">Error: {pricingError.message}</span>}
            {pricingPlans && (
              <span className="text-success fs-12">✅ {pricingPlans.length} plans loaded</span>
            )}
          </div>
        </div>

        {/* Services Test */}
        <div className="col-md-3">
          <div className="bg-dark-light p-2 rounded">
            <h6 className="text-info fs-14">Featured Services</h6>
            {servicesLoading && <span className="text-warning fs-12">Loading...</span>}
            {servicesError && <span className="text-danger fs-12">Error: {servicesError.message}</span>}
            {services && (
              <span className="text-success fs-12">✅ {services.length} services loaded</span>
            )}
          </div>
        </div>

        {/* API Status */}
        <div className="col-md-3">
          <div className="bg-dark-light p-2 rounded">
            <h6 className="text-info fs-14">API Status</h6>
            <div className="d-flex flex-column gap-1">
              <span className={`fs-12 ${(!blogError && !pricingError && !servicesError) ? 'text-success' : 'text-warning'}`}>
                {(!blogError && !pricingError && !servicesError) ? '✅ APIs Working' : '⚠️ Some Issues'}
              </span>
            </div>
          </div>
        </div>

        {/* Form Tests */}
        <div className="col-md-6">
          <div className="bg-dark-light p-2 rounded">
            <h6 className="text-info fs-14">Form Tests</h6>
            <div className="d-flex gap-2 mb-2">
              <button 
                className="btn btn-sm btn-outline-primary"
                onClick={testContact}
                disabled={contactLoading}
              >
                {contactLoading ? 'Testing...' : 'Test Contact'}
              </button>
              <button 
                className="btn btn-sm btn-outline-success"
                onClick={testNewsletter}
                disabled={newsletterLoading}
              >
                {newsletterLoading ? 'Testing...' : 'Test Newsletter'}
              </button>
            </div>
            {contactResult && <div className="text-success fs-12">✅ Contact: {contactResult.message}</div>}
            {newsletterResult && <div className="text-success fs-12">✅ Newsletter: {newsletterResult.message}</div>}
          </div>
        </div>

        {/* Connection Info */}
        <div className="col-md-6">
          <div className="bg-dark-light p-2 rounded">
            <h6 className="text-info fs-14">Connection Info</h6>
            <div className="fs-12 text-light">
              <div>Backend: http://127.0.0.1:8000</div>
              <div>API: http://127.0.0.1:8000/api/v1</div>
              <div>Admin: http://127.0.0.1:8000/admin</div>
            </div>
          </div>
        </div>
      </div>

      <div className="mt-2 text-center">
        <small className="text-muted">
          Open browser DevTools → Network tab to see API calls
        </small>
      </div>
    </div>
  );
};

export default ApiTest;