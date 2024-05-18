# cat-cv
Small program to detect cats in the webcam stream.

# Set up
1. In `./.env`, add the channel ID and token like this:
```
[id],[token]
```

2. Then get the cascade from [here](https://github.com/opencv/opencv/blob/master/data/haarcascades/haarcascade_frontalcatface.xml).
3. Create a directory named `frames` in `src`, this iss where we save the frames to send.
4. Finally, all you need to do is run `cd src && python main.py`

# TODO / Roadmap
- Detect black cats.