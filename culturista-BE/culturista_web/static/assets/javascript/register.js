function register() {
    $.ajax({
        type: "POST",
        url: "http://127.0.0.1:8000/culturista_web/register-user",
        data: JSON.stringify(
                {
                    "username": $('#username').val(),
                    "password": $('#password').val(),
                    "email": $('#email').val(),
                    "age": 1,
                    "gender": $('#gender').val(),
                    "role": 1,
                    "country": $('#country').val()
                }
            ),
        contentType: "application/json",
        dataType: "json",   
        success: function(data) {
            alert("Register succesfully");
            window.location = "http://127.0.0.1:8000/api/login";
        },
        error: function(xhr, status, error) {
            alert("An error occurred during register: " + xhr.responseText);
        }
    });
    return false;
}

