#include <Arduino.h> // Only needed for Arduino 1.6.5 and earlier

#define SDA 0
#define SCL 2

#include <Wire.h>        // Only needed for Arduino 1.6.5 and earlier

#include "SSD1306Wire.h" // legacy include: `#include "SSD1306.h"`
#include <Adafruit_MLX90614.h>

SSD1306Wire display(0x3c, SDA , SCL);
Adafruit_MLX90614 mlx = Adafruit_MLX90614();


void setup(){
  Serial.begin(115200);
  Serial.println();
  Serial.println();

  mlx.begin();

  display.init();
  display.flipScreenVertically();
  display.setFont(ArialMT_Plain_10);  
}

void loop(){
  String txt = "";  
  // clear the display
  display.clear();

  txt += "Ambient = ";
  txt += String(mlx.readAmbientTempC());
  Serial.println(txt);
  display.setTextAlignment(TEXT_ALIGN_CENTER);
  display.setFont(ArialMT_Plain_16);
  display.drawString(64, 10, txt);

  txt = "Object = ";
  txt += String(mlx.readObjectTempC());
  Serial.println(txt);
  display.setTextAlignment(TEXT_ALIGN_CENTER);
  display.setFont(ArialMT_Plain_16);
  display.drawString(64, 26, txt);
  

  // write the buffer to the display
  display.display();

  delay(500);
}