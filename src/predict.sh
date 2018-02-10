python3 train_satellites.py \
--arch linknet34 --batch-size 4 \
--imsize 1312 --preset mul_ps_vegetation --augs True \
--workers 6 --epochs 50 --start-epoch 0 \
--seed 42 --print-freq 10 \
--lr 1e-3 --optimizer adam \
--lognumber norm_ln34_mul_ps_vegetation_aug_dice_predict \
--predict --resume weights/norm_ln34_mul_ps_vegetation_aug_dice_best.pth.tar \
--params /data/AOI_2_Vegas_Roads_Test_Public /data/AOI_3_Paris_Roads_Test_Public /data/AOI_4_Shanghai_Roads_Test_Public /data/AOI_5_Khartoum_Roads_Test_Public out_test
