# LarsSlides

Detta dokument innehåller grundläggande information om hur programmet fungerar och hur du kommer igång.

## Kort bakgrund

LarsSlides är en ensidig hemsida som visar ett bildspel med bilder (standard: 1–4 bilder). Utöver detta visas även:

- Tid och datum
- Nyheter från SVT Snabbkollen (via web scraping)
- Väderinformation från SMHI (via web scraping)

Projektet består av två delar:
- En Python-del som samlar in nyheter och väder via web scraping
- En Svelte-del som utgör själva hemsidan

## Vad som krävs för att köra programmet

### Internetanslutning

Datorn måste vara ansluten till internet för att kunna hämta nyheter och väderdata.

### Docker

Projektet kräver [Docker Desktop](https://www.docker.com/products/docker-desktop). Applikationen körs som en Docker-container och fungerar inte utan detta.

### Visual Studio Code (valfritt men rekommenderas)

Det är rekommenderat att använda [Visual Studio Code](https://code.visualstudio.com/download) för att enkelt kunna redigera inställningar, till exempel antal bilder eller hur länge varje bild visas.

#### Tillägg för Visual Studio Code

Installera tillägget **Svelte for VS Code** för bättre stöd vid redigering:  
[https://marketplace.visualstudio.com/items?itemName=svelte.svelte-vscode](https://marketplace.visualstudio.com/items?itemName=svelte.svelte-vscode)

## Hur startar man programmet?

*Instruktioner kommer – tanken är att det ska räcka med att starta containern i Docker Desktop och låta den köra i bakgrunden.*

Just nu är det köra `python .\python\svt.py` för nyheterna.Ej stöd>> [ Sedan `python .\python\smhi.py` för väder. Uppderas bara när programmet startas.].

För få upp sidan, i slidesV2 mappen skriv i konsolen npm run dev `python .\python\svt.py`
Sedan gå till valfri webläsare datorn som kör programmet till webadresse `http://localhost:5173/`


## Bildhantering

### Byta ut bilder

1. Gå till mappen `SlidesV2/static/slides`
2. Lägg in dina bilder där. Programmet börjar med `1.png` och visar uppåt i nummerordning till 4(går att ändra) (exempel: `1.png`, `2.png`, etc.)
3. Bilderna måste vara i **.png-format** – andra format som `.jpg` fungerar inte.

Behöver du konvertera bilder? Du kan använda:  
[https://cloudconvert.com/png-converter]

### Ändra antal bilder och visningstid

1. Öppna mappen `SlidesV2/src/routes`
2. Redigera filen `+page.svelte`
3. Tidigt i filen finns inställningarna där du kan:
   - Ange vilken bild som är första respektive sista i bildspelet
   - Ändra hur länge varje bild visas (anges i minuter)
I filen är det tydligt makerat vart du ska ändra. 

Använd Visual Studio Code för att underlätta redigeringen. Annars i notepad. M

## Utvecklat av

- **Felix Lindblom**  
  GitHub: [Fennessy](https://github.com/Fennessy)  
  E-post: kingliker03@gmail.com

- **André Anberg**  
  GitHub: [andreanberg](https://github.com/andreanberg)
