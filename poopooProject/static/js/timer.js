const timer = document.querySelector(".js-timer"),
  stpBtn = document.querySelector(".js-timer__stopBtn"),
  strtBtn = document.querySelector(".js-timer__strBtn");

let TIME = 0;
let cron; // clearInterval을 위한 변수

function startBtn() {
  while (1) {
    TIME = TIME + 1;
    timer.innerHTML = TIME;
    sleep(1000);
  }
}

strtBtn.addEventListener("click", startBtn);
