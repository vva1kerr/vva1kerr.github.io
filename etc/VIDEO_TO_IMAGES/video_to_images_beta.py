# Importing all necessary libraries
import cv2
import os
from tqdm import tqdm

# Function to process a single video file
def process_video(video_path, save_path, sec):
    vid = cv2.VideoCapture(video_path)
    fps = vid.get(cv2.CAP_PROP_FPS)
    skip_frames = int(sec * fps)
    total_frame_length = int(vid.get(cv2.CAP_PROP_FRAME_COUNT))

    current_frame = 0
    past_second = -1

    for current_frame in tqdm(range(total_frame_length)):
        ret, frame = vid.read()

        if ret:
            if (current_frame - 1) % skip_frames == 0:
                frame_div_24 = str(current_frame / 24)
                frame_div_24_a = str(frame_div_24).split(".")[0]
                frame_div24a_div60 = int(frame_div_24_a) / 60

                minute = str(frame_div24a_div60).split(".")[0]
                f2460_back = str(frame_div24a_div60).split(".")[1][0:3]

                if len(str(f2460_back)) == len(str(1)):
                    f2460_back = int(f2460_back) / 10
                elif len(str(f2460_back)) == len(str(11)):
                    f2460_back = int(f2460_back) / 100
                elif len(str(f2460_back)) == len(str(111)):
                    f2460_back = int(f2460_back) / 1000
                else:
                    print("error")

                second = 60 * float(f2460_back)
                second = str(second).split(".")[0]
                if past_second == second:
                    second = second + "b"
                past_second = second

                timestr = "min" + minute + "-" + "sec" + str(second)
                name = f'{save_path}/{os.path.basename(video_path).split(".")[0]}-' + timestr + '.png'
                print('Creating...' + name)

                cv2.imwrite(name, frame)
        else:
            break

    vid.release()

def main():
    input_folder = input('--> input folder path containing videos: ').strip('"')
    sec = int(input('--> input seconds: '))

    # Create a folder on the desktop to save images
    save_path = f"C:/Users/{os.getlogin()}/Desktop/Images_from_videos_PSYCHO_series"
    if not os.path.exists(save_path):
        os.makedirs(save_path)

    # Iterate through all video files in the input folder
    for filename in os.listdir(input_folder):
        if filename.endswith(('.mp4', '.avi', '.mov', '.mkv')):
            video_path = os.path.join(input_folder, filename)
            process_video(video_path, save_path, sec)

if __name__ == "__main__":
    main()
