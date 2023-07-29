#include <virtuabotixRTC.h>  
#include <LiquidCrystal.h> 
int Contrast=0;
LiquidCrystal lcd(12, 11, 5, 4, 3, 2);  
int potdeger;

int CLK_PIN = 10;                                        
int DAT_PIN = 9;                                        
int RST_PIN = 8;

int dakika = 0;
int saat = 0;

virtuabotixRTC myRTC(CLK_PIN, DAT_PIN, RST_PIN); 

 void setup()
 {
     
     pinMode(7,OUTPUT);
     lcd.begin(16, 2);
     lcd.clear();
     pinMode(6,OUTPUT);
     
     pinMode(13,INPUT);
     lcd.setCursor(0, 0);
     lcd.print("Press to button!");
  } 
     void loop(){ 
    // Serial.println(analogRead(A0));
    

    int yeni = map(analogRead(A0),12,1023,0,60);
    
    
    if (digitalRead(13) == HIGH){
      lcd.clear();
      lcd.print("Time is:");
      
      while (1){  
        myRTC.updateTime();
        delay(400);
        lcd.setCursor(0, 1);                             
        lcd.print(myRTC.hours);                          
        lcd.print(":");
        lcd.print(myRTC.minutes);                          
        lcd.print(":");
        lcd.print(myRTC.seconds);


        if(myRTC.hours==saat && myRTC.minutes==dakika && myRTC.seconds == 0){
          lcd.clear();
          lcd.setCursor(0,0);
          lcd.print("Wake Up!");
          digitalWrite(7,HIGH);
          delay(7000);
          digitalWrite(6,HIGH);
        }

        
        if (digitalRead(13) == HIGH){
          lcd.clear();
          lcd.print("Setup Alarm:");
          delay(400);

          while (1){
            lcd.setCursor(3, 1);                             
            lcd.print(saat);
            lcd.print(":");
            lcd.print(dakika);

            if (digitalRead(13) == HIGH){
              lcd.clear();
              lcd.setCursor(0,0);
              lcd.print("Setup Hour:");
              delay(400);
            
              while (1){
                saat = map(analogRead(A0),16,1025,0,24);
                lcd.setCursor(3, 1);
                delay(100);
                lcd.print(String(saat) + " ");
                
                if (digitalRead(13) == HIGH){
                  lcd.clear();
                  lcd.setCursor(0,0);
                  lcd.print("Setup Minute:");
                  delay(400);

                  while (1){
                    dakika = map(analogRead(A0),16,1025,0,60);
                    lcd.setCursor(3, 1);
                    delay(100);
                    lcd.print(String(dakika) + " ");

                    if (digitalRead(13) == HIGH){
                      break;
                    }
                    
                  }
                  break;
                }
              
              }
              break;
              
            }
          }
          break;
          
      }

      }
    }
 }
