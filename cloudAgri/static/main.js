knobobject=[]
for(let i=1;i<=6;i++)
{   let knob=pureknob.createKnob(300, 300);
    knob.setProperty('readonly', true);
    knob.setProperty('angleStart', -0.75 * Math.PI);
    knob.setProperty('angleEnd', 0.75 * Math.PI);
    knob.setProperty('colorFG', '#cfd2d6');
    knob.setProperty('colorBG', '#666D7A');
    knob.setProperty('trackWidth', 0.4);
    
    if(i==1||i==4) {
    knob.setProperty('valMin', -40);
    knob.setProperty('valMax', 60);
   }
    else if(i==6){
      knob.setProperty('valMin', 0);
      knob.setProperty('valMax', 60);
    }
    else {
    knob.setProperty('valMin', 0);
    knob.setProperty('valMax', 100);
    }
        
    document.getElementById('knob'+i).appendChild(knob.node());
    knobobject.push(knob);
}


function setvaluesensor(data){
  knobobject[0].setValue(data['temperature']);
  knobobject[1].setValue(data['humidity']);
  knobobject[2].setValue(data['moisture']);
}

function setvalueweather(data){
  document.getElementById('wpi').innerHTML="WEATHER : "+data['type_of_weather'].toUpperCase();
  knobobject[3].setValue(data['temp']);
  knobobject[4].setValue(data['humidity']);
  knobobject[5 ].setValue(data['wind_speed']);
}

function update(url='/get') {
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
      if (this.readyState == 4 && this.status == 200) {
       let result=JSON.parse(this.responseText);
       setvaluesensor(result['sensor_data'])
       setvalueweather(result['weather_data'])
       let check=false
       if (result['motor_data']=="ON")
       check=true
       document.getElementsByClassName("switch-input")[0].checked=check;
      }
    };
    xhttp.open("GET", url, true);
    xhttp.send();
  }

function switchchng(event) {
  if (event.checked) {
    fetch('/on') .then(()=>{}).then(()=>{});
  }
  else {
    fetch('/off') .then(()=>{}).then(()=>{});

  }

}
function hardreload(){
  update('/hardreload')
}


