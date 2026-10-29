# Demonstration recording guide (2-3 minutes)

Record the deployed app in Chrome, with the public HTTPS URL visible.
This guide is not a substitute for the actual required recording.

1. **0:00-0:20 - Introduce the app.** Explain that Flask owns the game
   state, while HTML/CSS/JavaScript provides the browser interface.
2. **0:20-0:45 - Start and guess.** Choose Easy and click New game.
   Click one alphabet button, then use the physical keyboard. Point out
   revealed letters, used buttons, chances and the changing drawing.
3. **0:45-1:25 - Finish a game.** Continue until a win or a loss. If
   needed, guess uncommon letters to reach six misses. Show the revealed
   answer and disabled letter buttons.
4. **1:25-1:40 - Start again.** Select another difficulty and click New
   game without reloading the page.
5. **1:40-2:30 - Inspect HTTP and JSON.** Press F12 (or Ctrl+Shift+I),
   open Network and select Fetch/XHR. Guess an unused letter. Click the
   POST request ending in `/guess`. Show its Payload (`letter`), HTTP
   status 200 in Headers, and the Response JSON: pattern, guessed_letters,
   incorrect_letters, remaining_guesses and status. Explain why there is
   no `word` field while status is playing.
6. **2:30-2:45 - Explain the flow.** A button/keyboard event calls fetch;
   Flask validates the guess, updates the Python engine, returns JSON,
   and JavaScript redraws the page. The browser does not choose the word.

Before submitting, review the PDF's process/reflection draft and personalize
it to match your understanding. Verify both public links in a private
browser window. Submit all four required items on HuskyCT.
