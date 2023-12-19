          var stripe= Stripe('pk_test_51ONB6tDbuhlL5pczt2S7ajD8V4RYhs0Ug99aXIOFLEkLGtJ3yFd934FqHDZBcflAT0Ixys2iBXXFZ2H8mHjx11j900RzcztKTZ');

          var elements = stripe.elements();

          var style = {
              base:{
                  color: '#32325d',
                  fontFamily:'"Helvetica Neue" Helvetica, sans-serif',
                  fontSize: '16px',
                  '::placeholder':{
                      color: '#aab7c4'
                  }
              },
              invalid: {
                  color:'#fa755a',
                  iconColor:'#fa755a'
              }
          };

          var card = elements.create('card',{style:style});
          card.mount('#card-element');

          card.addEventListener('change', function(event){
              var displayError = document.getElementById('card-errors');
              if(event.error){
                  displayError.textContent = event.error.message;
              }
              else{
                  displayError.textContent='';
              }
          });

          var form = document.getElementById('payment-form');
          form.addEventListener('submit', function(event){
              event.preventDefault();

                stripe.createToken(card).then(function(result){
                  if(result.error){
                      var errorElement = document.getElementById('card-errors');
                      errorElement.textContent = result.error.message;
                  }
                  else{
                      stripeTokenHandler(result.token);
                  }
              });
          });

          function stripeTokenHandler(token){
              var form = document.getElementById('payment-form');
              var hiddenInput = document.createElement('input');
              hiddenInput.setAttribute('type', 'hidden');
              hiddenInput.setAttribute('name','stripeToken');
              hiddenInput.setAttribute('value',token.id);
              form.appendChild(hiddenInput);

              form.submit()
          }