<details>
  <summary>Tap to open heroku 🔎</summary>

<h2>🚀 Deploy on Heroku</h2>

<a href="https://dashboard.heroku.com/new?template=https://github.com/BABY-MUSIC/YBB">
    <img src="https://files.catbox.moe/krqmz8.jpg" alt="Deploy to Heroku" width="200">
</a>

</details>


<details>
  <summary>Tap to open VPS 🔎</summary>

### 🔧 Quick Setup

1. **Upgrade & Update:**
   ```bash
   sudo apt-get update && sudo apt-get upgrade -y
   ```

2. **Install Required Packages:**
   ```bash
   sudo apt-get install python3-pip ffmpeg -y
   ```
3. **Setting up PIP**
   ```bash
   sudo pip3 install -U pip
   ```
4. **Installing Node**
   ```bash
   curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.38.0/install.sh | bash && source ~/.bashrc && nvm install v18
   ```
5. **Clone the Repository**
   ```bash
   git clone https://github.com/BABY-MUSIC/SPOTIFY_MUSIC && cd SPOTIFY_MUSIC
   ```
6. **Install Requirements**
   ```bash
   pip3 install -U -r requirements.txt
   ```
7. **Create .env  with sample.env**
   ```bash
   cp sample.env .env
   ```
   - Edit .env with your vars
8. **Editing Vars:**
   ```bash
   vi .env
   ```
   - Edit .env with your values.
   - Press `I` button on keyboard to start editing.
   - Press `Ctrl + C`  once you are done with editing vars and type `:wq` to save .env or `:qa` to exit editing.
9. **Installing tmux**
    ```bash
    sudo apt install tmux -y && tmux
    ```
10. **Run the Bot**
    ```bash
    bash start
    ```

---
</details>

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
            <a href="https://github.com/BABY-MUSIC/YBB" target="_blank">🔄 Fork</a>
            <a href="https://github.com/BABY-MUSIC/YBB" target="_blank">📊 View Stats</a>
        </div>
    </div>

</body>
</html>
