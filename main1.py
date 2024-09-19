import cv2

#Format conversion for Raw Data.
image = cv2.imread('./test.jpeg')
cv2.imwrite('test.tiff', image)
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imwrite('test_gray.tiff', gray_image)

print("Image successfully converted to TIFF and grayscale.")

# Operations performed by LLFlow.

#Format conversion to snr after Image Enhancement by LLFlow.
def enhance_snr(image):
    blurred = cv2.GaussianBlur(image, (5, 5), 0)
    high_freq = cv2.absdiff(image, blurred)
    enhanced_image = cv2.add(image, high_freq)
    return enhanced_image

gray_image = cv2.imread('test1_gray.tiff', cv2.IMREAD_GRAYSCALE)
snr_enhanced_image = enhance_snr(gray_image)
cv2.imwrite('snr_test.tiff', snr_enhanced_image)

print("SNR enhanced image saved successfully.")
