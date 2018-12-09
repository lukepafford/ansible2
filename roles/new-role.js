#!/usr/bin/env node
const Mustache = require('mustache');
const process = require('process');
const fs = require('fs-extra');
const path = require('path');

if (process.argv.length !== 4) {
	console.log(`Usage: ${process.argv[1]}: roleName templateDir`);
	console.log('Description: Copies the templateDir into roleName. Files are rendered with Mustache');
	process.exit(1);
}

const roleName = process.argv[2];
const templateDir = process.argv[3];

// Recursively return all directories and files in an array
const walk = dir =>
	fs.readdirSync(dir)
	.reduce( (files, file) => {
		const fileName = path.join(dir, file);
		const isDirectory = fs.statSync(fileName).isDirectory();

		// magic recursion
		return isDirectory ? [ ...files, ...walk(fileName)] : [...files, fileName];
	}, []);

fs.ensureDir(roleName)
.then( () => fs.stat(templateDir))
.then( (stats) => { 
	if (!stats.isDirectory()) {
		let err = new Error(`${templateDir} is not a directory`);
		err.code = 'ENOTDIR';
		throw err;
	}
	return stats;
})
.then( () => fs.copy(templateDir, roleName) )
.then( () => {
	templateFiles = walk(roleName);
	const view = { roleName };

	// Read each file, render the template, and rewrite the file
	templateFiles.forEach( (templateFile) => {
		fs.readFile(templateFile, 'utf-8')
		.then( results => {
			const renderedTemplate = Mustache.render(results, view);
			fs.writeFile(templateFile, renderedTemplate);
		})
		.catch( (err) => console.error(err));
	})
})
.then( () => fs.writeFile(path.join(roleName, 'tasks', `${roleName}.yml`), '---', 'utf-8'))
.catch( (err) => console.error(err));
