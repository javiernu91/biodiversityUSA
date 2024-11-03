const main = document.querySelector(".biodiversity__main--section");
const boyCont = document.querySelector("#boyacaContainer");
const cundCont = document.querySelector("#cundinamarcaContainer");

async function loadBiodiversity() {
  const response = await fetch("http://127.0.0.1:5000/datosBoyaca");
  // const response = await fetch(".././frontend/biodiversity.json");

  const data = await response.json();

  createElements(data);

  // const container = document.createElement("section");
  // document.body.appendChild(container);
}

const createElements = (data) => {
  for (region in data) {
    const titleDepartment = document.createElement("h2");
    titleDepartment.classList = ".page__title biodiversity__page--title";
    titleDepartment.id = region;
    const container = document.createElement("section");
    main.append(titleDepartment);
    main.appendChild(container);
    container.classList = "biodiversity__section--container";
    titleDepartment.textContent = `Biodiversidad de ${region}`;
    console.log(region);
    data[region].map((element) => {
      let articleContainer = document.createElement("a");
      articleContainer.classList = "biodiversity__article--container";
      articleContainer.href = element.link;
      articleContainer.target = "_black";
      container.append(articleContainer);

      let article = document.createElement("article");
      article.classList = "biodiversity__article";
      articleContainer.append(article);

      let image = document.createElement("img");
      image.classList = "biodiversity__article--image";
      image.src = element.image;
      article.append(image);

      let subtitle = document.createElement("h2");
      subtitle.classList = "biodiversity__article--title";
      subtitle.innerHTML = element.title;
      article.append(subtitle);

      let description = document.createElement("p");
      description.classList = "biodiversity__article--description";
      description.innerHTML = element.description;
      article.append(description);
    });
  }
};

//cargar grafica desde el backend

// async function loadGraphic() {
//   const response = await fetch("http://127.0.0.1:5000/boyaca");
//   console.log("Data map: ", response);
//   const image = await response.blob();
//   const urlImage = URL.createObjectURL(image);

//   let graphicImage = document.createElement("img");
//   graphicImage.classList.add("boyaca__graphyc");
//   graphicImage.src = urlImage;

//   boyCont.appendChild(graphicImage);

//   // const container = document.createElement("section");
//   // document.body.appendChild(container);

//   // console.log(data);
// }

// loadGraphic();

loadBiodiversity();
