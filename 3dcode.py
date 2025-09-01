import cv2
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def load_images(image_paths):
    images = []
    for path in image_paths:
        image = cv2.imread(path)
        images.append(image)
    return images

def detect_keypoints(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    sift = cv2.SIFT_create()
    keypoints, descriptors = sift.detectAndCompute(gray, None)
    return keypoints, descriptors

def match_keypoints(descriptors1, descriptors2):
    bf = cv2.BFMatcher()
    matches = bf.knnMatch(descriptors1, descriptors2, k=2)
    good_matches = []
    for m, n in matches:
        if m.distance < 0.75 * n.distance:
            good_matches.append(m)
    return good_matches

def reconstruct_3d(image1, image2, keypoints1, keypoints2, matches):
    points3d = []
    for match in matches:
        img_idx1, img_idx2 = match.queryIdx, match.trainIdx
        x1, y1 = keypoints1[img_idx1].pt
        x2, y2 = keypoints2[img_idx2].pt
        points3d.append([x1, y1, x2, y2])  # Here, we store image coordinates
    return np.array(points3d)


# Paths to your images
image_paths = ['image1.jpg', 'image2.jpg', 'image3.jpg', 'image4.jpg']  # Add more images if needed

# Load images
images = load_images(image_paths)

# Detect keypoints and compute descriptors for each image
keypoints_list = []
descriptors_list = []
for image in images:
    keypoints, descriptors = detect_keypoints(image)
    keypoints_list.append(keypoints)
    descriptors_list.append(descriptors)

# Match keypoints between images
matches_list = []
for i in range(len(images) - 1):
    matches = match_keypoints(descriptors_list[i], descriptors_list[i + 1])
    matches_list.append(matches)

# Reconstruct 3D points
reconstructed_points = []
for i, matches in enumerate(matches_list):
    keypoints1 = keypoints_list[i]
    keypoints2 = keypoints_list[i + 1]
    points_3d = reconstruct_3d(images[i], images[i + 1], keypoints1, keypoints2, matches)
    reconstructed_points.append(points_3d)

# Convert reconstructed points to numpy array
point_cloud = np.vstack(reconstructed_points)

# Visualize point cloud using Matplotlib
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(point_cloud[:, 0], point_cloud[:, 1], point_cloud[:, 2], c='b', marker='o')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.show()
