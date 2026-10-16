
document.addEventListener("DOMContentLoaded", () => {
    const forms = document.querySelectorAll(".auth-card form");

    forms.forEach((form) => {
        form.addEventListener("submit", () => {
            const button = form.querySelector('button[type="submit"]');

            if (button && form.checkValidity()) {
                button.disabled = true;
                button.textContent = "Please wait...";
            }
        });
    });
});
