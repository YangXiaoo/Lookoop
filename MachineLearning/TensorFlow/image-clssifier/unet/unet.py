# coding:utf-8
# 2019-1-13
# unet

import os 
import numpy as np
from keras.models import *
from keras.layers import Input, merge, Conv2D, MaxPooling2D, UpSampling2D, Dropout, Cropping2D, concatenate
from keras.optimizers import *
from keras.preprocessing.image import array_to_img
from keras.callbacks import ModelCheckpoint, LearningRateScheduler
from keras import backend as keras
from data_factory import *




class myUnet(object):
	def __init__(self, 
				train_data_path,
				train_labels_path,
				test_data_path,
				predict_data_output,
				img_save_path,
				model_save_path,
				height, 
				width, 
				suffix,
				train_batch_size=2,
				epochs=10,
				validation_split=0.2,
				optimizer=Adam(lr = 1e-4), 
				loss='binary_crossentropy', 
				metrics=['accuracy']):
		self.height = height
		self.width = width
		self.suffix = suffix
		self.optimizer = optimizer
		self.loss = loss
		self.metrics = metrics
		self.train_data_path = train_data_path
		self.train_labels_path = train_labels_path
		self.test_data_path = test_data_path
		self.predict_data_output = predict_data_output
		self.img_save_path = img_save_path
		self.train_batch_size = train_batch_size
		self.epochs = epochs # 遍历轮询次数
		self.validation_split = validation_split
		self.model_save_path = os.path.join(model_save_path, 'my_unet.hdf5')


	def load_data(self):
		imgs_train, imgs_mask_train = load_train_data(self.train_data_path, self.train_labels_path)
		imgs_test = load_test_data(self.test_data_path)
		return imgs_train, imgs_mask_train, imgs_test

	def get_unet(self):
		inputs = Input((self.height, self.width,1))
		conv1 = Conv2D(64, 3, activation = 'relu', padding = 'same', kernel_initializer = 'he_normal')(inputs)
		print ("conv1 shape:",conv1.shape)
		conv1 = Conv2D(64, 3, activation = 'relu', padding = 'same', kernel_initializer = 'he_normal')(conv1)
		print ("conv1 shape:",conv1.shape)
		pool1 = MaxPooling2D(pool_size=(2, 2))(conv1)
		print ("pool1 shape:",pool1.shape)

		conv2 = Conv2D(128, 3, activation = 'relu', padding = 'same', kernel_initializer = 'he_normal')(pool1)
		print ("conv2 shape:",conv2.shape)
		conv2 = Conv2D(128, 3, activation = 'relu', padding = 'same', kernel_initializer = 'he_normal')(conv2)
		print ("conv2 shape:",conv2.shape)
		pool2 = MaxPooling2D(pool_size=(2, 2))(conv2)
		print ("pool2 shape:",pool2.shape)

		conv3 = Conv2D(256, 3, activation = 'relu', padding = 'same', kernel_initializer = 'he_normal')(pool2)
		print ("conv3 shape:",conv3.shape)
		conv3 = Conv2D(256, 3, activation = 'relu', padding = 'same', kernel_initializer = 'he_normal')(conv3)
		print ("conv3 shape:",conv3.shape)
		pool3 = MaxPooling2D(pool_size=(2, 2))(conv3)
		print ("pool3 shape:",pool3.shape)

		conv4 = Conv2D(512, 3, activation = 'relu', padding = 'same', kernel_initializer = 'he_normal')(pool3)
		conv4 = Conv2D(512, 3, activation = 'relu', padding = 'same', kernel_initializer = 'he_normal')(conv4)
		drop4 = Dropout(0.5)(conv4)
		pool4 = MaxPooling2D(pool_size=(2, 2))(drop4)

		conv5 = Conv2D(1024, 3, activation = 'relu', padding = 'same', kernel_initializer = 'he_normal')(pool4)
		conv5 = Conv2D(1024, 3, activation = 'relu', padding = 'same', kernel_initializer = 'he_normal')(conv5)
		drop5 = Dropout(0.5)(conv5)

		up6 = Conv2D(512, 2, activation = 'relu', padding = 'same', kernel_initializer = 'he_normal')(UpSampling2D(size = (2,2))(drop5))
		# merge6 = merge([drop4,up6], mode = 'concat', concat_axis = 3)
		merge6 = concatenate([drop4, up6], axis=3)
		conv6 = Conv2D(512, 3, activation = 'relu', padding = 'same', kernel_initializer = 'he_normal')(merge6)
		conv6 = Conv2D(512, 3, activation = 'relu', padding = 'same', kernel_initializer = 'he_normal')(conv6)

		up7 = Conv2D(256, 2, activation = 'relu', padding = 'same', kernel_initializer = 'he_normal')(UpSampling2D(size = (2,2))(conv6))
		# merge7 = merge([conv3,up7], mode = 'concat', concat_axis = 3)
		merge7 = concatenate([conv3, up7], axis=3)
		conv7 = Conv2D(256, 3, activation = 'relu', padding = 'same', kernel_initializer = 'he_normal')(merge7)
		conv7 = Conv2D(256, 3, activation = 'relu', padding = 'same', kernel_initializer = 'he_normal')(conv7)

		up8 = Conv2D(128, 2, activation = 'relu', padding = 'same', kernel_initializer = 'he_normal')(UpSampling2D(size = (2,2))(conv7))
		# merge8 = merge([conv2,up8], mode = 'concat', concat_axis = 3)
		merge8 = concatenate([conv2, up8], axis=3)
		conv8 = Conv2D(128, 3, activation = 'relu', padding = 'same', kernel_initializer = 'he_normal')(merge8)
		conv8 = Conv2D(128, 3, activation = 'relu', padding = 'same', kernel_initializer = 'he_normal')(conv8)

		up9 = Conv2D(64, 2, activation = 'relu', padding = 'same', kernel_initializer = 'he_normal')(UpSampling2D(size = (2,2))(conv8))
		# merge9 = merge([conv1,up9], mode = 'concat', concat_axis = 3)
		merge9 = concatenate([conv1, up9], axis=3)
		conv9 = Conv2D(64, 3, activation = 'relu', padding = 'same', kernel_initializer = 'he_normal')(merge9)
		conv9 = Conv2D(64, 3, activation = 'relu', padding = 'same', kernel_initializer = 'he_normal')(conv9)
		conv9 = Conv2D(2, 3, activation = 'relu', padding = 'same', kernel_initializer = 'he_normal')(conv9)
		conv10 = Conv2D(1, 1, activation = 'sigmoid')(conv9)

		model = Model(input = inputs, output = conv10)
		model.compile(optimizer = self.optimizer, loss = self.loss, metrics = self.metrics)
		return model


	def train(self):
		print("[INFO] loading data")
		imgs_train, imgs_mask_train, imgs_test = self.load_data()
		print("[INFO] loading data done")
		model = self.get_unet()
		model_checkpoint = ModelCheckpoint(self.model_save_path, monitor='loss', verbose=1, save_best_only=True)
		print('Fitting model...')
		model.fit(imgs_train, imgs_mask_train, batch_size=self.train_batch_size, epochs=self.epochs, verbose=1, validation_split=self.validation_split, shuffle=True, callbacks=[model_checkpoint])

		print('[INFO] Predicting test data.')
		imgs_mask_test = model.predict(imgs_test, batch_size=1, verbose=1)
		np.save(self.predict_data_output, imgs_mask_test)

	def save_img(self):
		print("[INFO] array to image")
		imgs = np.load(self.predict_data_output)
		for i in range(imgs.shape[0]):
			img = imgs[i]
			# for j in range(img.shape[0]):
			# 	print(max(img[j]), min(img[j]))
			img = img * 255  # [img > 0.1] = 255
			# img[img < 0.1] = 0
			img = array_to_img(img)
			img.save("%s/%d%s" % (self.img_save_path, i, self.suffix))
			
			# break


if __name__ == '__main__':
	train_data_path = r'D:\deep_learning\unet\imgs_train.npy'
	train_labels_path = r'D:\deep_learning\unet\imgs_mask_train.npy'
	test_data_path = r'D:\deep_learning\unet\imgs_test.npy'

	predict_data_output = r'D:\deep_learning\unet\prediction_test.npy'

	img_save_path = r'D:\deep_learning\unet\image_prediction_test'
	model_save_path = r'D:\deep_learning\unet'

	suffix = '.png'

	mkdir([img_save_path, model_save_path])

	myunet = myUnet(train_data_path,
					train_labels_path,
					test_data_path,
					predict_data_output,
					img_save_path,
					model_save_path,
					height=512, 
					width=512,
					suffix=suffix,
					train_batch_size=1, # 4
					epochs=10, # 100
					validation_split=0.1, # 0
					optimizer=Adam(lr=1e-4), 
					loss='binary_crossentropy', 
					metrics=['accuracy'])
	# myunet.train()
	myunet.save_img()
