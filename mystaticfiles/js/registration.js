// Function to show/hide pages
function showPage(pageNumber) {
  $(".form-step").removeClass("active");
  $("#page" + pageNumber).addClass("active");
}

// Function to handle the "Next" button click
$(".next-page").on("click", function() {
  var currentPage = $(this).closest(".form-step").attr("id").slice(-1);
  showPage(parseInt(currentPage) + 1);
});

// Function to handle the "Previous" button click
$(".prev-page").on("click", function() {
  var currentPage = $(this).closest(".form-step").attr("id").slice(-1);
  showPage(parseInt(currentPage) - 1);
});

// Function to handle form submission
let popup = document.getElementById("modal");
function openPopUp() {
  popup.classList.add("openPopUp");
};

// Show the first page initially
showPage(1);






