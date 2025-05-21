// 7-has_array_values.js

export default function hasValuesFromArray(aSet, array) {
  if (!(aSet instanceof Set) || !Array.isArray(array)) {
    return false;
  }
  return array.every((value) => aSet.has(value));
}
