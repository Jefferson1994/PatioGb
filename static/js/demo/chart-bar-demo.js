Chart.defaults.global.defaultFontFamily = 'Nunito', '-apple-system,system-ui,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif';
Chart.defaults.global.defaultFontColor = '#858796';

var endpoint=`/get_reportes2_id/`
$.ajax({
  method:"GET",
  url: endpoint,
  dataType: 'json',

  success: function (egreso_list) {
    const response=JSON.parse(egreso_list)
    //console.log("vista alquiler")
    //console.log(egreso_list)
   var array = new Array
var arrayVentas = new Array

for (let index = 0; index < response.length; index++) {
    var mes=moment(response[index].fields.Fecha_Salida)
    var objFinal = new Object();
    objFinal.Fecha = mes.format('MMMM')
    objFinal.costo = response[index].fields.valor
    //arrayVentas.push(response[index].fields.PrecioVenta)
    array.push(objFinal)
}

//console.log(array)

var suma = new Array
var inicial=0
var inicial2=0
var inicial3=0
var inicial4=0
var inicial5=0
var inicial6=0
var inicial7=0
var inicial8=0
var inicial9=0
var inicial10=0
var inicial11=0
var inicial12=0
for (let index = 0; index < 1; index++){
 
   var objFinalsuma1 = new Object();
  objFinalsuma1.Fecha ='January'
  objFinalsuma1.costo = 0
  suma[0]=objFinalsuma1
  var objFinalsuma1 = new Object();
  objFinalsuma1.Fecha="February"
  objFinalsuma1.costo = 0
  suma[1]=objFinalsuma1
  var objFinalsuma1 = new Object();
  objFinalsuma1.Fecha="March"
  objFinalsuma1.costo = 0
  suma[2]=objFinalsuma1
  var objFinalsuma1 = new Object();
  objFinalsuma1.Fecha= "April"
  objFinalsuma1.costo = 0
  suma[3]=objFinalsuma1
  var objFinalsuma1 = new Object();
 objFinalsuma1.Fecha="May"
 objFinalsuma1.costo = 0
suma[4]=objFinalsuma1
var objFinalsuma1 = new Object();
objFinalsuma1.Fecha="June"
objFinalsuma1.costo = 0
suma[5]=objFinalsuma1
var objFinalsuma1 = new Object();
objFinalsuma1.Fecha="July"
objFinalsuma1.costo = 0
suma[6]=objFinalsuma1
var objFinalsuma1 = new Object();
objFinalsuma1.Fecha="August"
objFinalsuma1.costo = 0
suma[7]=objFinalsuma1
var objFinalsuma1 = new Object();
objFinalsuma1.Fecha="September"
objFinalsuma1.costo = 0
suma[8]=objFinalsuma1
var objFinalsuma1 = new Object();
objFinalsuma1.Fecha="October"
objFinalsuma1.costo = 0
suma[9]=objFinalsuma1
var objFinalsuma1 = new Object();
objFinalsuma1.Fecha="November"
objFinalsuma1.costo = 0
suma[10]=objFinalsuma1
var objFinalsuma1 = new Object();
objFinalsuma1.Fecha="December"
objFinalsuma1.costo = 0
suma[11]=objFinalsuma1


}

for (let index = 0; index < array.length; index++) {
 var objFinalsuma = new Object();

  switch (array[index].Fecha) {
  case 'January':
    //console.log('mes abril');
    objFinalsuma.Fecha ='January'
    total1=parseFloat(array[index].costo)+inicial1
    objFinalsuma.costo = total1.toString();
    suma[0]=objFinalsuma
    inicial1=total1
    break;
  case 'February':
    //console.log('mes abril');
    objFinalsuma.Fecha ='February'
    total2=parseFloat(array[index].costo)+inicial2
    objFinalsuma.costo = total2.toString();
    suma[1]=objFinalsuma
    inicial2=total2
    break;
  case 'March':
    //console.log('mes abril');
    objFinalsuma.Fecha ='March'
    total3=parseFloat(array[index].costo)+inicial3
    objFinalsuma.costo = total3.toString();
    suma[2]=objFinalsuma
    inicial3=total3
    break;
  case 'April':
    //console.log('mes abril');
    objFinalsuma.Fecha ='April'
    total4=parseFloat(array[index].costo)+inicial4
    objFinalsuma.costo = total4.toString();
    suma[3]=objFinalsuma
    inicial4=total4
    break;
  case 'May':
    //console.log('mes abril');
    objFinalsuma.Fecha ='May'
    total5=parseFloat(array[index].costo)+inicial5
    objFinalsuma.costo = total5.toString();
    suma[4]=objFinalsuma
    inicial5=total5
    break;
  case 'June':
    //console.log('mes abril');
    objFinalsuma.Fecha ='June'
    total6=parseFloat(array[index].costo)+inicial6
    objFinalsuma.costo = total6.toString();
    suma[5]=objFinalsuma
    inicial6=total6
    break;
  case 'July':
    //console.log('mes abril');
    objFinalsuma.Fecha ='July'
    total7=parseFloat(array[index].costo)+inicial7
    objFinalsuma.costo = total7.toString();
    suma[6]=objFinalsuma
    inicial7=total7
    break;
  case 'August':
    //console.log('mes agostop');
    objFinalsuma.Fecha ='August'
    total8=parseFloat(array[index].costo)+inicial8
    objFinalsuma.costo = total8.toString();
    suma[7]=objFinalsuma
    inicial8=total8
    break;
  case 'September':
    //console.log('mes abril');
    objFinalsuma.Fecha ='September'
    total9=parseFloat(array[index].costo)+inicial9
    objFinalsuma.costo = total9.toString();
    suma[8]=objFinalsuma
    inicial9=total9
    break;
  case 'October':
    //console.log('mes abril');
    objFinalsuma.Fecha ='October'
    total10=parseFloat(array[index].costo)+inicial10
    objFinalsuma.costo = total10.toString();
    suma[9]=objFinalsuma
    inicial10=total10
    break;
  case 'November':
    //console.log('mes abril');
    objFinalsuma.Fecha ='November'
    total11=parseFloat(array[index].costo)+inicial11
    objFinalsuma.costo = total11.toString();
    suma[10]=objFinalsuma
    inicial11=total11
    break;
  case 'December':
    //console.log('mes abril');
    objFinalsuma.Fecha ='December'
    total12=parseFloat(array[index].costo)+inicial12
    objFinalsuma.costo = total12.toString();
    suma[11]=objFinalsuma
    inicial12=total12
    break;
  
  default:
    console.log('Lo lamentamos, por el momento no disponemos de ');
    break;
  }
    
}

//console.log("el total es ;"+total)
//console.log(suma)


  



    //console.log(array)
 
   
    grafica1(suma)


    
    // body...
  },
  error:function(error_egreso_list){
    console.log("error algo paso")
  }

})

