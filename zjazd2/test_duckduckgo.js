const { Builder, By, Key, until } = require('selenium-webdriver');
const assert = require('assert');

(async function testDuckDuckGo() {
    let driver = await new Builder().forBrowser('chrome').build();
    try {
        // 1. Przejdź na stronę duckduckgo.com
        await driver.get('https://www.duckduckgo.com');

        // 2. Sprawdź, czy tytuł strony zawiera "DuckDuckGo"
        let title = await driver.getTitle();
        assert.ok(title.includes('DuckDuckGo'), 'Tytuł nie zawiera "DuckDuckGo"');

        // 3. Znajdź pole wyszukiwania i wpisz "Polsko-Japońska Akademia Technik Komputerowych w Gdańsku"
        let searchBox = await driver.findElement(By.name('q'));
        await searchBox.sendKeys('Polsko-Japońska Akademia Technik Komputerowych w Gdańsku', Key.RETURN);

        // 4. Poczekaj na załadowanie wyników wyszukiwania
        await driver.wait(until.elementLocated(By.css('.wLL07_0Xnd1QZpzpfR4W')), 10000);

        // 5. Sprawdź, czy tytuł strony zawiera "Polsko-Japońska Akademia"
        title = await driver.getTitle();
        assert.ok(title.includes('Polsko-Japońska Akademia'), 'Tytuł nie zawiera "Polsko-Japońska Akademia"');

        // 6. Sprawdź, czy pojawiły się wyniki wyszukiwania
        let results = await driver.findElements(By.css('.wLL07_0Xnd1QZpzpfR4W'));
        assert.ok(results.length > 0, 'Brak wyników wyszukiwania');

        // 7. Sprawdź, czy pierwszy wynik zawiera słowo "Akademia" lub "PJATK"
        let firstResult = await results[0].getText();
        assert.ok(firstResult.includes('Akademia') || firstResult.includes('PJATK'), 'Pierwszy wynik nie zawiera "Akademia" ani "PJATK"');

        // 8. Wydrukuj komunikat o zakończeniu testu
        console.log('Test strony duckduckgo.com zakończony pomyślnie.');
    } catch (err) {
        console.error('Błąd podczas wykonywania testu duckduckgo.com:', err);
    } finally {
        await driver.quit();
    }
})();
