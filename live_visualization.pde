import processing.serial.*; 
 Serial myPort;  //the Serial port object
 String val;
 int[] input = new int [4];
 //int[] inputr = new int [2];
 int serialCount=0;
 int tiempoant;
boolean firstContact = false;
String sensorReading="";
import java.io.BufferedWriter;
import java.io.FileWriter;
String outFilename = "data.csv"; 
void setup() {
  size(960, 960,P3D); //make our canvas 200 x 200 pixels big
  
  myPort = new Serial(this, Serial.list()[0], 115200);
  appendTextToFile(outFilename,"Date,Time,Length_x,Length_y,Line_x,Line_y\n");
  }
void draw()  {
textSize(30);

fill(0,0,255);

    translate(800,800);
    rotateX(radians(60));
    background(0);

    
    for (int j=0; j<15; j++) {
      for (int i=0; i<12; i++) {
          stroke(255);
  if (j>=12 && j<=15){
  fill(255,255,51);
  rect(-60*i,-120*j,60,120);
  }
  else if(j>=6 && j<12){
    fill(0,255,0);
  rect(-60*i,-120*j,60,120);
  }
  else if(j>=3 && j<6){
    fill(255,0,0);
  rect(-60*i,-120*j,60,120);
  }
  else if(j<3){
    fill(100,149,237);
  rect(-60*i,-120*j,60,120);
  }
        }
  
      }
    int  a=input[1];
    int  b=input[0];
 fill(0,0,0);
  rect(-60*a,-120*b,60,120);
     pushMatrix();
     translate(-242,0,535);
      rotateX(radians(-60));
      scale(0.52);
        for (int i=0; i<12; i++) {
      for (int j=0; j<12; j++) {
          stroke(255);
        if (i>=8 && i<=11){
  fill(255,128,0);
   rect(-i*28,-j*28,28,28);
  }
  else if(i>=4 && i<8){
    fill(128,128,128);
  rect(-i*28,-j*28,28,28);
    if(i>=5 && i<=6 && j<4)
    {
       fill(204,204,0);
  rect(-i*28,-j*28,28,28);
    }
  }
  else if(i>=0 && i<4){
    fill(153,0,73);
  rect(-i*28,-j*28,28,28);
  }
   }
  }
    int  c=11-input[3];
    int  d=11-input[2];
  fill(0,0,0);
  rect(-28*c,-28*d,28,28);
  fill(255,255,51);
      text("Yorker", 40,60); 
fill(0,255,0);
text("Full", 125, 200);
fill(255,0,0);
text("Good", 215, 400);
fill(100,149,237);
text("Short", 330, 650);
tint(255, 200);
//image(img, -700, -475);

      popMatrix();
}
  void serialEvent(Serial myPort) {sensorReading = myPort.readStringUntil('\n');
  if(sensorReading != null){
    int d=day();
    int m=month();
    int y=year();
    String dmy=str(d)+"-"+str(m)+"-"+str(y);
    int h=hour();
    int mi=minute();
    int sec=second();
    String time=str(h)+":"+str(mi)+":"+str(sec);
    sensorReading=trim(sensorReading);
    int abc[] = int(split(sensorReading, ','));
  appendTextToFile(outFilename,dmy+","+time+","+sensorReading);
  input[0]=abc[0];
  input[1]=abc[1];
  input[2]=abc[2];
  input[3]=abc[3];
  println(abc);
     
void appendTextToFile(String filename, String text){
  File f = new File(dataPath(filename));
  if(!f.exists()){
    createFile(f);
  }
  try {
    PrintWriter out = new PrintWriter(new BufferedWriter(new FileWriter(f, true)));   // true to append the output
    out.println(text);
    out.close();                                      // clean close allows to read / copy file while processing runs
  }catch (IOException e){
      e.printStackTrace();
  }
}
void createFile(File f){
  File parentDir = f.getParentFile();
  try{
    parentDir.mkdirs(); 
    f.createNewFile();
     }
    catch(Exception e){
    e.printStackTrace();
    }
}    
