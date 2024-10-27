const main = document.querySelector(".biodiversity__main--section");

async function loadBiodiversity() {
  const response = await fetch(".././biodiversity.json");
  const data = await response.json();

  createElements(data);

  // const container = document.createElement("section");
  // document.body.appendChild(container);

  console.log(data);
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

loadBiodiversity();
