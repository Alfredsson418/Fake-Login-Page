

function animation() {
    const el = document.getElementsByClassName("signInElements");
        for (var i = 0; i <= el.length; i++) {
            el[i].animate([
            // keyframes

                { opacity: '0.55', offset: 0.5 },
                { transform: 'translate(0,0)'},
                { transform: 'translate(-100px, 0)'},
                { transform: 'translate(-100px, 0)'},
                { transform: 'translate(-100px, 0)', display: 'none', opacity: '0.55'},



            ], {
                // timing options
                duration: 1000,
                iterations: 1
            });
        }   

}   
function animation2() {
    const el = document.getElementsByClassName("passwordElements");
        for (var i = 0; i <= el.length; i++) {
            el[i].animate([
            // keyframes https://developer.mozilla.org/en-US/docs/Web/API/Element/animate

                { transform: 'translate(100px,0)', opacity: '0.55', offset: 0.2 },
                { transform: 'translate(100px,0)', opacity: '0.55'},
                { transform: 'translate(100px, 0)'},
                { transform: 'translate(0, 0)', opacity: '0.55'},
                { transform: 'translate(0, 0)', opacity: '0.55'},
                { transform: 'translate(0, 0)', opacity: '1'},



            ], {
                // timing options
                duration: 1000,
                iterations: 1
            });
        }   

}   
function toggleSignIn() {
    const el = document.getElementsByClassName("signInElements");
    for (var i = 0; i <= el.length; i++) {
            el[i].classList.toggle("hidden")
    } 
}

function togglePassword() {
    const el = document.getElementsByClassName("passwordElements");
    for (var i = 0; i <= el.length; i++) {
            el[i].classList.toggle("hidden")
    } 
}

function completeAnimation() {
    setTimeout(getEmail, 0)
    setTimeout(animation, 0)
    setTimeout(toggleSignIn, 700)
    setTimeout(animation2, 850)
    setTimeout(togglePassword, 1400)

}

function TogglePasswordShow() {
    var x = document.getElementById("passwordField");
    if (x.type === "password") {
        x.type = "text";
    } else {
        x.type = "password";
    }
}
