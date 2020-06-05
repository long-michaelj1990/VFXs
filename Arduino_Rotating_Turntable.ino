#include <Servo.h>

//Declare pin functions on RedBoard
#define dir 2
#define stp 3
#define MS1 4
#define MS2 5
#define EN  6

//Declare variables for functions
const byte numChars = 8;
char receivedChars[numChars];
boolean newData = false;
char *substringsA;
char *substringsB;
char *substringsC;
char user_input;
int degree;
int deg=0;
int x;
int y;
int state;
int rotation10=10;
int rotation20=20;
int rotation30=30;
int el =11;
int tw = 22;
int tt = 33;


void setup() {
  pinMode(dir, OUTPUT);
  pinMode(stp, OUTPUT);
  pinMode(MS1, OUTPUT);
  pinMode(EN, OUTPUT);
  pinMode(MS2, OUTPUT);
  resetEDPins(); //Set step, direction, microstep and enable pins to default states
  Serial.begin(9600);

}

 //Main loop
void loop() {
  int angle=0;
  recvWithEndMarker();
//  showNewData();
  DataOperation();
}

void recvWithEndMarker(){
  static byte ndx=0;
  char endMarker='\n';
  
  if (Serial.available()> 0){
    while(Serial.available()> 0 && newData ==false){
  user_input = Serial.read(); //Read user input and trigger appropriate function
  digitalWrite(EN, LOW); //Pull enable pin low to allow motor control
  
  if (user_input != endMarker){
    receivedChars[ndx]=user_input;
    ndx++;  
  
  if (ndx>=numChars){
    ndx =numChars -1;
  }
  }
  else{
    receivedChars[ndx]='\0';
    ndx = 0;
    newData=true;
  }
  }
}
}

//void showNewData(){
//if (newData==true){
//  newData=false;
//}
//}
  
void DataOperation(){
  
  if (newData==true){
    //  SmallStepModeFW();
      substringsA=strstr(receivedChars,"a_");
      substringsB=strstr(receivedChars,"b_");
      substringsC=strstr(receivedChars,"c_");
      if (substringsA)
      {
        SmallStepModeFW();
      }
      else if(substringsB)
      {
        SmallStepModeBW();
      }
      else if(substringsC)
      {
      resetEDPins();
      }
      else
      {
        Serial.println("Invalid option entered.");
      }
      resetEDPins();
      
  }
  }
  
// 1/2 microstep foward mode function
void SmallStepModeFW()
  {   
  digitalWrite(dir, LOW); //Pull direction pin low to move "forward"
  digitalWrite(MS1, LOW); //Pull MS1, and MS2 high to set logic to 1/2 microstep resolution
  digitalWrite(MS2, HIGH);
  for(x=0; x<20; x++)  //Loop the forward stepping enough times for motion to be visible
  {
    digitalWrite(stp,HIGH); //Trigger one step forward
    delay(1);
    digitalWrite(stp,LOW); //Pull step pin low so it can be triggered again
    delay(1);

  }
  newData=false;
  char *substringsA;
}

// 1/2 microstep backward mode function
void SmallStepModeBW()
{   
  digitalWrite(dir, HIGH); //Pull direction pin low to move "forward"
  digitalWrite(MS1, LOW); //Pull MS1, and MS2 high to set logic to 1/2 microstep resolution
  digitalWrite(MS2, HIGH);
  for(x= 0; x<20; x++)  //Loop the forward stepping enough times for motion to be visible
  {
    digitalWrite(stp,HIGH); //Trigger one step forward
    delay(1);
    digitalWrite(stp,LOW); //Pull step pin low so it can be triggered again
    delay(1);
    
  }
  newData=false;
  char *substringsB;
}

//Reset Easy Driver pins to default states
void resetEDPins()
{
  digitalWrite(stp, LOW);
  digitalWrite(dir, LOW);
  digitalWrite(MS1, LOW);
  digitalWrite(MS2, LOW);
  digitalWrite(EN, HIGH);
  newData=false;
  char *substringsC;
}
