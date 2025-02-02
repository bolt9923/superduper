<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>YouTube Music Intro</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            text-align: center;
            background-color: #121212;
            color: white;
        }
        .container {
            margin-top: 50px;
        }
        .logo {
            width: 150px;
            height: 150px;
            border-radius: 50%;
            border: 3px solid gold;
            object-fit: cover;
        }
        .quote {
            font-style: italic;
            font-size: 18px;
            margin: 20px 0;
            color: #ffcc00;
        }
        .buttons a {
            display: inline-block;
            padding: 10px 20px;
            margin: 10px;
            font-size: 16px;
            font-weight: bold;
            color: white;
            background-color: gold;
            text-decoration: none;
            border-radius: 25px;
            transition: 0.3s;
        }
        .buttons a:hover {
            background-color: #ffcc00;
        }
        details {
            margin: 20px auto;
            width: 80%;
            background: #1e1e1e;
            padding: 10px;
            border-radius: 10px;
        }
        summary {
            cursor: pointer;
            font-weight: bold;
            font-size: 18px;
            color: gold;
        }
    </style>
</head>
<body>

    <div class="container">
        <!-- Logo -->
        <img src="https://files.catbox.moe/krqmz8.jpg" alt="YouTube Music Logo" class="logo">

        <!-- Introduction -->
        <h2>🎵 Welcome to YouTube Music</h2>
        <p class="quote">"Music that touches your soul, anytime, anywhere!"</p>

        <!-- GitHub Buttons -->
        <div class="buttons">
            <a href="https://github.com/BABY-MUSIC/YBB" target="_blank">⭐ Star</a>
            <a href="https://github.com/BABY-MUSIC/YBB/fork" target="_blank">🔄 Fork</a>
            <a href="https://github.com/BABY-MUSIC/YBB" target="_blank">📊 View Stats</a>
        </div>
    </div>

    <!-- Heroku Deployment Section -->
    <details>
        <summary>Tap to open Heroku 🔎</summary>
        <h2>🚀 Deploy on Heroku</h2>
        <a href="https://dashboard.heroku.com/new?template=https://github.com/BABY-MUSIC/YBB">
            <img src="https://files.catbox.moe/krqmz8.jpg" alt="Deploy to Heroku" width="200">
        </a>
    </details>

    <!-- VPS Setup Guide -->
    <details>
        <summary>Tap to open VPS 🔎</summary>
        <h2>🔧 Quick Setup</h2>
        <p>Follow these steps to set up your VPS:</p>

        <ol>
            <li><strong>Upgrade & Update:</strong>
                <pre><code>sudo apt-get update && sudo apt-get upgrade -y</code></pre>
            </li>
            <li><strong>Install Required Packages:</strong>
                <pre><code>sudo apt-get install python3-pip ffmpeg -y</code></pre>
            </li>
            <li><strong>Setting up PIP:</strong>
                <pre><code>sudo pip3 install -U pip</code></pre>
            </li>
            <li><strong>Installing Node:</strong>
                <pre><code>curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.38.0/install.sh | bash && source ~/.bashrc && nvm install v18</code></pre>
            </li>
            <li><strong>Clone the Repository:</strong>
                <pre><code>git clone https://github.com/BABY-MUSIC/SPOTIFY_MUSIC && cd SPOTIFY_MUSIC</code></pre>
            </li>
            <li><strong>Install Requirements:</strong>
                <pre><code>pip3 install -U -r requirements.txt</code></pre>
            </li>
            <li><strong>Create .env with sample.env:</strong>
                <pre><code>cp sample.env .env</code></pre>
                <p>Edit .env with your vars</p>
            </li>
            <li><strong>Editing Vars:</strong>
                <pre><code>vi .env</code></pre>
                <p>- Edit .env with your values.</p>
                <p>- Press <code>I</code> button on keyboard to start editing.</p>
                <p>- Press <code>Ctrl + C</code> once you are done, then type <code>:wq</code> to save or <code>:qa</code> to exit without saving.</p>
            </li>
            <li><strong>Installing tmux:</strong>
                <pre><code>sudo apt install tmux -y && tmux</code></pre>
            </li>
            <li><strong>Run the Bot:</strong>
                <pre><code>bash start</code></pre>
            </li>
        </ol>
    </details>

</body>
</html>
