// Sending the completed form to emailjs API

function sendMail(contactForm) {
    emailjs.send("service_2hybwyq","template_a61ofcg", {
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

// validation of form before it can be sent off

function emailSent() {
    let x = document.forms["contact-form"]["name"].value;
    let y = document.forms["contact-form"]["details"].value;
    if (x == "") {
      alert("Name must be filled out");
    }
    else if (y == "") {
        alert("Message cannot be blank")
    }
    else {
    alert("Message sent!");
    }
}