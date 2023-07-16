/*
    Core logic/payment flow comes from this part of Stripe's docs (072023):
    https://stripe.com/docs/payments/accept-a-payment

    JS element Styling comes form here (072023):
    https://stripe.com/docs/js/appendix/style?type=card

    CSS Element container Styling is described here (072023)
    https://stripe.com/docs/js/element/the_element_container?type=card
*/

const stripe_public_key = $('#id_stripe_public_key').text().slice(1, -1);
const id_client_secret = $('#id_client_secret').text().slice(1, -1);
const stripe = Stripe(stripe_public_key);



let elements = stripe.elements();

let style = {
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
let card = elements.create('card', {
    style: style
});

card.mount('#card-element');

// const appearance = {
//     theme: 'stripe',
// };
// elements = stripe.elements({
//     appearance,
//     clientSecret
// });

// const linkAuthenticationElement = elements.create("linkAuthentication");
// linkAuthenticationElement.mount("#link-authentication-element");

// linkAuthenticationElement.on('change', (event) => {
//     emailAddress = event.value.email;
// });

// const paymentElementOptions = {
//     layout: "tabs",
// };

// const paymentElement = elements.create("payment", paymentElementOptions);
// paymentElement.mount("#payment-element");