const juice = require('juice');
const cheerio = require('cheerio');
const sass = require('node-sass');

const fs = require('fs-promise');
const mkdirp = require('mkdirp-promise/lib/node6');
const path = require('path');
const assign = require('object-assign');

const sassify = require('./sass');

module.exports = mkdirp(path.resolve('./dist'))
  .then(() => {
    return Promise.all([
      fs.readFile(path.resolve('./src/index.template'), 'utf-8'),
      sassify(path.resolve('./src/style.scss'))
    ])
      .then((files) => {
        return files
          .reduce((map, file) => {
            if ( file.match(/<html>/) ) {
              map.html = file;
            } else {
              map.css = file;
            }
            return map;
          }, {});
      });
  })
  .then((objMap) => {
    return sassify(path.resolve('./src/inline.scss'))
      .then((inlineCss) => {
        return [objMap, inlineCss];
      });
  })
  .then(([{ html, css }, inlineCss]) => {
    const $ = cheerio.load(html, {
      decodeEntities: false
    });

    const htmlContents = $('html').html();

    $('html').html(juice.inlineContent(htmlContents, css));

    $(`<style type="text/css">${inlineCss}</style>`).appendTo($('html').find('head'));

    return $.html();
  })
  .then((inlined) => {
    return fs.writeFile(path.resolve('./dist/html-dschau.template'), inlined, 'utf-8');
  })
  .then(() => {
    console.log('File written successfully');
  });
