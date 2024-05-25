function checkLogin(){
    var accessTokenObj = (localStorage.getItem("accessToken"));
    
    if (!accessTokenObj){
        document.getElementById("user-account").style.display = 'none';
    }
    else {
        document.getElementById("signIn").style.display = 'none';
        document.getElementById("signUp").style.display = 'none';
        document.getElementById("user-account__name").innerHTML = parseJwt(accessTokenObj).username;
    }
    
}

function parseJwt (token) {
    var base64Url = token.split('.')[1];
    var base64 = base64Url.replace(/-/g, '+').replace(/_/g, '/');
    var jsonPayload = decodeURIComponent(window.atob(base64).split('').map(function(c) {
        return '%' + ('00' + c.charCodeAt(0).toString(16)).slice(-2);
    }).join(''));

    return JSON.parse(jsonPayload);
}

function logout(){
    alert("Logout sucessfully");
    localStorage.removeItem("accessToken");
    localStorage.removeItem("refreshToken");
    window.location = "http://127.0.0.1:8000/api/";
}