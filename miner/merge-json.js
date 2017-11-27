const fs    = require('fs');
const _     = require('underscore');

var letters = JSON.parse(fs.readFileSync("toto.json", 'utf8'));

var textA   = JSON.parse(fs.readFileSync("textA.json", 'utf8'));
var textB   = JSON.parse(fs.readFileSync("textB.json", 'utf8'));
var textC   = JSON.parse(fs.readFileSync("textC.json", 'utf8'));

var cptA = 0;
var cptB = 0;
var cptC = 0;

for (var i = 0; i < letters.length; i++) {
	if (letters[i]["Phase"] == "A") {
		letters[i]["Autres informations"] = textA[cptA]["Autres informations"];
		letters[i]["Motivations"] = textA[cptA]["Motivations"];
		letters[i]["Parlez nous de vous"] = textA[cptA]["Parlez nous de vous"];
		console.log(letters[i]["Parlez nous de vous"])
		cptA ++
	}
	if (letters[i]["Phase"] == "B") {
		try {
		   	letters[i]["Autres informations"] = textB[cptB]["Autres informations"];
			letters[i]["Motivations"] = textB[cptB]["Motivations"];
			letters[i]["Parlez nous de vous"] = textB[cptB]["Parlez nous de vous"];
		}
		catch (e) {
		   	letters[i]["Autres informations"] = "";
			letters[i]["Motivations"] = "";
			letters[i]["Parlez nous de vous"] = "";
		}		
		cptB ++
	}
	if (letters[i]["Phase"] == "C") {
		letters[i]["Autres informations"] = textC[cptC]["Autres informations"];
		letters[i]["Motivations"] = textC[cptC]["Motivations"];
		letters[i]["Parlez nous de vous"] = textC[cptC]["Parlez nous de vous"];
		cptC ++
	}
	letters[i]["Ligne"] = letters[i]["Ligne"] + 1;
};

console.log(cptA);
console.log(cptB);
console.log(cptC);

fs.writeFile("letters.json",JSON.stringify(letters),function(err){
    if(err) throw err;
})
