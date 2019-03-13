
  function generateToken() {
    var s=document.createElement('script');
    s.type='text/javascript';
    var v=parseInt(Math.random()*1000000);
    s.src='https://sandbox.gerencianet.com.br/v1/cdn/79f97a9a7a34ec16065d9c62e86d0756/'+v;
    s.async=false;
    s.id='79f97a9a7a34ec16065d9c62e86d0756';

    if(!document.getElementById('79f97a9a7a34ec16065d9c62e86d0756')){
      document.getElementsByTagName('head')[0].appendChild(s);
    };

    $gn={
      validForm:true,
      processed:false,
      done:{},
      ready:function(fn){
        $gn.done=fn;
      }
    };

    $gn.ready(function(checkout) {

      var callback = function(error, response) {
        if(error) {
          console.log("Houve um problema ao gerar token.");
          console.error(error);
        } else {
          console.log("Token - " + response["data"]["payment_token"]);
          var token = document.getElementById("token");

          token.value = response["data"]["payment_token"];
        }
      };

      checkout.getPaymentToken({
          brand: document.getElementById("brand").value, // bandeira do cartão
          number: document.getElementById("number").value, // número do cartão
          cvv: document.getElementById("cvv").value, // código de segurança
          expiration_month: document.getElementById("month").value, // mês de vencimento
          expiration_year: document.getElementById("year").value // ano de vencimento
        }, callback);

    });

  }

  generateToken();
