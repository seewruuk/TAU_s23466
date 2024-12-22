package com.example.service;

import com.example.domain.Product;

public interface InventoryService {
    boolean isProductAvailable(Product product);
}
