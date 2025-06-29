try:
    """
    ------------------- FUNCTIONS -------------------------
    """

    def fn_1(file):
        import cv2
        import numpy as np
        import face_recognition as fr

        imgArya = fr.load_image_file("captured_image.jpg")
        imgArya = cv2.cvtColor(imgArya,cv2.COLOR_BGR2RGB)

        imgArya_test = fr.load_image_file(file)
        imgArya_test = cv2.cvtColor(imgArya_test,cv2.COLOR_BGR2RGB)

        faceloc = fr.face_locations(imgArya)[0]
        encodeArya = fr.face_encodings(imgArya)[0]
        # cv2.rectangle(imgArya,(faceloc[3],faceloc[0]),(faceloc[1],faceloc[2]),(255,0,255),2)

        faceloc_test = fr.face_locations(imgArya_test)[0]
        encodeArya_test = fr.face_encodings(imgArya_test)[0]
        # cv2.rectangle(imgArya_test,(faceloc_test[3],faceloc_test[0]),(faceloc_test[1],faceloc_test[2]),(255,0,255),2)

        results = fr.compare_faces([encodeArya],encodeArya_test,0.35)
        
        #Face_Recgonition --> database namedata

        # cv2.imshow("Aryaman",imgArya)
        # cv2.imshow("Aryaman Test",imgArya_test)
        # cv2.waitKey(3)
        return results[0]

    def fn_2():
        import cv2
        import time
        # Capture video from the default camera (usually the primary webcam)
        cap = cv2.VideoCapture(0)


        time.sleep(10)  # Wait for 3 seconds

        # Check if the camera was opened successfully
        if not cap.isOpened():
            print("Error: Camera not found or could not be opened.")
        else:
            # Read a frame from the camera
            ret, frame = cap.read()

            if not ret:
                print("Error: Failed to grab a frame.")
            else:
                # Save the captured frame as an image
                image_filename = 'captured_image.jpg'
                cv2.imwrite(image_filename, frame)
                print(f"Image saved as {image_filename}")

            # Release the camera
            cap.release()

    """
    ---------------------- DATA SET -----------------------------
    """

    names=["Ankush.jpg","Guddy.jpg","Nishq.jpg","Nity.jpg","Pupply.jpg","Aryaman.jpg"]


    """
    ------------------------ MAIN PROGRAM ----------------------------
    """

    fn_2()
    global flag
    global i
    for i in names:
        flag=1
        if fn_1(i):
            flag=0
            # print("The face detected is of : ", (i[-5::-1])[::-1])
            break
        else:
            flag=1
            # print("Face is unknown")
    if flag==1:
        print("Face is unknown")
    else:
        print("The face detected is of : ", (i[-5::-1])[::-1])

except:
    print("No face detected.")






