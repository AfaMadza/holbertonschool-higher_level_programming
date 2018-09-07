const $ = window.$;
$(function () {
  $.get('https://swapi.co/api/films/?format=json',
    function (data, textStatus) {
      let results = data.results;
      for (let result in results) {
        $('UL#list_movies').append('<li>' + results[result].title + '</li>');
      }
    });
});
