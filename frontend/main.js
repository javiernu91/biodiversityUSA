const $ = (el) => document.querySelector(el);

const map = $(".boyacá__map--image");
const boyCont = $(".images__boy--container");
const cundCont = $(".images__cund--container");

document.addEventListener("click", function (event) {
  const element = event.target; // El elemento donde se hizo clic

  if (element.classList.contains("maps__button--actions"))
    element.classList.toggle("maps__button--actions-hover");
  console.log(element);
});

// cargar grafica de boyacá desde el backend

async function loadBoyacaGraphic() {
  const response = await fetch("http://127.0.0.1:5000/boyaca");
  console.log("Data map: ", response);
  const image = await response.blob();
  const urlImage = URL.createObjectURL(image);

  let graphicImage = document.createElement("img");
  graphicImage.classList.add("boyaca__graphyc");
  graphicImage.src = urlImage;
  graphicImage.alt = "Gráfica de especies por municipio de cundinamarca";

  console.log(urlImage);

  boyCont.appendChild(graphicImage);

  // const container = document.createElement("section");
  // document.body.appendChild(container);
}

async function loadCundGraphic() {
  const response = await fetch("http://127.0.0.1:5000/cundinamarca");
  console.log("Data map: ", response);
  const image = await response.blob();
  const urlImage = URL.createObjectURL(image);

  let graphicImage = document.createElement("img");
  graphicImage.classList.add("cund__graphyc");
  graphicImage.src = urlImage;
  graphicImage.alt = "Gráfica de especies por municipio de cundinamarca";

  console.log(urlImage);

  cundCont.appendChild(graphicImage);

  // const container = document.createElement("section");
  // document.body.appendChild(container);
}

loadBoyacaGraphic();
loadCundGraphic();
