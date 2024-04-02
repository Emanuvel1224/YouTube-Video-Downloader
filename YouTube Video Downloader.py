from pytube import YouTube

# Prompt the user to enter the URL of the YouTube video
video_url = input("Enter the URL of the YouTube video: ")

try:
    # Create a YouTube object using the provided URL
    yt = YouTube(video_url)

    # Get all available video streams
    streams = yt.streams.filter(progressive=True).order_by('resolution').desc()

    # Display available video streams to the user
    for i, stream in enumerate(streams):
        print(f"{i+1}. Resolution: {stream.resolution}, Format: {stream.mime_type}")

    # Prompt the user to select the desired video quality
    choice = int(input("Enter the number corresponding to the desired video quality: "))
    
    # Get the selected stream
    selected_stream = streams[choice - 1]
    
    # Download the selected video stream
    selected_stream.download()
    
    print("Video downloaded successfully!")

except Exception as e:
    print("An error occurred:", e)
