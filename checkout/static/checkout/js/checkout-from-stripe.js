// Copied from Stripe docs then modified
// This is your test publishable API key.

// The items the customer wants to buy
const items = [{
    id: "xl-tshirt"
}];

let elements;
const stripe_public_key = $('#id_stripe_public_key').text().slice(1, -1);
const stripe = Stripe(stripe_public_key);

initialize();
checkStatus();

document
    .$("#payment-form")
    .addEventListener("submit_button", handleSubmit);

let emailAddress = '';
// Fetches a payment intent and captures the client secret
async function initialize() {
    const response = await fetch("/create-payment-intent", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            items
        }),
    });
    const {
        clientSecret
    } = await response.json();

    const appearance = {
        theme: 'stripe',
    };
    elements = stripe.elements({
        appearance,
        clientSecret
    });

    const linkAuthenticationElement = elements.create("linkAuthentication");
    linkAuthenticationElement.mount("#link-authentication-element");

    linkAuthenticationElement.on('change', (event) => {
        emailAddress = event.value.email;
    });

    const paymentElementOptions = {
        layout: "tabs",
    };

    const paymentElement = elements.create("payment", paymentElementOptions);
    paymentElement.mount("#payment-element");
}

// async function handleSubmit(e) {
//     e.preventDefault();
//     setLoading(true);

//     const {
//         error
//     } = await stripe.confirmPayment({
//         elements,
//         confirmParams: {
//             // Make sure to change this to your payment completion page
//             return_url: "http://localhost:5432/checkout.html",
//             receipt_email: emailAddress,
//         },
//     });

// This point will only be reached if there is an immediate error when
// confirming the payment. Otherwise, your customer will be redirected to
// your `return_url`. For some payment methods like iDEAL, your customer will
// be redirected to an intermediate site first to authorize the payment, then
// redirected to the `return_url`.
//     if (error.type === "card_error" || error.type === "validation_error") {
//         showMessage(error.message);
//     } else {
//         showMessage("An unexpected error occurred.");
//     }

//     setLoading(false);
// }

// Fetches the payment intent status after payment submission
// async function checkStatus() {
//     const clientSecret = new URLSearchParams(window.location.search).get(
//         "payment_intent_client_secret"
//     );

//     if (!clientSecret) {
//         return;
//     }

//     const {
//         paymentIntent
//     } = await stripe.retrievePaymentIntent(clientSecret);

//     switch (paymentIntent.status) {
//         case "succeeded":
//             showMessage("Payment succeeded!");
//             break;
//         case "processing":
//             showMessage("Your payment is processing.");
//             break;
//         case "requires_payment_method":
//             showMessage("Your payment was not successful, please try again.");
//             break;
//         default:
//             showMessage("Something went wrong.");
//             break;
//     }
// }

// ------- UI helpers -------

function showMessage(messageText) {
    const messageContainer = document.querySelector("#payment-message");

    messageContainer.classList.remove("hidden");
    messageContainer.textContent = messageText;

    setTimeout(function () {
        messageContainer.classList.add("hidden");
        messageContainer.textContent = "";
    }, 4000);
}

// Show a spinner on payment submission

function setLoading(isLoading) {
    if (isLoading) {
        // Disable the button and show a spinner
        document.$("#submit").disabled = true;
        document.$("#spinner").classList.remove("hidden");
        document.$("#button-text").classList.add("hidden");
    } else {
        document.$("#submit").disabled = false;
        document.$("#spinner").classList.add("hidden");
        document.$("#button-text").classList.remove("hidden");
    }
}