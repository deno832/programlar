#include <IRremote.h>

#define B1 0xFFA25D
#define B2 0xFF629D
#define B3 0xFFE21D
#define B4 0xFF22DD
#define B5 0xFF02FD
#define B6 0xFFC23D
#define B7 0xFFE01F
#define B8 0xFFA857
#define B9 0xFF906F
#define B0 0xFF9867
#define STAR 0xFF6897
#define HASH 0xFFB04F
#define UP 0xFF18E7
#define RIGHT 0xFF5AA5
#define DOWN 0xFF4AB5
#define LEFT 0xFF10EF
#define OK 0xFF38C7

int RECV_PIN = 2;

IRrecv irrecv(RECV_PIN);
decode_results results;

void setup() {
  irrecv.enableIRIn();
  Serial.begin(9600);
  pinMode(8,OUTPUT);
  pinMode(9,OUTPUT);
}

void loop() {
  if (irrecv.decode(&results))
  {
    Serial.println(results.value,HEX);   
    if (results.value == OK)
    {
      Serial.println("basla");
    }
    irrecv.resume();
  }

  if (Serial.available()) {
    String teststr = Serial.readString();  
      teststr.trim();                     
      Serial.println(teststr);
      if (teststr == "kapa") 
      {
        digitalWrite(8,LOW);
        digitalWrite(9,LOW);
      }
      
      else if (teststr == "ac")
      {
        digitalWrite(8,HIGH);
        digitalWrite(9,HIGH);
      }

      else
      {
        Serial.println("Something else");
      }
  }
  
}
