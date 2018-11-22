
module.exports = function(eleventyConfig) {

  eleventyConfig.addPassthroughCopy("src/assets/css");
  // Add a date formatter filter to Nunjucks
  // config.addFilter("dateDisplay", require("./filters/dates.js") );
  // config.addFilter("timestamp", require("./filters/timestamp.js") );
  // config.addFilter("squash", require("./filters/squash.js") );

  return {
    dir: {
      input: "src",
      output: "dist",
      data: "data",
      includes: "includes"
    },
    templateFormats : ["pug", "md"],
    htmlTemplateEngine : "pug"
  };

};
