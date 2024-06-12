# Extract-Audio-from-Video-Using-MoviePy-and-Tkinter


1.Import Required Libraries:
-moviepy.editor: For handling video and audio processing.
-tkinter.filedialog: For opening a file dialog to select the video file.

2.Open File Dialog:
Use askopenfilename() from tkinter.filedialog to open a dialog window where the user can select a video file.

3.Load Video and Extract Audio:
-Load the selected video file using VideoFileClip from moviepy.editor.
-Extract the audio from the video.

4.Save the Extracted Audio:
Write the extracted audio to an MP3 file in the specified directory.

5.End Notification:
Print a message indicating the end of the process.
