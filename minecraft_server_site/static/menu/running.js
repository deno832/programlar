fetch('http://say-clusters.at.ply.gg:2395/is-running/1', {
   headers: {
      'Accept': 'application/json'
   }
})
.then(response => response.json())
.then(function (text){
    console.log(text.message)
    if (text.message == true){
        document.getElementById("durum-lbl").innerHTML="Running...";
        document.getElementById("start").innerHTML="Running...";
    }
})

const propArea = document.getElementById('properties');

var url = "http://say-clusters.at.ply.gg:2395/get-prop";
var params = {
    "token": 1,
};

var options = {
    method: "POST",
    headers: {
        "Content-type": "application/json"
    },
    body: JSON.stringify(params) // İstek gövdesi
};

fetch(url, options)
.then(response => response.json())
.then(function (response) {
    propArea.value = "# Bunlara asla ama asla dokunma!! (Güvenlik eklemeye üşendim :D):"
    propArea.value += "\n#rcon.port ,server-ip, server-port, enable-rcon, rcon-password,  \n"
    propArea.value += "\n"+response.message;
})