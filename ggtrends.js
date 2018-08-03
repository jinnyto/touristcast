'use strict';

 const googleTrends = require('google-trends-api')

 var rl = require('readline');
 var sleep = require('system-sleep');


/* ******************* Interest over time **************************/
var readline = require('readline');
var rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
  terminal: false
});

rl.on('line', function(line){
 googleTrends.interestOverTime({
   keyword: line,
   startTime: new Date('2016-01-01'),
   endTime: new Date(Date.now()),
   category: 67, 
})
 .then((res) => {
   var o = {}; // empty Object
   var key = line;
   o[key] = [];
   o[key].push(res);
   console.log(o);
   //sleep(100000);
 })
 .catch((err) => {
   console.log('got the error', err);
   console.log('error message', err.message);
   console.log('request body',  err.requestBody);
 });

})
