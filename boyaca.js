const main = document.querySelector(".biodiversity__main--section");

async function loadBiodiversity() {
  const response = await fetch(".././biodiversity.json");
  const data = await response.json();
  for (const region in data) {
    if (region === "Boyacá") {
      const title = document.querySelector("#biodiversityTitle");
      let container = document.createElement("section");
      main.appendChild(container);
      container.classList = "biodiversity__section--container";
      title.textContent = `Biodiversidad de ${region}`;
      // console.log(region);
      data[region].map((element) => {
        console.log(
          "title: ",
          element.title,
          "Description: ",
          element.description
        );

        let article = document.createElement("article");
        article.classList = "biodiversity__article";
        container.append(article);

        let subtitle = document.createElement("h2");
        subtitle.classList = "biodiversity__article--title";
        subtitle.innerHTML = element.title;
        article.append(subtitle);

        let description = document.createElement("p");
        description.classList = "biodiversity__article--description";
        description.innerHTML = element.description;
        article.append(description);

        let image = document.createElement("img");
        image.classList = "biodiversity__article--image";
        image.src = element.image;
        article.append(image);
      });
    }
  }
  // const container = document.createElement("section");
  // document.body.appendChild(container);

  console.log(data);
}

loadBiodiversity();
