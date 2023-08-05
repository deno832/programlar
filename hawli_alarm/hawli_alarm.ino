#include <LiquidCrystal.h>                              //LCD kütüphanemizi başlatıyoruz.
int trigPin = 7;                                        //Ultrasonik sensör trig pini değişkeni
int echoPin = 6;                                        //Ultrasonik sensör echo pini değişkeni
int sure;                                               //Ses dalgasının gidip gelme süresi değişkeni
int uzaklik;                                            //Ölçülen uzaklık değeri değişkeni
int ilk_uzaklik;
int uyari = 8;
int ilk_uzaklik_fa;
int ilk_uzaklik_az;
int i = 2;

LiquidCrystal lcd(12, 11, 5, 4, 3, 2);  
void setup() {
  pinMode(9,OUTPUT);
  Serial.begin(9600);
  pinMode(trigPin, OUTPUT);                             //trig pinini OUTPUT olarak ayarlıyoruz.
  pinMode(echoPin,INPUT);                              //echo pinini INPUT olarak ayarlıyoruz.
  pinMode(8,INPUT);
  lcd.begin(16, 2);
  digitalWrite(trigPin, LOW);                           //Ultrasonik sensör ile ölçüm sekansını başlatıyoruz.
  delayMicroseconds(5);
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);
  sure = pulseIn(echoPin, HIGH, 11600);                 //Ses dalgasının gidip gelme süresini ölçüyoruz.
  ilk_uzaklik = sure*0.0345/2;
  ilk_uzaklik_fa = ilk_uzaklik + 5;
  ilk_uzaklik_az = ilk_uzaklik - 5;
  lcd.clear();
  lcd.setCursor(0,0);
  lcd.print("Limit uzaklik:");
  lcd.setCursor(0,1);
  lcd.print(ilk_uzaklik);
  lcd.setCursor(3,1);
  lcd.print("cm");
  delay(4000);              
}
void loop() {
  delay(10);
  digitalWrite(trigPin, LOW);                           //Ultrasonik sensör ile ölçüm sekansını başlatıyoruz.
  delayMicroseconds(5);
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);
  sure = pulseIn(echoPin, HIGH, 11600);                 //Ses dalgasının gidip gelme süresini ölçüyoruz.
  uzaklik = sure*0.0345/2;
  if (digitalRead(8) == true){
    digitalWrite(9,HIGH);
    lcd.clear();
    digitalWrite(9,HIGH);
    while (i < 10){
      lcd.setCursor(0,0);
      lcd.print("HIRSIZ VAR!!");
      lcd.setCursor(0,1);
      lcd.print("HIRSIZ VAR!!");
  }
  }    
  if (uzaklik < ilk_uzaklik_fa && uzaklik >ilk_uzaklik_az){
    delay(50);
    lcd.clear();
    lcd.setCursor(0,0);
    lcd.print("Su anki uzaklik:");
    lcd.setCursor(0,1);
    lcd.print(uzaklik);
    lcd.setCursor(7,1);
    lcd.print("Sorun Yok!");
    lcd.setCursor(3,1);
    lcd.print("cm");    
  }
  else{
    lcd.clear();
    digitalWrite(9,HIGH);
    while (i < 10){
      lcd.setCursor(0,0);
      lcd.print("HIRSIZ VAR!!");
      lcd.setCursor(0,1);
      lcd.print("HIRSIZ VAR!!");
    }
    
  }


}
