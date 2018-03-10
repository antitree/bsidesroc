const functions = require('firebase-functions');
const fs = require('fs');
const { execSync } = require('child_process');

// // Create and Deploy Your First Cloud Functions
// // https://firebase.google.com/docs/functions/write-firebase-functions
//
exports.helloWorld = functions.https.onRequest((request, response) => {
 let initial = request.query.test || "wololo";
 fs.writeFileSync('/tmp/test', initial);

 let final = fs.readFileSync('/tmp/test');
 fs.unlinkSync('/tmp/test');

 osver = execSync('cat /etc/*relea* && uname -a');
 listing = execSync('ls -lash');
 //hugo = execSync('./hugo --help');
 hugo = execSync('curl -o push.zip 
 // follow 301 from: repository['html_url'] + '/archive/' + head_commit['tree_id'] + '.zip'

 response.send("Hello "+final+"<br/><br/>(try ?test=bojack)<br/><br/>"+osver+"<br/><br/>"+listing+"<br/><br/>"+hugo);
});
