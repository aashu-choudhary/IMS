/* =====================================================
                CUSTOMER DASHBOARD
===================================================== */

document.addEventListener("DOMContentLoaded", function () {

    console.log("Customer Dashboard Loaded");

    initializeFilters();
    initializeDeleteButtons();
    initializeCards();
    initializeExportButtons();

});


/* =====================================================
                FILTERS
===================================================== */

function initializeFilters() {

    const form = document.getElementById("filterForm");

    if (!form) return;

    const selects = form.querySelectorAll("select");

    selects.forEach(function (select) {

        select.addEventListener("change", function () {

            form.submit();

        });

    });

}


/* =====================================================
                DELETE CONFIRMATION
===================================================== */

function initializeDeleteButtons() {

    const forms = document.querySelectorAll(".delete-form");

    forms.forEach(function (form) {

        form.addEventListener("submit", function (e) {

            if (!confirm("Are you sure you want to delete this customer?")) {

                e.preventDefault();

            }

        });

    });

}


/* =====================================================
                CARD HOVER
===================================================== */

function initializeCards() {

    const cards = document.querySelectorAll(".stat-card");

    cards.forEach(function (card) {

        card.addEventListener("mouseenter", function () {

            card.style.transform = "translateY(-4px)";

        });

        card.addEventListener("mouseleave", function () {

            card.style.transform = "";

        });

    });

}


/* =====================================================
                EXPORT BUTTONS
===================================================== */

function initializeExportButtons() {

    const buttons = document.querySelectorAll(".secondary-btn");

    buttons.forEach(function (button) {

        button.addEventListener("click", function () {

            alert("Export feature will be connected after Reports Module.");

        });

    });

}


/* =====================================================
                FUTURE FEATURES
===================================================== */

// Charts
// Customer Analytics
// Live Statistics
// Notifications
// Customer Profile Loader
// Export PDF
// Export Excel