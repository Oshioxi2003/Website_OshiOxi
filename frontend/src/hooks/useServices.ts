import { useApi, useAsyncOperation } from './useApi';
import { servicesService } from '../services';
import { Service, ServiceCategory, ServiceInquiry, ServiceStats } from '../types/api';

// Hook to get services
export function useServices(params?: {
  page?: number;
  category?: string;
  search?: string;
  is_featured?: boolean;
  ordering?: string;
}) {
  return useApi(() => servicesService.getServices(params), [JSON.stringify(params)]);
}

// Hook to get single service
export function useService(slug: string) {
  return useApi(() => servicesService.getService(slug), [slug]);
}

// Hook to get featured services
export function useFeaturedServices() {
  return useApi(() => servicesService.getFeaturedServices(), []);
}

// Hook to get service categories
export function useServiceCategories() {
  return useApi(() => servicesService.getCategories(), []);
}

// Hook to get service stats
export function useServiceStats() {
  return useApi(() => servicesService.getStats(), []);
}

// Hook for service inquiry submission
export function useServiceInquiry() {
  return useAsyncOperation<
    { message: string; inquiry_id: number },
    [ServiceInquiry]
  >();
}