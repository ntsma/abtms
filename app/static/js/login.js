var PROTOCOL = window.location.protocol;
var HOSTNAME = window.location.hostname;
var PORT = window.location.port;

var URL = PROTOCOL + "//" + HOSTNAME + ":" + PORT;

$(document).ready(function(event){
  $("#btnLogin").click(function(event) {
    var email = $("#email").val();
    var password = $("#password").val();

    $.ajax({
      url: URL + "/auth/login/",
      type: "POST",
      data: {"email": email, "password": password},
      success: function(data) {
        console.log("Entrar realizado com sucesso.");
        window.location.replace("/abtms/modules/");            
      },
      error: function(data) {
        $.ajax({
          url: URL + "/auth/login/bussiness/",
          type: "POST",
          data: {"email": email, "password": password},
          success: function(data) {
            console.log("Entrar realizado com sucesso.");
            window.location.replace("/abtms/modules/");            
          },
          error: function(data) {
            console.log("Houve um problema ao entrar na aplicação.");
            window.location.replace("/abtms/login/");
          }
        });
      }
    });
  });
});
