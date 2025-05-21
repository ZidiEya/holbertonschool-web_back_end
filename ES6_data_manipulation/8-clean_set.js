// 8-clean_set.js

export default function cleanSet(aSet, startString) {
  if (!(aSet instanceof Set) || typeof startString !== 'string') {
    return '';
  }

  const result = [];

  for (const value of aSet) {
    if (value.startsWith(startString)) {
      // append the remainder of the string after startString
      result.push(value.slice(startString.length));
    }
  }

  // join all pieces with hyphens
  return result.join('-');
}
