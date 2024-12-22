package com.example.service;

import com.example.domain.User;

public interface NotificationService {
    void notifyUser(User user, String message);
}
