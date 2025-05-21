# ES6 Basic

> A Holberton School project focusing on modern JavaScript (ES6) syntax and features.

## 📚 Description

This project explores the fundamentals of ECMAScript 6 (ES6), a major update to JavaScript that includes new syntax and features for writing clean, modern, and more efficient code.

Topics covered:

- `let` and `const`
- Arrow functions
- Default parameters
- Rest and spread operators
- Object shorthand
- Destructuring
- Classes and inheritance
- Modules (import/export)
- Promises (basic introduction
2. Create babel.config.json
json
Copier
Modifier
{
  "presets": ["@babel/preset-env"]
}
3. Run Your Scripts
To run a specific ES6 file with Babel:

bash
Copier
Modifier
npx babel-node ./0-constants.js
Or to transpile all files into a dist/ directory:

bash
Copier
Modifier
npx babel . --out-dir dist
📁 Project Structure
csharp
Copier
Modifier
ES6_basic/
├── 0-constants.js
├── 1-block-scoped.js
├── 2-arrow.js
├── 3-default-parameter.js
├── 4-rest-parameter.js
├── 5-spread-operator.js
├── 6-string-interpolation.js
├── 7-object-shorthand.js
├── 8-object-destructuring.js
├── 9-classroom.js
├── 10-car.js
├── 11-hoisting.js
├── 12-classes.js
├── 13-main.js
└── babel.config.json
👨‍💻 Author
Your Name
