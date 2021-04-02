function draw(id,temp,moist,humid){   
    let xaxis=[]
    for(let i=0;i<temp.length;i++)
    xaxis.push(i);
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
            labels:xaxis,
            datasets:[temp_data,moist_data,humid_data ]
        },
        options:{
            maintainAspectRatio : false,
            tooltips: {
                callbacks: { 
                    title: function(tooltipItem, data) { 
                        return "";
                     }
                    }
                },
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
                    labelString: 'Latest →',
                    fontSize:"20",
    
                  }
            }],
        },
    }});
    
}
