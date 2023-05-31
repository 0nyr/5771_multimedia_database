# Exercices sheet 5

## 1 : JPEG baseline process

### What are the main goals of the baseline process?

The main goal of the baseline process in the JPEG compression algorithm is to achieve efficient compression of digital images while maintaining an acceptable level of visual quality. It aims to significantly reduce the file size of an image by exploiting redundancies and perceptual limitations of the human visual system, thereby making it more suitable for storage, transmission, and display purposes.

By employing techniques such as color space conversion, Discrete Cosine Transform (DCT), quantization, run-length encoding (RLE), and Huffman coding, the baseline process seeks to achieve high compression ratios. It focuses on compressing the image data without compromising critical visual information and perceptual quality.

The baseline process of JPEG compression is widely used due to its effectiveness in balancing compression efficiency and visual fidelity. It provides a good trade-off between file size reduction and maintaining a reasonable level of image quality, making it suitable for various applications, including web graphics, digital photography, and multimedia content.

### Shortly summarize the function of each step, and outline which ones are lossy

The lossy sequential Discrete Cosine Transform (DCT)-based JPEG compression algorithm, commonly known as the Baseline Process or Basis mode, is a widely used method for compressing digital images. It involves several steps that aim to reduce the file size of an image while maintaining an acceptable level of visual quality. Here is an overview of the process:

1. Color Space Conversion: The algorithm begins by converting the image from the RGB color space to the YCbCr color space. This conversion separates the image into three components: luminance (Y) and two chrominance components (Cb and Cr). The human visual system is more sensitive to changes in luminance than chrominance, so separating these components helps optimize compression efficiency.
2. Partitioning into Blocks: The image is divided into 8x8-pixel blocks. Each block contains 64 pixels, which will be processed independently during compression. The subsequent steps are applied to each block separately.
3. Discrete Cosine Transform (DCT): A two-dimensional DCT is applied to each block. The DCT converts the pixel values from the spatial domain to the frequency domain, representing the image as a combination of different frequency components. This transformation helps to concentrate most of the image information into fewer significant coefficients, which can be more efficiently compressed. This is a lossy operation, but only slightly due to floating point precision operation.
4. Quantization: The DCT coefficients obtained in the previous step are divided by a quantization matrix. This matrix determines the compression level and is typically adjusted based on user preferences or application requirements. The quantization process discards high-frequency components, which are less perceptually important, resulting in loss of information. Higher compression ratios lead to more aggressive quantization and greater loss of quality.
5. Zigzag Scanning: The quantized DCT coefficients are arranged in a zigzag pattern to convert the two-dimensional array into a one-dimensional sequence. This reordering helps to group the significant coefficients together, facilitating their subsequent encoding and compression.
6. Run-Length Encoding (RLE): The zigzag-ordered DCT coefficients are then encoded using RLE. The RLE algorithm replaces consecutive runs of zeros with a special symbol indicating the number of zeros in the run. This step helps to exploit the high occurrence of zero-valued coefficients in images, further reducing the amount of data to be encoded.
7. Huffman Coding: The encoded coefficients are compressed using Huffman coding, a variable-length prefix coding technique. Huffman tables specific to luminance and chrominance components are used to map the encoded values to shorter codes for more frequent symbols and longer codes for less frequent symbols. Huffman coding exploits the statistical properties of the encoded coefficients to achieve efficient compression.
8. File Format: The compressed data, consisting of the Huffman-coded symbols, along with the quantization matrix, image dimensions, and other metadata, is typically stored in a JPEG file format.

During decompression, the reverse operations are performed in the same order to reconstruct the image. The quantized DCT coefficients are multiplied by the quantization matrix, and the inverse DCT is applied to obtain the pixel values. Finally, color space conversion and any necessary post-processing are performed to reconstruct the original image.

It's important to note that the lossy sequential DCT-based JPEG compression algorithm introduces irreversible loss of information due to quantization and subsequent compression steps. The degree of loss can be controlled by adjusting compression parameters, balancing the desired file size reduction with the acceptable level of visual quality.

#### lossy step :

Lossy steps in the baseline process of JPEG compression refer to the operations that introduce irreversible loss of information in order to achieve higher compression ratios. These steps intentionally discard some image details that are considered less perceptually important. The lossy steps in the baseline process include:

