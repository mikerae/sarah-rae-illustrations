/*  Core logic/paymentElement and  styling using the API - Stripe's docs (072023):
    https://stripe.com/docs/payments/quickstart

    Modified for this project.
*/
let elements;

const stripePublicKey = $('#id_stripe_public_key').text().slice(1, -1);
const stripe = Stripe(stripePublicKey);
const successUrl = $('#id_checkout_success_url').text().slice(1, -1);
let form = document.getElementById("payment-form");
const saveInfoElement = document.getElementById('id-save-info');

let emailAddress = '';

// Initializes the setup variables and puts elements in the DOM
initialize();
checkStatus();

// Set eventListner on payment form submit button "Complete Order"
document.getElementById("payment-form").addEventListener("submit", handleSubmit);
// Set eventListner on payment form submit button to post User preference to save_userdata_checked()
document.getElementById("payment-form").addEventListener("submit", saveInfo);
// Set eventListner on save-info checkbox when state is
saveInfoElement.addEventListener("change", toggleSaveInfoState);

//set initial state of saveInfoState to true matching the DOM state
let saveInfoState = true;
console.log(`saveInfoState initial value on load: ${saveInfoState}`);

// Fetches a payment intent and captures the client secret
// then loads DOM payment elements
async function initialize() {
    const response = await fetch("create_payment_intent/", {
        method: "GET",
        headers: {
            "Content-Type": "application/json"
        },
    });

    const {
        clientSecret
    } = await response.json();

    const appearance = {
        theme: 'stripe',
        variables: {
            colorText: '#da920c',
            colorPrimary: '#da920c',
            colorPrimaryText: '#4d0052',
            colorBackground: '#4d0052',
        },
    };
    elements = stripe.elements({
        appearance,
        clientSecret
    });

    // Create the Address Element in shipping mode
    const shippingAddressElement = elements.create('address', {
        mode: 'shipping',
    });
    shippingAddressElement.mount("#shipping-address-element");

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

// When submit button is clicked, if the user has checked 
// save-info, 'save-info' wll be stored in the current session.
// This will then be used on the server to store user details.
function saveInfo(e) {
    e.preventDefault(e);
    let csrfToken = $('input[name="csrfmiddlewaretoken"]').val();
    let postData = {
        'csrfmiddlewaretoken': csrfToken,
        'save-info': saveInfoState,
    };
    let url = '/checkout/save_userdata_checked/';
    $.post(url, postData);
}

async function handleSubmit(e) {
    e.preventDefault();
    setLoading(true);


    const {
        error
    } = await stripe.confirmPayment({
        elements,
        confirmParams: {

            // Redirects to payment completion page
            return_url: successUrl,
            receipt_email: emailAddress,
        },
    });

    // This point will only be reached if there is an immediate error when
    // confirming the payment. Otherwise, your customer will be redirected to
    // your `return_url`. For some payment methods like iDEAL, your customer will
    // be redirected to an intermediate site first to authorize the payment, then
    // redirected to the `return_url`.
    if (error.type === "card_error" || error.type === "validation_error") {
        showMessage(error.message);
    } else {
        showMessage("An unexpected error occurred.");
    }

    setLoading(false);

}

// Toggles value of saveInfoState when checkbox is changed
function toggleSaveInfoState() {
    if (saveInfoState == true) {
        saveInfoState = false;
    } else {
        saveInfoState = true;
    }
    console.log(`saveInfoState toggled value: ${saveInfoState}`);
}

// Fetches the payment intent status after payment submission
async function checkStatus() {
    const clientSecret = new URLSearchParams(window.location.search).get(
        "payment_intent_client_secret"
    );

    if (!clientSecret) {
        return;
    }


    const {
        paymentIntent
    } = await stripe.retrievePaymentIntent(clientSecret);
    console.log(`Check Status called: clientSecret: ${clientSecret}`);


    switch (paymentIntent.status) {
        case "succeeded":
            showMessage("Payment succeeded!");
            break;
        case "processing":
            showMessage("Your payment is processing.");
            break;
        case "requires_payment_method":
            showMessage("Your payment was not successful, please try again.");
            break;
        default:
            showMessage("Something went wrong.");
            break;
    }
}

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
        document.querySelector("#submit").disabled = true;
        document.querySelector("#spinner").classList.remove("hidden");
        document.querySelector("#button-text").classList.add("hidden");
    } else {
        document.querySelector("#submit").disabled = false;
        document.querySelector("#spinner").classList.add("hidden");
        document.querySelector("#button-text").classList.remove("hidden");
    }
}