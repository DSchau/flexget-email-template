const sass = require('node-sass');
const postcss = require('postcss');
const autoprefixer = require('autoprefixer');

const path = require('path');

module.exports = function(file) {
  return new Promise((resolve, reject) => {
    sass.render({ file: path.resolve(file) }, (err, result) => {
      if ( err ) {
        reject(err);
      }
      resolve(result.css.toString('utf-8'));
    });
  })
    .then((css) => {
      return postcss([
        require('autoprefixer')
      ])
        .process(css)
        .then((result) => result.css);
    });
};
