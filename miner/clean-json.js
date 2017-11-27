const fs    = require('fs');
const _     = require('underscore');
const argv  = require('yargs').demandOption(['input'])
    .argv;


var tmp = JSON.parse(fs.readFileSync(argv.input, 'utf8'));
var letters = []

for (var i = 0; i < tmp.length; i++) {
	var l = _.pick(tmp[i], "Date d'inscription","Ligne","Phase","Code Postal","Annee de naissance","Mois de naissance","Jour de naissance","Type de couchage","Salle de bain", "WC",	"Superficie","Duree d'accueil","Personne seule","Couple","Enfant(s)","Famille","Capacite d'accueil","Enseignement metier","Partage Reseau","Animaux","Fumeur","Langues","CSP","Situation professionnelle / domaine");
	var date = l["Date d'inscription"].split(' ')[0];
	if (date == null || date.trim() == "" || date.split('/') == null) {
		l["Date d'inscription"] = null;
	} else {
		date = date.split('/')
		var d = new Date(date[1] + ' ' + date[0] + ' ' + date[2]);
		d = d.setDate(d.getDate() + 1)
		try {
		   l["Date d'inscription"] = new Date(d).toISOString(); 
		}
		catch (e) {
		   console.log(l["Date d'inscription"]);
		   l["Date d'inscription"] = null;
		}		
	}
	
	letters.push(l);
};

fs.writeFile("toto.json",JSON.stringify(letters),function(err){
    if(err) throw err;
  })