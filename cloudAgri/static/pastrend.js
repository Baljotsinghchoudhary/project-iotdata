function draw(id,temp,moist,humid,timestamp){   
    let temp_data={ 
        label:"TEMPERATURE",
        data:temp,
        borderColor:"#ff0000",
        pointBackgroundColor:"#FFFFFF",
        fill:false,
     
    }
    let moist_data={
        label: "        MOISTURE",
        data:moist,
        borderColor:"#00cc44",
        pointBackgroundColor:"#FFFFFF",
        fill:false,
    }
    let humid_data={
        label:"        HUMIDITY ",
        data:humid,
        borderColor:"#ffff00",
        pointBackgroundColor:"#FFFFFF",
        fill:false,
    }
    let myChart = new Chart(id, {
        type: 'line',
        data: {
            labels:timestamp,
            datasets:[temp_data,moist_data,humid_data ]
        },
        options:{
            maintainAspectRatio : false,
            legend: {
            display: true,
            position: 'top',
            
            labels: {
              boxWidth: 80,
              fontColor: 'white',

            }
          },
          layout: {
            padding: {
                left: 10,
                right: 10,
                top: 10,
                bottom: 10
            },
        },
          scales: {
            type:'linear',
            xAxes: [{
                scaleLabel: {
                    display: true,
                    labelString: 'Time-Stamp',
                    fontSize:"20",
    
                  }
            }],
        },
    }});
    
}
