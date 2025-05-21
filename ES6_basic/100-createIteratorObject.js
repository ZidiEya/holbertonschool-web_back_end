export default function createIteratorObject(report) {
  // Get all employees arrays from all departments in one flat array
  const allEmployees = Object.values(report.allEmployees).flat();

  // Return the iterator for that array
  return allEmployees[Symbol.iterator]();
}
