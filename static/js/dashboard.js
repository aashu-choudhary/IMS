/* ==========================================================
                    IMS DASHBOARD
========================================================== */

document.addEventListener("DOMContentLoaded", function () {

    /* ==========================================
                ELEMENTS
    ========================================== */

    const sidebar = document.getElementById("sidebar");

    const toggleBtn = document.getElementById("sidebarToggle");



    /* ==========================================
            SIDEBAR COLLAPSE (DESKTOP)
    ========================================== */

    if (toggleBtn && sidebar) {

        toggleBtn.addEventListener("click", function () {

            if (window.innerWidth > 768) {

                sidebar.classList.toggle("collapsed");

            } else {

                sidebar.classList.toggle("active");

            }

        });

    }



    /* ==========================================
            CLOSE MOBILE SIDEBAR
    ========================================== */

    document.addEventListener("click", function (event) {

        if (window.innerWidth > 768) return;

        if (
            sidebar &&
            sidebar.classList.contains("active") &&
            !sidebar.contains(event.target) &&
            !toggleBtn.contains(event.target)
        ) {

            sidebar.classList.remove("active");

        }

    });



    /* ==========================================
            ACTIVE SIDEBAR LINK
    ========================================== */

    const links = document.querySelectorAll(".sidebar-menu a");

    const currentPath = window.location.pathname;

    links.forEach(function (link) {

        if (link.getAttribute("href") === currentPath) {

            links.forEach(function (item) {

                item.classList.remove("active");

            });

            link.classList.add("active");

        }

    });



    /* ==========================================
            WINDOW RESIZE
    ========================================== */

    window.addEventListener("resize", function () {

        if (window.innerWidth > 768) {

            sidebar.classList.remove("active");

        }

    });



    /* ==========================================
            INVENTORY CHART PLACEHOLDER
    ========================================== */

    const chart = document.getElementById("inventoryChart");

    if (chart) {

        /*
            Chart.js code will be added
            after Inventory Module is completed.
        */

        console.log("Inventory Chart Ready");

    }

});
