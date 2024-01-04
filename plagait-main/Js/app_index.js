const user_file = document.getElementById("user_file");
const user_text = document.getElementById("user_text");
const form = document.getElementById("form");

if (form) {
  form.addEventListener("submit", (event) => {
    if (user_text.value == "") {
      if (user_file.value == "") {
        event.preventDefault();
        alert("Please put a text or choose a document.");
      }
    }
  });
}
//--------------------
