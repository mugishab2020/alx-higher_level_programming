// Waiting for the document to be ready
$(document).ready(function() {
    // Making AJAX request to fetch the list of movies
    $.ajax({
      url: "https://swapi-api.alx-tools.com/api/films/?format=json",
      method: "GET",
      dataType: "json",
      success: function(data) {
        var movies = data.results;
        var $listMovies = $("#list_movies");
  
        $.each(movies, function(index, movie) {
          $listMovies.append("<li>" + movie.title + "</li>");
        });
      },
    });
  });
  