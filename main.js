const map = document.querySelector(".boyacá__map--image");

document.addEventListener("click", function (event) {
  const element = event.target; // El elemento donde se hizo clic

  if (element.classList.contains("maps__button--actions"))
    element.classList.toggle("maps__button--actions-hover");
  console.log(element);
});

console.log("Aqui estamos");
