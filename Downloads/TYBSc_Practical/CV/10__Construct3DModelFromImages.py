# import cv2
# import numpy as np


# def save_ply(filename, pts):
#     pts = pts[:3].T
#     with open(filename, 'w') as f:
#         f.write("ply\nformat ascii 1.0\n")
#         f.write(f"element Vertex {len(pts)}\n")
#         f.write("Property Float x\nproperty Float y\nproperty Float z\n")
#         f.write("end_header\n")
#         for p in pts:
#             f.write(f"{p[0]} {p[1]} {p[2]}\n")


# img1 = cv2.imread(r"C:\Users\admin\OneDrive\TYDS_surya_the_hero\B1.png")
# img2 = cv2.imread(r"C:\Users\admin\OneDrive\TYDS_surya_the_hero\B.png")
# gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
# gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)


# orb = cv2.ORB_create()
# kp1, des1 = orb.detectAndCompute(gray1, None)
# kp2, des2 = orb.detectAndCompute(gray2, None)

# bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
# matches = bf.match(des1, des2)

# pts1 = np.float32([kp1[m.queryIdx].pt for m in matches])
# pts2 = np.float32([kp2[m.trainIdx].pt for m in matches])


# E, _ = cv2.findEssentialMat(pts1, pts2)
# _, R, t, _ = cv2.recoverPose(E, pts1, pts2)


# proj1 = np.hstack((np.eye(3), np.zeros((3,1))))
# proj2 = np.hstack((R, t))
# pts4D = cv2.triangulatePoints(proj1, proj2, pts1.T, pts2.T)
# pts3D = pts4D / pts4D[3]


# save_ply("output.ply", pts3D)
# print("3D model saved as output.ply")








import cv2
import numpy as np
import open3d as o3d
IMAGE_PATH = "srk1.jfif"
image = cv2.imread(IMAGE_PATH)
if image is None:
    print("ERROR: Image not found!")
    print("Check:", IMAGE_PATH)
    exit()
print("Image loaded successfully")
print("Image size:", image.shape)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray = cv2.equalizeHist(gray)
depth = gray.astype(np.float32) / 255.0
height, width = depth.shape
max_width = 500
if width > max_width:
    scale = max_width / width
    new_width = int(width * scale)
    new_height = int(height * scale)
    image = cv2.resize(image, (new_width, new_height))
    depth = cv2.resize(depth, (new_width, new_height))
rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
rgb_o3d = o3d.geometry.Image(rgb)
depth_16 = (depth * 1000).astype(np.uint16)
depth_o3d = o3d.geometry.Image(depth_16)
rgbd = o3d.geometry.RGBDImage.create_from_color_and_depth(
    rgb_o3d,
    depth_o3d,
    depth_scale=1000.0,
    depth_trunc=1.0,
    convert_rgb_to_intensity=False
)
camera = o3d.camera.PinholeCameraIntrinsic(
    width,
    height,
    width,
    height,
    width / 2,
    height / 2
)
pcd = o3d.geometry.PointCloud.create_from_rgbd_image(
    rgbd,
    camera
)
pcd.transform([
    [1, 0, 0, 0],
    [0, -1, 0, 0],
    [0, 0, -1, 0],
    [0, 0, 0, 1]
])
print("Point cloud created!")
print("Number of points:", len(pcd.points))
output_file = "output/pointcloud.ply"
o3d.io.write_point_cloud(output_file, pcd)
print("Point cloud saved to:", output_file)
o3d.visualization.draw_geometries(
    [pcd],
    window_name="OpenCV + Open3D Point Cloud"
)
print("Program completed successfully!")