const { Builder, By, Key, until } = require('selenium-webdriver');
const assert = require('assert');

(async function testGoogle() {
    let driver = await new Builder().forBrowser('chrome').build();
    try {
        // 1. Przejdź na stronę google.com
        await driver.get('https://www.google.com');

        // 2. Zaakceptuj politykę prywatności (jeśli pojawi się komunikat)
        try {
            let agreeButton = await driver.findElement(By.id('L2AGLb'));
            await agreeButton.click();
        } catch (e) {
            // Ignoruj, jeśli przycisk nie istnieje
        }

        // 3. Sprawdź, czy tytuł strony zawiera "Google"
        let title = await driver.getTitle();
        assert.ok(title.includes('Google'), 'Tytuł nie zawiera "Google"');

        // 4. Wpisz "Selenium WebDriver" w polu wyszukiwania i naciśnij Enter
        let searchBox = await driver.findElement(By.name('q'));
        await searchBox.sendKeys('Selenium WebDriver', Key.RETURN);

        // 5. Poczekaj na załadowanie wyników wyszukiwania
        await driver.wait(until.titleContains('Selenium WebDriver'), 10000);

        // 6. Sprawdź, czy tytuł strony zawiera "Selenium WebDriver"
        title = await driver.getTitle();
        assert.ok(title.includes('Selenium WebDriver'), 'Tytuł nie zawiera "Selenium WebDriver"');

        // 7. Sprawdź, czy pojawiły się wyniki wyszukiwania
        let results = await driver.findElements(By.css('div.g'));
        assert.ok(results.length > 0, 'Brak wyników wyszukiwania');

        // 8. Sprawdź, czy adres URL zawiera słowo kluczowe "Selenium"
        let currentUrl = await driver.getCurrentUrl();
        assert.ok(currentUrl.includes('Selenium'), 'Adres URL nie zawiera "Selenium"');

        console.log('Test strony google.com zakończony pomyślnie.');
    } catch (err) {
        console.error('Błąd podczas wykonywania testu google.com:', err);
    } finally {
        await driver.quit();
    }
})();
