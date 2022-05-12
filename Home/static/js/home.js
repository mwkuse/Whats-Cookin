
let buttonSearch = document.querySelector("#search")
let enterSearch = document.querySelector("#recipeInput")
let recipeButton = document.querySelector("#recipes")

enterSearch.addEventListener('keypress', function (e) {
    if (e.key === 'Enter') {
      query=document.getElementById("recipeInput").value
      localStorage.setItem("recipeVal", query)
    }
})

buttonSearch.addEventListener("click", ()=>{
  query=document.getElementById("recipeInput").value
  localStorage.setItem("recipeVal", query)
})

recipeButton.addEventListener("click", ()=>{
  localStorage.removeItem("recipeVal")
})
