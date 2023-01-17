
#include <Stepper.h>
#include <Servo.h>

// Define step constants
const int stepsPerRevolution = 2038;
const int step = 50;
const int servoMovement = 25; // 40 degree

int mapX = 0;
int mapY = 0;

int VRx = A0;
int VRy = A1;
int pos = 0;

// Creates two instances
// Pins entered in sequence IN1-IN3-IN2-IN4 for proper step sequence


Stepper xMotor = Stepper(stepsPerRevolution, 8, 10, 9, 11);
Stepper yMotor = Stepper(stepsPerRevolution, 4, 6, 5, 7);
Servo servo;

int xPosition = 0;
int yPosition = 0;

void setup() {
  Serial.flush();
  Serial.begin(9600);
  servo.attach(3);
  down();
  
  xMotor.setSpeed(8);
  yMotor.setSpeed(8);

  pinMode(VRx, INPUT);
  pinMode(VRy, INPUT);
}

void gotoDot(int x, int y) {
  xMotor.step((x - xPosition) * step);
  yMotor.step((y - yPosition) * step);
  pullDown();

  xPosition = x;
  yPosition = y;
}

void right() {
  xMotor.step(+step);
}
void left() {
  xMotor.step(-step);
}
void bottom() {
  yMotor.step(+step);
}
void top() {
  yMotor.step(-step);
}
void up() {
  for (pos = 0; pos <= servoMovement; pos += 1) {
    servo.write(pos);              
    delay(5);                       // waits 15ms for the servo to reach the position
  }
}


void down() {

  for (pos = servoMovement; pos >= 0; pos -= 1) { 
    servo.write(pos);             
    delay(5);                      
  }
}

void pullDown() {
    up();
    delay(100); // stay down
    down();
}





void loop() {

  if (Serial.available() > 0) {
    String command = Serial.readString();
    command.trim();

    
    if(command == "left") left();
    else if(command == "right") right();
    else if(command == "top") top();
    else if(command == "bottom") bottom();
    else if(command == "pullDown") pullDown();
    else if(command.startsWith("gotoDot")) {
      int x = command.substring(command.indexOf("_") + 1, command.lastIndexOf("_")).toInt();
      int y = command.substring(command.lastIndexOf("_") + 1).toInt();
      gotoDot(x, y);
    }
    Serial.write("ok");
  }

}