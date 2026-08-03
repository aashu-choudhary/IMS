/* ==========================================================
                    LOGIN PAGE
========================================================== */

document.addEventListener("DOMContentLoaded", () => {

    /* ==========================================
            PASSWORD SHOW / HIDE
    ========================================== */

    const passwordInput = document.getElementById("password");

    const toggleButton = document.querySelector(".toggle-password");

    if (passwordInput && toggleButton) {

        toggleButton.addEventListener("click", () => {

            const icon = toggleButton.querySelector("i");

            if (passwordInput.type === "password") {

                passwordInput.type = "text";

                icon.classList.remove("fa-eye");
                icon.classList.add("fa-eye-slash");

            } else {

                passwordInput.type = "password";

                icon.classList.remove("fa-eye-slash");
                icon.classList.add("fa-eye");

            }

        });

    }



    /* ==========================================
            AUTO FOCUS USERNAME
    ========================================== */

    const username = document.querySelector(
        'input[name="username"]'
    );

    if (username) {

        username.focus();

    }



    /* ==========================================
            LOGIN BUTTON LOADING
    ========================================== */

    const form = document.querySelector("form");

    const loginButton = document.querySelector(".login-btn");

    if (form && loginButton) {

        form.addEventListener("submit", () => {

            loginButton.disabled = true;

            loginButton.innerHTML = "Signing In...";

        });

    }



    /* ==========================================
            ENTER KEY SUPPORT
    ========================================== */

    document.addEventListener("keydown", (event) => {

        if (event.key === "Enter") {

            if (form) {

                form.requestSubmit();

            }

        }

    });

});