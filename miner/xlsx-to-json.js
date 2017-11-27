const xlsxj = require("xlsx-to-json");
const argv  = require('yargs').demandOption(['inputPath','outputName'])
    .default('outputName')
    .argv;

var input  = argv.inputPath + ".xlsx";
var output = argv.outputName + ".json";

xlsxj({
  input: input, 
  output: output
}, function(err, result) {
  if(err) {
    console.error(err);
  }else {
    console.log(result);
  }
});