<script>
    import { onMount } from 'svelte';
// 🔧 Inställningar – ändra dessa
const startIndex = 1;
const endIndex = 4;
const minutes = 0.1; // t.ex. 0.5 = 30 sekunder

// 🔄 Automatisk växling
let currentIndex = startIndex;
const interval = minutes * 60 * 1000;

onMount(() => {
		const timer = setInterval(() => {
			currentIndex++;
			if (currentIndex > endIndex) currentIndex = startIndex;

			const img = document.getElementById("slide");
			if (img) {
				img.src = `/slides/${currentIndex}.png`;
			}
		}, interval);

		return () => clearInterval(timer); // städa upp om komponenten tas bort
	});




    // Nyheter{
    //     "titel": "Regeringen föreslår bolånelättnader",
    //     "datum": "Regeringen föreslår bolånelättnader",
    //     "text": "Regeringen och SD föreslår lättnader i amortering"
    // }
 
    let time = '';
    let date = '';

    function formatDate(now) {
        const options = { day: 'numeric', month: 'long' };
        return now.toLocaleDateString('sv-SE', options);
    }
    function formatTime(now) {
        return now.toLocaleTimeString('sv-SE', {
            hour: '2-digit',
            minute: '2-digit',
            hour12: false
        });
    }

    function updateClock() {
        const now = new Date();
        date = formatDate(now);
        time = formatTime(now);
    }

    onMount(() => {
        updateClock();
        const interval = setInterval(updateClock, 1000);
        return () => clearInterval(interval);
    });
</script>
<div class="wrapper">
    <header>
        <h1>"Företag Namn Går Här"</h1>
    </header>
    <aside class="clock">
        <h1>{date}</h1>
        <h1>{time}</h1>
    </aside>
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
            <li id="tittle">
                <h2>Regeringen föreslår bolånelättnader</h2>
                <h4>11:28</h4>
            </li>
            <li><p>Regeringen och SD föreslår lättnader i amorteringskraven och höjt bolånetak, meddelar man på en pressträff. Tidöpartierna vill höja bolånetaket från 85 procent till 90 procent. Man vill också skrota amorteringskravet som infördes 2018. Det krävde ytterligare en procent amortering om lån överstiger 450 procent av brutto- inkomsten. Ett tidigare krav blir dock kvar. Det blir alltså ingen paus av alla krav - ett vallöfte från M. De nya reglerna ska träda i kraft den 1 april 2026. </p>
            </li>
            <li><p>Källa SVT</p></li>
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
            "header clock"
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
    .clock {
        grid-area: clock;
        display: flex;
        flex-wrap: wrap;
        gap: 2rem;
        align-items: center;
        justify-content: center;
        font-size: 2rem;
        padding: 1.5%;
        border: solid 0.1rem rgba(255, 255, 255, 0.2);
    }
    .clock h1 {
        font-size: 3rem;
        font-weight: bold;
        width: fit-content;
        height: fit-content;
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
    .nyheter li{
        display: flex;
        flex-direction: column;
        
    }
    .nyheter h2{
        font-size: 1.75rem;
        font-weight: bold;
        padding: .75rem 1rem;
        border: solid 0.1rem rgba(255, 255, 255, 0.2);
        width: fit-content;
        
    }
    .nyheter h4{
        font-size: .9rem;
        font-weight: bold;
        padding: .5rem .5rem;
        padding-left: 0%;
        width: fit-content;
        height: 100%;
    }
    .nyheter p{
        font-size: 1.2rem;
    }
</style>