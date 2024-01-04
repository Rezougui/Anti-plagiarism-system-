const div_Porcessing = document.getElementsByClassName("result_processing");
const div_result = document.getElementsByClassName("result");
const result_file = document.getElementById("result_file").textContent.trim();
const execute_file = document.getElementById("execute_file").textContent.trim();
const timer_load = document.getElementById("timer_load");

hide_result();
fetch("./" + execute_file);

/******************* */
var x = setInterval(function () {
  let timer_value = parseInt(timer_load.textContent.trim());
  timer_load.innerHTML = timer_value - 1;
  console.log(timer_value);
  if (timer_value == 1) {
    clearInterval(x);
  }
}, 1000);

function show_result() {
  div_Porcessing[0].style.display = "none";
  div_result[0].style.display = "block";
}
function hide_result() {
  div_Porcessing[0].style.display = "block";
  div_result[0].style.display = "none";
}

async function getPlagiatResult() {
  let url = "./temp/" + result_file + ".json";
  try {
    let response = await fetch(url);

    if (response) {
      result = await response.json();
      clearInterval(getLogsID);

      renderResult(result);
      show_result();
    }
  } catch (e) {}
}

function renderResult(result) {
  console.log(result);
  let result_length = result.length;
  let nbr_plagait = 0;
  let nbr_unique = 0;
  let nbr_probably = 0;
  let html_result_details = "";
  let html_result_header = "";
  result.forEach((res) => {
    if (res[2] == -1) nbr_plagait++;
    if (res[2] == 0) nbr_probably++;
    if (res[2] == 1) nbr_unique++;

    let htmlSegment = `<div class="card">
                    <div class="icon ${return_color(res[2])}"></div>
                    <div class="card-info">
                          <p><a href='https://www.google.com/search?q="${
                            res[1]
                          }"'>${res[1].slice(0, 76) + "..."}<a></p>
                          <h2 >
                        ${return_text(res[2])}
                          </h2>
                    </div>
                    <h2 class="percentage">${Math.floor(res[0] * 100)}%</h2>
                </div>`;

    html_result_details += htmlSegment;
  });
  html_result_header = ` <div class="result_head" >
                    <div class="">
                        <div class="icon icon_red icon_big ">
                            <h3>
                                ${Math.floor(
                                  (nbr_plagait * 100) / result_length
                                )}%
                                <small>Plagait</small>
                            </h3>
                        </div>

                    </div>
                    <div class="">
                        <div class="icon icon_green icon_big ">
                            <h3>
                                  ${Math.floor(
                                    (nbr_unique * 100) / result_length
                                  )}%
                                <small>Unique</small>
                            </h3>
                        </div>

                    </div>
                    <div class="">
                        <div class="icon icon_yellow icon_big ">
                            <h3>
                                   ${Math.floor(
                                     (nbr_probably * 100) / result_length
                                   )}%
                                <small>Probably</small>
                            </h3>
                        </div>

                    </div>
                </div>
                <h2>More Details </h2>
                `;

  div_result[0].innerHTML += html_result_header + html_result_details;
}
function return_color(color) {
  if (color == -1) return " icon_red";
  if (color == 0) return " icon_yellow";
  if (color == 1) return " icon_green";
}
function return_text(color) {
  if (color == -1) return " Plagiat";
  if (color == 0) return " Not sure";
  if (color == 1) return " Unique";
}
var getLogsID;
getLogsID = setInterval(getPlagiatResult, 300);
//execute();
