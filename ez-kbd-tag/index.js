const readline = require('readline');

const SEPARATOR = /[\ \+,]+/;
const SPECIAL_KEY_MATCH = [/^(command|cmd)$/i,
                           /^(option|opt|alt)$/i,
                           /^(control|ctrl|ctl)$/i,
                           /^(shift)$/i,
                           /^(left)$/i,
                           /^(right)$/i,
                           /^(up)$/i,
                           /^(down)$/i,
                           /^(delete|del|backspace)$/i,
                           /^(enter|return)$/i,
                           /^(tab)$/i,
                           /^(escape|esc)$/i,
                           /^(plus)$/i,
                           /^(comma)$/i,];
const SPECIAL_KEY_REPLACE = ['⌘',
                             '⌥',
                             '⌃',
                             '⇧',
                             '←',
                             '→',
                             '↑',
                             '↓',
                             '⌫',
                             '↩︎',
                             '⇥',
                             '⎋',
                             '+',
                             ',',];

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

rl.question('Input your key combination: ', (combination) => {
  if (combination.length > 1000) {
    console.error("Too long!");
    return;
  }

  var combinationList = [];
  var c = 0;

  while (combination.length > 0 && c < 20) {
    nextSeparator = combination.match(SEPARATOR);
    if (nextSeparator == null) {
      combinationList.push(combination);
      combination = '';
      break;
    }

    combinationList.push(combination.substr(0, nextSeparator.index));
    combinationList.push(combination.substr(nextSeparator.index, nextSeparator[0].length));
    combination = combination.substr(nextSeparator.index + nextSeparator[0].length);

    c++;
  }

  var kbdTag = '';
  for (var i = 0; i < combinationList.length; i++) {
    if (combinationList[i].match(SEPARATOR)) {
      if (combinationList[i].match(',')) {
        combinationList[i] = ', ';
        kbdTag += combinationList[i];
      } else if (combinationList[i].match(/\+/)) {
        combinationList[i] = '+';
        kbdTag += combinationList[i];
      }
    } else {
      for (var j = 0; j < SPECIAL_KEY_MATCH.length; j++) {
        if (combinationList[i].match(SPECIAL_KEY_MATCH[j])) {
          combinationList[i] = SPECIAL_KEY_REPLACE[j];
          break;
        }
      }
      kbdTag += `<kbd>${combinationList[i]}</kbd>`;
    }
  }

  console.log(kbdTag);
  console.log(combinationList.join(''));

  rl.close();
});
