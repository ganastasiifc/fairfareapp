$(document).ready(function () {
  $.getJSON('https://randomuser.me/api/', function (response) {
    console.log(response);
  });
});

