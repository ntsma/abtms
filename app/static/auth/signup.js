var PROTOCOL = window.location.protocol;
var HOSTNAME = window.location.hostname;
var PORT = window.location.port;

var URL = PROTOCOL + "//" + HOSTNAME + ":" + PORT;

$(document).ready(function(event){
  $("#btnSignupP").click(function(event) {
    var name = $("#name").val();
    var email = $("#email").val();
    var password = $("#password").val();
    var phone = $("#phone").val();
    var cpf = $("#cpf").val();

    $.ajax({
      url: URL + "/auth/signup/person/",
      type: "POST",
      data: {"name": name, "email": email, "password": password, "phone": phone, "cpf": cpf},
      success: function(data) {
        console.log("Cadastrado realizado com sucesso.");
        window.location.replace("/abtms/login/");
      },
      error: function(data) {
        console.log("Houve um problema ao entrar na aplicação.");
        window.location.replace("/abtms/");
      }
    });
  });

  $("#btnSignupB").click(function(event) {
    var name = $("#name").val();
    var email = $("#email").val();
    var password = $("#password").val();
    var phone = $("#phone").val();
    var cnpj = $("#cnpj").val();

    $.ajax({
      url: URL + "/auth/signup/bussiness/",
      type: "POST",
      data: {"name": name, "email": email, "password": password, "phone": phone, "cnpj": cnpj},
      success: function(data) {
        console.log("Cadastrado realizado com sucesso.");
        window.location.replace("/abtms/login/");
      },
      error: function(data) {
        console.log("Houve um problema ao entrar na aplicação.");
        window.location.replace("/abtms/");
      }
    });
  });
});
