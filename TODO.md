# Hangman browser assignment - reduced roadmap

The original Specification.md is retained unchanged. ASSIGNMENT.md takes
precedence where it narrows the original system.

## Phase 1 - Engine and word management
- [x] Implement independent game state, validation, win/loss and safe serialization.
- [x] Add three curated word lists and a validated random word loader.
- [x] Test core rules, answer secrecy and word loading (11 tests).

## Phase 2 - Flask REST API
- [ ] Create unique games and implement the three required JSON endpoints.
- [ ] Validate bodies and return 201/200, 400, 404, 409 and 415 as appropriate.
- [ ] Test separate games, invalid requests and complete win/loss flows.

## Phase 3 - Browser interface
- [ ] Add responsive HTML/CSS, SVG drawing and alphabet buttons.
- [ ] Use fetch for server-authoritative gameplay; support physical keyboard.
- [ ] Show guesses, lives, results, errors and new-game flow.
- [ ] Verify browser interaction and layout.

## Phase 4 - Testing and documentation
- [ ] Run automated engine/API tests and browser checks.
- [ ] Document setup, API, limitations and deployment.
- [ ] Prepare 1-2 page PDF development report with truthful verification status.

## Phase 5 - Public deployment and submission
- [ ] Publish source to a GitHub repository.
- [ ] Deploy Flask to Render and verify a complete game at its public HTTPS URL.
- [ ] Update report with the verified public URLs.
- [ ] Record the required 2-3 minute demonstration, including DevTools JSON.
- [ ] Submit repository URL, public app URL, PDF and recording on HuskyCT.

## Explicitly out of scope
Terminal client, automated bots, evaluation, scoring, leaderboard, replay,
accounts and multiplayer are excluded from this assignment.
