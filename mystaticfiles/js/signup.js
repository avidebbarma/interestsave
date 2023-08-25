  document.addEventListener("DOMContentLoaded", function() {
    const pages = document.querySelectorAll('.page');
    const nextButtons = document.querySelectorAll('.next');
    const previousButtons = document.querySelectorAll('.previous');

    let currentPage = 0;

    function showPage(pageNumber) {
      pages.forEach(function(page, index) {
        if (index === pageNumber) {
          page.style.display = 'block';
        } else {
          page.style.display = 'none';
        }
      });
    }

    function goToNextPage() {
      if (currentPage < pages.length - 1) {
        currentPage++;
        showPage(currentPage);
      }
    }

    function goToPreviousPage() {
      if (currentPage > 0) {
        currentPage--;
        showPage(currentPage);
      }
    }

    nextButtons.forEach(function(button) {
      button.addEventListener('click', goToNextPage);
    });

    previousButtons.forEach(function(button) {
      button.addEventListener('click', goToPreviousPage);
    });

    showPage(currentPage);
  });
