//Link -> https://www.codewars.com/kata/52e1476c8147a7547a000811

function validate(password) {
  return /(?=.{6,})(?=.*[a-z])(?=.*[A-Z]).*\d.[^\W]*$/.test(password);
}
