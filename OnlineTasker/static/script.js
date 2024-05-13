function resetLists() {
           window.location.reload();
        }
window.addEventListener('pageshow', function(event) {
    // Если страница была кэширована и восстановлена из кэша,
    // то event.persisted будет true и мы должны сбросить списки
    if (event.persisted) {
        resetLists();
    }
});

let structure_fst = [[1, 2, 3, 4], [1, 2, 3, 4, 5, 6]]
let structure_scd = [[[], [], [], []], [[], [], [], [], [], [], [], []]]
structure_scd[0][0] = ["Аналитическая геометрия", "Введение в математический анализ", "Дискретная математика"]
structure_scd[0][1] = ["Линейная алгебра", "Многомерный анализ, интегралы и ряды", "Математическая логика и теория алгоритмов"]
structure_scd[0][2] = ["Элементы дифференциальных уравнений", "Теория вероятностей", "Дискретная математика"]
structure_scd[0][3] = ["Гармонический анализ", "Математическая статистика", "Математическая логика и теория алгоритмов"]
structure_scd[1][0] = ["Аналитическая геометрия", "Введение в математический анализ"]
structure_scd[1][1] = ["Линейная алгебра", "Многомерный анализ, интегралы и ряды"]
structure_scd[1][2] = ["Дифференциальные уравнения", "Кратные интегралы и теория поля", "Теория вероятностей"]
structure_scd[1][3] = ["Гармонический анализ", "Дифференциальные уравнения"]
structure_scd[1][4] = ["Теория функций комплексного переменного", "Уравнения математической физики"]
structure_scd[1][5] = ["Уравнения математической физики"]
let structure_third = [[[], [], [], []], [[], [], [], [], [], [], [], []]]
// вшпи 1 сем Аналитическая геометрия
structure_third[0][0][0] = [1, 2, 3]
// вшпи 1 сем Введение в математический анализ
structure_third[0][0][1] = [1, 2, 3]
// вшпи 1 сем Дискретная математика
structure_third[0][0][2] = [1, 2]
// вшпи 2 сем Линейная алгебра
structure_third[0][1][0] = [1, 2]
// вшпи 2 сем Многомерный анализ, интегралы и ряды
structure_third[0][1][1] = [1, 2, 3]
// вшпи 2 сем Математическая логика и теория алгоритмов
structure_third[0][1][2] = [1, 2]
// вшпи 3 сем Элементы дифференциальных уравнений
structure_third[0][2][0] = [1, 2]
// вшпи 3 сем Теория вероятностей
structure_third[0][2][1] = [1, 2]
// вшпи 3 сем Дискретная математика
structure_third[0][2][2] = [1, 2]
// вшпи 4 сем Гармонический анализ
structure_third[0][3][0] = [1, 2]
// вшпи 4 сем Математическая статистика
structure_third[0][3][1] = [1, 2]
// вшпи 4 сем Математическая логика и теория алгоритмов
structure_third[0][3][2] = [1, 2]
// фэфм 1 сем Аналитическая геометрия
structure_third[1][0][0] = [1, 2, 3]
// фэфм 1 сем Введение в математический анализ
structure_third[1][0][1] = [1, 2, 3]
// фэфм 2 сем Линейная алгебра
structure_third[1][1][0] = [1, 2]
// фэфм 2 сем Многомерный анализ, интегралы и ряды
structure_third[1][1][1] = [1, 2, 3]
// фэфм 3 сем Дифференциальные уравнения
structure_third[1][2][0] = [1, 2]
// фэфм 3 сем Кратные интегралы и теория поля
structure_third[1][2][1] = [1, 2]
// фэфм 3 сем Теория вероятностей
structure_third[1][2][2] = [1, 2]
// фэфм 4 сем Гармонический анализ
structure_third[1][3][0] = [1, 2]
// фэфм 4 сем Дифференциальные уравнения
structure_third[1][3][1] = [1, 2]
// фэфм 5 сем Теория функций комплексного переменного
structure_third[1][4][0] = [1, 2, 3]
// фэфм 5 сем Уравнения математической физики
structure_third[1][4][1] = [1, 2]
// фэфм 6 сем Уравнения математической физики
structure_third[1][5][0] = [1, 2]
schools.onchange=function(){
  semester.disabled = false;
  subject.disabled = true;
  number_task.disabled = true;
  semester.innerHTML = "<option value=\"0\">-- Выберите семестр --</option>";
  subject.innerHTML= "<option value=\"0\">-- Выберите предмет --</option>";
  number_task.innerHTML="<option value=\"0\">-- Выберите номер задания --</option>";
  myschool = this.value - 1;
  if (myschool != -1) {
    semester.innerHTML+='<hr />'
    for(var i= 0;i < structure_fst[myschool].length; i++) {
        semester.innerHTML += '<option value="'+(i+1)+'">'+structure_fst[myschool][i]+'</option>';
    }
  } else {
    semester.disabled = true;
  }
}

semester.onchange=function(){
  subject.disabled=false;
  number_task.disabled = true;
  subject.innerHTML= "<option value=\"0\">-- Выберите предмет --</option>";
  number_task.innerHTML="<option value=\"0\">-- Выберите номер задания --</option>";
  mysemester = this.value - 1;
  if (mysemester != -1) {
    subject.innerHTML+='<hr />'
    for(var i= 0;i < structure_scd[myschool][mysemester].length; i++) {
        subject.innerHTML+='<option value="'+(i+1)+'">'+structure_scd[myschool][mysemester][i]+'</option>';
    }
  } else {
    subject.disabled = true;
  }
}

subject.onchange=function(){
  number_task.disabled=false;
  number_task.innerHTML="<option value=\"0\">-- Выберите номер задания --</option>";
  mysubject = this.value - 1;
  if(mysubject != -1) {
    number_task.innerHTML+='<hr />'
    for(var i= 0;i < structure_third[myschool][mysemester][mysubject].length; i++){
        number_task.innerHTML+='<option value="'+(i+1)+'">'+structure_third[myschool][mysemester][mysubject][i]+'</option>';
    }
  } else {
    number_task.disabled=true;
  }
}