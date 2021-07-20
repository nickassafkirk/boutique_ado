/* 
Core logic/payment flow comes from this article:
https://stripe.com/docs/payments/accept-a-payment?platform=web&ui=elements

css from:
https://stripe.com/docs/js
*/

var stripe_public_key = $('#id_stripe_public_key').text().slice(1, -1); /* Get the public key from the template using .text method*/
var client_secret = $('#id_client_secret').text().slice(1, -1); /* The slice method removes the first and last apostrophe chars */
var stripe = Stripe(stripe_public_key); /* Set up stripe using our public key, Stripe function comes from the stripe.js script in our base template */
var elements = stripe.elements(); /* create an instance of stripe.elements so we can make a card details form */

var style = {
      base: {
        color: '#000',
        fontFamily: 'Helvetica Neue, Helvetica, sans-serif',
        fontSize: '16px',
        fontSmoothing: 'antialiased',
        '::placeholder': {
          color: '#aab7c4'
        }
      },
      invalid: {
        iconColor: '#dc3545',
        color: '#dc3545',
      }
};

var card = elements.create('card', {style: style}); 
card.mount('#card-element'); /* mount the new card element to the appropriate part of our template */