Bu proje raspberry pi ve kamera kullanarak odanın kapısını izler. Biri her geldiğinde yüzünü tanımaya çalışır. Yüzünü tanıyabilirse ismiyle, tanıyamazsa unknow adıyla saat ve tarih ile birlikte
sqlite dosyasına kaydeder. Aynı kodun içerisindeki soket sunucusu bağlantıları dinleyip kabul eder. Eğer istemciden "al" mesajı gelirse o istemciye veri tabanını gönderir. İstemci olarak ise android studioda Java kullanarak
bir mobil uygulama yazdım. Mobil uygulama en son girilen port ve ipyi SharedPreferences kullanarak kaydeder ve sonraki seferde otomatik olarak kutuya koyar. 


![uygulama2](https://github.com/deno832/programlar/assets/94462464/258bb056-1343-404a-810a-e1eec857fa42)


![uygulama1](https://github.com/deno832/programlar/assets/94462464/48538f51-b9de-4cf2-a4a6-22d78b565f29)
