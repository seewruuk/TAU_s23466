const { Builder, By, Key, until } = require('selenium-webdriver');
const assert = require('assert');

(async function testWikipedia() {
    let driver = await new Builder().forBrowser('chrome').build();
    try {
        // 1. Przejdź na stronę wikipedia.org
        await driver.get('https://www.wikipedia.org');

        // 2. Sprawdź, czy tytuł strony zawiera "Wikipedia"
        let title = await driver.getTitle();
        assert.ok(title.includes('Wikipedia'), 'Tytuł nie zawiera "Wikipedia"');

        // 3. Wpisz "Selenium" w polu wyszukiwania i naciśnij Enter
        let searchBox = await driver.findElement(By.name('search'));
        await searchBox.sendKeys('Selenium', Key.RETURN);

        // 4. Poczekaj na załadowanie artykułu i sprawdź tytuł artykułu
        await driver.wait(until.elementLocated(By.id('firstHeading')), 10000);
        let heading = await driver.findElement(By.id('firstHeading')).getText();
        assert.ok(heading.includes('Selenium'), 'Tytuł artykułu nie zawiera "Selenium"');

        // 5. Sprawdź, czy treść artykułu zawiera słowo "chemical"
        let bodyContent = await driver.findElement(By.id('bodyContent')).getText();
        assert.ok(bodyContent.includes('chemical'), 'Treść artykułu nie zawiera słowa "chemical"');

        // 6. Znajdź pierwszy link w głównym artykule i kliknij go
        let firstLink = await driver.findElement(By.css('#bodyContent a'));
        let linkText = await firstLink.getText();
        await firstLink.click();

        // 7. Poczekaj na załadowanie nowej strony i sprawdź, czy tytuł artykułu zawiera tekst linku
        await driver.wait(until.elementLocated(By.id('firstHeading')), 10000);
        heading = await driver.findElement(By.id('firstHeading')).getText();
        assert.ok(heading.includes(linkText), `Tytuł artykułu nie zawiera "${linkText}"`);

        // 8. Sprawdź, czy nowa strona zawiera słowo "element"
        bodyContent = await driver.findElement(By.id('bodyContent')).getText();
        assert.ok(bodyContent.includes('element'), 'Treść nowej strony nie zawiera słowa "element"');

        console.log('Test strony wikipedia.org zakończony pomyślnie.');
    } catch (err) {
        console.error('Błąd podczas wykonywania testu wikipedia.org:', err);
    } finally {
        await driver.quit();
    }
})();
