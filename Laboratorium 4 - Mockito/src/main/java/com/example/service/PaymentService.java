package com.example.service;

import com.example.domain.Order;

public interface PaymentService {
    boolean processPayment(Order order);
}
