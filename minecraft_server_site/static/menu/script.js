const startBtn = document.getElementById('start');
const sendBtn = document.getElementById('command-btn');

const token = document.getElementById('my-paragraph').value;

const commandEntry = document.getElementById('command-entry');
const commandOut = document.getElementById('command-out');

const propBtn = document.getElementById('prop-btn');
const propArea = document.getElementById('properties');
const propReset = document.getElementById('prop-reset');

propReset.addEventListener('click', function() {
  fetch('http://say-clusters.at.ply.gg:2395/reset-settings/1', {
  headers: {
      'Accept': 'application/json'
  }
})
  .then(response => response.json())
  .then(function (text){
      console.log(text.message)
      if (text.message == "Success"){
        alert("Succesfull! Refresh the page")
      }
      else if (text.message == "Çalışıyor"){
        alert("Cannot reset while server is running!!")
      }
  })
})

propBtn.addEventListener('click', function() {
  console.log("sende bastın reis")
  var url = "http://say-clusters.at.ply.gg:2395/send-prop";
  var params = {
      "token": 1,
      "file": propArea.value
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
    alert(response.message)
  })
})

startBtn.addEventListener('click', function() {
    const xhr = new XMLHttpRequest();
    xhr.open('GET', "http://say-clusters.at.ply.gg:2395/start/1");
    xhr.send();
    alert("Server IP: direct-slip.at.ply.gg:8302")
});

sendBtn.addEventListener('click', function() {
  var command = commandEntry.value;
  console.log(command);
  if (command == "stop"){
    alert("Server Durduruldu!!")
    setTimeout(() => { location.reload();}, 2000);
  }

  var url = "http://say-clusters.at.ply.gg:2395/send-command";
  var params = {
      "token": 1,
      "command": command
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
    commandOut.value += "\n" + response.command_out
    commandEntry.value = ""
  
  })
});

commandEntry.addEventListener("keypress", function(event) {
  // If the user presses the "Enter" key on the keyboard
  
  if (event.key === "Enter") {
    var command = commandEntry.value;
  
  var url = "say-clusters.at.ply.gg:2395/send-command";
  var params = {
    "token": 1,
    "command": command
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
      commandOut.value += "\n" + response.command_out
      commandEntry.value = ""
    })

    }
});