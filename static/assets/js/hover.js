  // document.addEventListener("DOMContentLoaded", function() {
  //   var navbarItems = document.querySelectorAll(".navbar-nav .nav-item");
  //
  //   navbarItems.forEach(function(item) {
  //     item.addEventListener("click", function() {
  //       // Remove the 'active' class from all other items
  //       navbarItems.forEach(function(innerItem) {
  //         innerItem.classList.remove("active");
  //       });
  //
  //       // Add the 'active' class to the clicked item
  //       item.classList.add("active");
  //     });
  //   });
  // });

   $(document).ready(function () {
        // Get the current path of the page
        var currentPath = window.location.pathname;

        // Loop through each navigation link and check if it matches the current path
        $('.nav-item a').each(function () {
            var linkPath = $(this).attr('href');

            if (currentPath === linkPath) {
                // Add the 'active' class to the matching link
                $(this).parent('.nav-item').addClass('active');
            }
        });

        // Add a click event to update the 'active' class on click
        $('.nav-item a').click(function () {
            $('.nav-item').removeClass('active');
            $(this).parent('.nav-item').addClass('active');
        });
    });