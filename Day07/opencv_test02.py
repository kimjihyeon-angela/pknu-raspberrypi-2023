import cv2

# 01. 일반 이미지
# img = cv2.imread('./Day07/test.jpg')
# cv2.imshow('Original', img)

# 02. Grayscale (흑백과 조금 다름)
# img = cv2.imread('./Day07/test.jpg', cv2.IMREAD_GRAYSCALE)
# cv2.imshow('GrayScale', img)

#03. 이미지 사이즈 축소
# img = cv2.imread('./Day07/test.jpg', cv2.IMREAD_GRAYSCALE)
# img_small = cv2.resize(img, (200, 120))
# cv2.imshow('Small', img_small)

#04. 원본을 그대로 두고 흑백 추가 (원본과 흑백이 2개 나옴)
# img = cv2.imread('./Day07/test.jpg')
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# cv2.imshow('Original', img) # 원본 show
# cv2.imshow('Gray', gray)    # 흑백 show

# 05. 이미지 자르기
# img = cv2.imread('./Day07/test.jpg')
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# height, width, channel = img.shape
# print(height, width, channel)

# img_crop = img[:, :int(width / 2)] # height, width
# gray_crop = gray[:, :int(width / 2)]

# cv2.imshow('Original_Crop', img_crop) # 원본 show
# cv2.imshow('Gray_Crop', gray_crop)    # 흑백 show

# 05. 이미지 블러
# img = cv2.imread('./Day07/test.jpg')
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# height, width, channel = img.shape

# img_crop = img[:, :int(width / 2)] # height, width
# gray_crop = gray[:, :int(width / 2)]

# img_blur = cv2.blur(img_crop, (30, 30)) # 숫자가 커질 수록 blur 효과 커짐

# cv2.imshow('Original_Crop', img_blur) # 원본 show
# cv2.imshow('Gray_Crop', gray_crop)    # 흑백 show

cv2.waitKey(0)
cv2.destroyAllWindows()