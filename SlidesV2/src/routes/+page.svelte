<script>
    import { onMount } from 'svelte';

    // Nyheter setup
    let news = null;
	let newsError = false;

    // Hämtar nyheter från en JSON-fil, måste starta pyton för skapa filen
    // cd ./ ||CMD>| $python .\python\svt.py
	onMount(async () => {
		try {
			const res = await fetch('/src/lib/svt_news/svt_news.json');
			if (!res.ok) throw new Error('Nyhetsfilen kunde inte hämtas');
			news = await res.json();
		} catch (err) {
			console.error('Fel vid hämtning av nyheter:', err);
			newsError = true;
		}
	});
    let newsIndex = 0
    const maxIndex = 2; 

	const newsTimer = 0.75 * 60 * 1000;
	onMount(() => {
		const interval = setInterval(() => {
			newsIndex = (newsIndex + 1) > maxIndex ? 0 : newsIndex + 1;
		}, newsTimer);

		return () => clearInterval(interval);
	});

// Bildspel setup    
// Inställningar - Bildspel -----------------------------------------
const startIndex = 1; // Starta siffra (rekomderas 1)
const endIndex = 4; // Sluta siffra
const minutes = 0.5; //Tids intervalvet att byta bilder i minuter (t.ex. 0.5 = 30 sekunder)
// Inställningar - Bildspel - slut -----------------------------------------


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

		return () => clearInterval(timer); 
	});

    // Klocka setup
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
        <img src="/dahlenbergs.svg" alt="Dahlenbergs logo">
    </header>
    <aside class="clock">
        <h1>{date}</h1>
        <h1>{time}</h1>
    </aside>
    <main>
    <img id="slide" src="/slides/1.png" alt="Slide">
    </main>
    <aside class="Väder">
        <!-- Smhi data -->
    <!-- https://opendata.smhi.se/metobs/introduction -->
        <h1>Vädert i Skene</h1>
        <h2>Luft tempratur: 4°</h2>
        <h2>Vindhastighet: 0,45 m/s</h2>
        <h2>Nederbörd "kod"</h2>
        <h2>Nederbördsintensitet: 20 ml/s</h2>
        <h2>Snödjup: 1m</h2>
    </aside>
    <aside class="nyheter">
        <h1>Nyheter</h1>
        {#if news}
		<ol>
			<li id="tittle">
				<h2>{news[newsIndex].title}</h2>
				<h4>{news[newsIndex].published}</h4>
			</li>
			<li>
				<p>{@html news[newsIndex].body.replace(/\n/g, '<br>')}</p>
			</li>
			<li id="source"><p>Källa: SVT</p></li>
		</ol>
	{:else if newsError}
		<p>Kunde inte hämta nyheter (fil saknas?)</p>
	{:else}
		<p>kan inte läsa in nyheter</p>
	{/if}
        
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
        
        background-image: linear-gradient(#003467, rgb(37, 37, 37));
        display: grid;
        grid-template-areas: 
            "clock header "
            "main aside1"
            "aside2 aside2";
        grid-template-rows: 1fr 6fr 4fr;
        grid-template-columns: 3fr 1fr;
    }
    header {
        grid-area: header;
        display: flex;
        justify-content: center;
        align-items: center;
        font-size: 5rem;
    }
    header img {
        height: fit-content;
        padding: 5%;
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
        /* border: solid 0.1rem rgba(255, 255, 255, 0.2); */
    }
    .clock h1 {
        font-size: 5rem;
        font-weight: bold;
        width: fit-content;
        height: fit-content;
    }
    main{
        grid-area: main;
        height: 100%;
    }
    .Väder{
        grid-area: aside2; 
        padding: 0% .5%;
        display: flex;
        flex-wrap: wrap;
        align-items: center;
        justify-content: center;
        font-size: 1.5rem;
        gap: 4rem;
        font-weight: bold;
    }
    .Väder h1{
        font-size: 3rem;
        font-weight: bold;
        width: fit-content;
        height: fit-content;
        margin: 0% 5%;
    }
    .nyheter{
        grid-area: aside1; 
        padding: 5%;
        font-size: 1.75rem;
        gap: 1rem;
        box-shadow: 0 0 0.5rem rgba(255, 255, 255, 0.1);
        overflow: hidden;
    }
    .nyheter h1{
        font-size: 3rem;
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
        font-size: 1.5rem;
        font-weight: bold;
        padding: .75rem 1rem;
        border: solid 0.1rem rgba(255, 255, 255, 0.2);
        width: fit-content;
    }
    .nyheter h4{
        font-size: 1.1rem;
        font-weight: bold;
        padding: .5rem .5rem;
        padding-left: 0%;
        width: fit-content;
        height: 100%;
    }
    .nyheter p{
        /* Text storlek på nyheter ändras här */
        font-size: 1.3rem;
    }
    #source{
        text-align: end;
        width: 100%;
        font-style: italic;
        font-weight: 100;
    }
</style>