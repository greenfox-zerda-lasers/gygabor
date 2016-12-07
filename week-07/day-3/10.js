'use strict';

// create a student object
// that has a method `addgrade`, that takes a grade from 1 to 5
// an other method `getAverage`, that returns the average of the grades

var student = {
  grades : [],
  addgrade : function(num){
    if (num >= 1 && num <= 5){
      this.grades.push(num);
    }
  },
  getAverage : function(gradeList){
    var sum = 0;
    for (var i = 0; i < gradeList.length; i++){
      sum += gradeList[i];
    }
    return sum / gradeList.length;
  }
}

student.addgrade(4);
student.addgrade(5);
student.addgrade(1);
student.addgrade(2);
console.log(student.getAverage(student.grades), student.grades)
