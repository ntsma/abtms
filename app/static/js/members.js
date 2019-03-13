var PROTOCOL = window.location.protocol;
var HOSTNAME = window.location.hostname;
var PORT = window.location.port;

var URL = PROTOCOL + "//" + HOSTNAME + ":" + PORT;

$(document).ready(function(event){
  $(".bankingBilletValues").each(function(index){
    $(this).text(parseInt($(this).text()) / 100);
  });
});
