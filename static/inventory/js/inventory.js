/* ==========================================================
                    INVENTORY MODULE
========================================================== */

document.addEventListener("DOMContentLoaded", function () {

    /* =====================================================
                    ACTIVE NAVIGATION
    ====================================================== */

    const currentPath = window.location.pathname;

    const navLinks = document.querySelectorAll(".inventory-nav a");

    navLinks.forEach(function (link) {

        link.classList.remove("active");

        const href = link.getAttribute("href");

        if (href && currentPath === href) {

            link.classList.add("active");

        }

    });



    /* =====================================================
                    TABLE ROW HOVER
    ====================================================== */

    const rows = document.querySelectorAll(".dashboard-table tbody tr");

    rows.forEach(function (row) {

        row.addEventListener("mouseenter", function () {

            row.style.cursor = "pointer";

        });

    });



    /* =====================================================
                    QUICK ACCESS EFFECT
    ====================================================== */

    const quickCards = document.querySelectorAll(".quick-card");

    quickCards.forEach(function (card) {

        card.addEventListener("mouseenter", function () {

            card.style.transition = "all .25s ease";

        });

    });



    /* =====================================================
                    AUTO CLOSE MOBILE NAV
    ====================================================== */

    if (window.innerWidth <= 768) {

        navLinks.forEach(function (link) {

            link.addEventListener("click", function () {

                document.activeElement.blur();

            });

        });

    }



    /* =====================================================
                    PLACEHOLDER
    ====================================================== */

    console.log("Inventory Module Loaded");

});