1. Quantization: After the Discrete Cosine Transform (DCT) is applied to the image blocks, the resulting DCT coefficients are divided by a quantization matrix. This process involves rounding the coefficients to the nearest integer and dividing them by corresponding values in the quantization matrix. Higher compression ratios involve more aggressive quantization, resulting in a greater loss of information. The quantization process eliminates high-frequency components, which contain fine details and noise, leading to a loss of image sharpness and fidelity.
2. Run-Length Encoding (RLE): After quantization, the DCT coefficients are encoded using Run-Length Encoding (RLE). RLE replaces consecutive runs of zeros (which are prevalent in the quantized coefficients) with a special symbol indicating the number of zeros in the run. While this encoding step helps reduce the size of the encoded data, it discards information about the exact positions of the zero-valued coefficients, resulting in a loss of spatial accuracy.
3. Huffman Coding: The encoded coefficients obtained from RLE are further compressed using Huffman coding. Huffman tables specific to luminance and chrominance components are used to assign variable-length codes to the encoded symbols. This step exploits the statistical properties of the coefficients to assign shorter codes to more frequent symbols and longer codes to less frequent symbols. While Huffman coding is lossless in itself, it is applied to the already quantized and RLE-encoded data, which has undergone lossy transformations, resulting in an overall lossy compression process.

It's important to note that the lossy steps in JPEG compression aim to balance the reduction in file size with an acceptable level of visual quality degradation. By adjusting the compression parameters, it is possible to control the trade-off between compression ratio and visual fidelity based on the specific requirements of the application or user preferences.

## Pre-processing

### What are the advantages of converting the color space from RGB to YUV (or. Y CbCr)?

> The human visual system is more sensitive to changes in luminance than chrominance.

Converting the color space from RGB to YUV (or YCbCr) in the JPEG compression algorithm offers several advantages. These include:

1. Separation of Luminance and Chrominance: The YUV color space separates the image into two components: luminance (Y) and chrominance (U and V or Cb and Cr). The human visual system is more sensitive to changes in luminance than chrominance. By separating these components, the compression algorithm can allocate more bits to accurately represent the luminance information, while reducing the bits allocated to chrominance information. This leads to better overall compression efficiency.
2. Reduced Redundancy: The RGB color space represents color information using three channels (red, green, and blue) that are highly correlated. In contrast, the YUV color space separates the brightness information (Y) from the color difference information (U and V). This separation helps in reducing redundancy in the image data, making it easier to compress. The color difference channels (U and V) typically have lower spatial resolution and can be subsampled further without significantly impacting visual quality, leading to additional compression gains.
3. Improved Compression Efficiency: The properties of the YUV color space make it more suitable for efficient compression. The DCT-based compression algorithms, such as JPEG, exploit the statistical properties of the image data in the frequency domain. The separation of luminance and chrominance components allows the DCT to concentrate most of the image information into fewer significant coefficients, resulting in better compression efficiency. This is particularly beneficial since the human visual system is more sensitive to luminance details than color details.
4. Compatibility with Video Coding: The YUV color space is widely used in video coding standards, such as MPEG and H.264. By converting the image to YUV color space in the JPEG compression algorithm, the resulting compressed image can be easily integrated into video streams or used as a video frame. This compatibility simplifies the integration of JPEG compressed images into multimedia applications and facilitates interoperability between image and video compression systems.

Overall, converting the color space from RGB to YUV (YCbCr) in JPEG compression provides advantages in terms of better compression efficiency, reduced redundancy, and compatibility with video coding. These benefits help achieve higher compression ratios while maintaining acceptable visual quality.

### What does subsampling of chrominance elements mean? (Consider the ratios 4:4:4, 4:2:2 and 4:2:0).

Subsampling of chrominance elements refers to the process of reducing the spatial resolution or sampling rate of the chrominance components (U and V or Cb and Cr) compared to the luminance component (Y) in an image or video signal. It is a technique commonly used in compression algorithms, such as JPEG and video coding standards like MPEG, to achieve further data reduction while minimizing the impact on perceived visual quality.

