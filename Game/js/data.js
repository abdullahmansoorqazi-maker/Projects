const GameData = {

  saveHighScore(score){

    let highScore =
    localStorage.getItem("highScore");

    if(
      !highScore ||
      score > highScore
    ){

      localStorage.setItem(
        "highScore",
        score
      );
    }

  },

  getHighScore(){

    return localStorage
    .getItem("highScore") || 0;
  },

  resetGame(){

    localStorage.removeItem(
      "mediumUnlocked"
    );

    localStorage.removeItem(
      "fastUnlocked"
    );

    localStorage.removeItem(
      "extremeUnlocked"
    );

    localStorage.removeItem(
      "highScore"
    );

  }

};