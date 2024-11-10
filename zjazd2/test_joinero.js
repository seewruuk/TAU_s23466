const {Builder, By, Key, until} = require('selenium-webdriver');
const assert = require('assert');

(async function testJoinero() {
    let driver = await new Builder().forBrowser('chrome').build();
    try {
        // 1. Przejdź na stronę joinero.pl
        await driver.get('https://joinero.pl');

        // 2. Sprawdź, czy tytuł strony zawiera "Joinero"
        let title = await driver.getTitle();
        assert.ok(title.includes('Joinero'), 'Tytuł nie zawiera "Joinero"');

        // 3. Znalezienie inputa
        let searchBox = await driver.findElement(By.css('input[placeholder="Szukaj produktów..."]'));

        // 4. Wpisanie "a"
        await searchBox.sendKeys('a');

        // 5. Poczekanie na sugestie
        await driver.wait(until.elementLocated(By.css('div[class*="absolute"] a')), 5000);

        // 6. Kliknięcie w pierwszą sugestię
        let suggestions = await driver.findElements(By.css('div[class*="absolute"] a'));
        await suggestions[0].click();

        // 6. Poczekaj na załadowanie strony produktu
        await driver.wait(until.titleContains('Przeczytaj'), 10000);

        // 7. Znajdż przycisk "Dodaj do koszyka"
        await driver.wait(until.elementLocated(By.xpath("//button[contains(text(), 'Dodaj do koszyka')]")), 10000);
        let addToCartButton = await driver.findElement(By.xpath("//button[contains(text(), 'Dodaj do koszyka')]"));
        await addToCartButton.click();

        // 8. Poczekaj na potwierdzenie dodania do koszyka
        await driver.wait(until.elementTextIs(driver.findElement(By.css('a[href="/koszyk"] div span')), '1'), 5000);

        console.log('Test strony joinero.pl zakończony pomyślnie.');
    } catch (err) {
        console.error('Błąd podczas wykonywania testu joinero.pl:', err);
    } finally {
        await driver.quit();
    }
})();
