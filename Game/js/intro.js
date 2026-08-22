// js/intro.js

function startGame(){

  // Next page
  window.location.href = "levels.html";
}

function showAbout(){

  document
  .getElementById("aboutPopup")
  .style.display = "flex";
}

function closeAbout(){

  document
  .getElementById("aboutPopup")
  .style.display = "none";
}