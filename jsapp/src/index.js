async function randomSVG(){
  const response= await fetch('https://api.github.com/repos/FTurci/write-logos/git/trees/main?recursive=1',{});

  const json = await response.json();
  let tree = json.tree;
  var images = [];

  for (index = 0; index < tree.length; ++index){

    element = tree[index];
    // console.log(element['path'].substring(0,7))
    if (element['path'].substring(0,12)==='src/pathsvg/'){
      // console.log(element);
      images.push(element)
    }

  }
  let which = Math.floor(Math.random() * images.length);

  const path = 'https://raw.githubusercontent.com/FTurci/write-logos/main/'+images[which]['path'];
  console.log("the path", path);
  // resolve(data);
  return path;

  }


async function update(){
    const logo = await randomSVG();
    console.log("the logo", logo);
    let logoDiv = document.getElementById('logo')
    logoDiv.innerHTML = `<img src="${logo}"/>`
}

function toDataURL(url) {
    return fetch(url).then((response) => {
            return response.blob();
        }).then(blob => {
            return URL.createObjectURL(blob);
        });
}

async function downloadSVG() {
      const svg = document.getElementById('logo')
      var url = svg.getElementsByTagName('img')[0].src;
        const a = document.createElement("a");
        a.href = await toDataURL(url);
        a.download = "eXtemporanea.svg";
        document.body.appendChild(a);
        a.click();
        document.body.removeChild(a);
}

async function downloadPNG() {
      const svg = document.getElementById('logo')
      var url = svg.getElementsByTagName('img')[0].src;
      var png = url.replace("pathsvg","pngs")

      url = png.substr(0,png.length-3)+"png"
      console.log(url)
      const a = document.createElement("a");
      a.href = await toDataURL(url);
      a.download = "eXtemporanea.png";
      document.body.appendChild(a);
      a.click();
      document.body.removeChild(a);
}


update();
