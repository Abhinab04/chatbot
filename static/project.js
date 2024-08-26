document.addEventListener("DOMContentLoaded", () => {
    const micBtn = document.getElementById("mic-btn");
    micBtn.addEventListener("click", () => {
        navigator.mediaDevices.getUserMedia({ audio: true })
            .then(stream => {
                alert("Microphone access granted. Start speaking.");                
                fetch("/get_response", {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/x-www-form-urlencoded"
                    },
                    body: "user_input="
                })
                .then(response => response.json())
                .then(data => {
                    appendResponse(data.response);
                })
                .catch(error => {
                    console.error("Error:", error);
                });
            })
            .catch(error => {
                console.error("Microphone access denied or an error occurred:", error);
                alert("Microphone access denied. Please enable the microphone to use this feature.");
            });
    });
    function appendResponse(response) {
        const output = document.getElementById("output");
        output.value += response + "\n";
        output.scrollTop = output.scrollHeight; 
    }
});




