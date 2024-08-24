/*document.getElementById("btn1").addEventListener('click',function(){
   alert("start speaking");
    //deploy your code here....
    function getResponse() {
        var outputTextArea = document.getElementById('output');
        outputTextArea.value = '';  
        var xhr = new XMLHttpRequest();
        xhr.open('GET', '/get_response', true);
        xhr.onreadystatechange = function() {
            if (xhr.readyState == 3 && xhr.status == 200) {
                outputTextArea.value += xhr.responseText;  
                outputTextArea.scrollTop = outputTextArea.scrollHeight;  
            }
        };
        xhr.send();
    }
});*/
document.addEventListener('DOMContentLoaded', () => {
    const micBtn = document.getElementById('mic-btn');
    micBtn.addEventListener('click', () => {
        alert("start speaking")
        fetch('/get_response', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded'
            },
            body: 'user_input='
        })
        .then(response => response.json())
        .then(data => {
            appendResponse(data.response);
        })
        .catch(error => {
            console.error('Error:', error);
        });
    });

    function appendResponse(response) {
        const output = document.getElementById('output');
        output.value += response + '\n';
        output.scrollTop = output.scrollHeight; // Auto-scroll to bottom
    }
});



