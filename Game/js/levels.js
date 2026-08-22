// js/levels.js

// FIRST LEVEL ALWAYS OPEN

if(!localStorage.getItem("mediumUnlocked")){
  localStorage.setItem("mediumUnlocked", "false");
}

if(!localStorage.getItem("fastUnlocked")){
  localStorage.setItem("fastUnlocked", "false");
}

if(!localStorage.getItem("extremeUnlocked")){
  localStorage.setItem("extremeUnlocked", "false");
}

/* CHECK UNLOCKS */

const mediumUnlocked =
localStorage.getItem("mediumUnlocked");

const fastUnlocked =
localStorage.getItem("fastUnlocked");

const extremeUnlocked =
localStorage.getItem("extremeUnlocked");

/* MEDIUM */

if(mediumUnlocked === "true"){

  const medium =
  document.getElementById("mediumLevel");

  medium.classList.remove("locked");

  medium.classList.add("unlocked");

  medium.innerHTML = `
    <h2>MEDIUM</h2>
    <p>Normal Mode</p>
  `;

  medium.onclick = function(){
    selectLevel('medium');
  };
}

/* FAST */

if(fastUnlocked === "true"){

  const fast =
  document.getElementById("fastLevel");

  fast.classList.remove("locked");

  fast.classList.add("unlocked");

  fast.innerHTML = `
    <h2>FAST</h2>
    <p>Hard Mode</p>
  `;

  fast.onclick = function(){
    selectLevel('fast');
  };
}

/* EXTREME */

if(extremeUnlocked === "true"){

  const extreme =
  document.getElementById("extremeLevel");

  extreme.classList.remove("locked");

  extreme.classList.add("unlocked");

  extreme.innerHTML = `
    <h2>EXTREME</h2>
    <p>Insane Mode</p>
  `;

  extreme.onclick = function(){
    selectLevel('extreme');
  };
}

/* SELECT LEVEL */

function selectLevel(level){

  localStorage.setItem("selectedLevel", level);

  window.location.href = "game.html";
}

/* BACK */

function goBack(){

  window.location.href = "index.html";
}