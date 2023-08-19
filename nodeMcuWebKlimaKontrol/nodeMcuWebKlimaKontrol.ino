#include <ESP8266WiFi.h>
#include <WiFiClient.h>
#include <ESP8266WebServer.h>
#include <Arduino.h>
#include <IRremoteESP8266.h>
#include <IRsend.h>

const uint16_t kIrLed = 4;  // ESP8266 GPIO pin to use. Recommended: 4 (D2).

IRsend irsend(kIrLed);  // Set the GPIO to be used to sending the message.

const char* ssid = "";
const char* password = "";

ESP8266WebServer server(80);

#define RELAY_PIN D1

bool relayState = LOW;

void setup() {
  irsend.begin();
  pinMode(RELAY_PIN, OUTPUT);
  digitalWrite(RELAY_PIN, relayState);

  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.println("Connecting to WiFi...");
  }
  Serial.println("Connected to WiFi");

  server.on("/", handleRoot);
  server.on("/on", handleOn);
  server.on("/off", handleOff);
  server.on("/submit", HTTP_GET, handleFormSubmit);
  server.begin();
}

void loop() {
  server.handleClient();
}

void handleRoot() {
  server.send(200, "text/html", "<!DOCTYPE html><html><head> <meta charset=\"UTF-8\"> <title>NodeMCU Control Panel</title> <style> body { font-family: Arial, sans-serif; margin: 0; padding: 0; background-color: #f0f0f0; } h1 { text-align: center; margin: 20px 0; } form { background-color: #ffffff; padding: 20px; border-radius: 5px; box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1); max-width: 400px; margin: 0 auto; } label { display: block; margin-bottom: 8px; } input[type=\"number\"], select { width: 100%; padding: 8px; margin-bottom: 12px; border: 1px solid #ccc; border-radius: 4px; box-sizing: border-box; } input[type=\"submit\"] { background-color: #4CAF50; color: white; padding: 10px 20px; border: none; border-radius: 4px; cursor: pointer; width: 100%; } input[type=\"submit\"]:hover { background-color: #45a049; } .control-buttons { text-align: center; margin-top: 20px; } .button { display: inline-block; padding: 10px 20px; margin: 0 10px; background-color: #333; color: white; border: none; border-radius: 4px; cursor: pointer; } .button:hover { background-color: #555; } </style></head><body> <h1>NodeMCU Control Panel</h1> <form action=\"/submit\" method=\"GET\"> <label for=\"temperature\">Sıcaklık (18-30 arası):</label> <input type=\"number\" id=\"temperature\" name=\"temperature\" min=\"18\" max=\"30\" required> <label for=\"fanSpeed\">Fan Hızı:</label> <select id=\"fanSpeed\" name=\"fanSpeed\"> <option value=\"min\">Minimum</option> <option value=\"max\">Maximum</option> </select> <input type=\"submit\" value=\"Gönder\"> </form> <div class=\"control-buttons\"> <button onclick=\"window.location.href='/on';\" class=\"button\">Aç</button> <button onclick=\"window.location.href='/off';\" class=\"button\">Kapat</button> </div></body></html>");
  
  }

void handleOn() {
  irsend.sendLG(0x8800B4F);
  server.send(200, "text/html", "<h1>Röle Açıldı</h1><p><a href='/'>Geri</a></p>");
}

void handleFormSubmit() {
    if (server.hasArg("temperature") && server.hasArg("fanSpeed")) {
        String temperatureValue = server.arg("temperature");
        String fanSpeedValue = server.arg("fanSpeed");

        if (fanSpeedValue == "max"){
          if (temperatureValue == "18"){
            irsend.sendLG(0x880834F);
          }else if (temperatureValue == "19"){
            irsend.sendLG(0x8808440);
          }else if (temperatureValue == "20"){
            irsend.sendLG(0x8808541);
          }else if (temperatureValue == "21"){
            irsend.sendLG(0x8808642);
          }else if (temperatureValue == "22"){
            irsend.sendLG(0x8808743);
          }else if (temperatureValue == "23"){
            irsend.sendLG(0x8808844);
          }else if (temperatureValue == "24"){
            irsend.sendLG(0x8808945);
          }else if (temperatureValue == "25"){
            irsend.sendLG(0x8808A46);
          }else if (temperatureValue == "26"){
            irsend.sendLG(0x8808B47);
          }else if (temperatureValue == "27"){
            irsend.sendLG(0x8808C48);
          }else if (temperatureValue == "28"){
            irsend.sendLG(0x8808D49);
          }else if (temperatureValue == "29"){
            irsend.sendLG(0x8808E4A);
          }else if (temperatureValue == "30"){
            irsend.sendLG(0x8808F4B);
          }
        }else if (fanSpeedValue == "min"){
          if (temperatureValue == "18"){
            irsend.sendLG(0x880830B);
          }else if (temperatureValue == "19"){
            irsend.sendLG(0x880840C);
          }else if (temperatureValue == "20"){
            irsend.sendLG(0x880850D);
          }else if (temperatureValue == "21"){
            irsend.sendLG(0x880860E);
          }else if (temperatureValue == "22"){
            irsend.sendLG(0x880870F);
          }else if (temperatureValue == "23"){
            irsend.sendLG(0x8808800);
          }else if (temperatureValue == "24"){
            irsend.sendLG(0x8808901);
          }else if (temperatureValue == "25"){
            irsend.sendLG(0x8808A02);
          }else if (temperatureValue == "26"){
            irsend.sendLG(0x8808B03);
          }else if (temperatureValue == "27"){
            irsend.sendLG(0x8808C04);
          }else if (temperatureValue == "28"){
            irsend.sendLG(0x8808D05);
          }else if (temperatureValue == "29"){
            irsend.sendLG(0x8808E06);
          }else if (temperatureValue == "30"){
            irsend.sendLG(0x8808F07);
          }
        }

        handleRoot();
    } else {
        server.send(400, "text/plain", "Eksik veya hatalı veri girişi.");
    }
}


void handleOff() {
  irsend.sendLG(0x88C0051);
  server.send(200, "text/html", "<h1>Röle Kapatıldı</h1><p><a href='/'>Geri</a></p>");
}
