function sendMail(contactForm) {
    emailjs.send("service_vbk3i2q","template_a61ofcg", {
        "from_name": contactForm.name.value,
        "full_request": contactForm.details.value
    })
    .then(
        function(response) {
            console.log("SUCCESS", response);
        },
        function(error) {
            console.log("FAILED", error);
        }
    );
    return false;
}