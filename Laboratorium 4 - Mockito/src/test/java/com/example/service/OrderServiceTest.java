package com.example.service;

import com.example.domain.Order;
import com.example.domain.Product;
import com.example.domain.User;


import org.junit.Before;
import org.junit.Test;
import org.mockito.InjectMocks;
import org.mockito.Mock;
import org.mockito.MockitoAnnotations;

import static org.mockito.Mockito.*;
import static org.junit.Assert.*;

public class OrderServiceTest {

    @Mock
    private PaymentService paymentService;
    @Mock
    private InventoryService inventoryService;
    @Mock
    private NotificationService notificationService;

    @InjectMocks
    private OrderService orderService;

    private User testUser;
    private Product testProduct;
    private Order testOrder;

    @Before
    public void setUp() {
        MockitoAnnotations.openMocks(this);
        testUser = new User("test@example.com");
        testProduct = new Product("Example Product", 1);
        testOrder = new Order(testUser, testProduct);
    }

    /**
     * Scenariusz: zamówienie jest pomyślnie złożone
     * - Produkt dostępny
     * - Płatność przetworzona pomyślnie
     * - Powiadomienie wysłane
     */
    @Test
    public void testPlaceOrder_Successful() {
        // Given
        when(inventoryService.isProductAvailable(testProduct)).thenReturn(true);
        when(paymentService.processPayment(testOrder)).thenReturn(true);

        // When
        boolean result = orderService.placeOrder(testOrder);

        // Then
        assertTrue(result);
        verify(inventoryService, times(1)).isProductAvailable(testProduct);
        verify(paymentService, times(1)).processPayment(testOrder);
        verify(notificationService, times(1)).notifyUser(testUser, "Your order has been placed successfully.");
    }

    /**
     * Scenariusz: produkt niedostępny
     */
    @Test
    public void testPlaceOrder_ProductUnavailable() {
        // Given
        when(inventoryService.isProductAvailable(testProduct)).thenReturn(false);

        // When
        boolean result = orderService.placeOrder(testOrder);

        // Then
        assertFalse(result);
        verify(inventoryService, times(1)).isProductAvailable(testProduct);
        verify(paymentService, never()).processPayment(any(Order.class));
        verify(notificationService, never()).notifyUser(any(User.class), anyString());
    }

    /**
     * Scenariusz: płatność nie została przetworzona pomyślnie
     */
    @Test
    public void testPlaceOrder_PaymentFailed() {
        // Given
        when(inventoryService.isProductAvailable(testProduct)).thenReturn(true);
        when(paymentService.processPayment(testOrder)).thenReturn(false);

        // When
        boolean result = orderService.placeOrder(testOrder);

        // Then
        assertFalse(result);
        verify(inventoryService, times(1)).isProductAvailable(testProduct);
        verify(paymentService, times(1)).processPayment(testOrder);
        verify(notificationService, never()).notifyUser(any(User.class), anyString());
    }

    /**
     * Scenariusz: wyjątek rzucany przez usługę płatności
     */
    @Test
    public void testPlaceOrder_PaymentException() {
        // Given
        when(inventoryService.isProductAvailable(testProduct)).thenReturn(true);
        when(paymentService.processPayment(testOrder)).thenThrow(new RuntimeException("Payment Service Error"));

        // When
        boolean result = orderService.placeOrder(testOrder);

        // Then
        assertFalse(result);
        verify(inventoryService, times(1)).isProductAvailable(testProduct);
        verify(paymentService, times(1)).processPayment(testOrder);
        verify(notificationService, never()).notifyUser(any(User.class), anyString());
    }
}
