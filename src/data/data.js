yaml = require('js-yaml');
fs   = require('fs');

// Site data

siteTitle = "Joyce Word Dictionary";
github = "https://github.com/open-editions/joyce-word-dictionary";
coda = "Produced in conjunction with Open Editions.";

// Load word data from YAML
try {
    var filename = "src/data/words.yaml";
    var jsonData = yaml.safeLoad(fs.readFileSync(filename, 'utf8'));
    // console.log(jsonData);
    jsonDataWrapped = {"data": jsonData}
    // console.log(JSON.stringify(jsonDataWrapped,null,'\t')
    module.exports = function() {
        return jsonDataWrapped;
    };
} catch (e) {
    console.log(e);
}
