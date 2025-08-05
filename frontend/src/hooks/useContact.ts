import { useApi, useAsyncOperation } from './useApi';
import { contactService } from '../services';
import { ContactMessage, Newsletter, FAQ, ContactStats } from '../types/api';

// Hook to get FAQ
export function useFAQ(category?: string) {
  return useApi(() => contactService.getFAQ(category), [category]);
}

// Hook to get FAQ categories
export function useFAQCategories() {
  return useApi(() => contactService.getFAQCategories(), []);
}

// Hook to get contact stats
export function useContactStats() {
  return useApi(() => contactService.getStats(), []);
}

// Hook for contact message submission
export function useContactSubmission() {
  return useAsyncOperation<
    { message: string; contact_id: number },
    [ContactMessage]
  >();
}

// Hook for newsletter subscription
export function useNewsletterSubscription() {
  return useAsyncOperation<
    { message: string; email: string },
    [Newsletter]
  >();
}