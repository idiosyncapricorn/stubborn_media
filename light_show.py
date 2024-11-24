import time
import random
import librosa
import pygame
import requests
import tempfile

def analyze_bpm(mp3_file):
    """Analyze the MP3 file to extract BPM."""
    print(f"Analyzing BPM for: {mp3_file}")
    y, sr = librosa.load(mp3_file)
    tempo, _ = librosa.beat.beat_track(y=y, sr=sr)
    tempo = float(tempo)  # Convert BPM to scalar value
    print(f"Detected BPM: {tempo}")
    return tempo

def generate_light_show_with_strobe(mp3_file, bpm):
    """Play MP3 and create a light show with BPM-based color changes and periodic strobe."""
    # Initialize Pygame for both audio and graphics
    pygame.init()
    pygame.mixer.init()
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)  # Full-screen mode
    pygame.display.set_caption("Full-Screen Light Show")

    # Load and play the MP3
    pygame.mixer.music.load(mp3_file)
    pygame.mixer.music.play()

    # Colors: pink and its complementary choices
    colors = [
        (255, 105, 180),  # Pink
        (64, 224, 208),   # Turquoise
        (152, 251, 152),  # Mint Green
        (255, 215, 0)     # Gold
    ]

    # Calculate beat interval from BPM
    beat_interval = 60 / bpm

    # Strobe times (15s, 30s, 1m, 1m30s, ...)
    strobe_intervals = [15, 30, 60, 90, 120, 150, 180]

    running = True
    start_time = time.time()  # Track elapsed time
    print("Starting full-screen light show...")
    while running:
        elapsed_time = time.time() - start_time

        # Trigger strobe effect at predefined intervals
        if int(elapsed_time) in strobe_intervals:
            print(f"Starting strobe effect at {int(elapsed_time)} seconds...")
            strobe_end_time = time.time() + 5  # Strobe for 5 seconds
            while time.time() < strobe_end_time:
                screen.fill((255, 255, 255))  # White
                pygame.display.flip()
                time.sleep(0.1)
                screen.fill((0, 0, 0))  # Black
                pygame.display.flip()
                time.sleep(0.1)
            print(f"Strobe effect complete at {int(elapsed_time)} seconds.")

        # Alternate between pink and a random complementary color
        for color in colors:
            screen.fill(color)
            pygame.display.flip()
            time.sleep(beat_interval)

        # Stop if the music has ended
        if not pygame.mixer.music.get_busy():
            running = False

    pygame.quit()

if __name__ == "__main__":
    # Input the online link to the MP3
    mp3_url = "https://on.soundcloud.com/Wnk6RfwqMJysX67J7"
    try:
        print("Downloading MP3 from the provided link...")
        with requests.get(mp3_url, stream=True) as response:
            response.raise_for_status()
            with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as temp_mp3:
                temp_mp3.write(response.content)
                temp_mp3_path = temp_mp3.name
        print(f"MP3 downloaded and saved as: {temp_mp3_path}")

        # Analyze BPM and generate the light show
        bpm = analyze_bpm(temp_mp3_path)  # Analyze BPM from the MP3
        generate_light_show_with_strobe(temp_mp3_path, bpm)

    except FileNotFoundError:
        print(f"Error: File not found at the provided URL {mp3_url}")
    except requests.exceptions.RequestException as e:
        print(f"Error: Unable to download MP3 - {e}")
    except Exception as e:
        print(f"An error occurred: {e}")