import apiClient from './api';
import { API_ENDPOINTS } from '../config/api';
import { Service, ServiceCategory, ServiceInquiry, ServiceStats, ApiResponse } from '../types/api';

export const servicesService = {
  // Get all services with optional filters
  getServices: async (params?: {
    page?: number;
    category?: string;
    search?: string;
    is_featured?: boolean;
    ordering?: string;
  }): Promise<ApiResponse<Service>> => {
    const response = await apiClient.get(API_ENDPOINTS.SERVICES.LIST, { params });
    return response.data;
  },

  // Get single service by slug
  getService: async (slug: string): Promise<Service> => {
    const response = await apiClient.get(API_ENDPOINTS.SERVICES.DETAIL(slug));
    return response.data;
  },

  // Get featured services
  getFeaturedServices: async (): Promise<Service[]> => {
    const response = await apiClient.get(API_ENDPOINTS.SERVICES.FEATURED);
    return response.data;
  },

  // Get service categories
  getCategories: async (): Promise<ServiceCategory[]> => {
    const response = await apiClient.get(API_ENDPOINTS.SERVICES.CATEGORIES);
    return response.data;
  },

  // Submit service inquiry
  submitInquiry: async (inquiryData: ServiceInquiry): Promise<{ message: string; inquiry_id: number }> => {
    const response = await apiClient.post(API_ENDPOINTS.SERVICES.INQUIRIES, inquiryData);
    return response.data;
  },

  // Get service stats
  getStats: async (): Promise<ServiceStats> => {
    const response = await apiClient.get(API_ENDPOINTS.SERVICES.STATS);
    return response.data;
  },
};