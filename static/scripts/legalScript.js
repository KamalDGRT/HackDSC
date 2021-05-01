//SumBtn Dynamic Display
const sumBtn = $(".sumBtn");
const sumTxt  = $(".sumTxtP");

let si = 1;
sumBtn.click( ()=>{
    sumTxt.toggleClass("dis");

    if(si%2 == 0){
        sumBtn.html("Show Text");
    }else{
        sumTxt.css("margin-bottom", "0");
        sumBtn.html("Hide Text");
    }

    si++;
});

var perValue = Number($('.perValue').html());

anychart.onDocumentReady(function() {

  // set the data
  var data = [
      {x: "Risk", value: perValue, exploded: true},
      {x: "Safe", value: 100-perValue},
  ];

  // create the chart
  var chart = anychart.pie();

  // set the chart title
  chart.title("");

  // add the data
  chart.data(data);

  chart.legend().itemsLayout("vertical");

  // display the chart in the container
  chart.container('pieChartCon');
  chart.draw();

});