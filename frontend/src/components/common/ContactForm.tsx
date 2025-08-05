import React, { useState } from 'react';
import { useContactSubmission } from '../../hooks';
import { ContactMessage } from '../../types/api';

const ContactForm = () => {
  const { execute: submitMessage, loading, error, data } = useContactSubmission();
  const [formData, setFormData] = useState<ContactMessage>({
    name: '',
    email: '',
    phone: '',
    company: '',
    subject: 'general',
    message: '',
  });
  const [submitted, setSubmitted] = useState(false);

  const handleChange = (e: React.ChangeEvent<HTMLInputElement | HTMLTextAreaElement | HTMLSelectElement>) => {
    const { name, value } = e.target;
    setFormData(prev => ({
      ...prev,
      [name]: value
    }));
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    
    if (!formData.name || !formData.email || !formData.message) {
      return;
    }

    const result = await submitMessage(formData);
    if (result) {
      setSubmitted(true);
      setFormData({
        name: '',
        email: '',
        phone: '',
        company: '',
        subject: 'general',
        message: '',
      });
      
      // Reset success message after 5 seconds
      setTimeout(() => {
        setSubmitted(false);
      }, 5000);
    }
  };

  return (
    <div className="bg-dark-light rounded-4 p-6 position-relative overflow-hidden">
      <div className="row">
        <div className="col-lg-8">
          <h3 className="text-light mb-4">Get In Touch</h3>
          
          {submitted && data && (
            <div className="alert alert-success mb-4" role="alert">
              <i className="bi bi-check-circle me-2"></i>
              {data.message}
            </div>
          )}

          {error && (
            <div className="alert alert-danger mb-4" role="alert">
              <i className="bi bi-exclamation-triangle me-2"></i>
              {error.message}
            </div>
          )}

          <form onSubmit={handleSubmit}>
            <div className="row g-4">
              <div className="col-md-6">
                <label htmlFor="name" className="form-label text-light">
                  Full Name *
                </label>
                <input
                  type="text"
                  className="form-control bg-dark text-light border-secondary"
                  id="name"
                  name="name"
                  value={formData.name}
                  onChange={handleChange}
                  required
                />
              </div>
              <div className="col-md-6">
                <label htmlFor="email" className="form-label text-light">
                  Email Address *
                </label>
                <input
                  type="email"
                  className="form-control bg-dark text-light border-secondary"
                  id="email"
                  name="email"
                  value={formData.email}
                  onChange={handleChange}
                  required
                />
              </div>
              <div className="col-md-6">
                <label htmlFor="phone" className="form-label text-light">
                  Phone Number
                </label>
                <input
                  type="tel"
                  className="form-control bg-dark text-light border-secondary"
                  id="phone"
                  name="phone"
                  value={formData.phone}
                  onChange={handleChange}
                />
              </div>
              <div className="col-md-6">
                <label htmlFor="company" className="form-label text-light">
                  Company
                </label>
                <input
                  type="text"
                  className="form-control bg-dark text-light border-secondary"
                  id="company"
                  name="company"
                  value={formData.company}
                  onChange={handleChange}
                />
              </div>
              <div className="col-12">
                <label htmlFor="subject" className="form-label text-light">
                  Subject
                </label>
                <select
                  className="form-select bg-dark text-light border-secondary"
                  id="subject"
                  name="subject"
                  value={formData.subject}
                  onChange={handleChange}
                >
                  <option value="general">General Inquiry</option>
                  <option value="support">Technical Support</option>
                  <option value="business">Business Partnership</option>
                  <option value="quote">Request Quote</option>
                  <option value="feedback">Feedback</option>
                  <option value="other">Other</option>
                </select>
              </div>
              <div className="col-12">
                <label htmlFor="message" className="form-label text-light">
                  Message *
                </label>
                <textarea
                  className="form-control bg-dark text-light border-secondary"
                  id="message"
                  name="message"
                  rows={5}
                  value={formData.message}
                  onChange={handleChange}
                  required
                ></textarea>
              </div>
              <div className="col-12">
                <button
                  type="submit"
                  className="btn btn-primary rounded-pill px-4 py-2"
                  disabled={loading}
                >
                  {loading ? (
                    <>
                      <span className="spinner-border spinner-border-sm me-2" role="status">
                        <span className="visually-hidden">Loading...</span>
                      </span>
                      Sending...
                    </>
                  ) : (
                    <>
                      Send Message
                      <i className="bi bi-arrow-right ms-2"></i>
                    </>
                  )}
                </button>
              </div>
            </div>
          </form>
        </div>
        <div className="col-lg-4 d-none d-lg-block">
          <div className="position-absolute top-0 end-0 h-100 w-25">
            <div className="bg-primary opacity-10 h-100 rounded-start-4"></div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default ContactForm;