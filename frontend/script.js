fetch("/api/hello")
    .then(response => response.json())
    .then(data => {
        document.getElementById("api-response").textContent = data.message;
    });