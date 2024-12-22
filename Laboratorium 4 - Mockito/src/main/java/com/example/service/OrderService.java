package com.example.service;

import com.example.domain.Order;

public class OrderService {
    private PaymentService paymentService;
    private InventoryService inventoryService;
    private NotificationService notificationService;


    public OrderService(PaymentService paymentService,
                        InventoryService inventoryService,
                        NotificationService notificationService) {
        this.paymentService = paymentService;
        this.inventoryService = inventoryService;
        this.notificationService = notificationService;
    }

    public boolean placeOrder(Order order) {
        // Sprawdź dostępność produktu
        if (!inventoryService.isProductAvailable(order.getProduct())) {
            return false;
        }

        // Spróbuj przetworzyć płatność
        boolean paymentResult;
        try {
            paymentResult = paymentService.processPayment(order);
        } catch (Exception e) {
            // Obsługa wyjątku np. logowanie, ale tu zwróćmy po prostu false
            return false;
        }

        if (!paymentResult) {
            return false;
        }

        // Jeśli wszystko OK, wyślij powiadomienie
        notificationService.notifyUser(order.getUser(), "Your order has been placed successfully.");
        return true;
    }
}
