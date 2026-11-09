window.onload = function () {
  console.log("loaded script_get.js");
  document
    .querySelector("#insertPlantFormFetch")
    .addEventListener("submit", async function (event) {
      event.preventDefault();
      console.log("button clicked");
    });
};

const htmlForm = document.querySelector("#insertPlantFormFetch");
const formData = new FormData(htmlForm);
const queryParams = new URLSearchParams(formData).toString();
const url = `/getDataFromForm?${queryParams}`;
try{
    let res = await fetch(url)
    let resJSON = await res.json()
    document.querySelector("#result-container").innerHTML += 
       ` THE NEW RESULT: ${resJSON.data_received}
        OWNER NAME : ${resJSON.owner}
        PLANT NAME : ${resJSON.plantname}`
    console.log(resJSON)

}
   catch(err) { 
   console.log(err)
}