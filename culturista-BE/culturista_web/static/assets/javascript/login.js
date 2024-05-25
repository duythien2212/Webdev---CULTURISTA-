
function login() {
    $.ajax({
        type: "POST",
        url: "http://127.0.0.1:8000/culturista_web/login-user",
        data: JSON.stringify(
                {
                    "username": $('#username').val(),
                    "password": $('#password').val()
                }
            ),
        contentType: "application/json",
        dataType: "json",   
        success: function(data) {
            if (data.access) {

                // console.log(data);
                localStorage.setItem('accessToken', data.access);
                localStorage.setItem('refreshToken', data.refresh);    
                
                window.location = "http://127.0.0.1:8000/api/";
            } else {
                alert("An error occurred");
            }
        },
        error: function(xhr, status, error) {
            alert("An error occurred during login: " + xhr.responseText);
        }
    });
    return false;
}

