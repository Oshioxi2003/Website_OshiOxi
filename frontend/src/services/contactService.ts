import apiClient from './api';
import { API_ENDPOINTS } from '../config/api';
import { ContactMessage, Newsletter, FAQ, ContactStats } from '../types/api';

export const contactService = {
  // Submit contact message
  submitMessage: async (messageData: ContactMessage): Promise<{ message: string; contact_id: number }> => {
    const response = await apiClient.post(API_ENDPOINTS.CONTACT.MESSAGES, messageData);
    return response.data;
  },

  // Subscribe to newsletter
  subscribeNewsletter: async (subscriptionData: Newsletter): Promise<{ message: string; email: string }> => {
    const response = await apiClient.post(API_ENDPOINTS.CONTACT.NEWSLETTER, subscriptionData);
    return response.data;
  },

  // Get FAQ list
  getFAQ: async (category?: string): Promise<FAQ[]> => {
    const params = category ? { category } : undefined;
    const response = await apiClient.get(API_ENDPOINTS.CONTACT.FAQ, { params });
    return response.data;
  },

  // Get FAQ categories
  getFAQCategories: async (): Promise<{ categories: string[] }> => {
    const response = await apiClient.get(API_ENDPOINTS.CONTACT.FAQ_CATEGORIES);
    return response.data;
  },

  // Get contact stats
  getStats: async (): Promise<ContactStats> => {
    const response = await apiClient.get(API_ENDPOINTS.CONTACT.STATS);
    return response.data;
  },
};