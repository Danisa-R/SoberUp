from IPython.display import display, Javascript
from google.colab.output import eval_js
from base64 import b64decode
import uuid
import os
import time

class Camera:

    PATH_IMAGES = os.path.join('data', 'images') # return type: /data/images
    labels = ['drunk', 'not drunk']
    number_images = 20
    video = cv2.VideoCapture(2) 


    def __init__(self) -> None:
        pass


    # todo : need to access google colab specific API -- 
    # Colab code exectures on a VM that doesn't have webcam attached 
    # (APIs that presume direct hardware access won't work)

    def take_photo(filename='photo.jpg', quality=0.8):
        js = Javascript('''
            async function takePhoto(quality) {
            const div = document.createElement('div');
            const capture = document.createElement('button');
            capture.textContent = 'Capture';
            div.appendChild(capture);

            const video = document.createElement('video');
            video.style.display = 'block';
            const stream = await navigator.mediaDevices.getUserMedia({video: true});

            document.body.appendChild(div);
            div.appendChild(video);
            video.srcObject = stream;
            await video.play();

            // Resize the output to fit the video element.
            google.colab.output.setIframeHeight(document.documentElement.scrollHeight, true);

            // Wait for Capture to be clicked.
            await new Promise((resolve) => capture.onclick = resolve);

            const canvas = document.createElement('canvas');
            canvas.width = video.videoWidth;
            canvas.height = video.videoHeight;
            canvas.getContext('2d').drawImage(video, 0, 0);
            stream.getVideoTracks()[0].stop();
            div.remove();
            return canvas.toDataURL('image/jpeg', quality);
            }
            ''')
        display(js)
        data = eval_js('takePhoto({})'.format(quality))
        binary = b64decode(data.split(',')[1])
        with open(filename, 'wb') as f:
            f.write(binary)
        return filename


# loop thru labels then loop thru images then take a picture to save inside data folder
    def get_picture(self):
        for label in labels:
            print(f"Collecting images for {labels}")
            image_name=os.path.join(PATH_IMAGES, label+'.'+str(uuid.uuid1()+'.jpg'))
            
            # saves an image to file b/c When working with OpenCV, images are stored in numpy ndarray
            for image_num in range(number_images):
                print(f"Collecting images for {label} and {image_num})

                check, frame = cap.read() # webcam feed
                cv2.imwrite(image_name, frame)  # writes out image to file
                cv2.imshow('Image Collection', frame)  # render to the screen
                time.sleep(2)

                # 2 sec delay between image captures
            if key & 0xFF == ord('q'): # hit 'q' on keyboard to quit
                break
            video.release()
            cv2.destroyAllWindows()


    # todo: might not use webcam to access data points, only use access webcam
    def open_webcam(self):
        while video.isOpened():
        check, frame = video.read()
        cv2.imshow('YOLO', frame)

        # Make detecions
        results=model(frame)

        cv2.imshow('Color Frame', np.squeeze(results.render()))

        # if check:
        key = cv2.waitKey(10)
        if key & 0xFF == ord('q'): # hit 'q' on keyboard to quit
            break
        else:
          print('Frame not available')
          print(video.isOpened())

        video.release()
        cv2.destroyAllWindows()

    def get_uploaded_keys(self):
        for fn in uploaded.keys():
            print('User uploaded file "{name}" with length {length} bytes'.format(
            name=fn, length=len(uploaded[fn])))