function getEmail() {
    const el = document.getElementById("usernameToPassword");
    const emailField = document.getElementById("Google-Email");
    emailField.innerHTML = el.value;
}

function TogglePasswordShow() {
    var x = document.getElementById("passwordField");
    if (x.type === "password") {
        x.type = "text";
    } else {
        x.type = "password";
    }
}