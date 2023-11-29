const form = document.getElementById("form");

form.addEventListener("submit", function (e) {
  e.preventDefault();
  console.log("clicked");
  var formData = new FormData(this);
  // Make a POST request using fetch API
  fetch("", {
    method: "POST",
    body: formData
  }).then(function(response) {
    if (response.ok) {
      // Successful response handling
    } else {
      // Error response handling
      console.log("An error occurred whilst translating.");
    }
  })
  .catch(function(error) {
    // Network or fetch API error handling
    console.log("An error occurred whilst translating. - data:", error);
  });
});