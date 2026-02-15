#include <Arduino.h>
// #include <LiquidCrystal.h> //literally just here so that it would ignore all my other errors
void setColor(int redValue, int greenValue, int blueValue);
void fadeToColor(int r1, int g1, int b1, int r2, int g2, int b2, int duration);
void ambientMode(int r1, int g1, int b1, int duration);

int redPin = 11;
int greenPin = 10;
int bluePin = 9;

// Base (initial) color — change these to set the starting color
int baseR = 255;
int baseG = 0;
int baseB = 255;

int lastR = 0;
int lastG = 0;
int lastB = 0;

void setup()
{
  Serial.begin(9600);

  while (!Serial)
  {
    ; // wait for serial port to be ready (for boards with native USB)
  }
  // Defining the pins as OUTPUT
  pinMode(redPin, OUTPUT);
  pinMode(greenPin, OUTPUT);
  pinMode(bluePin, OUTPUT);

  // pinMode(buttonPin, INPUT_PULLUP);

  // Start with the configured base color
  setColor(baseR, baseG, baseB);
}

void loop()
{
  // Fade from the base color to a darker version, then back
  // const int darkPercent = 30; // darker color = darkPercent% of base (0-100)
  // int darkR = baseR * darkPercent / 100;
  // int darkG = baseG * darkPercent / 100;
  // int darkB = baseB * darkPercent / 100;

  const int durationMs = 10000; // fade duration in milliseconds

  // // Fade to darker
  // fadeToColor(baseR, baseG, baseB, darkR, darkG, darkB, durationMs);
  // delay(250);

  // // Fade back to base
  // fadeToColor(darkR, darkG, darkB, baseR, baseG, baseB, durationMs);
  // delay(1000);
  ambientMode(baseR, baseG, baseB, durationMs);
}
void setColor(int redValue, int greenValue, int blueValue)
{

  // fadeToColor(redValue, greenValue, blueValue, r2, g2, b2, 1000);
  analogWrite(redPin, redValue);
  analogWrite(greenPin, greenValue);
  analogWrite(bluePin, blueValue);

  if (redValue != 0 || greenValue != 0 || blueValue != 0)
  {
    lastR = redValue;
    lastG = greenValue;
    lastB = blueValue;
  }
}

void fadeToColor(int r1, int g1, int b1, int r2, int g2, int b2, int duration)
{

  int steps = 200;
  float rStep = (r2 - r1) / float(steps);
  float gStep = (g2 - g1) / float(steps);
  float bStep = (b2 - b1) / float(steps);

  for (int i = 0; i <= steps; i++)
  {
    analogWrite(redPin, r1 + rStep * i);
    analogWrite(greenPin, g1 + gStep * i);
    analogWrite(bluePin, b1 + bStep * i);
    delay(duration / steps);
  }
}

void ambientMode(int r1, int g1, int b1, int duration) // first set is original
{
  int darkerR = r1 * 0.2;
  int darkerG = g1 * 0.1;
  int darkerB = b1 * 0.4;

  fadeToColor(r1, g1, b1, darkerR, darkerG, darkerB, duration); // first we need to fade original color to darker
  delay(700);
  fadeToColor(darkerR, darkerG, darkerB, r1, g1, b1, duration); // darker color back to original
  delay(700);
}
