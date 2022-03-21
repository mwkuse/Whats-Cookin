let buttonSearch = document.querySelector("#search")
let enterSearch = document.querySelector("#recipeInput")

enterSearch.addEventListener('keypress', function (e) {
    if (e.key === 'Enter') {
      query=document.getElementById("recipeInput").value
      sendAPIRequest(query)
    }
})

buttonSearch.addEventListener("click", ()=>{
  query=document.getElementById("recipeInput").value
  sendAPIRequest(query)
})

async function sendAPIRequest(query){
  let API_ID = "API ID HERE"
  let API_KEY = "API KEY HERE"
  let response = await fetch(`https://api.edamam.com/api/recipes/v2?type=public&q=${query}&app_id=${API_ID}&app_key=${API_KEY}`);
  let data = await response.json()
  console.log(data)
  useAPIData(data)
}

function useAPIData(data){
  document.querySelector("#content").innerHTML = ``
  if (data.hits.length > 0){
    for (let i = 0; i < data.hits.length; i++) {
      document.querySelector("#content").innerHTML += `
        <div class="col-md-6">
          <div class="card" style="width: 28rem;">
            <img src="${data.hits[i].recipe.image}" class="card-img-top" alt="...">
            <div class="card-body">
              <h5 class="card-title">${data.hits[i].recipe.label}</h5>
              <p class="card-text">
                Source: ${data.hits[i].recipe.source}
              </p>
              <a href="${data.hits[i].recipe.url}" class="btn btn-primary">Explore Recipe</a>
            </div>
          </div>
        </div>
      `
    }
  }
  else{
    document.querySelector("#content").innerHTML = `<h1> No Recipe Found </h1>`
  }
}
