    // This function will be called after a successful Google sign-in
    function onSignIn(googleUser) {
      var profile = googleUser.getBasicProfile();
      var email = profile.getEmail();
      // Do something with the user's email (e.g., pass it to the server for authentication)
    }

    // Handle the form submission
    document.getElementById('login-form').addEventListener('submit', function(event) {
      event.preventDefault();
      var email = document.getElementById('email').value;
      var password = document.getElementById('password').value;
      // Add your login logic here
    });
  