The notation used to represent chrominance subsampling ratios is in the form of "Y:U:V" or "Y:Cb:Cr," where the numbers indicate the sampling rates of the respective components. Let's consider the common subsampling ratios:

1. 4:4:4: In this ratio, the chrominance components (U and V or Cb and Cr) are sampled at the same rate as the luminance component (Y). Each chrominance sample corresponds to a unique pixel in the image or video frame. This means that there is no subsampling, and the full color resolution is maintained. The 4:4:4 ratio is often used in professional applications and situations where high-quality color reproduction is critical.
2. 4:2:2: In this ratio, the chrominance components are sampled at half the rate horizontally compared to the luminance component. This means that for every two consecutive pixels in the horizontal direction, there is only one chrominance sample. The vertical sampling rate remains the same as the luminance component. As a result, 4:2:2 subsampling reduces the horizontal color resolution while maintaining the full vertical color resolution. This ratio is commonly used in video coding and broadcasting applications.
3. 4:2:0: In this ratio, both the horizontal and vertical sampling rates of the chrominance components are reduced by half compared to the luminance component. This means that for every four consecutive pixels in both the horizontal and vertical directions, there is only one chrominance sample. The 4:2:0 subsampling reduces both horizontal and vertical color resolutions, resulting in a significant reduction in data. This ratio is widely used in various compression algorithms, including JPEG, to achieve higher compression ratios while maintaining acceptable visual quality.

It's important to note that chrominance subsampling introduces a loss of color information, particularly in fine color details and textures. However, the human visual system is less sensitive to color changes compared to luminance changes, making chrominance subsampling an effective technique for reducing data without significant perceptual degradation. The choice of subsampling ratio depends on the specific application requirements, available bandwidth, and desired trade-off between compression efficiency and color fidelity.

### Why should the size of the image be scaled first before encoding? And how does scaling work with respect to image blocks and minimum coded units (MCUs)?

Scaling the size of the image before encoding in the JPEG compression algorithm is beneficial for several reasons:

1. Compression Efficiency: Scaling down the image size reduces the overall amount of data that needs to be processed and encoded. Smaller images require fewer bits for encoding, resulting in higher compression ratios and smaller file sizes. This is particularly advantageous when dealing with large or high-resolution images, as it helps to achieve more efficient compression.
2. Computational Efficiency: Image scaling can also improve computational efficiency during the encoding process. With a smaller image size, the encoding algorithms, such as the Discrete Cosine Transform (DCT) and quantization, can be applied more quickly. This can lead to faster encoding times and improved processing performance.

When scaling the image, two concepts need to be considered: image blocks and Minimum Coded Units (MCUs). In JPEG compression, the image is divided into blocks of pixels, typically 8x8 pixels in size. Each block is processed independently during encoding. The MCUs represent a group of blocks that are treated as a unit during compression. The size of an MCU depends on the subsampling ratio used for chrominance components.

Scaling the image affects both the arrangement of blocks and the size of the MCUs:

1. Block Arrangement: When scaling down the image, the original blocks of pixels are merged or interpolated to create new blocks of the desired size. The process of merging or interpolating pixels ensures that the new blocks capture the essential information from the original image while reducing the resolution. The arrangement of the blocks remains the same, with fewer blocks in the scaled image compared to the original image.
2. MCU Size: The size of the MCUs is determined by the subsampling ratio used for chrominance components. When scaling the image, the subsampling ratio remains unchanged. Therefore, the size of the MCUs remains the same after scaling. However, the number of MCUs in the scaled image changes because the overall image size has been reduced.

It's important to note that scaling the image before encoding is an optional preprocessing step, and its usage depends on the specific requirements of the application or the desired trade-off between image quality and compression efficiency. Scaling can help achieve higher compression ratios and faster processing times, but it may also result in a loss of image details and potential degradation in visual quality.

## Discrete Cosinus Transformation

### What is the task of the Forward Discrete Cosine Transform (F-DCT) during the JPEG compression?

The task of the Forward Discrete Cosine Transform (F-DCT) during JPEG compression is to convert the image data from the spatial domain to the frequency domain. It is a key step in the compression process and plays a fundamental role in achieving efficient compression of digital images.

