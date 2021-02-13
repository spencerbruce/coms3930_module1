// center of circle 
int x1; int y1;

void setup(){
  // size(displayWidth, displayHeight);
  size(1024, 768);
  //smooth();
  textAlign(BOTTOM, CENTER);
  x1 = width/2;
  y1 = height*2;
}

void draw(){
  background(30);
  float radius = x1*4;   
  
  // Setting up my colors 
  color black = color(23, 25, 26);  
  color pink = color(238, 115, 149); 
  color yellow = color(238, 219, 178);
  color blue = color(111, 197, 255);  
  
  // convert the time to the degree offset, assuming a 6:55 AM sunrise (24900 seconds)  
  float time = second() + minute()*60 +  hour()*3600 +  3300;
  float offset = (450 - map(time, 0, 86400, 0, 360)) % 360; 
  
  // draw each of the gradients according to this offset 
  drawArc(15, 30, pink, black, radius, offset);
  drawArc(30, 150, black, black, radius, offset);
  drawArc(150,165, black, pink, radius, offset);
  drawArc(165,195, pink, yellow, radius, offset);
  drawArc(195,210, yellow, blue, radius, offset);
  drawArc(210,330, blue, blue, radius, offset);
  drawArc(330,345, blue, yellow, radius, offset);
  drawArc(345,375, yellow, pink, radius, offset);
}

void drawArc(float ang1, float ang2, color c1, color c2, float radius, float offset){
  float res = 1/radius * 25; 
  for(float angle = ang1; angle < ang2; angle += res){
    // inter is the interpolation point to determine the gradient
    float inter = map(angle, ang1, ang2, 0, 1);
    color c = lerpColor(c1, c2, inter);
    stroke(c);
    // Drawing the lines based on the current radius and angle, including offset
    float x2 = x1 + cos(radians(angle + offset)) * radius;
    float y2 = y1 + sin(radians(angle + offset)) * radius;
    line(x1, y1, x2, y2);
  }
}
