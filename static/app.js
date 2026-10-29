const $ = id => document.getElementById(id);
let game = null, busy = false;
const letters = 'abcdefghijklmnopqrstuvwxyz';
for (const letter of letters) {
  const button = document.createElement('button');
  button.textContent = letter.toUpperCase();
  button.dataset.letter = letter;
  button.setAttribute('aria-label', `Guess ${letter.toUpperCase()}`);
  button.addEventListener('click', () => guess(letter));
  $('keyboard').append(button);
}
function controls() {
  $('new-game').disabled = busy;
  $('difficulty').disabled = busy;
  for (const button of $('keyboard').children) {
    button.disabled = busy || !game || game.status !== 'playing' || game.guessed_letters.includes(button.dataset.letter);
  }
}
function render() {
  $('pattern').replaceChildren(...game.pattern.split(' ').map(letter => {
    const cell = document.createElement('span');
    cell.textContent = letter === '_' ? '\u00a0' : letter.toUpperCase();
    return cell;
  }));
  $('pattern').setAttribute('aria-label', `Word: ${game.pattern}`);
  $('word-length').textContent = `${game.pattern.split(' ').length} LETTERS`;
  $('lives').textContent = `${game.remaining_guesses} / 6 chances`;
  $('guessed').textContent = game.guessed_letters.join(' ').toUpperCase() || 'None yet';
  $('status').textContent = game.status === 'won' ? `Well played! The word was ${game.word.toUpperCase()}.` : game.status === 'lost' ? `The word was ${game.word.toUpperCase()}. Try another?` : 'Your next letter could be the one.';
  [...$('figure').children].forEach((part, index) => part.style.visibility = index < 6 - game.remaining_guesses ? 'visible' : 'hidden');
  for (const button of $('keyboard').children) {
    const letter = button.dataset.letter;
    button.className = game.incorrect_letters.includes(letter) ? 'wrong' : game.guessed_letters.includes(letter) ? 'correct' : '';
  }
  controls();
}
async function api(path, data) {
  const response = await fetch(path, {method:'POST', headers:{'Content-Type':'application/json'}, body:JSON.stringify(data)});
  const result = await response.json();
  if (!response.ok) throw new Error(result.error || 'The request failed.');
  return result;
}
async function start() {
  if (busy) return;
  busy = true; controls(); $('error').textContent = '';
  try { game = await api('/api/games', {difficulty:$('difficulty').value}); render(); }
  catch (error) { $('error').textContent = error.message; }
  finally { busy = false; controls(); }
}
async function guess(letter) {
  if (busy || !game || game.status !== 'playing' || game.guessed_letters.includes(letter)) return;
  busy = true; controls(); $('error').textContent = '';
  try { game = await api(`/api/games/${game.game_id}/guess`, {letter}); render(); }
  catch (error) { $('error').textContent = error.message; }
  finally { busy = false; controls(); }
}
$('new-game').addEventListener('click', start);
document.addEventListener('keydown', event => {
  if (event.ctrlKey || event.metaKey || event.altKey || event.target.closest('select,input,textarea')) return;
  if (/^[a-zA-Z]$/.test(event.key)) { event.preventDefault(); guess(event.key.toLowerCase()); }
});
controls();
