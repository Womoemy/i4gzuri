let operator = prompt("What operation do you want to perform? [' + ', ' - ', ' / ', ' x ']: ");
let num1 = parseInt(prompt("Enter first number: ", "0"));
let num2 = parseInt(prompt("Enter second number: ", "0"));
let result;

switch(operator) {
  case "+":
    result = `${num1} + ${num2} = ${num1 + num2}`;
    alert(result);
    break;
  case "-":
    result = `${num1} - ${num2} = ${num1 - num2}`;
    alert(result);
    break;
  case "x":
    result = `${num1} * ${num2} = ${num1 * num2}`;
    alert(result);
    break;
  case "*":
    result = `${num1} * ${num2} = ${num1 * num2}`;
    alert(result);
    break;
  case "/":
    result = `${num1} * ${num2} = ${num1 * num2}`;
    alert(result);
    break;
  default:
    alert("Invalid operation entered, try again...");
}
// Exit the program
// alert("Thank for using the Calculator. See you later!");

// let operator = prompt("What operation do you want to perform? [' + ', ' - ', ' / ', ' x ']: ");
// let num1 = parseInt(prompt("Enter first number: ", "0"));
// let num2 = parseInt(prompt("Enter second number: ", "0"));
// let result;

// switch(operator) {
//   case "+":
//     result = `${num1} + ${num2} = ${num1 + num2}`;
//     alert(result);
//     break;
//   case "-":
//     result = `${num1} - ${num2} = ${num1 - num2}`;
//     alert(result);
//     break;
//   case "x":
//     result = `${num1} * ${num2} = ${num1 * num2}`;
//     alert(result);
//     break;
//   case "/":
//     result = `${num1} * ${num2} = ${num1 * num2}`;
//     alert(result);
//     break;
//   default:
//     alert("Invalid operation entered, try again...");
// }
