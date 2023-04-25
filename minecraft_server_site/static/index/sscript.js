const submitBtn = document.getElementById("submit");

function submitForm(event) {
    event.preventDefault();

    const nameInput = document.getElementById("fname").value;
    const passwdInput = document.getElementById("passwd").value;

    console.log({"first_name": nameInput, "password": passwdInput})
    const url = "http://192.168.1.5:800/login";

    fetch('http://say-clusters.at.ply.gg:2395/login', {
    method: 'POST',
    headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    },
    body: JSON.stringify({first_name:nameInput, password: passwdInput}),
    
})
   .then(response => response.json())
   .then(function(response){
    
    if (response.message == "Kullanıcı yok"){
        alert("Geçersiz Kullanıcı adı!")
    }
    else if (response.message == "Başarılı giriş") {
        window.location.replace("http://instructions-visibility.at.ply.gg:2382/dashboard/" + response.token);
    }
    else{
        alert("Hatalı Şifre")
    }
   })
   
}

submitBtn.addEventListener("click", submitForm);