The F-DCT transforms each 8x8 block of pixel values in the image into a corresponding 8x8 block of frequency coefficients. This transformation is based on the mathematical concept of the Discrete Cosine Transform (DCT), which represents the image as a combination of different frequency components.

The F-DCT operates on the assumption that most of the image information is concentrated in the lower-frequency components, while higher-frequency components contain less perceptually important details and noise. By converting the image to the frequency domain using the F-DCT, the JPEG compression algorithm can exploit this property to achieve better compression efficiency.

The F-DCT calculates the DCT coefficients by performing a series of mathematical operations on the input pixel values within each 8x8 block. The resulting coefficients represent the amplitudes of different frequency components present in the block.

Once the image is transformed into the frequency domain, the DCT coefficients can be quantized, encoded, and compressed more efficiently. The quantization step, which follows the F-DCT, allows for the removal of high-frequency components that contribute less to the visual quality. The subsequent encoding and compression steps take advantage of the statistical properties of the transformed coefficients to achieve further reduction in file size while maintaining an acceptable level of visual fidelity.

During the decompression process, the inverse Discrete Cosine Transform (IDCT) is applied to the compressed frequency coefficients to reconstruct the original pixel values and reconstruct the image.

In summary, the task of the Forward Discrete Cosine Transform (F-DCT) in JPEG compression is to convert the image data from the spatial domain to the frequency domain, facilitating efficient compression by concentrating most of the image information into fewer significant coefficients.

### In a DCT-transformed block, which parts are most useful for compression ?

In a DCT-transformed block, the coefficients located in the top-left corner (low-frequency region) are generally the most useful for compression. These coefficients represent the lower-frequency components of the block, which tend to contain the majority of the visually important information in an image.

The DCT coefficients in the top-left corner correspond to the lower spatial frequencies, which capture large-scale patterns, smooth variations, and overall structure of the image. These coefficients have a higher magnitude compared to the coefficients in the high-frequency regions, indicating their significance in representing the image content.

The high-frequency components, located in the bottom-right corner of the DCT block, represent fine details, edges, and noise in the image. While these coefficients may be visually important for preserving image details, they are typically less perceptually significant and contribute less to the overall image quality.

During the compression process, quantization is applied to the DCT coefficients. The quantization step involves dividing the coefficients by specific values based on a quantization matrix. Higher-frequency components, located towards the bottom-right corner, tend to have lower magnitudes and are more susceptible to quantization. Consequently, they can be quantized more aggressively, resulting in more significant reduction in data and higher compression ratios.

By quantizing and reducing the precision of the higher-frequency components, which contain less perceptually important information, the compression algorithm can achieve more efficient compression while minimizing the impact on visual quality. The preserved lower-frequency components retain most of the visually important information, allowing for the reconstruction of a visually acceptable approximation of the original image during decompression.

It's worth noting that the specific coefficients considered most useful for compression may vary depending on the specific application, image content, and compression parameters used. Different compression algorithms may also employ variations in how the DCT coefficients are quantized and encoded to optimize compression efficiency and visual quality.

### In this context, explain the notions DC coefficient and AC coefficient

In the context of JPEG compression and the Discrete Cosine Transform (DCT), the terms "DC coefficient" and "AC coefficient" refer to different types of coefficients obtained from the transformed image blocks.

1. DC Coefficient: The DC coefficient represents the average brightness or intensity of an image block. It corresponds to the zero-frequency component or the constant offset in the DCT-transformed block. In other words, the DC coefficient captures the overall brightness level of the block. The DC coefficient is located at the top-left corner of the DCT block, which is the low-frequency region.

The DC coefficient is often considered the most visually significant coefficient as it represents the baseline intensity information for the block. It carries the primary visual energy and contributes to the overall appearance and brightness of the reconstructed image. In terms of compression, the DC coefficient is usually less susceptible to quantization compared to the AC coefficients.

2. AC Coefficients: AC coefficients, also known as alternate current coefficients, represent the variations or deviations from the average brightness captured by the DC coefficient. AC coefficients capture the high-frequency details, textures, and subtle changes in the image block. They provide information about the finer spatial variations within the block.

The AC coefficients are located in the remaining positions of the DCT block, excluding the top-left corner where the DC coefficient resides. They are ordered based on their frequencies, with the higher-frequency components placed towards the bottom-right corner of the block.

