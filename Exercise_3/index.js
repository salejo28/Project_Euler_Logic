const palindromeArr = []

function palindrome(value) {
  if (typeof value === 'number') {
    return palindrome(value.toString())
  }

  const re = /[\W_]/g
  const string = value.toLowerCase().replace(re, '')
  const reverse = string.split('').reverse().join('')

  return string === reverse
}

let number = 100
function getPalindrome(num) {
  for (let index = 100; index < 999; index++) {
    const product = num * index
    if (palindrome(product)) {
      palindromeArr.push(product)
    }
  }
}

do {
  getPalindrome(number)
  number++
} while (number <= 999)

console.log(palindromeArr.sort((a, b) => b - a)[0])
