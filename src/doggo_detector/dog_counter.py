import cv2
import matplotlib.pyplot as plt

def count_doggo(img_path: str, i: int, fig) -> int:
    face_cascade = cv2.CascadeClassifier(r'..\data\catface.xml')
    img = cv2.imread(img_path)
    grayscale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(grayscale)
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x - 10,y - 10), (x+w+20, y+h+20), (0, 0, 255), 10)
    cv_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    fig.add_subplot(2, 2, i + 1)
    plt.imshow(cv_rgb)
    return len(faces)


if __name__ == "__main__":
    fig = plt.figure()
    fig.suptitle("Project Laika")
    for i in range(4):
        print(f"Number of cats: {count_doggo(f'../data/cat{i}.jpeg', i, fig)}")
    plt.savefig("fig.png")