<script>
// 🔧 Inställningar – ändra dessa
const startIndex = 1;
const endIndex = 4;
const minutes = 0.1; // t.ex. 0.5 = 30 sekunder

// 🔄 Automatisk växling
let currentIndex = startIndex;
const interval = minutes * 60 * 1000;

setInterval(() => {
currentIndex++;
if (currentIndex > endIndex) currentIndex = startIndex;
document.getElementById("slide").src = `/slides/${currentIndex}.png`;
}, interval);




    // Nyheter{
    //     "titel": "Regeringen föreslår bolånelättnader",
    //     "datum": "Regeringen föreslår bolånelättnader",
    //     "text": "Regeringen och SD föreslår lättnader i amortering"
    // }
 



</script>
<div class="wrapper">
    <header>
        <h1>"Företag Namn Går Här"</h1>
    </header>
    <main>
    <img id="slide" src="/slides/1.png" alt="Slide image">
    </main>
    <aside class="Väder">
        <!-- Smhi data -->
    <!-- https://opendata.smhi.se/metobs/introduction -->
        <h1>Väder</h1>
        <h2>Luft tempratur: 4°</h2>
        <h2>Vindhastighet: 0,45 m/s</h2>
        <h2>Nederbörd "kod"</h2>
        <h2>Nederbördsintensitet: 20 ml/s</h2>
        <h2>Snödjup: 1m</h2>
    </aside>
    <aside class="nyheter">
        <h1>Nyheter</h1>
        <ol>
            <li id="tittle"><h2>Regeringen föreslår bolånelättnader</h2></li>
            <li><p>Regeringen och SD föreslår lättnader i amorteringskraven och höjt bolånetak, meddelar man på en pressträff. Tidöpartierna vill höja bolånetaket från 85 procent till 90 procent. Man vill också skrota amorteringskravet som infördes 2018. Det krävde ytterligare en procent amortering om lån överstiger 450 procent av brutto- inkomsten. Ett tidigare krav blir dock kvar. Det blir alltså ingen paus av alla krav - ett vallöfte från M. De nya reglerna ska träda i kraft den 1 april 2026. </p>
            </li><li><p>Källa SVT</p></li>
        </ol>
        
    </aside>
</div>
<style>
    *{
        color: white;
        font: "Host Grotesk", sans-serif ;
    }
    .wrapper {
        height: 100vh;
        background-color: rgb(37, 37, 37);   
        display: grid;
        grid-template-areas: 
            "header header"
            "main aside1"
            "aside2 aside2";
        grid-template-rows: 1fr 5fr 2fr;
        grid-template-columns: 2fr 1fr;
    }
    header {
        width: 100%;
        height: fit-content;
        display: flex;
        justify-content: center;
        align-items: center;
        font-size: 5rem;
        
    }
    main{
        grid-area: main;
        height: 100%;
    }
    .Väder{
        grid-area: aside1; 
        padding: 1.5%;
        display: flex;
        flex-wrap: wrap;
        align-items: start;
        justify-content: center;
        flex-direction: column;
        font-size: 1.5rem;
        gap: .1rem;
        font-weight: bold;
        border:  solid 0.1rem rgba(255, 255, 255, 0.2);
    }
    .Väder h1{
        font-size: 3rem;
        font-weight: bold;
        width: fit-content;
        height: fit-content;
    }
    .nyheter{
        grid-area: aside2; 
        padding: 1%;
        display: grid;
        grid-template-columns: 1fr 3fr;
        font-size: 1.75rem;
        gap: 1rem;
        box-shadow: 0 0 0.5rem rgba(255, 255, 255, 0.1);
    }
    .nyheter h1{
        font-size: 4rem;
        font-weight: bold;
        padding: .75rem 1rem;
        width: fit-content;
        height: fit-content;
        align-self: center;
    }
    .nyheter ol{
        display: flex;
        flex-wrap: wrap;
    }
    .nyheter h2{
        font-size: 1.75rem;
        font-weight: bold;
        padding: .75rem 1rem;
        border: solid 0.1rem rgba(255, 255, 255, 0.2);
        width: fit-content;
        height: fit-content;
    }
    .nyheter p{
        font-size: 1rem;
    }
</style>