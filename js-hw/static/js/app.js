// from data.js
var tableData = data;

// YOUR CODE HERE!
console.log(tableData);

var tbody = d3.select("tbody");

console.log(data);

 data.forEach(function(ufoReport) {
  console.log(ufoReport);
  var row = tbody.append("tr");
   Object.entries(ufoReport).forEach(function([key, value]) {
     console.log(key, value);
     var cell = row.append("td");
     cell.text(value);
   });
 });

var submit = d3.select("#filter-btn");

 // Take input and recreate table
 submit.on("click", function() {

   d3.event.preventDefault();

  //  d3.select(".summary").html("");

   // User Input
   var inputElement = d3.select("#datetime");
   var inputValue = inputElement.property("value");

   console.log(inputValue);
   console.log(tableData);

   // Filtering Data
   var filteredData = tableData.filter(tableDatas => tableDatas.datetime === inputValue);

   console.log(filteredData);

    tbody.html("")
   filteredData.forEach(function(dateData) {
     var row = tbody.append("tr");
     Object.entries(dateData).forEach(function([key, value]) {
       var cell = row.append("td");
       cell.text(value);
     });
   });
 });

 
