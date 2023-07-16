/*
    Core logic/payment flow comes from this part of Stripe's docs (072023):
    https://stripe.com/docs/payments/accept-a-payment

    JS element Styling comes form here (072023):
    https://stripe.com/docs/js/appendix/style?type=card

    CSS Element container Styling is described here (072023)
    https://stripe.com/docs/js/element/the_element_container?type=card
*/

var stripe_public_key = $('#id_stripe_public_key').text().slice(1, -1);
var id_client_secret = $('#id_client_secret').text().slice(1, -1);
var stripe = Stripe(stripe_public_key);
var elements = stripe.elements();

var style = {
    base: {
        iconColor: '#4d005299',
        color: '#4d0052d9',
        fontWeight: '500',
        fontFamily: 'Roboto, Open Sans, Segoe UI, sans-serif',
        fontSize: '16px',
        fontSmoothing: 'antialiased',
        ':-webkit-autofill': {
            color: '#4d0052d9',
        },
        '::placeholder': {
            color: '#4d005299',
        },
    },
    invalid: {
        iconColor: '#dc3545',
        color: '#dc3545',
        fontSize: '19px',
    },
}
var payment = elements.create('card', {
    style: style
});

card.mount('#card-element');