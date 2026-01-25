document.querySelectorAll("form").forEach(form => {
    form.addEventListener("submit", function (e) {

        const cnicInput = form.querySelector("input[name='cnic']");

        if (cnicInput) {
            const value = cnicInput.value.trim();

            if (!/^\d{13}$/.test(value)) {
                alert("CNIC must be exactly 13 digits (numbers only).");
                cnicInput.focus();
                e.preventDefault();
                return;
            }
        }

        // Soft AI-style UX delay (feels secure)
        const btn = form.querySelector("button");
        if (btn) {
            btn.innerText = "Verifying…";
            btn.disabled = true;
        }
    });
});
