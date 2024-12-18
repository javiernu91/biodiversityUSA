import pandas as pd
import numpy as np
from flask import Flask, jsonify, request, Response
from flask_cors import CORS
import matplotlib.pyplot as plt
import io

app = Flask(__name__)

CORS(app)

@app.route('/cundinamarca', methods= ['GET'])

def sendInfoCundBiodiversity():
  #Set the data and save in top_values dataframe
  allEspecies = pd.read_csv('assets/cundBio.csv', usecols=['label', 'count'])
  top_values = allEspecies.nlargest(15, 'count')

  fig, ax = plt.subplots()
 
  # plt.bar(top_values['label'], top_values['count'], color='g')
  # plt.title('TOTAL ESPECIFES OBSERVADAS POR MUNICIPIO', fontsize=18)
  # plt.xlabel('MUNICIPIOS', fontsize=14)
  # plt.ylabel('TOTAL ESPECIES', fontsize=14)

  bars = ax.bar(top_values['label'], top_values['count'], color='limegreen', edgecolor='seagreen', alpha=0.6, width=.8)
  ax.set_title('TOTAL ESPECIFES OBSERVADAS POR MUNICIPIO', fontsize=16, pad=10)
  ax.set_xlabel('MUNICIPIOS', fontsize=12)
  ax.set_ylabel('TOTAL ESPECIES', fontsize=12)

  # Add background color 
  ax.set_facecolor('honeydew')

  # Add padding between maximum value and edge graph
  max_val = top_values['count'].max()
  ax.set_ylim(0, max_val * 1.2)
  # Add a grid background
  ax.grid(axis='y', linestyle='--', alpha=0.7)

  plt.yticks(fontsize=8)
  plt.xticks(fontsize=8, rotation=90)

  # Show the height of every bar
  for bar in bars:
      ax.text(
          bar.get_x() + bar.get_width() / 2,
          bar.get_height() ,
          f'{bar.get_height():.0f}',
          ha='center',
          va='bottom',
          rotation=45,
          fontsize=6,
          color='darkslategrey',
          
      )

  # Adjust margins around the chart
  plt.subplots_adjust(bottom=0.42, left=0.15, right=0.9, top=0.9)

  # Save the grafic in buffer
  buf = io.BytesIO()
  fig.savefig(buf, format="png")
  buf.seek(0)
  # print(buf)

  #Close the figure to free memory
  plt.close(fig)
  return Response(buf.getvalue(), mimetype='image/png')

@app.route('/boyaca', methods= ['GET'])

def sendInfoBoyBiodiversity():
  #Set the data and save in top_values dataframe
  allEspecies = pd.read_csv('assets/boyacaTotalEspecies.csv', usecols=['label', 'especies_region_total'])
  top_values = allEspecies.nlargest(15, 'especies_region_total')

  fig, ax = plt.subplots()

  # plt.bar(top_values['label'], top_values['especies_region_total'], color='g')
  # plt.title('TOTAL ESPECIFES OBSERVADAS POR MUNICIPIO', fontsize=18)
  # plt.xlabel('MUNICIPIOS', fontsize=14)
  # plt.ylabel('TOTAL ESPECIES', fontsize=14)  
  # plt.yticks(fontsize=12, rotation=90)
  # plt.xticks(totalEspecies.label) 

  bars = ax.bar(top_values['label'], top_values['especies_region_total'], color='limegreen', edgecolor='seagreen', alpha=0.6, width=.8)
  ax.set_title('TOTAL ESPECIFES OBSERVADAS POR MUNICIPIO', fontsize=16)
  ax.set_xlabel('MUNICIPIOS', fontsize=12)
  ax.set_ylabel('TOTAL ESPECIES', fontsize=12)

  # Add background color 
  ax.set_facecolor('honeydew')

  # Add height data to bars
  for bar in bars:
    ax.text(
        bar.get_x() + bar.get_width() / 2,
        bar.get_height(),
        f'{bar.get_height():.0f}',
        ha='center',
        va='bottom',
        rotation=45,
        fontsize=6,
        color='darkslategrey'
    )
  # Add padding between maximum value and edge graph
  max_val = top_values['especies_region_total'].max()
  ax.set_ylim(0, max_val * 1.2)

  # Add a grid background
  ax.grid(axis='y', linestyle='--', alpha=0.7)

  plt.yticks(fontsize=8)
  plt.xticks(fontsize=8, rotation=90)

   # Adjust margins around the chart
  plt.subplots_adjust(bottom=0.38, left=0.15, right=0.9, top=0.9)

  buf = io.BytesIO()
  plt.savefig(buf, format="png")
  buf.seek(0)
  # print(buf)
  plt.close(fig)

  return Response(buf.getvalue(), mimetype='image/png')

