document.addEventListener('DOMContentLoaded', () => {
    const micBtn = document.getElementById('mic-btn');
    micBtn.addEventListener('click', () => {
        fetch('/get_response', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded'
            },
            body: 'user_input='
        })
        .then(response => response.json())
        .then(data => {
            document.getElementById('output').value = data.response;
        })
        .catch(error => {
            console.error('Error:', error);
        });
    });
});
