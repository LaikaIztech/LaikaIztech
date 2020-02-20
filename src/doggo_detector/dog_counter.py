import cv2
import matplotlib.pyplot as plt
from nms.nms import boxes

def count_doggo(img_path: str) -> int:
    face_cascade = cv2.CascadeClassifier(r'..\data\catface.xml')
    img = cv2.imread(img_path)
    grayscale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    objs = []
    reject_levels = []
    level_weights = []
    objs, rej, scores = face_cascade.detectMultiScale3(grayscale, outputRejectLevels=True)
    indices = boxes([[x, y, x + w, y + h] for (x, y,w, h) in objs], scores)
    detections = [objs[i] for i in indices]
    scores = [scores[i] for i in indices]
    i = 0
    for (x, y, w, h) in detections:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 10)
        cv2.putText(img, f"{scores[i]}", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 2, (36, 255, 12), 4)
        i += 1
    cv_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    plt.imshow(cv_rgb)
    return len(detections)


if __name__ == "__main__":
    fig = plt.figure()
    fig.suptitle("Project Laika")
    print(f"Number of cats: {count_doggo('../data/cat0.jpeg')}")
    plt.savefig("fig.png")