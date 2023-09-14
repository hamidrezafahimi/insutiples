


## Not able to open video file by cv2.VideoCapture()

### Useful links:

[Link1](https://answers.opencv.org/question/1965/cv2videocapture-cannot-read-from-file/) -> What to do with conda

[Link2](https://github.com/opencv/opencv/issues/8471) A lot of talks ... maybe useful



### Solution:

It has something to do with `ffmpeg` it seems.

I didn't figure out what to do exactly.

Maybe I had to enable some flags when building the opencv source code.

Anyway, I installed the ffmpeg and then opencv on a conda environment and resolved the problem.
