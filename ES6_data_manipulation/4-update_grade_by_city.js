// 4-update_grade_by_city.js

export default function updateStudentGradeByCity(students, city, newGrades) {
  if (!Array.isArray(students) || !Array.isArray(newGrades)) return [];

  // Filter students by the given city
  return students
    .filter((student) => student.location === city)
    .map((student) => {
      // Find matching grade entry
      const gradeEntry = newGrades.find((g) => g.studentId === student.id);
      // If found, use that grade; otherwise default to 'N/A'
      const grade = gradeEntry ? gradeEntry.grade : 'N/A';
      // Return a new object with the added grade property
      return { ...student, grade };
    });
}
