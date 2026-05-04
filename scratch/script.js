const fs = require('fs');
let html = fs.readFileSync('/home/gregory/Voilier/site/index.html', 'utf8');

// 1. Move tarifs section before contact section
const tarifsRegex = /(<!-- TARIFS -->[\s\S]*?<section id="tarifs"[\s\S]*?<\/section>\s*)/;
const tarifsMatch = html.match(tarifsRegex);

if (tarifsMatch) {
  html = html.replace(tarifsMatch[0], '');
  const contactRegex = /(<!-- CONTACT -->\s*<section id="contact")/i;
  html = html.replace(contactRegex, tarifsMatch[0] + '$1');
}

// 2. Make form inputs lighter
html = html.replace(/background:\s*var\(--sand\);/g, 'background: var(--white);');

fs.writeFileSync('/home/gregory/Voilier/site/index.html', html);
console.log("Done");
