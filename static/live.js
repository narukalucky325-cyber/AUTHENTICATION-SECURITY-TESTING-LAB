async function load(){
    let res = await fetch("/api/live");
    let data = await res.json();

    let box = document.getElementById("logs");
    box.innerHTML = "";

    data.forEach(l=>{
        box.innerHTML += `<p>[${l[2]}] ${l[0]} - ${l[1]}</p>`;
    });
}

setInterval(load, 2000);
load();