In terms of compression, the AC coefficients tend to have smaller magnitudes compared to the DC coefficient. They encode the fine details and high-frequency variations that are often less perceptually important than the low-frequency components. Therefore, during quantization, the AC coefficients are more aggressively quantized or even set to zero, resulting in higher compression and reduced data size.

The AC coefficients, due to their high-frequency nature, are also more prone to noise and quantization artifacts. Hence, they are more likely to exhibit visual degradation when subjected to aggressive compression.

In summary, the DC coefficient represents the average brightness or intensity of an image block, while the AC coefficients capture the variations and high-frequency details. The DC coefficient is usually more visually significant and less susceptible to quantization, while the AC coefficients provide finer spatial information but are more prone to compression artifacts.

### How can the values of the quantization matrix (and quantization factor) influence the perceived quality?

The values of the quantization matrix and the quantization factor in JPEG compression play a crucial role in determining the perceived quality of the compressed image. These values directly affect the level of compression applied to the DCT coefficients and, consequently, the visual fidelity of the reconstructed image. Here's how the values of the quantization matrix and quantization factor influence perceived quality:

1. Quantization Matrix: The quantization matrix determines the amount of quantization applied to each DCT coefficient during the compression process. It is a matrix of values that are multiplied with the DCT coefficients before rounding and truncation. Higher values in the quantization matrix result in more aggressive quantization, leading to a greater reduction in data and higher compression ratios. Conversely, lower values in the quantization matrix result in less quantization and potentially higher visual quality.

By adjusting the values in the quantization matrix, it is possible to prioritize different aspects of the image during compression. For example, increasing the values corresponding to high-frequency components in the quantization matrix would result in stronger quantization of high-frequency details, leading to a loss of fine details and textures. On the other hand, reducing the values for low-frequency components can help preserve overall image structure and smooth transitions.

2. Quantization Factor: The quantization factor, often denoted as Q, is a scalar value applied to the quantization matrix during compression. It determines the overall strength of quantization applied to the DCT coefficients. A higher quantization factor leads to stronger quantization and higher compression ratios, but at the expense of visual quality. Conversely, a lower quantization factor results in less quantization and potentially higher visual quality, but with larger file sizes.

The choice of the quantization factor is often a trade-off between compression efficiency and perceived image quality. A smaller quantization factor results in higher visual fidelity but also larger file sizes. Conversely, a larger quantization factor achieves higher compression ratios but at the cost of increased visual degradation and loss of fine details.

It's important to note that adjusting the quantization matrix and quantization factor is a subjective process, as the desired level of compression and acceptable visual quality can vary depending on the specific application, image content, and viewer preferences. Finding the right balance between compression efficiency and perceived quality involves carefully tuning these parameters based on the specific requirements and constraints of the application.

## Entropy coding

### Describe in general the purpose of entropy coding as a last step of JPEG compression. Is it a lossy or a lossless process?

The purpose of entropy coding as the last step of JPEG compression is to further reduce the file size by encoding the quantized DCT coefficients using a more efficient representation. It is a lossless process that achieves data compression without introducing any additional loss of information.

After quantization, the DCT coefficients are typically represented as floating-point or integer values, which may require a significant number of bits to store. Entropy coding techniques exploit the statistical properties of the coefficient values to assign shorter bit representations to more probable values and longer bit representations to less probable values.

One commonly used entropy coding algorithm in JPEG compression is Huffman coding. Huffman coding constructs a variable-length code table based on the frequency distribution of the coefficient values. The more frequently occurring coefficient values are assigned shorter code words, while less frequent values are assigned longer code words. This ensures that the most common coefficient values are represented using fewer bits, leading to more efficient data storage.

By applying entropy coding, the file size is significantly reduced compared to a straightforward representation of the quantized coefficients. The reduction in file size depends on the distribution of coefficient values and the efficiency of the chosen entropy coding algorithm.

During decompression, the entropy-coded data is decoded, and the original quantized DCT coefficients are reconstructed. Since entropy coding is a lossless process, the original coefficient values are accurately recovered, preserving the fidelity of the compressed image.

