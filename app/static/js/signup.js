var PROTOCOL = window.location.protocol;
var HOSTNAME = window.location.hostname;
var PORT = window.location.port;

var URL = PROTOCOL + "//" + HOSTNAME + ":" + PORT;

$(document).ready(function(event){
  $("#btnSignup").click(function(event) {
    var name = $("#name").val();
    var email = $("#email").val();
    var password = $("#password").val();

    $.ajax({
      url: URL + "/auth/signup/",
      type: "POST",
      data: {"name": name, "email": email, "password": password},
      success: function(data) {
        console.log("Cadastro realizado com sucesso.");
        window.location.replace("/abtms/login/");              
      },
      error: function(data) {
        console.log("Houve um problema ao cadastrar-se na aplicação.");
        window.location.replace("/abtms/signup/");
      }
    });
  });
});
