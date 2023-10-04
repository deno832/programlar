const socket = new WebSocket('ws://she-creativity.at.ply.gg:64524');

const ileri_btn  = document.getElementById('İleri');
const geri_btn  = document.getElementById('Geri');
const sag_btn  = document.getElementById('Sağ');
const sol_btn  = document.getElementById('Sol');

const hiz_btn  = document.getElementById('hiz_btn');
const hizEntry = document.getElementById('hiz_entry');

const sokla_btn = document.getElementById('sokla');

const kafa_sag_btn = document.getElementById('kafa_sag');
const kafa_orta_btn = document.getElementById('kafa_orta');
const kafa_sol_btn = document.getElementById('kafa_sol');


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


sokla_btn.addEventListener("click", hareketEt("sok"));

kafa_orta_btn.addEventListener("click", hareketEt("ortala"));
kafa_sag_btn.addEventListener("click", hareketEt("kafa_sag"));
kafa_sol_btn.addEventListener("click", hareketEt("kafa_sol"));