To summarize, the purpose of entropy coding as the last step of JPEG compression is to achieve further data reduction by encoding the quantized DCT coefficients using a more efficient representation. It is a lossless process that reduces file size without introducing additional loss of information.

### What is the main contibution of (Run Length Encoding (RLE)) to data compression? How is a data block processed at this stage?

The main contribution of Run Length Encoding (RLE) to data compression is its ability to efficiently represent sequences of repeated data values. RLE is a simple and straightforward compression technique that is particularly effective when there are long runs of the same value in the data.

In RLE, a data block is processed by identifying consecutive runs of the same value and encoding them using a compact representation. Instead of explicitly storing each value individually, RLE represents the data as a sequence of value-count pairs.

Here's how a data block is typically processed in RLE:

1. Scanning the Data: The data block is scanned sequentially, examining consecutive elements to identify runs of the same value.
2. Run Detection: When a run of the same value is detected, the algorithm determines the length or count of that run. The count represents the number of times the value is repeated consecutively in the data block.
3. Encoding the Runs: The runs of consecutive values are encoded using value-count pairs. Each pair consists of the value and the count of that value in the run. For example, if a run consists of five consecutive occurrences of the value "A," it would be encoded as "A5." The pair "A5" represents five consecutive occurrences of the value "A."
4. Handling Single Values: If a single value occurs without repetition, it is typically encoded as a value-count pair with a count of one. For example, if there is a single occurrence of the value "B," it would be encoded as "B1."
5. Storing the Encoded Data: The encoded value-count pairs are stored or transmitted as the compressed representation of the data block. The encoded data requires significantly fewer bits than the original uncompressed data, particularly when there are long runs of the same value.

During decompression, the encoded data is processed in reverse to reconstruct the original data block. The algorithm reads the value-count pairs and reproduces the original sequence of values by repeating each value the specified number of times.

RLE is most effective when there are repeated values or long runs of the same value in the data. It achieves good compression ratios in such scenarios by eliminating the need to store each value individually, instead representing them as value-count pairs. However, RLE may not provide significant compression gains when there is little or no repetition in the data, as the encoding overhead may outweigh the compression benefits.

### Why are DC- and AC-coefficients entropy coded differently? Which procedure is generally recommended for encoding DC-coefficients, and which one for AC-coefficients?

DC-coefficients and AC-coefficients in JPEG compression are entropy coded differently due to their statistical characteristics and perceptual importance.

DC-Coefficients:
The DC-coefficients represent the average intensity or brightness of an image block. They tend to have a smoother distribution and exhibit more predictable patterns compared to the AC-coefficients. Therefore, a simple and efficient entropy coding technique called Differential Pulse Code Modulation (DPCM) is commonly used for encoding DC-coefficients.

In DPCM, the DC-coefficients are encoded differentially by taking the difference between the current DC-coefficient and the previous one. The resulting differences are then entropy coded using Huffman coding or other entropy coding methods. This approach exploits the correlation between adjacent DC-coefficients, as neighboring blocks often have similar average brightness levels.

AC-Coefficients:
The AC-coefficients capture the high-frequency details and variations within an image block. They tend to have a more complex and less predictable distribution compared to the DC-coefficients. Therefore, a different entropy coding technique known as Run-Length Encoding (RLE) combined with Huffman coding is generally recommended for encoding AC-coefficients.

In this approach, the AC-coefficients are scanned in a zigzag pattern from the top-left corner to the bottom-right corner of the DCT block. The zero-valued AC-coefficients that occur consecutively are run-length encoded, representing the number of consecutive zeros and the number of non-zero AC-coefficients that follow. The run-length encoded values are then entropy coded using Huffman coding. This technique is effective in compressing sequences of zero-valued AC-coefficients that are common in the high-frequency regions of an image.

By using different entropy coding procedures for DC- and AC-coefficients, JPEG takes advantage of their distinct characteristics and achieves more efficient compression. The DPCM-based encoding of DC-coefficients leverages their smoothness and correlation, while the RLE combined with Huffman coding of AC-coefficients efficiently handles the high-frequency variations and zero-valued runs.

It's important to note that while DPCM and RLE with Huffman coding are commonly recommended for DC- and AC-coefficients, respectively, there can be variations and improvements in entropy coding techniques based on specific implementations and requirements.