@app.route('/datosBoyaca')
def getData():
  return {
  "Boyacá": [
    {
      "title": "Ortalis columbiana Hellmayr, 1906",
      "description": "La chachalaca colombiana o guacharaca colombiana2​ (Ortalis columbiana) es una especie de ave crácida del género Ortalis. Es una de las especies endémicas más carismáticas de Colombia, donde habita en bosques del norte, centro y oeste de ese país sudamericano, siempre al oeste de los Andes. Fue considerada como una subespecie de Ortalis guttata, pero a la luz de diferencias vocales, morfológicas y consideraciones biogeográficas, en una mejor aproximación hacia el concepto de especie biológica, y teniendo en consideración las formas prevalecientes en la constitución de los límites entre el resto de las especies del género (del cual se postuló que todos sus integrantes podrían ser considerados como formando una única superespecie), fue reconocido su carácter específico.",
      "image": "https://api.gbif.org/v1/image/cache/200x/occurrence/4867842430/media/67bde138b064089a47620b5fa414e8b1",
      "link": "https://es.wikipedia.org/wiki/Ortalis_columbiana"
    },
    {
      "title": "Synallaxis subpudica P.L.Sclater, 1874",
      "description": "El pijuí de Cundinamarca (Synallaxis subpudica), también denominado chamicero cundiboyacense, pijuí de garganta plateada o rastrojero rabilargo, es una especie de ave paseriforme de la familia Furnariidae perteneciente al numeroso género Synallaxis. Es endémica de Colombia. Mide entre 17 y 18 cm de longitud. La cola es larga, alcanza 10,9 cm de largo y es de color pardo grisáceo. La corona y las alas de color castaño rojizo o rufo contrastan con el dorso pardo con matices grisáceos a oliváceos, la frente y las mejillas grises, las partes inferiores color gris claro blancuzco, brillante en la garganta, que presenta una pequeña mancha negra.",
      "image": "https://avesdeperu.org/wp-content/uploads/2019/03/cinereous-breasted_spinetail-2.jpg",
      "link": "https://es.wikipedia.org/wiki/Synallaxis_subpudica"
    },
    {
      "title": "Crax alberti Fraser, 1852",
      "description": "El paujil colombiano (Crax alberti), también conocido como pavón piquiazul, pavón colombiano, hocco piguiazul, muitú de pico azul y opón, es una especie de ave galliforme de la familia Cracidae endémica del norte de Colombia, desde el piedemonte de la Sierra Nevada de Santa Marta hasta la cuenca baja y media del río Magdalena. No se conocen subespecies. Alcanza en promedio 91 cm de longitud. Sus plumas son negras y brillantes, excepto en la punta de la cola y el abdomen, donde son blancas. El macho presenta sobre el pico carúnculas y cera de color azul. El pico de la hembra carece de prominencias pero la base también es azul, sus partes bajas castañas, pecho y cola con línas blancas y tiene una fase de color rojizo.",
      "image": "https://inaturalist-open-data.s3.amazonaws.com/photos/278952229/large.jpeg",
      "link": "https://es.wikipedia.org/wiki/Crax_alberti"
    },
    {
      "title": "Cistothorus apolinari Chapman, 1914",
      "description": "El cucarachero de pantano o chirriador (Cistothorus apolinari) es una especie de ave de la familia Troglodytidae , endémico de la Cordillera Oriental de los Andes de Colombia. En promedio mide 12,5 cm de longitud. Es de color marrón, más oscuro en la cabeza, con parches color gris alrededor de los ojos; rayas oscuras en el dorso; la garganta, el pecho y el abdomen de color blancuzco a anteado. y cola rojiza. Su canto se compone principalmente de notas bajas, con un sonido característico de twii y hace un llamado territorial que suena como tchorr. Se alimenta de arañas e insectos.",
      "image": "https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcSXDqrxCc_sB2ZpqW-9Os6enm8JZMnm7Z1suqwuCdJWkhuKU_vM",
      "link": "https://es.wikipedia.org/wiki/Cistothorus_apolinari"
    },
    {
      "title": "Pristimantis lynchi (Duellman & Simmons, 1977)",
      "description": "Esta especie es endémica de la Cordillera Oriental en Colombia. Habita en los departamentos de Boyacá y Santander entre los 2460 y 3340 m sobre el nivel del mar en el Páramo de Vigajual. Los machos miden de 21.0 a 27.9 mm y las hembras de 26.7 a 36.4 mm. Esta especie lleva el nombre en honor a John Douglas Lynch.",
      "image": "https://i.ytimg.com/vi/W_amZwEYZtk/maxresdefault.jpg",
      "link": "https://es.wikipedia.org/wiki/Pristimantis_lynchi"
    },
    {
      "title": "Thryophilus nicefori (Meyer de Schauensee, 1946)",
      "description": "El cucarachero de Nicéforo, cucarachero del Chicamocha o ratona de Nicéforo (Thryophilus nicefori) es una especie de ave de la familia Troglodytidae, endémica de Colombia. Vive en el bosque seco y plantaciones con sombrío, entre los 1.100 y 1850 m de altitud. Registrada en matorrales xerofíticos dominados por Acacia y bosques riparios de los municipios de San Gil, Barichara y Galán (Santander). Mide 14,5 cm de longitud. El plumaje de las partes superiores es rufo; presenta superciliar blanco, mejillas y cuello blancos con rayas negras; las partes inferiores son blancuzcas, con matices de color castaño en los lados y los flancos y barras negras en el crísum.",
      "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/ab/Thryothorus_sinaloa_Arizona.jpg/1200px-Thryothorus_sinaloa_Arizona.jpg",
      "link": "https://es.wikipedia.org/wiki/Thryophilus_nicefori"
    },
    {
      "title": "Andinobates virolinensis (Ruiz-Carranza & Ramírez-Pinilla, 1992)",
      "description": "Andinobates virolinensis2​ es una especie de anfibio anuro de la familia Dendrobatidae. Esta especie es endémica de Colombia. Se encuentra en los departamentos de Cundinamarca y Santander entre los 1300 y 1850 m sobre el nivel del mar en la vertiente occidental de la Cordillera Oriental. ",
      "image": "https://i.pinimg.com/736x/a2/b5/2b/a2b52b05f0790f73ca1d7c70f062e7cf.jpg",
      "link": "https://es.wikipedia.org/wiki/Andinobates_virolinensis"
    },
    {
      "title": "Agalychnis terranova Rivera-Correa, Duarte-Cubides, Rueda-Almonacid & Daza-R., 2013",
      "description": "Agalychnis terranova es una especie de anfibio anuro perteneciente a la familia Hylidae. Vive en Colombia. Los científicos la han lo visto entre 240 y 900 metros sobre el nivel del mar. La rana adulta mide 4.7 cm de largo, y la hembra es más grande que el macho. Su piel es verde con muchas verrugas. Esta rana se parece mucho a otras ranas de su género, pero sus lados son anaranjados con verrugas blancas en lugar de azules. Los científicos creen que esta rana es nocturna. Esta especie está amenazada por la actividad minera en y cerca de su hábitat.",
      "image": "https://www.researchgate.net/publication/352881755/figure/fig1/AS:1040765031563264@1625149128105/Adult-male-of-Agalychnis-terranova-CBUMAGANF01173-SVL-437-mm-from-south-western.jpg",
      "link": "https://es.wikipedia.org/wiki/Agalychnis_terranova"
    },
    {
      "title": "Capito hypoleucus Salvin, 1897",
      "description": "El cabezón dorsiblanco, torito dorsiblanco, torito capiblanco, chaboclo de espalda blanca o barbudo de manto blanco, (Capito hypoleucus) es una especie de ave de la familia Capitonidae, es endémica de Colombia, se encuentra principalmente en las sierras de Las Quinchas (Valle del Magdalena). Mide 19 cm, habita en bosques húmedos, principalmente a partir de los 1000 m s. n. m., se los ha visualizado además en cultivos de café y pastizales, se alimentan de semillas, insectos y frutos. Es una especie amenazada, la causa principal es la desforestación.",
      "image": "https://miniaturas.biodiversidad.co/400x,q60/https://inaturalist-open-data.s3.amazonaws.com/photos/133380737/original.jpg",
      "link": "https://es.wikipedia.org/wiki/Capito_hypoleucus"
    },
    {
      "title": "Colostethus inguinalis (Cope, 1868)",
      "description": "Colostethus inguinalis es una especie de anfibio anuro de la familia Dendrobatidae. Esta especie es endémica de Colombia. Habita en los departamentos de Chocó, Antioquia, Córdoba y Boyacá desde el nivel del mar hasta 400 m de altitud.",
      "image": "https://inaturalist-open-data.s3.amazonaws.com/photos/246303669/small.jpeg",
      "link": "https://en.wikipedia.org/wiki/Colostethus_inguinalis"
    }
  ],
  "Cundinamarca": [
    {
      "title": "Allobates niputidea Grant, Acosta-Galvis & Rada, 2007",
      "description": "Allobates niputidea es una especie de anfibio anuro de la familia Aromobatidae. Dorso de color marrón oscuro; franja dorsolateral más clara, desde marrón pálido hasta crema o gris claro, extendiéndose desde el borde posterior del párpado. Flanco marrón oscuro interrumpido por una región pálida, difusa y discreta o un grupo de pequeñas manchas extendiéndose hasta el punto medio del brazo. Patas marrón. Los machos adultos miden aproximadamente 17 mm, presentan garganta, pecho y vientre anterior negros, con una franja lateral oblicua pálida difusa. Las hembras miden 18 mm y tienen el vientre blanco.",
      "image": "https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg26Qchk0MAV9kgAeY2CsyAeOlhnWK5ZNXkn934WPm-67qKECKUhOe11UW4t-X2HwzCkvxbgEPG3K7H1-L5RGvJDNQtkmb4XDmL78jy2HBVzFX5rHT0UaDfPfNYX4OtlE7Vm5BzsNm2wbXg/w1200-h630-p-k-no-nu/allobates-zaparo.jpg",
      "link": "https://es.wikipedia.org/wiki/Allobates_niputidea"
    },
    {
      "title": "Allobates niputidea Grant, Acosta-Galvis & Rada, 2007",
      "description": "Anthocephala es un género de aves apodiformes de la familia Trochilidae que incluye dos especies de colibríes endémicas de Colombia.",
      "image": "https://live.staticflickr.com/65535/50662931161_cc93e2775e_b.jpg",
      "link": "https://es.wikipedia.org/wiki/Anthocephala"
    },
    {
      "title": "Atelopus muisca",
      "description": "Atelopus muisca es una especie de anfibios de la familia Bufonidae. Es endémica de Colombia. Su hábitat natural incluye montanos secos, praderas tropicales o subtropicales a gran altitud, y ríos. Está amenazada de extinción por la pérdida de su hábitat natural.",
      "image": "https://inaturalist-open-data.s3.amazonaws.com/photos/25635/medium.jpg",
      "link": "https://es.wikipedia.org/wiki/Atelopus_muisca"
    },
    {
      "title": "Bolitoglossa adspersa",
      "description": "La salamandra de Chingaza, charchala o salamandra escaladora de Peters (Bolitoglossa adspersa') es una especie de anfibio urodelo de la familia Plethodontidae. Es endémica de los departamentos colombianos de Boyacá, Santander y Cundinamarca y el distrito de Bogotá, en la región de los Andes. Su hábitat son las montañas tropicales húmedas y cubiertas de vegetación, entre los 1750 y los 3600 m de altitud. Su piel es de pigmentación negruzca frecuentemente con líneas cortas de color rojo o anaranjado. Mide en promedio 69 cm de longitud. Carece de membranas interdigitales. Sus hábitos son nocturnos y pasa el día bajo piedras o bajo las hojas caídas de los frailejones. Se alimenta de pequeños invertebrados.",
      "image": "https://s3.animalia.bio/animals/photos/full/1.25x1/bolitoglossa-phalarosoma01.webp?id=4a2a70d751bda0a77634e366b42453b7",
      "link": "https://es.wikipedia.org/wiki/Bolitoglossa_adspersa"
    },
    {
      "title": "Cryptotis thomasi (Merriam, 1897)",
      "description": "Endémica de la Cordillera Oriental de los Andes de Colombia, se encuentra en el bosque nuboso, bosques húmedos y páramos, entre los 2.600 y 3.500 m de altitud.Mide en promedio 8,3 cm de longitud, con cola de 2,9 cm de largo. Pesa entre 7 y 12 gr. Cabeza larga y puntiaguda con ojos muy pequeños y un pigmento rojo en la frente. Pelaje aterciopelado, el dorsal castaño grisáceo a marrón obscuro, el ventral de color ante.Terrestres fosoriales. Solitarios. Se alimentan de insectos, arañas, milpiés y de otros invertebrados como lombrices de tierra. Para desplazarse utilizan pequeños senderos entre la hojarasca, el musgo y las plantas herbáceas. Se refugian debajo de rocas y árboles caídos, preferentemente entre las capas de musgo.",
      "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT9d_FijMl2F8yjjFbSZZzkvw5t7ARF3s_w64Xd0ClTSkMzbGWHxgW_QWQq21yT0AfA6no&usqp=CAU",
      "link": "https://es.wikipedia.org/wiki/Cryptotis_thomasi"
    },
    {
      "title": "Dendropsophus padreluna (Kaplan & Ruiz-Carranza, 1997)",
      "description": "Dendropsophus padreluna es una especie de anfibios de la familia Hylidae. Es endémica de Colombia. Sus hábitats naturales incluyen praderas a gran altitud, pantanos, marismas intermitentes de agua dulce, pastos, jardines rurales y estanques.",
      "image": "https://upload.wikimedia.org/wikipedia/commons/5/50/Dendropsophus_padreluna.jpg",
      "link": "https://es.wikipedia.org/wiki/Dendropsophus_padreluna"
    },
    {
      "title": "Grallaria kaestneri F.G.Stiles, 1992",
      "description": "El tororoí de Cundinamarca (Grallaria kaestneri) ye una especie d'ave de la familia Grallariidae, enantes incluyida na familia Formicariidae, endémica de Colombia. Vive nel monte nublu bien húmedu de l'aguada oriental del Cordal Oriental de los Andes, ente los 1.800 y 2.300 m d'altitú. Mide 15,5 cm de llargor. Plumaxe pardu olivaceu escuru, con lores y aniellu ocular blancos; el gargüelu blancu opaca y el pechu oliva abuxáu con estríes delgaes blanques.",
      "image": "https://cdn.download.ams.birds.cornell.edu/api/v1/asset/561745231/640",
      "link": "https://ast.wikipedia.org/wiki/Grallaria_kaestneri"
    },
    {
      "title": "Hypopyrrhus pyrohypogaster (Tarragon, 1847)",
      "description": "El cacique candela, turpial de vientre rojo o chango ventrirrojo (Hypopyrrhus pyrohypogaster) es una especie de ave paseriforme de la familia Icteridae endémica de Colombia. Es el único miembro del género Hypopyrrhus. Vive en la canopia y los bordes de bosques tropicales de montañas del oeste de Colombia, entre los 1.200 y 2.700 m de altitud. Está amenazado por pérdida de hábitat. El macho mide 31,5 cm de longitud y la hembra 27 cm. Plumaje negro mate, en la cabeza, el cuello y la nuca con ejes brillantes; vientre rojo brillante. El pico y las patas son negros.El iris es amarillo.",
      "image": "https://sao.org.co/wp-content/uploads/2021/11/cacique-candela-Hypopyrrhus-pyrohypogaster.jpg",
      "link": "https://es.wikipedia.org/wiki/Hypopyrrhus_pyrohypogaster#:~:text=El%20cacique%20candela%2C%20turpial%20de,%C3%BAnico%20miembro%20del%20g%C3%A9nero%20Hypopyrrhus."
    }
  ]
}


if __name__ == '__main__':
    app.run(debug=True)