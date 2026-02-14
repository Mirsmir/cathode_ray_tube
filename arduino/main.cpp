#include <LiquidCrystal.h> //literally just here so that it would ignore all my other errors

int redPin = 11;
int greenPin = 10;
int bluePin = 9;

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

    pinMode(buttonPin, INPUT_PULLUP);

    setColor(lastR, lastG, lastB);
}

void loop()
{

    setColor(lastR, lastG, lastB);
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
