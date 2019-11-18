#define trigPin 9
#define echoPin 10
float duration,distancem1,distancem2,speed0,distm,sum=0,i=0;

void setup() {
  Serial.begin(9600);
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
  pinMode(13,OUTPUT);
  pinMode(7,OUTPUT);

}
  void loop() {
//distance 1
digitalWrite(trigPin, LOW);
delayMicroseconds(2);
digitalWrite(trigPin, HIGH);
delayMicroseconds(10);
digitalWrite(trigPin, LOW);
duration = pulseIn(echoPin, HIGH);
distancem1= duration*0.034/200;
//Serial.println(distancem1);
delay(150);

//distance 2
digitalWrite(trigPin, LOW);
delayMicroseconds(2);
digitalWrite(trigPin, HIGH);
delayMicroseconds(10);
digitalWrite(trigPin, LOW);
duration = pulseIn(echoPin, HIGH);
distancem2= duration*0.034/200;
//Serial.println(distancem2);

distm=distancem1-distancem2;
speed0=distm/0.15;
//speed is in kmph
speed0=speed0*3.6;

if (distancem1<=300)  {
    if(distancem1>distancem2){
         sum=sum+speed0;
         i=i+1;
         }
}

if(i==2)
{
  if(sum>0){
Serial.print(distancem1) ;
Serial.print(":");
Serial.print(distancem2)  ; 
Serial.print(":");
Serial.print(sum/2);
Serial.println();
}

i=0;
sum=0;
}
 
