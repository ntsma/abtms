var PROTOCOL = window.location.protocol;
var HOSTNAME = window.location.hostname;
var PORT = window.location.port;

var URL = PROTOCOL + "//" + HOSTNAME + ":" + PORT;

$(document).ready(function(event){
  $("#btnResetCPF").click(function(event) {
    var cpf = $("#cpf").val();

    $.ajax({
      url: URL + "/abtms/auth/reset/pf/",
      type: "POST",
      data: {"cpf": cpf},
      success: function(data) {
        console.log("Entrar realizado com sucesso.");
        window.location.replace("/abtms/login/");
      },
      error: function(data) {
        console.log("Houve um problema ao entrar na aplicação.");
        window.location.replace("/abtms/auth/reset/");
      }
    });
  });

  $("#btnResetCNPJ").click(function(event) {
    var cnpj = $("#cnpj").val();

    $.ajax({
      url: URL + "/abtms/auth/reset/pj/",
      type: "POST",
      data: {"cnpj": cnpj},
      success: function(data) {
        console.log("Entrar realizado com sucesso.");
        window.location.replace("/abtms/login/");
      },
      error: function(data) {
        console.log("Houve um problema ao entrar na aplicação.");
        window.location.replace("/abtms/auth/reset/");
      }
    });
  });
});
