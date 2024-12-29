// Simple validation to enhance user experience
document.addEventListener("DOMContentLoaded", () => {
    const form = document.querySelector("form");
    const num1 = document.querySelector("#num1");
    const num2 = document.querySelector("#num2");

    form.addEventListener("submit", (event) => {
        if (!num1.value || !num2.value) {
            alert("Please fill in both numbers.");
            event.preventDefault();
        }
    });
});
