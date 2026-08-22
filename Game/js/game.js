// js/game.js

const gameArea =
document.getElementById("gameArea");

const player =
document.getElementById("player");

const scoreText =
document.getElementById("score");

const healthText =
document.getElementById("health");

const levelText =
document.getElementById("currentLevel");

const highScoreText =
document.getElementById("highScore");

/* HIGH SCORE */

highScoreText.innerText =
localStorage.getItem("highScore")
|| 0;

/* GAME VARIABLES */

let score = 0;
let health = 100;

let playerX =
window.innerWidth / 2;

let gameRunning = true;

/* LEVEL SYSTEM */

const level =
localStorage.getItem("selectedLevel");

levelText.innerText =
level.toUpperCase();

/* DIFFICULTY */

let enemySpeed = 3;
let enemySpawn = 1500;

if(level === "medium"){

  enemySpeed = 5;
  enemySpawn = 1000;
}

if(level === "fast"){

  enemySpeed = 7;
  enemySpawn = 700;
}

if(level === "extreme"){

  enemySpeed = 10;
  enemySpawn = 450;
}

/* KEYBOARD */

const keys = {

  left:false,
  right:false
};

document.addEventListener("keydown", e => {

  if(e.key === "ArrowLeft"){

    keys.left = true;
  }

  if(e.key === "ArrowRight"){

    keys.right = true;
  }

  if(e.key === " "){

    shootLaser();
  }

});

document.addEventListener("keyup", e => {

  if(e.key === "ArrowLeft"){

    keys.left = false;
  }

  if(e.key === "ArrowRight"){

    keys.right = false;
  }

});

/* PLAYER MOVE */

function movePlayer(){

  if(keys.left && playerX > 0){

    playerX -= 8;
  }

  if(
    keys.right &&
    playerX < window.innerWidth - 80
  ){

    playerX += 8;
  }

  player.style.left =
  playerX + "px";
}

/* SHOOT */

function shootLaser(){

  if(!gameRunning) return;

  const laser =
  document.createElement("div");

  laser.classList.add("laser");

  laser.style.left =
  (playerX + 37) + "px";

  laser.style.bottom =
  "110px";

  gameArea.appendChild(laser);

  const laserMove =
  setInterval(() => {

    laser.style.bottom =
    parseInt(laser.style.bottom)
    + 12 + "px";

    /* REMOVE LASER */

    if(
      parseInt(laser.style.bottom)
      > window.innerHeight
    ){

      laser.remove();

      clearInterval(laserMove);
    }

    /* COLLISION */

    document
    .querySelectorAll(".enemy")
    .forEach(enemy => {

      const laserRect =
      laser.getBoundingClientRect();

      const enemyRect =
      enemy.getBoundingClientRect();

      if(

        laserRect.left <
        enemyRect.right &&

        laserRect.right >
        enemyRect.left &&

        laserRect.top <
        enemyRect.bottom &&

        laserRect.bottom >
        enemyRect.top

      ){

        /* EXPLOSION EFFECT */

        const explosion =
        document.createElement("div");

        explosion.style.position =
        "absolute";

        explosion.style.left =
        enemy.style.left;

        explosion.style.top =
        enemy.style.top;

        explosion.style.width =
        "80px";

        explosion.style.height =
        "80px";

        explosion.style.borderRadius =
        "50%";

        explosion.style.background =
        "orange";

        explosion.style.boxShadow =
        "0 0 40px red";

        explosion.classList.add(
          "explosion"
        );

        gameArea.appendChild(
          explosion
        );

        setTimeout(() => {

          explosion.remove();

        }, 200);

        /* REMOVE ENEMY */

        enemy.remove();

        laser.remove();

        clearInterval(laserMove);

        /* SCORE */

        score += 10;

        scoreText.innerText =
        score;
      }

    });

  }, 20);

}

/* CREATE ENEMY */

function createEnemy(){

  if(!gameRunning) return;

  const enemy =
  document.createElement("img");

  enemy.src =
  "asid/16.png";

  enemy.classList.add("enemy");

  enemy.style.left =
  Math.random()
  * (window.innerWidth - 70)
  + "px";

  gameArea.appendChild(enemy);

  const enemyMove =
  setInterval(() => {

    enemy.style.top =

    parseInt(
      enemy.style.top || -100
    )

    + enemySpeed + "px";

    /* PLAYER HIT */

    const enemyRect =
    enemy.getBoundingClientRect();

    const playerRect =
    player.getBoundingClientRect();

    if(

      enemyRect.left <
      playerRect.right &&

      enemyRect.right >
      playerRect.left &&

      enemyRect.top <
      playerRect.bottom &&

      enemyRect.bottom >
      playerRect.top

    ){

      enemy.remove();

      clearInterval(enemyMove);

      /* DAMAGE */

      health -= 20;

      /* DAMAGE FLASH */

      document.body.classList.add(
        "damage"
      );

      setTimeout(() => {

        document.body.classList.remove(
          "damage"
        );

      }, 300);

      /* UPDATE HEALTH */

      healthText.innerText =
      health;

      /* GAME OVER */

      if(health <= 0){

        endGame();
      }

    }

    /* REMOVE ENEMY */

    if(
      parseInt(enemy.style.top)
      > window.innerHeight
    ){

      enemy.remove();

      clearInterval(enemyMove);
    }

  }, 20);

}

/* ENEMY SPAWN */

setInterval(
  createEnemy,
  enemySpawn
);

/* GAME LOOP */

function gameLoop(){

  if(gameRunning){

    movePlayer();

    requestAnimationFrame(
      gameLoop
    );
  }

}

gameLoop();

/* END GAME */

function endGame(){

  /* SAVE HIGH SCORE */

  GameData.saveHighScore(
    score
  );

  gameRunning = false;

  document
  .getElementById("finalScore")
  .innerText = score;

  document
  .getElementById("gameOverScreen")
  .style.display = "flex";

  /* LEVEL UNLOCK */

  if(
    level === "slow" &&
    score >= 100
  ){

    localStorage.setItem(
      "mediumUnlocked",
      "true"
    );
  }

  if(
    level === "medium" &&
    score >= 200
  ){

    localStorage.setItem(
      "fastUnlocked",
      "true"
    );
  }

  if(
    level === "fast" &&
    score >= 300
  ){

    localStorage.setItem(
      "extremeUnlocked",
      "true"
    );
  }

}

/* BUTTONS */

function restartGame(){

  location.reload();
}

function goLevels(){

  window.location.href =
  "levels.html";
}