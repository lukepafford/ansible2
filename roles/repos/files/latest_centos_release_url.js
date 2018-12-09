#!/usr/bin/env node
const axios = require('axios');
const htmlparser = require('htmlparser2');
const path = require('path');

const getLatestPackageUrl = (url, pattern) => {
  const parser = new htmlparser.Parser({
    onopentag: (name, attribs) => {
      if (attribs.href) {
        if (pattern.test(attribs.href)) {
          console.log([url, attribs.href].join(path.sep));
        }
      }
    }
  }, {decodeEntities: true});
  
  axios.get(url)
  .then( res => {
    parser.write(res.data)
    parser.end()
  })
  .catch(console.log)
}

const url = 'http://mirror.centos.org/centos/7/os/x86_64/Packages'
const pattern = new RegExp('centos-release.*\.rpm')

getLatestPackageUrl(url, pattern);
