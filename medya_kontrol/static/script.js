const oncekiButton = document.getElementById('Önceki');
const sonrakiButton = document.getElementById('Sonraki');
const baslatDurdurButton = document.getElementById('BaşlatDurdur');
const ses_arti = document.getElementById("SesArtı");
const ses_eksi = document.getElementById("SesEksi");
const myParagraph = document.getElementById("my-paragraph");
const IPAdress = myParagraph.innerText;

console.log(IPAdress);

const ip_durdur = "http://" + IPAdress + ":" + 4593 + "/play-pause"
const ip_arttir = "http://" + IPAdress + ":" + 4593 + "/arttir"
const ip_azalt = "http://" + IPAdress + ":" + 4593 + "/azalt"
const ip_sonraki = "http://" + IPAdress + ":" + 4593 + "/sonraki"
const ip_önceki = "http://" + IPAdress + ":" + 4593 + "/önceki"

console.log(ip_durdur);

oncekiButton.addEventListener('click', function() {
  const xhr = new XMLHttpRequest();
  xhr.open('GET', ip_önceki , true);
  xhr.onload = () => {
  if (xhr.status === 200) {
    console.log('Talep başarıyla gönderildi.');
  } else {
    alert("Başarısız!");
    console.log('Talep gönderilirken bir hata oluştu.');
  }
  };
  xhr.send();

  console.log('Önceki butonuna tıklandı');

});

ses_arti.addEventListener('click', function() {
  const xhr = new XMLHttpRequest();
        xhr.open('GET', ip_arttir , true);
        xhr.onload = () => {
          if (xhr.status === 200) {
            console.log('Talep başarıyla gönderildi.');
          } else {
            alert("Başarısız!");
            console.log('Talep gönderilirken bir hata oluştu.');
          }
        };
        xhr.send();
  console.log('Ses Artı butonuna tıklandı');
});

ses_eksi.addEventListener('click', function() {
  const xhr = new XMLHttpRequest();
        xhr.open('GET', ip_azalt , true);
        xhr.onload = () => {
          if (xhr.status === 200) {
            console.log('Talep başarıyla gönderildi.');
          } else {
            alert("Başarısız!");
            console.log('Talep gönderilirken bir hata oluştu.');
          }
        };
        xhr.send();
  console.log('Ses Eksi butonuna tıklandı');
});

sonrakiButton.addEventListener('click', function() {
  const xhr = new XMLHttpRequest();
        xhr.open('GET', ip_sonraki , true);
        xhr.onload = () => {
          if (xhr.status === 200) {
            console.log('Talep başarıyla gönderildi.');
          } else {
            alert("Başarısız!");
            console.log('Talep gönderilirken bir hata oluştu.');
          }
        };
        xhr.send();

  console.log('Sonraki butonuna tıklandı');
});

baslatDurdurButton.addEventListener('click', function() {
  const xhr = new XMLHttpRequest();
        xhr.open('GET', ip_durdur , true);
        xhr.onload = () => {
          if (xhr.status === 200) {
            console.log('Talep başarıyla gönderildi.');
          } else {
            alert("Başarısız!");
            console.log('Talep gönderilirken bir hata oluştu.');
          }
        };
        xhr.send();
  console.log('Başlat/Durdur butonuna tıklandı');
});