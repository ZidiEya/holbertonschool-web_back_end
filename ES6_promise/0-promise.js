// 0-promise.js

export default function getResponseFromAPI() {
  return new Promise((resolve, reject) => {
    // No actual async operation needed, just return a Promise
    resolve();
  });
}
