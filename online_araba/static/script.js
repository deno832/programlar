const socket = new WebSocket('ws://she-creativity.at.ply.gg:64524');

const ileri_btn  = document.getElementById('İleri');
const geri_btn  = document.getElementById('Geri');
const sag_btn  = document.getElementById('Sağ');
const sol_btn  = document.getElementById('Sol');

const hiz_btn  = document.getElementById('hiz_btn');
const hizEntry = document.getElementById('hiz_entry');

socket.onopen = function(event) {
  alert("Bağlantı başarılı!!")
};
socket.onclose = function(event) {
  alert("Bağlantı Hatası!!")
};

function dur(){
  console.log("Durdu");
  socket.send("Dur");
}

function hareketEt(yön){
  return function(){
    console.log(yön+"a gidiliyor");
    socket.send(yön);
  }
}


hiz_btn.addEventListener("click", function(){
  socket.send("hiz " + hizEntry.value);
  alert("Hızınız " + hizEntry.value + " olarak ayarlandı!")
})


ileri_btn.addEventListener("touchstart", hareketEt("İleri"));
ileri_btn.addEventListener("touchend", dur);
ileri_btn.addEventListener("mousedown", hareketEt("İleri"));
ileri_btn.addEventListener("mouseup", dur);


geri_btn.addEventListener("touchstart", hareketEt("Geri"));
geri_btn.addEventListener("touchend", dur);
geri_btn.addEventListener("mousedown", hareketEt("Geri"));
geri_btn.addEventListener("mouseup", dur);


sag_btn.addEventListener("touchstart", hareketEt("Sağ"));
sag_btn.addEventListener("touchend", dur);
sag_btn.addEventListener("mousedown", hareketEt("Sağ"));
sag_btn.addEventListener("mouseup", dur);


sol_btn.addEventListener("touchstart", hareketEt("Sol"));
sol_btn.addEventListener("touchend", dur);
sol_btn.addEventListener("mousedown", hareketEt("Sol"));
sol_btn.addEventListener("mouseup", dur);