var grafica1= function(data1){
  var t = new Array
  var venta = new Array
  
  for (let index = 0; index < data1.length; index++) {
    t.push(data1[index].Fecha)
    venta.push(data1[index].costo)
  var ctx = document.getElementById("myBarChart");
  var myBarChart = new Chart(ctx, {
  type: 'bar',
  data: {
    labels: t,
    datasets: [{
      label: "Revenue",
      backgroundColor: "#4e73df",
      hoverBackgroundColor: "#2e59d9",
      borderColor: "#4e73df",
      data:  venta,
    }],
  },
  options: {
    maintainAspectRatio: false,
    layout: {
      padding: {
        left: 10,
        right: 25,
        top: 25,
        bottom: 0
      }
    },
    scales: {
      xAxes: [{
        time: {
          unit: 'month'
        },
        gridLines: {
          display: false,
          drawBorder: false
        },
        ticks: {
          maxTicksLimit: 6
        },
        maxBarThickness: 25,
      }],
      yAxes: [{
        ticks: {
          min: 0,
          max: 3000,
          maxTicksLimit: 5,
          padding: 10,
          // Include a dollar sign in the ticks
        
        },
        gridLines: {
          color: "rgb(234, 236, 244)",
          zeroLineColor: "rgb(234, 236, 244)",
          drawBorder: false,
          borderDash: [2],
          zeroLineBorderDash: [2]
        }
      }],
    },
    legend: {
      display: false
    },
    tooltips: {
      titleMarginBottom: 10,
      titleFontColor: '#6e707e',
      titleFontSize: 14,
      backgroundColor: "rgb(255,255,255)",
      bodyFontColor: "#858796",
      borderColor: '#dddfeb',
      borderWidth: 1,
      xPadding: 15,
      yPadding: 15,
      displayColors: false,
      caretPadding: 10,
      callbacks: {
        
      }
    },
  }
});
  }

}
