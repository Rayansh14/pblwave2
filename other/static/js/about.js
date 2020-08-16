let imgDiv = document.getElementById("img-div");

if (screen.width < 1000) {
  imgDiv.classList.add("col-7");
  imgDiv.classList.remove("col-5");
  document.getElementById("pDiv").classList.remove("mx-5");
}
