clc;
clear all;
close all;

img = imread('bld1_5.jpg');
img_hsv = rgb2hsv(img);

min_h = 0.; max_h = 0.85;
min_s = 0; max_s = 0.25;
min_v = 0.5; max_v = 0.9;

bin = img_hsv(:,:,1) >= min_h  & img_hsv(:,:,1) < max_h & img_hsv(:,:,2) >= min_s & img_hsv(:,:,2) < max_s & img_hsv(:,:,3) >= min_v & img_hsv(:,:,3) < max_v;
se = strel('rectangle',[5,5]);
bin = imdilate(bin,se);
imshow(img_hsv)
imshow(bin)