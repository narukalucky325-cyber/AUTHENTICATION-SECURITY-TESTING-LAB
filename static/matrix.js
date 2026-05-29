const canvas = document.getElementById("matrix");
const ctx = canvas.getContext("2d");

canvas.width = window.innerWidth;
canvas.height = window.innerHeight;

let chars = "01ABCDEFGHIJKLMNOPQRSTUVWXYZ";
chars = chars.split("");

let font = 14;
let cols = canvas.width / font;
let drops = Array(Math.floor(cols)).fill(1);

function draw(){
    ctx.fillStyle = "rgba(0,0,0,0.08)";
    ctx.fillRect(0,0,canvas.width,canvas.height);

    ctx.fillStyle = "#00ff88";
    ctx.font = font + "px monospace";

    for(let i=0;i<drops.length;i++){
        let text = chars[Math.floor(Math.random()*chars.length)];
        ctx.fillText(text, i*font, drops[i]*font);

        if(drops[i]*font > canvas.height){
            drops[i]=0;
        }
        drops[i]++;
    }
}

setInterval(draw, 35);