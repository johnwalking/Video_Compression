# Video_Compression
Video Compression – HW1 (03/22/2021)
Instructions – Follow these carefully:

1.	Please upload your work to Moodle. The zip file must have the source code and a PDF report where you explain and display the outputs for each problem.  
2.	You can use either C, Python, or Matlab to do the homework work.
3.	Please feel free to read related materials available in the official Matlab/Python documentation.

Assignment:

1.	(30%) Please transform “foreman_qcif_0_rgb.bmp”  from the RGB to YCbCr color space. Subsample Cb and Cr components based on the 4:2:0 YCbCr format, and then transform it back to the RGB color space.
Display all the results (including intermediate ones, such as Y, Cb, and Cr images) and compare the original image with the subsampled version of the image in the RGB color space.


2.	(20%) Please transform “foreman_qcif_0_rgb.bmp,” “foreman_qcif_1_rgb.bmp,” and “foreman_qcif_2_rgb.bmp” from the RGB to YCbCr color space. Subsample Cb and Cr components based on the 4:2:0 YCbCr format. Save all three frames in a file with its extension “.yuv” , and then display it with “YUVDisplay.exe” provided. 



3.	(50%) Following Question 2, please quantize all the possible intensities evenly with 5 levels (0, 1, 2, 3, 4) for the three frames and use Huffman coding to encode these frames. Your report should include the Huffman tree, code for each level, and decoded frames (including dequantization). You also need to turn in the code for encoding and decoding as well as the encoded bitstream.  
