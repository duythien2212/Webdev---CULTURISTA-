function createForum(){
    var accessTokenObj = (localStorage.getItem("accessToken"));
    if (!accessTokenObj){
        window.location = "http://127.0.0.1:8000/api/login";
        return;
    }
    username = parseJwt(accessTokenObj).username;

    $.ajax({
        type: "POST",
        url: "http://127.0.0.1:8000/api/create-forum",
        data: JSON.stringify(
                {
                    "content_id": Math.floor(Math.random() * 1000000000),
                    "title": $('#title').val(),
                    "content": $('#content').val(),
                    "tag": $('#tag').val(),
                    "user_created_name": username
                }
            ),
        contentType: "application/json",
        dataType: "json",   
        success: function(data) {
            alert('Create forum successfully!'); // Đảm bảo rằng 'a' được hiển thị khi yêu cầu AJAX thành công
            // Sau đó, bạn có thể thực hiện các xử lý khác với dữ liệu trả về
        },
        error: function(xhr, status, error) {
            alert("An error occurred: " + xhr.responseText);
        }
    });
    return false;
}

function parseJwt (token) {
    var base64Url = token.split('.')[1];
    var base64 = base64Url.replace(/-/g, '+').replace(/_/g, '/');
    var jsonPayload = decodeURIComponent(window.atob(base64).split('').map(function(c) {
        return '%' + ('00' + c.charCodeAt(0).toString(16)).slice(-2);
    }).join(''));

    return JSON.parse(jsonPayload);
}