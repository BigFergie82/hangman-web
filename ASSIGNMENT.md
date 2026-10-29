### CSE 4095 — Agentic Programming

### Programming Assignment: Build and Deploy a Web-Based Hangman Game

**Assignment Type:** Individual

**Duration:** One week

**Total Points:** 100

**Development Tools:** Cursor or another AI coding agent, Python, Flask, HTML, CSS, JavaScript, GitHub, and Render

### 1. Overview

In this assignment, you will use an AI coding agent to develop and deploy a web-based Hangman game.

You will be provided with three reference materials:

1. **SPECIFICATION.md** — The original software specification for the Hangman project.
2. **TODO.md** — The original phased implementation plan.
3. **Instructor's Cursor Transcript** — A record of how the instructor used Cursor to implement and deploy the Hangman application.

Your task is to use these materials to guide the development of your own Hangman web application.

The original specification describes a larger system with several types of clients and automated bot functionality. **For this assignment, you only need to implement the Hangman server and browser-based client.**

You do not need to implement a terminal client, automated Hangman bots, bot evaluation, or a leaderboard.

You may explore the instructor's deployed application as a reference:

[https://hangman-ex89.onrender.com/](https://hangman-ex89.onrender.com/)

However, you must develop and deploy your own implementation.

### 2. Learning Objectives

By completing this assignment, you should be able to:

- Use a software specification to guide AI-assisted software development.
- Adapt an existing implementation plan to a reduced project scope.
- Use Cursor or another AI coding agent to implement a multi-component application.
- Understand client-server architecture.
- Develop a Flask server that exposes REST API endpoints.
- Use HTML, CSS, and JavaScript to build an interactive browser interface.
- Understand how HTTP requests and JSON responses connect the frontend and backend.
- Test and debug an AI-generated application.
- Deploy a complete web application to a cloud hosting platform.

### 3. Project Requirements

Your application must include the following components.

#### A. Hangman Game Engine

Implement the Hangman game logic in Python.

The game engine must support:

- Random word selection.
- Easy, Medium, and Hard difficulty levels.
- Validating letter guesses.
- Tracking correct and incorrect guesses.
- Displaying the current word pattern.
- Tracking remaining incorrect guesses.
- Detecting wins and losses.
- Preventing further guesses after a game ends.

The game engine should be independent of the browser interface.

#### B. Flask Server and REST API

Implement a Flask server that manages games and provides a REST API.

At minimum, implement these endpoints:

| &#x20;&#x20;&#x20;Method | &#x20;Endpoint                   | &#x20;Purpose                         |
| ------------------------ | -------------------------------- | ------------------------------------- |
| &#x20;&#x20;&#x20;POST   | &#x20;/api/games                 | &#x20;Create a new Hangman game       |
| &#x20;&#x20;&#x20;GET    | &#x20;/api/games/{game_id}       | &#x20;Retrieve the current game state |
| &#x20;&#x20;&#x20;POST   | &#x20;/api/games/{game_id}/guess | &#x20;Submit a letter guess           |

&#x20;  Your server must:

- Accept and return JSON.
- Generate unique game identifiers.
- Maintain separate game states.
- Validate incoming requests.
- Return appropriate HTTP status codes.
- Keep the hidden word on the server during active gameplay.

The browser must communicate with the Flask server through the REST API.

#### C. Web-Based Client

Implement an interactive browser interface using HTML, CSS, and JavaScript.

Your interface must allow users to:

1. Select Easy, Medium, or Hard difficulty.
2. Start a new Hangman game.
3. Guess letters by clicking buttons or using the keyboard.
4. See the current word pattern.
5. See previously guessed letters.
6. See the number of remaining incorrect guesses.
7. See a Hangman drawing that changes as incorrect guesses accumulate.
8. See a message when the game is won or lost.
9. Start another game without reloading the application.

The web interface should communicate with Flask using JavaScript fetch() or an equivalent mechanism.

You may use SVG, HTML elements, or another suitable approach to draw the Hangman figure.

**Important:** The browser must not implement its own independent game engine or contain the hidden word during active gameplay. The Flask server is responsible for determining the results of guesses.

#### D. Testing

Test both the game engine and the web application.

At minimum, verify:

- Starting games at all three difficulty levels.
- Making correct and incorrect guesses.
- Repeated or invalid guesses.
- Winning and losing games.
- Starting a new game after completing one.
- Handling invalid API requests.
- Ensuring the hidden word is not exposed during active gameplay.
- Updating the browser correctly after each guess.

You may use AI-generated automated tests, manual browser testing, or both. Automated tests for the game engine and API are strongly encouraged.

#### E. Cloud Deployment

Deploy your application to Render or another suitable cloud hosting platform.

Your deployed application must:

- Be accessible through a public HTTPS URL.
- Display the Hangman web interface.
- Support the required REST API endpoints.
- Allow a user to play a complete game through the browser.
- Work without requiring the user to install Python or run a local server.

### 4. Development Instructions

#### Step 1 — Review the Provided Materials

Read SPECIFICATION.md, TODO.md, and the instructor's Cursor transcript.

Identify which features are required for this assignment and which are outside its scope.

Use Cursor to revise the original TODO file so it focuses on:

1. Game engine and word management.
2. Flask server and REST API.
3. Browser-based client.
4. Testing and debugging.
5. Cloud deployment.

You should remove or mark as out of scope the tasks related to terminal clients, automated bots, evaluation, and leaderboards.

#### Step 2 — Initialize the Project

Create a project directory and GitHub repository.

Open the project in Cursor and provide the specification and TODO file.

Suggested initial prompt:

Read SPECIFICATION.md and TODO.md carefully. I need to build and deploy a web-based Hangman game with a Flask backend and an HTML/CSS/JavaScript frontend. Terminal clients, automated bots, evaluation, and leaderboards are outside the scope of this assignment. Revise TODO.md into a phased implementation plan for the required features. Do not implement code yet.

Review the revised plan before proceeding.

#### Step 3 — Implement the Application Incrementally

Work through the revised TODO file one phase at a time.

Suggested prompt:

Implement the next incomplete phase in TODO.md according to SPECIFICATION.md and the reduced assignment scope. Run relevant tests, explain the changes, and update TODO.md only after verifying the implementation.

After each phase:

1. Review the generated code.
2. Run the application or relevant tests.
3. Identify and resolve errors.
4. Update TODO.md.
5. Commit your changes to GitHub.

You should not ask the AI agent to implement the entire application in a single prompt.

#### Step 4 — Test the Application Locally

Run the Flask application on your computer.

Open the web interface in a browser and play several games.

Use Chrome Developer Tools to inspect at least one REST API request.

Verify that:

- JavaScript sends an HTTP request when a user guesses a letter.
- Flask processes the request.
- The server returns JSON containing the updated game state.
- JavaScript updates the webpage using the response.

You should be able to explain this sequence.

#### Step 5 — Deploy the Application

Push your project to GitHub.

Deploy the application to Render or another suitable cloud hosting service.

If using Gunicorn, an example startup command is:

```
gunicorn --bind 0.0.0.0:$PORT --workers 1 server:app

```

Adjust the command to match your project structure.

After deployment, open the public URL and play a complete game.

Verify that the deployed application works independently of your local development environment.

### 5. Suggested One-Week Schedule

| &#x20;&#x20;&#x20;Day   | &#x20;Recommended Work                                 |
| ----------------------- | ------------------------------------------------------ |
| &#x20;&#x20;&#x20;Day 1 | &#x20;Review materials, revise TODO, create repository |
| &#x20;&#x20;&#x20;Day 2 | &#x20;Implement game engine and word management        |
| &#x20;&#x20;&#x20;Day 3 | &#x20;Implement Flask server and REST API              |
| &#x20;&#x20;&#x20;Day 4 | &#x20;Implement web interface                          |
| &#x20;&#x20;&#x20;Day 5 | &#x20;Test and debug the complete application          |
| &#x20;&#x20;&#x20;Day 6 | &#x20;Deploy to Render and verify functionality        |
| &#x20;&#x20;&#x20;Day 7 | &#x20;Prepare submission and final demonstration       |

### &#x20;  6. Submission Requirements

Submit the following through HuskyCT.

**A. GitHub Repository URL**

Your repository should contain:

- Python game engine and Flask server.
- HTML, CSS, and JavaScript frontend.
- Word lists and other required resources.
- Original specification.
- Updated TODO file.
- Dependency and deployment configuration.
- Tests, if developed.
- README with instructions for running the application locally.

**B. Deployed Application URL**

Provide the public URL of your Hangman web application.

The application must remain accessible during grading.

**C. Short Development Report (1–2 Pages)**

Submit a PDF report covering:

1. **Development process:** How you used Cursor or another AI coding agent.
2. **Implementation:** Briefly describe the game engine, Flask server, REST API, and browser interface.
3. **Testing:** Describe how you verified the application.
4. **Deployment:** Explain how you deployed the application.
5. **Challenges:** Describe at least one problem and how you resolved it.
6. **Reflection:** What did you learn about AI-assisted development?

Include two or three representative prompts from your interactions with the coding agent.

**D. Demonstration**

Submit a short screen recording (approximately 2–3 minutes) showing:

1. Your deployed Hangman webpage.
2. Starting a game and guessing letters.
3. A complete game ending in a win or loss.
4. Starting a new game.
5. At least one HTTP request and JSON response in Chrome Developer Tools.

### 7. Grading Rubric

| &#x20;&#x20;&#x20;Component                              | &#x20;Points  |
| -------------------------------------------------------- | ------------- |
| &#x20;&#x20;&#x20;Hangman game engine and correctness    | &#x20;20      |
| &#x20;&#x20;&#x20;Flask server and REST API              | &#x20;20      |
| &#x20;&#x20;&#x20;Web interface and usability            | &#x20;20      |
| &#x20;&#x20;&#x20;Testing and reliability                | &#x20;15      |
| &#x20;&#x20;&#x20;Cloud deployment                       | &#x20;15      |
| &#x20;&#x20;&#x20;Agentic development process and report | &#x20;10      |
| &#x20;&#x20;&#x20;**Total**                              | &#x20;**100** |

### &#x20;  8. Important Guidelines

- This is an individual assignment.
- You may use AI coding agents extensively.
- You are responsible for verifying the correctness of AI-generated code.
- You may refer to the instructor's Cursor transcript, but you should develop your own implementation and prompts.
- Do not copy the instructor's completed source code.
- You are not required to implement a terminal client, automated bots, bot evaluation, or leaderboard functionality.
- You must be able to explain how your application works.
- Do not commit credentials or other secrets to GitHub.
- Clearly document any incomplete functionality or known limitations.

### 9. Expected Outcome

By the end of the assignment, you should have a fully functioning, publicly accessible Hangman web application.

More importantly, you should understand how to guide an AI coding agent through a complete development process, from software specification and implementation planning to testing and cloud deployment.
