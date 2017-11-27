const fs    = require('fs');
const _     = require('underscore');

var letters = JSON.parse(fs.readFileSync("letters.json", 'utf8'));

var sample  = letters.slice(2500,3000);

fs.writeFile("sample.json",JSON.stringify(sample),function(err){
    if(err) throw err;
})
