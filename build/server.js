const browserSync = require('browser-sync').create('flexget-email');
const exec = require('child_process').exec;

browserSync.init({
  server: true,
  serveStatic: ['dist']
});

browserSync.watch('src/*.{template}', buildAndReload);
browserSync.watch('src/**/*.scss', buildAndReload);

function buildAndReload() {
  if ( browserSync.active ) {
    exec('npm run preserve', browserSync.reload);
  }
}
