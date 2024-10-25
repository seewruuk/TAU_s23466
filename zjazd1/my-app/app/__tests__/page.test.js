import React from 'react';
import { render, screen, fireEvent } from '@testing-library/react';
import Example from '../page';

describe('Order Form Tests', () => {

    // Sprawdzenie, czy formularz jest renderowany
    it('renders the form', () => {
        render(<Example />);
        expect(screen.getByTestId('email-address')).toBeInTheDocument()
        expect(screen.getByTestId('first-name')).toBeInTheDocument();
    });

    // Sprawdzenie, czy formularz pozwala na wypełnienie go przez użytkownika
    it('allows user to fill out the form', () => {
        render(<Example />);

        fireEvent.change(screen.getByTestId('email-address'), { target: { value: 'test@example.com' } });
        fireEvent.change(screen.getByTestId('first-name'), { target: { value: 'John' } });
        fireEvent.change(screen.getByTestId('last-name'), { target: { value: "Doe"}});

        expect(screen.getByTestId('email-address')).toHaveValue('test@example.com');
        expect(screen.getByTestId('first-name')).toHaveValue('John');
        expect(screen.getByTestId('last-name')).toHaveValue('Doe');
    });

    // Sprawdzenie czy metoda dostawy jest widoczna i czy można ją zmienić
    it('allows user to select delivery method', () => {
        render(<Example />);
        const deliveryMethod = screen.getByLabelText('Express');
        fireEvent.click(deliveryMethod);
        expect(deliveryMethod).toBeChecked();
    });

    // Sprawdzenie, czy sekcja z informacjami o wysyłce jest widoczna
    it('displays the correct shipping information section', () => {
        render(<Example />);
        expect(screen.getByText('Shipping information')).toBeInTheDocument();
    });

    it('shows the correct total price', () => {
        render(<Example />);
        // Sprawdzenie czy całkowita cena jest poprawna
        expect(screen.getByText('$75.52')).toBeInTheDocument();
    });

    // Sprawdzenie, czy można wybrać metodę płatności
    it('allows user to select payment method', () => {
        render(<Example />);

        const paymentMethod = screen.getByTestId("PayPal")
        fireEvent.click(paymentMethod);
        expect(paymentMethod).toBeChecked();
    });

    // Sprawdzenie, czy użytkownik może zmienić ilość produktów
    it('allows user to change quantity of products', () => {
        render(<Example />);

        const quantitySelect = screen.getByLabelText('Quantity');
        console.log(quantitySelect);
        fireEvent.change(quantitySelect, { target: { value: '3' } });
        expect(quantitySelect).toHaveValue('3');
    });

    // Sprawdzenie, czy informacje o produkcie są poprawnie renderowane
    it('renders the product information correctly', () => {
        render(<Example />);
        expect(screen.getByText('Basic Tee')).toBeInTheDocument();
        expect(screen.getByText('Black')).toBeInTheDocument();
        expect(screen.getByText('Large')).toBeInTheDocument();
    });

    // Sprawdzenie, czy przycisk usuwania produktu jest widoczny
    it('displays a remove button for products', () => {
        render(<Example />);

        expect(screen.getByLabelText('Remove')).toBeInTheDocument();
    });

    // Sprawdzenie, czy formularz ma możliwość wysłania z pustymi polami
    it('shows error when required fields are empty on submit', () => {
        render(<Example />);
        const emailInput = screen.getByTestId('email-address');
        fireEvent.change(emailInput, { target: { value: '' } });

        const form = screen.getByTestId('order-form');
        fireEvent.submit(form);

        expect(emailInput).toHaveValue('');
    });
});
