// 5-typed_arrays.js

export default function createInt8TypedArray(length, position, value) {
  // Create an ArrayBuffer of given length
  const buffer = new ArrayBuffer(length);
  const view = new DataView(buffer);

  // Check position bounds
  if (position < 0 || position >= length) {
    throw new Error('Position outside range');
  }

  // Set the Int8 value at the specified position
  view.setInt8(position, value);

  return view;
}
