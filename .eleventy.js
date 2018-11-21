module.exports = function(config) {

  // Add a date formatter filter to Nunjucks
  // config.addFilter("dateDisplay", require("./filters/dates.js") );
  // config.addFilter("timestamp", require("./filters/timestamp.js") );
  // config.addFilter("squash", require("./filters/squash.js") );

  return {
    dir: {
      input: "src",
      output: "dist",
      includes: "includes"
    },
    templateFormats : ["pug", "md"],
    htmlTemplateEngine : "pug"
  };

};
